class Text:
    def __init__(self, file_name):
        file = open(file_name)
        self.text = file.read()


    def count_characters(self):
        return len(self.text)


    def count_words(self):
        return len(self.text.split())


    def count_sentenses(self):
        count = 0
        for i in [ '!', '?', '...', '. ']:
            count+=self.text.count(i)
        return count


test = Text('text_for_test.txt')

print(test.count_characters())
print(test.count_words())
print(test.count_sentenses())
