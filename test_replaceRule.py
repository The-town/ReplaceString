import unittest

from typing import Tuple

from replaceRule import delete_blank_line, change_string


class TestDeleteBlankLine(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_replace_string(self) -> None:
        string: str = "aaa\n　　a\nbあb\na\n\n\nccc"
        self.assertEqual(delete_blank_line(string), "aaa\n　　a\nbあb\na\nccc")

    def test_change_string_one_change_pattern(self) -> None:
        text: str = "aaa b1b c%cあ"
        strings_before_change: Tuple[str] = ("a",)
        strings_after_change: Tuple[str] = ("c",)

        self.assertEqual(change_string(text, strings_before_change, strings_after_change), "ccc b1b c%cあ")

    def test_change_string_one_change_re_pattern_hat(self) -> None:
        text: str = "aaa b1b c%cあ"
        strings_before_change: Tuple[str] = ("^a",)
        strings_after_change: Tuple[str] = ("c",)

        self.assertEqual(change_string(text, strings_before_change, strings_after_change), "caa b1b c%cあ")

    def test_change_string_many_change_pattern(self) -> None:
        text: str = "aaa b1b c%cあ"
        strings_before_change: Tuple[str, ...] = ("a", "b")
        strings_after_change: Tuple[str, ...] = ("c", "c")

        self.assertEqual(change_string(text, strings_before_change, strings_after_change), "ccc c1c c%cあ")

    def test_change_string_many_change_re_pattern_hat(self) -> None:
        text: str = "aaa b1b c%cあ"
        strings_before_change: Tuple[str, ...] = ("^a", "b")
        strings_after_change: Tuple[str, ...] = ("c", "c")

        self.assertEqual(change_string(text, strings_before_change, strings_after_change), "caa c1c c%cあ")
