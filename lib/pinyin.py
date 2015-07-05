# coding=utf-8
from os.path import exists

class PinYin(object):
    def __init__(self, dict_file=''):
        self.word_dict = {}
        self.dict_file = dict_file

    def load_word(self):
        if not exists(self.dict_file):
            raise IOError('NotFoundFile')

        with file(self.dict_file) as f_obj:
            for f_line in f_obj.readlines():
                line = f_line.split()
                self.word_dict[line[0]] = ' '.join(line[1:])

    def hanzi2pinyin(self, string=''):
        result = []
        if not isinstance(string, unicode):
            string = string.decode('utf-8')

        for char in string:
            key = '%X' % ord(char)
            pinyin = self.word_dict.get(key, char).split()[0][:-1].lower()
            result.append(pinyin if pinyin else char)

        return result