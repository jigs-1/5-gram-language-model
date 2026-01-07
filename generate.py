from ngram_model import build_ngram_model, generate_text

def main():
    with open("data/conan_doyle.txt", "r", encoding="utf-8") as f:
        text = f.read()

    model = build_ngram_model(text, n=5)
    generated = generate_text(model, num_words=100)
    print(generated)

if __name__ == "__main__":
    main()
