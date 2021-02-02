import abc


class VideoSourceInterface(metaclass=abc.ABCMeta):
    """Interface for video stream basic operations"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'start') and
                callable(subclass.start) and
                hasattr(subclass, 'stop') and
                callable(subclass.stop))

    @abc.abstractmethod
    def start(self):
        """Start video source"""
        raise NotImplementedError

    @abc.abstractmethod
    def stop(self):
        """Stop video source"""
        raise NotImplementedError

    @abc.abstractmethod
    def read(self):
        """Read frame from video source"""
        raise NotImplementedError
