# Домашнее задание по теме "Оператор "with".

# Домашнее задание по теме "Оператор "with".

class WordsFinder:

    def __init__(self, *files):
        self.file_names = files
        self.make_all_words()

    def get_all_words(self):
        return self.all_words

    def make_all_words(self):
        self.all_words = {}
        for file_name in self.file_names:
            with open(file_name,"r",encoding="Utf-8") as file:
                words = []
                for line in file:
                    words += self.clean_str(line.lower()).split()
                self.all_words[file_name] = words

    def clean_str(self, str):
        for mask in [',', '.', '=', '!', '?', ';', ':', ' - ']:
            str.replace(mask,'')
        return str

    def find(self, word):
        result = {}
        for file, words  in self.all_words.items():
            if word.lower() in words:
                result[file] = words.index(word.lower()) + 1
        return result

    def count(self, word):
        result = {}
        for file, words in self.all_words.items():
            if word.lower() in words:
                result[file] = words.count(word.lower())

        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
