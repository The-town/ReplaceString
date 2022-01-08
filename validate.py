from typing import Tuple


def validate_number_of_replace_rule(strings_before_change: list, strings_after_change: list) -> Tuple[bool, str]:
    """
    置換規則が正しく記述されているか確認する関数
    置換前の文字列と置換後の文字列の数を確認する。

    Parameters
    ----------
    strings_before_change: list
    strings_after_change: list

    Returns
    -------
    bool, error_msg: tuple[bool, str]
    """
    if len(strings_before_change) == len(strings_after_change):
        return True, ""
    else:
        return False, "【エラー】置換前の文字列と置換後の文字列の数が合いません。"
