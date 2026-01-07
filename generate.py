from ngram_model import build_ngram_model, generate_text


def main():
    with open("data/conan_doyle.txt", "r", encoding="utf-8") as f:
        corpus = f.read()

    model = build_ngram_model(corpus, n=5)

    seed = input("Enter starting text (at least 4 words): ")
    output = generate_text(seed, model, n=5, length=50)

    print("\nGenerated text:\n")
    print(output)


if __name__ == "__main__":
    main()
