from VideoManager.video_recorder_interface import VideoRecorderInterface
from datetime import datetime
import cv2
import os


class VideoRecorder(VideoRecorderInterface):
    def __init__(self, record_path):
        self.__recording_path = record_path + self.__generate_time_stamp()[0] + "/"
        self.__video_writer = None
        self.__current_vid_file = None
        self.__started_record = False

    def record_frame(self, frame):
        if self.__started_record:
            self.__video_writer.write(frame)

    def start_record(self):
        if not self.__started_record:
            print("--> initializing record")
            self.__current_vid_file = self.__generate_time_stamp()[1] + ".avi"
            self.__init_writer()
            self.__started_record = True
        return self.__started_record

    def stop_record(self):
        print("--> stopping record")
        self.__video_writer.release()
        self.__started_record = False

    def __init_writer(self):
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        self.__create_dir(self.__recording_path)
        self.__video_writer = cv2.VideoWriter(self.__recording_path + self.__current_vid_file, fourcc, 30.0, (640, 480))

    @staticmethod
    def __generate_time_stamp():
        now = datetime.now()
        date = now.strftime("%m_%d_%Y")
        time = now.strftime("%H_%M_%S")
        return date, time

    @staticmethod
    def __create_dir(path):
        if not os.path.exists(path):
            os.makedirs(path)
