import json

BATCH = 1


def main():
    row = {str(i): round(1 / i, 3) for i in range(1, 513, 1)}
    data = {"batch": [row for _ in range(BATCH)]}
    with open(f"request_{BATCH}.json", "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=None, separators=(",", ":"))


if __name__ == "__main__":
    main()
