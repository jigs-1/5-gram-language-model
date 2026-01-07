from collections import defaultdict, Counter


def build_ngram_model(text, n=5):
    """
    Builds a strict n-gram (here 5-gram) language model.
    Maps (n-1)-word context -> Counter of next words.
    """
    tokens = text.lower().split()
    model = defaultdict(Counter)

    for i in range(len(tokens) - n + 1):
        context = tuple(tokens[i:i + n - 1])   # previous 4 words
        next_word = tokens[i + n - 1]           # 5th word
        model[context][next_word] += 1

    return model


def generate_text(seed, model, n=5, length=50):
    """
    Generates text strictly following the n-gram rule:
    next word depends ONLY on previous (n-1) words.
    """
    tokens = seed.lower().split()

    if len(tokens) < n - 1:
        print(f"[ERROR] Seed must contain at least {n-1} words.")
        return seed

    for _ in range(length):
        context = tuple(tokens[-(n - 1):])

        if context not in model:
            print(
                "\n[INFO] Context not found in corpus."
                " Generation stopped as per strict 5-gram rule.\n"
            )
            break

        # Choose word with maximum conditional probability
        next_word = model[context].most_common(1)[0][0]
        tokens.append(next_word)

    return " ".join(tokens)



