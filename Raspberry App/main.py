import numpy as np
import picamera
import argparse
import time

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

from utils import load_image
from detector import ObjectDetectorLite

def parse_args():
    parser = argparse.ArgumentParser(description='Object Detection')
    parser.add_argument('--model_path', type=str, help='Specify the model path',
                        default='model.tflite')
    parser.add_argument('--confidence', type=float, help='Minimum required confidence level of bounding boxes',
                        default=0.6)
    
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    detector = ObjectDetectorLite(model_path=args.model_path)
    input_size = detector.get_input_size()
    
    plt.ion()
    plt.tight_layout()
    
    fig = plt.gcf()
    fig.canvas.set_window_title('Object Detection')
    ax = plt.gca()
    ax.set_axis_off()
    tmp = np.zeros(input_size + [3], np.uint8)
    preview = ax.imshow(tmp)
    
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        while True:
            stream = np.empty((480, 640, 3), dtype=np.uint8)
            camera.capture(stream, 'rgb')
            
            image = load_image(stream, (224, 224))
            image = image.astype('float32')
            scores = detector.detect(image, args.confidence)
            image = image.astype('uint8')
            print(scores)
            
            if (scores > 0.75 ):
                fig.suptitle('Detected')
            else:
                fig.suptitle('Detecting...')
                
            
            preview.set_data(image)
            fig.canvas.get_tk_widget().update()
            
            start = time.time()
            while time.time() - start < 1:
                pass
