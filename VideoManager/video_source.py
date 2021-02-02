from imutils.video import VideoStream
from datetime import datetime
from VideoManager.video_source_interface import VideoSourceInterface
from VideoManager.video_recorder_interface import VideoRecorderInterface

import time
import cv2


class VideoSource(VideoSourceInterface, VideoRecorderInterface):
    def __init__(self, source, record_path):
        self.__recording_path = record_path
        self.__video_stream = VideoStream(src=source)
        self.__video_writer = None
        self.__current_vid_file = None
        self.__started_record = False

    def start(self):
        print("[INFO] starting video stream...")
        time.sleep(2)
        self.__video_stream.start()

    def read(self):
        return self.__video_stream.read()

    def stop(self):
        self.__video_stream.stop()
        if self.__video_writer:
            self.__video_writer.release()

    def start_record(self):
        if not self.__started_record:
            print("--> initializing record")
            self.__current_vid_file = self.__generate_time_stamp() + ".avi"
            self.__init_writer()
            self.__started_record = True
        return self.__started_record

    def record_frame(self, frame):
        if self.__started_record:
            self.__video_writer.write(frame)

    def stop_record(self):
        print("--> stopping record")
        self.__video_writer.release()
        self.__started_record = False

    def __init_writer(self):
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        self.__video_writer = cv2.VideoWriter(self.__recording_path + self.__current_vid_file, fourcc, 30.0, (640, 480))

    @staticmethod
    def __generate_time_stamp():
        now = datetime.now()  # current date and time
        date_time = now.strftime("%m_%d_%Y_%H_%M_%S")
        return date_time
