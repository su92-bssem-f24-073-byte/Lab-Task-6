import re

samples = [
    "AI, search!", 
    "I can't log in.", 
    "help@example.com", 
    "CS4944 version 2.1", 
    ""
]

print("=== Tokenization Comparison ===")
for text in samples:
    ws = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print(f"Original: {repr(text)}")
    print(f"  Whitespace: {ws} (Count: {len(ws)})")
    print(f"  Word-like:  {words} (Count: {len(words)})\n")

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    print("=== Model Subword Tokenizer Check ===")
    for text in samples[:2]:
        tokens = model.tokenizer.tokenize(text)
        print(f"Text: {text} -> Subwords: {tokens}")
except Exception as e:
    print("Model tokenizer skipped or downloading:", e)