from ObjectAnalyzer.object_analyzer import ObjectAnalyzer
from VideoManager.video_source import VideoSource
from VideoManager.empty_frame_exception import EmptyFrame

import cv2
import copy

CAFFE_PROTOTXT = "resources/MobileNetSSD_deploy.prototxt.txt"
CAFFE_MODEL = "resources/MobileNetSSD_deploy.caffemodel"
VIDEO_STORAGE_PATH = "/home/tf/myrepos/smart_monitoring/temp/"


def main():
    video_source = VideoSource(0, VIDEO_STORAGE_PATH)
    video_source.start()
    analyzer = ObjectAnalyzer(CAFFE_PROTOTXT, CAFFE_MODEL)

    while True:
        try:
            frame = video_source.read()
            processed_frame = copy.deepcopy(frame)
            detected_objects = analyzer.process(processed_frame)
        except EmptyFrame:
            print("skipping empty frame")
            break

        cv2.imshow("Frame", processed_frame)
        if "person" in detected_objects:
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
