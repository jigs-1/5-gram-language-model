from ngram_model import FiveGramLanguageModel

print("[INFO] Loading corpus...")
with open("data/conan_doyle.txt", "r", encoding="utf-8") as f:
    corpus = f.read()

model = FiveGramLanguageModel(n=5)
model.train(corpus)

print("\n[INFO] 5-gram Language Model ready.")
print("Type a sentence (at least 4 words).")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Input > ").strip()

    if user_input.lower() == "exit":
        print("[INFO] Exiting model.")
        break

    if not user_input:
        print("[WARNING] Empty input. Please enter some text.")
        continue

    output = model.generate(user_input)
    print("Output >", output)
    print("-" * 60)
