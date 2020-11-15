class Guest:

    def __init__(self, name):
        self.name = name
        self.group = []

    def group_size(self):
        return len(self.group)

    def add_to_group(self, new_guest):
        self.group.append(new_guest)
      