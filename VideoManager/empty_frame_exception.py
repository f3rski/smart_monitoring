
class EmptyFrame(Exception):
    """Empty frame exception class"""
    def __init__(self):
        pass

    def __str__(self):
        return 'The frame is None type'
