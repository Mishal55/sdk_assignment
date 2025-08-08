
class Agent:
    def __init__(self, name, tools=None, input_filter=None):
        self.name = name
        self.tools = tools or []
        self.input_filter = input_filter or (lambda x: True)
