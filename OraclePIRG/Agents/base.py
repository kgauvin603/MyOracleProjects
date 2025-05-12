
class Agent:
    def __init__(self, name):
        self.name = name

    def process(self, input_data):
        raise NotImplementedError(f"{self.name} must implement its own process method.")
