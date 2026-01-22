import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

import PartA


def _write_temp_file(directory, name, content):
    path = f"{directory}/{name}"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)
    return path


class TestPartA(unittest.TestCase):
    def test_tokenize_basic_and_casefold(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = _write_temp_file(
                tmpdir, "sample.txt", "Apple apple aPpLe banana!"
            )
            tokens = PartA.tokenize(path)
            self.assertEqual(tokens, ["apple", "apple", "apple", "banana"])

    def test_tokenize_splits_on_non_ascii(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = _write_temp_file(tmpdir, "sample.txt", "café naïve")
            tokens = PartA.tokenize(path)
            self.assertEqual(tokens, ["caf", "na", "ve"])

    def test_compute_word_frequencies(self):
        tokens = ["a", "b", "a", "c", "b", "a"]
        frequencies = PartA.computeWordFrequencies(tokens)
        self.assertEqual(frequencies["a"], 3)
        self.assertEqual(frequencies["b"], 2)
        self.assertEqual(frequencies["c"], 1)

    def test_print_frequencies_sorted(self):
        frequencies = {"banana": 2, "apple": 3, "cherry": 2}
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            PartA.printFrequencies(frequencies)
        output = buffer.getvalue().strip().splitlines()
        self.assertEqual(output[0], "apple\t3")
        self.assertEqual(output[1], "banana\t2")
        self.assertEqual(output[2], "cherry\t2")

    def test_main_usage_error(self):
        buffer = io.StringIO()
        with redirect_stderr(buffer):
            code = PartA.main(["PartA.py"])
        self.assertEqual(code, 2)
