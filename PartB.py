import os
import sys


# Runtime: O(n) where n is the number of characters in the file.
def tokenize_stream(file_path):
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
                            yield "".join(current)
                            current = []
    except OSError as exc:
        raise RuntimeError(f"Failed to read file: {file_path}") from exc

    if current:
        yield "".join(current)


# Runtime: O(1) per character check.
def _is_ascii_alnum(ch):
    code = ord(ch)
    return (
        48 <= code <= 57  # 0-9
        or 65 <= code <= 90  # A-Z
        or 97 <= code <= 122  # a-z
    )


# Runtime: O(n + m) where n and m are characters in each file.
def count_common_tokens(file_path_a, file_path_b):
    size_a = _safe_size(file_path_a)
    size_b = _safe_size(file_path_b)

    if size_a <= size_b:
        smaller = file_path_a
        larger = file_path_b
    else:
        smaller = file_path_b
        larger = file_path_a

    tokens_in_smaller = set()
    for token in tokenize_stream(smaller):
        tokens_in_smaller.add(token)

    common = set()
    for token in tokenize_stream(larger):
        if token in tokens_in_smaller:
            common.add(token)

    return len(common)


# Runtime: O(1), uses file metadata.
def _safe_size(file_path):
    try:
        return os.path.getsize(file_path)
    except OSError:
        return 0


def main(argv):
    if len(argv) != 3:
        print("Usage: python PartB.py <text_file_1> <text_file_2>", file=sys.stderr)
        return 2

    file_path_a = argv[1]
    file_path_b = argv[2]
    count = count_common_tokens(file_path_a, file_path_b)
    print(count)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
