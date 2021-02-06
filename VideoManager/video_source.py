from imutils.video import VideoStream
from VideoManager.video_source_interface import VideoSourceInterface
from VideoManager.video_recorder_interface import VideoRecorderInterface
from VideoManager.video_recorder import VideoRecorder

import time


class VideoSource(VideoSourceInterface, VideoRecorderInterface):
    def __init__(self, source, record_path):
        self.__video_recorder = VideoRecorder(record_path)
        self.__video_stream = VideoStream(src=source)

    def start(self):
        print("[INFO] starting video stream...")
        time.sleep(2)
        self.__video_stream.start()

    def read(self):
        return self.__video_stream.read()

    def stop(self):
        self.__video_stream.stop()
        self.__video_recorder.stop_record()

    def start_record(self):
        return self.__video_recorder.start_record()

    def record_frame(self, frame):
        self.__video_recorder.record_frame(frame)

    def stop_record(self):
        return self.__video_recorder.stop_record()
