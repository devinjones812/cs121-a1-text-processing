import tempfile
import unittest

import PartB


def _write_temp_file(directory, name, content):
    path = f"{directory}/{name}"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)
    return path


class TestPartB(unittest.TestCase):
    def test_count_common_tokens_basic(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path_a = _write_temp_file(tmpdir, "a.txt", "Apple banana apple")
            path_b = _write_temp_file(tmpdir, "b.txt", "banana cherry apple")
            count = PartB.count_common_tokens(path_a, path_b)
            self.assertEqual(count, 2)

    def test_count_common_tokens_distinct_only(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path_a = _write_temp_file(tmpdir, "a.txt", "a a a b b c")
            path_b = _write_temp_file(tmpdir, "b.txt", "b b d d")
            count = PartB.count_common_tokens(path_a, path_b)
            self.assertEqual(count, 1)

    def test_count_common_tokens_empty(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path_a = _write_temp_file(tmpdir, "a.txt", "")
            path_b = _write_temp_file(tmpdir, "b.txt", "")
            count = PartB.count_common_tokens(path_a, path_b)
            self.assertEqual(count, 0)

    def test_tokenize_stream_non_ascii(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = _write_temp_file(tmpdir, "a.txt", "café")
            tokens = list(PartB.tokenize_stream(path))
            self.assertEqual(tokens, ["caf"])
