
class Lexicon(object):

    def __init__(self, game):
        self.game = game
        self.vocab = {}

    def add_path(self, path):
        self.vocab.update({path: "path"})
        return self.vocab

    def add_verb(self, verb):
        self.vocab.update({verb: "verb"})
        return self.vocab

    def add_noun(self, noun):
        self.vocab.update({noun: "noun"})
        return self.vocab

    def add_ignore(self, ignore):
        self.vocab.update({ignore: "ignore"})
        return self.vocab

    def scan(self, sentence):

        words = sentence.split()
        result = []

        for word in words:
            try:
                word_lower = word.lower()
                result.append((self.vocab[word_lower], word_lower))
            except KeyError:
                if word.isdigit():
                    number = int(word)
                    result.append(("number", number))

                else:
                    result.append(("error", word))

        return result
