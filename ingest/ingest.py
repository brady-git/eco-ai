import argparse
from .loaders import load_texts

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--persist-dir", required=True)
    args = ap.parse_args()

    docs = load_texts(args.input)
    print(f"Loaded {len(docs)} docs")
    # TODO: chunk, embed, and persist to Chroma at args.persist_dir

if __name__ == "__main__":
    main()
