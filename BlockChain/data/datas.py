class Data:

    def __init__(self, tag1, tag2, tag3):
        self.tag1 = tag1
        self.tag2 = tag2
        self.tag3 = tag3

    def __str__(self):
        return str(self.tag1) + " | " + str(self.tag2) + " | " + str(self.tag3)
