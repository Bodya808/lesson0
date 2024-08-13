class WordsFinder:
    def __init__(self, *files):
        self.file_names = []
        for file in files:
            files = [file.strip() for file in file.split(',')]
            self.file_names.extend(files)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(punct, ' ')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []
        return all_words

    def find(self, word):
        dict_ = self.get_all_words()
        list_ = []
        for name, words in dict_.items():
            for w in words:
                if word.lower() in w:
                    index = words.index(w)
                    list_.append(self.file_names)
                    list_.append(index + 1)
                    break
        return list_

    def count(self, word):
        dict_ = self.get_all_words()
        list_ = []
        count = 0
        for name, words in dict_.items():
            for w in words:
                if word.lower() in w:
                    count += 1
        list_.append(self.file_names)
        list_.append(count)
        return list_


# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # Позиция первого вхождения слова
print(finder2.count('teXT'))  # Количество вхождений слова
