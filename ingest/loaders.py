from pathlib import Path

def load_texts(path: str) -> list[dict]:
    p = Path(path)
    docs = []
    for fp in p.rglob("*"):
        if fp.suffix.lower() in {".txt", ".md"}:
            docs.append({"path": str(fp), "text": fp.read_text(encoding="utf-8", errors="ignore")})
    return docs
