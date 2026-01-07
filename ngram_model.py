from collections import defaultdict
import random


def build_ngram_model(text, n=5):
    """
    Build an n-gram language model.
    Returns a dictionary mapping (n-1)-word context -> list of possible next words.
    """
    tokens = text.lower().split()
    model = defaultdict(list)

    for i in range(len(tokens) - n + 1):
        context = tuple(tokens[i:i + n - 1])
        next_word = tokens[i + n - 1]
        model[context].append(next_word)

    return model


def generate_text(model, n=5, length=100):
    """
    Generate text using the trained n-gram model.
    """
    # Pick a random starting context
    context = random.choice(list(model.keys()))
    generated = list(context)

    for _ in range(length):
        next_words = model.get(tuple(generated[-(n - 1):]))
        if not next_words:
            break
        generated.append(random.choice(next_words))

    return " ".join(generated)

