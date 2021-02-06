from VideoManager.video_recorder_interface import VideoRecorderInterface
from datetime import datetime
import cv2


class VideoRecorder(VideoRecorderInterface):
    def __init__(self, record_path):
        self.__recording_path = record_path
        self.__video_writer = None
        self.__current_vid_file = None
        self.__started_record = False

    def record_frame(self, frame):
        if self.__started_record:
            self.__video_writer.write(frame)

    def start_record(self):
        if not self.__started_record:
            print("--> initializing record")
            self.__current_vid_file = self.__generate_time_stamp() + ".avi"
            self.__init_writer()
            self.__started_record = True
        return self.__started_record

    def stop_record(self):
        print("--> stopping record")
        self.__video_writer.release()
        self.__started_record = False

    def __init_writer(self):
        fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
        self.__video_writer = cv2.VideoWriter(self.__recording_path + self.__current_vid_file, fourcc, 30.0, (640, 480))

    @staticmethod
    def __generate_time_stamp():
        now = datetime.now()
        date_time = now.strftime("%m_%d_%Y_%H_%M_%S")
        return date_time
