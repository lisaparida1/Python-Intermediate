KILO = 1.609


class Convert:

    def __init__(self, input):
        self.input = input

    def convert(self):
        kilometer = self.input*KILO
        final_kilo = round(kilometer)
        return final_kilo