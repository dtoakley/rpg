
class Lexicon(object):

    def __init__(self, paths, verbs, ignores):
        self.vocab = {}

        for path in paths:
            self.vocab.update({path: "path"})

        for verb in verbs:
            self.vocab.update({verb: "verb"})

        for ignore in ignores:
            self.vocab.update({ignore: "ignore"})

    def get_action_from_sentence(self, sentence):

        words = sentence.split()
        result = []

        for word in words:
            try:
                word_lower = word.lower()
                if self.vocab[word_lower]:
                    result.append({self.vocab[word_lower]: word_lower})
                else:
                    result.append({"noun": word_lower})
            except KeyError:
                if word.isdigit():
                    number = int(word)
                    result.append({"number": number})
                else:
                    result.append({"error": word})

        return result


