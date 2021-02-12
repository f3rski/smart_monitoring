from Logic.model_interface import ModelInterface
import json


class SimpleModel(ModelInterface):
    def __init__(self, input_data_path):
        self.__target_objects = []
        self.init(input_data_path)

    def evaluate(self, input_data):
        for detected_object in input_data:
            if detected_object in self.__target_objects:
                return True
        return False

    def save(self):
        pass

    def init(self, input_data_path):
        with open(input_data_path, 'r') as input_file:
            data = input_file.read()

        json_obj = json.loads(data)
        self.__target_objects = json_obj["targets"]


