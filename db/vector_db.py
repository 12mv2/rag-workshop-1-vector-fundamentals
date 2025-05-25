import json
import os

class VectorDB:
    def __init__(self, path="data/runners.json"):
        self.data = []
        self.load_data(path)

    def load_data(self, path):
        with open(path, "r") as f:
            self.data = json.load(f)

    def get_all(self):
        return self.data
