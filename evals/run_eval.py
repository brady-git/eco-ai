import csv
from pathlib import Path

def run():
    rows = list(csv.DictReader(open(Path(__file__).with_name("questions.csv"), newline="", encoding="utf-8")))
    print(f"Loaded {len(rows)} eval questions")

if __name__ == "__main__":
    run()
