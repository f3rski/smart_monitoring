import cv2
import numpy as np
from VideoManager.empty_frame_exception import EmptyFrame
from ObjectAnalyzer.object_analyzer_interface import ObjectAnalyzerInterface


class ObjectAnalyzer(ObjectAnalyzerInterface):
    def __init__(self, prototxt_path, caffe_path):
        self.colors = None
        self.__detections = None
        self.__frame_dims = tuple
        self.__CONFIDENCE_LEVEL = 0.6
        self.__net = None
        self.__classes = []
        self.__colors = None

        self.prepare_model((prototxt_path, caffe_path))

    def prepare_model(self, configuration):
        # initialize the list of class labels MobileNet SSD was trained to
        # detect, then generate a set of bounding box colors for each class
        self.__classes = ["background", "aeroplane", "bicycle", "bird", "boat",
                        "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                        "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                        "sofa", "train", "tvmonitor"]
        self.__colors = np.random.uniform(0, 255, size=(len(self.__classes), 3))
        print("[INFO] loading model...")
        self.__net = cv2.dnn.readNetFromCaffe(configuration[0], configuration[1])

    def process(self, frame):
        if frame is None:
            raise EmptyFrame

        classes = []
        blob = self.preprocess_object(frame)
        self.__net.setInput(blob)
        self.__detections = self.__net.forward()
        # loop over the detections
        for i in np.arange(0, self.__detections.shape[2]):
            # extract the confidence (i.e., probability) associated with
            # the prediction
            confidence = self.__detections[0, 0, i, 2]

            # filter out weak detections by ensuring the `confidence` is
            # greater than the minimum confidence
            if confidence > self.__CONFIDENCE_LEVEL:
                idx = int(self.__detections[0, 0, i, 1])
                (boxX0, boxY0, boxX1, boxY1) = self.__compute_object_coords(i)
                classes.append(self.__classes[idx])
                # draw the prediction on the frame
                label = "{}: {:.2f}%".format(self.__classes[idx],
                                             confidence * 100)
                cv2.rectangle(frame, (boxX0, boxY0), (boxX1, boxY1),
                              self.__colors[idx], 2)
                y = boxY0 - 15 if boxY0 - 15 > 15 else boxY0 + 15
                cv2.putText(frame, label, (boxX0, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.__colors[idx], 2)
            return classes

    def preprocess_object(self, frame):
        self.__frame_dims = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                     0.007843, (300, 300), 127.5)
        return blob

    def __compute_object_coords(self, detect_idx):
        # extract the index of the class label from the
        # `detections`, then compute the (x, y)-coordinates of
        # the bounding box for the object
        box = self.__detections[0, 0, detect_idx, 3:7] * np.array([self.__frame_dims[0], self.__frame_dims[1],
                                                                   self.__frame_dims[0], self.__frame_dims[1]])
        return box.astype("int")
