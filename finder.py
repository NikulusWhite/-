class FileWork:
    def __init__(self, text):
        self.text = text

    def FindStart(self, b):
        return self.text.find('#' + b)

    def FindEnd(self, c):
        return self.text.find('@' + c)

    def ExtractAnswer(self, beg, en):
        if beg == -1 or en == -1 or beg >= en:
            return None
        return self.text[beg:en]
