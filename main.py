from ObjectAnalyzer.object_analyzer import ObjectAnalyzer
from VideoManager.video_source import VideoSource
from VideoManager.empty_frame_exception import EmptyFrame

import cv2

CAFFE_PROTOTXT = "resources/MobileNetSSD_deploy.prototxt.txt"
CAFFE_MODEL = "resources/MobileNetSSD_deploy.caffemodel"
VIDEO_STORAGE_PATH = "/home/tf/myrepos/smart_monitoring/temp/"

video_source = VideoSource(0, VIDEO_STORAGE_PATH)
video_source.start()
analyzer = ObjectAnalyzer(CAFFE_PROTOTXT, CAFFE_MODEL)

while True:
    try:
        frame = video_source.read()
        detected_objects = analyzer.process(frame)
    except EmptyFrame:
        print("skipping empty frame")
        break

    cv2.imshow("Frame", frame)
    if "person" in detected_objects:
        if video_source.start_record():
            video_source.record_frame(frame)
    else:
        print("no person stopping record")
        video_source.stop_record()
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        video_source.stop_record()
        break
cv2.destroyAllWindows()
video_source.stop()
