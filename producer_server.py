from kafka import KafkaProducer
import json
import time

class ProducerServer(KafkaProducer):
    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    def generate_data(self):
        record = ''
        with open(self.input_file) as f:
            for line in f:
                if '}' in line:
                    record += '}'
                    json_dict = json.loads(record)
                    message = self.dict_to_binary(json_dict)
                    self.send(topic=self.topic, value=message)
                    record = ''
                    time.sleep(1)
                elif '[' in line:
                    pass
                else:
                    record += line

    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf-8')
