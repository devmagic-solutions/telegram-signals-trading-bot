import json


class ParsersAggregator:
    def __init__(self):
        with open('parsers/parsers.json', 'r') as fcc_file:
            self.parsers = json.load(fcc_file)['parsers']

    def get_parser(self, publisher_id: str):
        if publisher_id in self.parsers:
            return self.parsers[publisher_id]

        return False
