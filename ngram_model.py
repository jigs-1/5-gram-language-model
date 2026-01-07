from collections import defaultdict
import re

class FiveGramLanguageModel:
    def __init__(self, n=5):
        self.n = n
        self.model = defaultdict(lambda: defaultdict(int))
        self.context_counts = defaultdict(int)

    def preprocess(self, text):
        """
        Preprocessing:
        - lowercase
        - remove punctuation
        - tokenize
        """
        text = text.lower()
        text = re.sub(r"[^a-z\s]", "", text)
        return text.split()

    def train(self, text):
        tokens = self.preprocess(text)

        if len(tokens) < self.n:
            print("[INFO] Corpus too small to train a 5-gram model.")
            return

        for i in range(len(tokens) - self.n + 1):
            context = tuple(tokens[i:i+self.n-1])
            next_word = tokens[i+self.n-1]

            self.model[context][next_word] += 1
            self.context_counts[context] += 1

        print(f"[INFO] Training completed using {len(self.model)} unique contexts.")

    def generate(self, seed, max_length=30):
        tokens = self.preprocess(seed)

        if len(tokens) < self.n - 1:
            print("[WARNING] Not enough context. "
                  "Seed must contain at least 4 words for a 5-gram model.")
            return seed

        for step in range(max_length):
            found = False

            # Backoff from 4-gram → 1-gram
            for k in range(self.n-1, 0, -1):
                context = tuple(tokens[-k:])

                if context in self.model:
                    if k < self.n - 1:
                        print(f"[INFO] Backoff applied: using {k}-word context.")

                    next_words = self.model[context]
                    best_word = max(next_words, key=next_words.get)
                    tokens.append(best_word)
                    found = True
                    break

            if not found:
                print("[WARNING] Context not found in model. "
                      "Text generation stopped.")
                break

        return " ".join(tokens)
