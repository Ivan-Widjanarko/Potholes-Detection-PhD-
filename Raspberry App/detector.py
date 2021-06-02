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
        
        return boxes
        
    def get_input_size(self):
            return self.size
        
        
        
