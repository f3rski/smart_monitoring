import abc


class ModelInterface(metaclass=abc.ABCMeta):
    """Interface for Logic basic operations"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'evaluate') and
                callable(subclass.evaluate) and
                hasattr(subclass, 'save') and
                callable(subclass.save) and
                hasattr(subclass, 'init') and
                callable(subclass.init))

    @abc.abstractmethod
    def evaluate(self, input_data):
        """Perform model evaluation for provided data"""
        raise NotImplementedError

    @abc.abstractmethod
    def save(self):
        """Save model data"""
        raise NotImplementedError

    @abc.abstractmethod
    def init(self):
        """Init model data"""
        raise NotImplementedError
