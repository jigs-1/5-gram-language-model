from ngram_model import build_ngram_model, generate_text

with open("data/conan_doyle.txt", "r", encoding="utf-8") as f:
    text = f.read()

model = build_ngram_model(text, n=5)

samples = [
    "the day was very",
    "mr sherlock holmes",
    "i had my doubts"
]

for s in samples:
    print("Input:", s)
    print("Output:", generate_text(s, model))
    print()
