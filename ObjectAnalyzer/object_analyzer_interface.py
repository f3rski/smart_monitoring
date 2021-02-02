import abc


class ObjectAnalyzerInterface(metaclass=abc.ABCMeta):
    """Interface for object analyzer classes"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'prepare_model') and
                callable(subclass.prepare_model) and
                hasattr(subclass, 'process') and
                callable(subclass.process) and
                hasattr(subclass, 'preprocess_object') and
                callable(subclass.preprocess_object))

    @abc.abstractmethod
    def prepare_model(self):
        """Setup model"""
        raise NotImplementedError

    @abc.abstractmethod
    def process(self, subject):
        """Perform desired object processing/analyzing"""
        raise NotImplementedError

    @abc.abstractmethod
    def preprocess_object(self, subject):
        """Perform preprocessing of object to be able to perform analysis"""
        raise NotImplementedError
