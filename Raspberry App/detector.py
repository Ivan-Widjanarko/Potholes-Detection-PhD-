from tflite_runtime.interpreter import Interpreter
import numpy as np

class ObjectDetectorLite:
    def __init__(self, model_path):
        # Define lite graph and Load Tensorflow Lite model into memory
        self.interpreter = Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        
        # Get input size from model
        input_shape = self.input_details[0]['shape']
        self.size = input_shape[:2] if len(input_shape) == 3 else input_shape[1:3]

    def detect(self, image, threshold=0.1):
        # Add a batch dimension
        frame = np.expand_dims(image, axis=0)
        
        # run model
        self.interpreter.set_tensor(self.input_details[0]['index'], frame)
        self.interpreter.invoke()
        
        # get results
        #print()
        #print(self.interpreter.get_tensor(self.output_details[0]['index']))
        #print(self.interpreter.get_tensor(self.output_details[0]['shape'][0]))
        #print()
        boxes = self.interpreter.get_tensor(self.output_details[0]['index'])
        print()
        print(boxes)
        print(self.output_details)
        print(self.interpreter.get_tensor)
        #classes = self.interpreter.get_tensor(self.output_details[1]['index'])
        #scores = self.interpreter.get_tensor(self.output_details[2]['index'])
        #num = self.interpreter.get_tensor(self.output_details[3]['index'])
        
        return [], boxes, [0]
        
        # Find detected boxes coordinates
        return self._boxes_coordinates(image,
                                        np.squeeze(boxes[0]),
                                        np.squeeze(classes[0]+1).astype(np.int32),
                                        np.squeeze(scores[0]),
                                        min_score_thresh=threshold)

    def _boxes_coordinates(self,
                        image,
                        boxes,
                        classes,
                        scores,
                        max_boxes_to_draw=20,
                        min_score_thresh=.5):
        """
        This function groups boxes that correspond to the same location
        and creates a display string for each detection 
        
        Args:
          image: uint8 numpy array with shape (img_height, img_width, 3)
          boxes: a numpy array of shape [N, 4]
          classes: a numpy array of shape [N]
          scores: a numpy array of shape [N] or None.  If scores=None, then
            this function assumes that the boxes to be plotted are groundtruth
            boxes and plot all boxes as black with no classes or scores.
          max_boxes_to_draw: maximum number of boxes to visualize.  If None, draw
            all boxes.
          min_score_thresh: minimum score threshold for a box to be visualized
        """
        
        if not max_boxes_to_draw:
            max_boxes_to_draw = boxes.shape[0]
        number_boxes = min(max_boxes_to_draw, boxes.shape[0])
        detected_boxes = []
        probabilities = []
        categories = []
        
        for i in range(number_boxes):
            if scores is None or scores[i] > min_score_thresh:
                box = tuple(boxes[i].tolist())
                detected_boxes.append(box)
                probabilities.append(scores[i])
                # KASIH IF BUAT CEK SEBERAPA GEDE UKURAN BOXNYA
                # BUAT NENTUIN DIA TERMASUK LUBANG BESAR/SEDANG/KECIL
                # TERUS APPEND KE CATEGORIES BUAT GANTIIN YANG DIBAWAH INI
                # INI SEMENTARA DOANG, CUMA CETAK PERSENTASENYA
                categories.append(classes[i])
        return np.array(detected_boxes), probabilities, categories

    def get_input_size(self):
        return self.size
