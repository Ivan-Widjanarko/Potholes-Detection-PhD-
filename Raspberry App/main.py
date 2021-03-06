import numpy as np
import picamera
import argparse
import requests
import time
import calendar

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

from utils import load_image
from detector import ObjectDetectorLite
from upload import upload_to_gstorage
from PIL import Image

def parse_args():
    parser = argparse.ArgumentParser(description='Object Detection')
    parser.add_argument('--model_path', type=str, help='Specify the model path',
                        default='model.tflite')
    
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    
    # Setup variable
    root = 'https://pothole-detection-315702.et.r.appspot.com'
    bucket_name ='pothole-detection1'
    device_id = 1
    state = 'detecting'
    counter = 0
    
    # Setup model
    detector = ObjectDetectorLite(model_path=args.model_path)
    input_size = detector.get_input_size()
    
    # Setup matplotlib
    plt.ion()
    plt.tight_layout()
    fig = plt.gcf()
    fig.canvas.set_window_title('Object Detection')
    ax = plt.gca()
    ax.set_axis_off()
    tmp = np.zeros(input_size + [3], np.uint8)
    preview = ax.imshow(tmp)
    
    # Using camera
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        tim = time.time()
        start = 0
        while True:
            # Get status from google cloud SQL via API
            if (time.time() - tim > 5.0):
                link = f'{root}/user/get/status/{device_id}'
                x = requests.get(link)
                start = x.json()['status']
                tim = time.time()
                
            # Checking status
            if (start!=1):
                fig.suptitle('stop')
                preview.set_data([[0, 0, 0]])
                fig.canvas.get_tk_widget().update()
                continue
            
            # Upload image to cloud storage and data to cloud SQL
            if (state == 'upload'):
                # Save image
                im = Image.fromarray(image)
                im.save("image.jpeg")
                
                # Store image to google cloud storage
                gmt = time.gmtime()
                timestamp = calendar.timegm(gmt)
                file_name = str(device_id)+'_'+str(timestamp)
                img_url = upload_to_gstorage(bucket_name, file_name, "image.jpeg")
                
                if(img_url != 'error'):
                    # Store data to google cloud SQL via API
                    latitude = 6.363869
                    longitude = 106.823835
                    hole_size = 'Medium'
                    link = f'{root}/data/post/{device_id}/{latitude}/{longitude}/{hole_size}/{file_name}'
                    x = requests.post(link)
                    status = x.json()['message']
                    if (status == 'Data added'):
                        print('upload successful')
                        print(f'api link {link}')
                        state = 'halt'
                        count = 0
                    else:
                        print('problem with API or database, trying to re-upload')
                        continue
                else:
                    print('problem with Cloud Storage, trying to re-upload')
                    continue
            
            # Get image from camera
            stream = np.empty((480, 640, 3), dtype=np.uint8)
            camera.capture(stream, 'rgb')
            image = load_image(stream, (224, 224))
            
            # Detect an object
            image = image.astype('float32')
            scores = detector.detect(image)
            image = image.astype('uint8')
            print(scores)
            
            # Check class and select state
            fig.suptitle(state)
            if (scores > 0.5 ):
                if (state == 'detecting'):
                    state = 'detected'
                    count = 0
                elif (state == 'detected'):
                    state = 'upload'
                elif (state == 'halt'):
                    count = 0
            else:
                if (state == 'detected'):
                    state = 'detecting'
                elif (state == 'halt'):
                    if (count > 1):
                        state = 'detecting'
                    else:
                        count += 1
            
            # Show image for debugging
            preview.set_data(image)
            fig.canvas.get_tk_widget().update()
