from ObjectAnalyzer.object_analyzer import ObjectAnalyzer
from VideoManager.video_source import VideoSource
from VideoManager.empty_frame_exception import EmptyFrame
from Logic.simple_model import SimpleModel

import cv2
import copy

CAFFE_PROTOTXT = "resources/MobileNetSSD_deploy.prototxt.txt"
CAFFE_MODEL = "resources/MobileNetSSD_deploy.caffemodel"
VIDEO_STORAGE_PATH = "video_storage/"


def main():
    video_source = VideoSource(0, VIDEO_STORAGE_PATH)
    video_source.start()
    analyzer = ObjectAnalyzer(CAFFE_PROTOTXT, CAFFE_MODEL)
    model = SimpleModel("policy.json")

    while True:
        try:
            frame = video_source.read()
            processed_frame = copy.deepcopy(frame)
            detected_objects = analyzer.process(processed_frame)
        except EmptyFrame:
            print("skipping empty frame")
            break

        cv2.imshow("Frame", processed_frame)
        if model.evaluate(detected_objects):
            if video_source.init_record():
                video_source.start_record(frame)
        else:
            video_source.stop_record()

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            video_source.stop_record()
            break
    cv2.destroyAllWindows()
    video_source.stop()


if __name__ == "__main__":
    main()
