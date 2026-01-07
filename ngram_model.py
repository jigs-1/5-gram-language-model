from collections import defaultdict
import random

def build_ngram_model(text, n=5):
    tokens = text.lower().split()
    model = defaultdict(list)

    for i in range(len(tokens) - n):
        context = tuple(tokens[i:i+n-1])
        next_word = tokens[i+n-1]
        model[context].append(next_word)

    return model

def generate_text(seed, model, n=5, length=30):
    tokens = seed.lower().split()

    for _ in range(length):
        context = tuple(tokens[-(n-1):])
        if context not in model:
            break
        tokens.append(random.choice(model[context]))

    return " ".join(tokens)
