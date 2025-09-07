import finder

class FileOpener:
    def __init__(self):
        self.text = self.read_file()
        if self.text is not None:
            self.fw = finder.FileWork(self.text)
        else:
            self.fw = None

    def read_file(self):
        try:
            with open('matmod.txt', 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return None

    def get_answer(self, q_number):
        if self.fw is None:
            return None
        beg = self.fw.FindStart(q_number)
        en = self.fw.FindEnd(q_number)
        return self.fw.ExtractAnswer(beg, en)
