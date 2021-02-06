import abc


class VideoRecorderInterface(metaclass=abc.ABCMeta):
    """Interface for video stream recording operations"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'start_record') and
                callable(subclass.start_record) and
                hasattr(subclass, 'stop_record') and
                callable(subclass.stop_record) and
                hasattr(subclass, 'record_frame') and
                callable(subclass.record_frame))

    @abc.abstractmethod
    def start_record(self):
        """Start recording video source"""
        raise NotImplementedError

    @abc.abstractmethod
    def stop_record(self):
        """Stop recording video source"""
        raise NotImplementedError

    @abc.abstractmethod
    def record_frame(self, frame):
        """Write frame"""
        raise NotImplementedError
