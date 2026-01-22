import sys


# Runtime: O(n) where n is the number of characters in the file.
def tokenize(file_path):
    tokens = []
    current = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as infile:
            while True:
                chunk = infile.read(4096)
                if not chunk:
                    break
                for ch in chunk:
                    if _is_ascii_alnum(ch):
                        current.append(ch.lower())
                    else:
                        if current:
                            tokens.append("".join(current))
                            current = []
    except OSError as exc:
        raise RuntimeError(f"Failed to read file: {file_path}") from exc

    if current:
        tokens.append("".join(current))
    return tokens


# Runtime: O(1) per character check.
def _is_ascii_alnum(ch):
    code = ord(ch)
    return (
        48 <= code <= 57  # 0-9
        or 65 <= code <= 90  # A-Z
        or 97 <= code <= 122  # a-z
    )


# Runtime: O(m) where m is the number of tokens.
def computeWordFrequencies(tokens):
    frequencies = {}
    for token in tokens:
        if token in frequencies:
            frequencies[token] += 1
        else:
            frequencies[token] = 1
    return frequencies


# Runtime: O(k log k) where k is number of unique tokens.
def printFrequencies(frequencies):
    for token, count in sorted(
        frequencies.items(), key=lambda item: (-item[1], item[0])
    ):
        print(f"{token}\t{count}")


def main(argv):
    if len(argv) != 2:
        print("Usage: python PartA.py <text_file>", file=sys.stderr)
        return 2

    file_path = argv[1]
    tokens = tokenize(file_path)
    frequencies = computeWordFrequencies(tokens)
    printFrequencies(frequencies)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
