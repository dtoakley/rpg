
class Lexicon(object):

    def __init__(self, paths, verbs, nouns, ignores):
        self.vocab = {}

        for path in paths:
            self.vocab.update({"path": path})

        for verb in verbs:
            self.vocab.update({"verb": verb})

        for noun in nouns:
            self.vocab.update({"noun": noun})

        for ignore in ignores:
            self.vocab.update({"ignore": ignore})

    def convert_sentence_to_action(self, sentence):

        words = sentence.split()
        result = {}

        for word in words:
            try:
                word_lower = word.lower()
                result.update({self.vocab[word_lower]: word_lower})
            except KeyError:
                if word.isdigit():
                    number = int(word)
                    result.update({"number": number})
                else:
                    result.update({"error": word})

        return result


