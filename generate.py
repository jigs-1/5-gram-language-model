from ngram_model import FiveGramLanguageModel

print("[INFO] Loading corpus...")
with open("data/conan_doyle.txt", "r", encoding="utf-8") as f:
    corpus = f.read()

model = FiveGramLanguageModel(n=5)
model.train(corpus)

samples = [
    "the day was very",
    "mr sherlock holmes",
    "i had my doubts",
    "holmes"
]

print("\n[INFO] Starting text generation...\n")

for s in samples:
    print("Input :", s)
    output = model.generate(s)
    print("Output:", output)
    print("-" * 60)
