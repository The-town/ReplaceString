import re

from typing import Tuple, List


def delete_blank_line(text: str) -> str:
    """
    空白行を削除する関数

    Parameters
    ----------
    text: str
        置換する文字列

    Returns
    -------
    re.sub(re_obj_blank_line, "\n", text): str
        空白行を削除した後の文字列
    """
    re_obj_blank_line: re.Pattern = re.compile(r"\n+")
    return re.sub(re_obj_blank_line, "\n", text)


def change_string(text: str, strings_before_change: Tuple[str], strings_after_change: Tuple[str]) -> str:
    """
    文章中にある、複数の指定した文字列を、複数の指定した文字列へ変換する関数

    Parameters
    ----------
    text: str
        置換対象の文章
    strings_before_change: Tuple[str]
        置換する文字列のタプル
    strings_after_change: Tuple[str]
        置換後の文字列のタプル

    Returns
    --------
    text: str
        置換後の文章
    """
    for i in range(len(strings_after_change)):
        re_obj_change_string: re.Pattern = re.compile(rf"{strings_before_change[i]}")
        text = re.sub(re_obj_change_string, strings_after_change[i], text)
    return text


def change_string_list(texts: Tuple[str, ...], strings_before_change: Tuple[str, ...],
                       strings_after_change: Tuple[str, ...]) -> str:
    """
    リストとして受け取った文章中にある、複数の指定した文字列を、複数の指定した文字列へ変換する関数
    正規表現の「^」や「$」をリストの要素ごとに実行するために作成した。

    例；
    texts = [123, abc, 145c]
    ^1 -> a
    [a23, abc, a45c]

    Parameters
    ----------
    texts: Tuple[str, ...]
        置換対象の文章
    strings_before_change: Tuple[str, ...]
        置換する文字列のタプル
    strings_after_change: Tuple[str, ...]
        置換後の文字列のタプル

    Returns
    --------
    text: str
        置換後の文章
    """
    tmp_texts: List[str] = list(texts)
    for i in range(len(strings_after_change)):
        re_obj_change_string: re.Pattern = re.compile(rf"{strings_before_change[i]}")
        tmp_texts = [re.sub(re_obj_change_string, strings_after_change[i], text) for text in tmp_texts]
    return "\n".join(tmp_texts)
