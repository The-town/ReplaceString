import tkinter.scrolledtext as scrolled_text
import tkinter as tk
from typing import List

from replaceRule import delete_blank_line, change_string


class Main:
    def __init__(self) -> None:
        root: tk.Tk = tk.Tk()
        root.title("文字列置換")
        root.configure(background='white')

        text_frame: Frame = Frame(root)
        text_frame.grid(column=0, row=1)

        self.input_replace_text: InputReplaceText = InputReplaceText(text_frame)
        self.input_replace_text.grid(column=0, row=0)

        self.rule_replace_text: RuleReplaceText = RuleReplaceText(text_frame)
        self.rule_replace_text.grid(column=1, row=0)

        self.output_replace_text: OutputReplaceText = OutputReplaceText(text_frame)
        self.output_replace_text.grid(column=2, row=0)

        function_frame: Frame = Frame(root)
        function_frame.grid(column=0, row=0)
        button: Button = Button(function_frame)
        button["text"] = "置換"
        button.grid(column=0, row=0)
        button["command"] = self.execute_replace_rule

        root.mainloop()

    def execute_replace_rule(self, event=None) -> None:
        input_text: str = self.input_replace_text.get(1.0, tk.END)[:-1]
        # output_text: str = delete_blank_line(input_text)
        rule_replace_text: str = self.rule_replace_text.get(1.0, tk.END)[:-1]
        strings_before_change: List[str] = []
        strings_after_change: List[str] = []
        for rule in rule_replace_text.split("\n"):
            if " -> " in rule:
                strings_before_change.append(rule.split(" -> ")[0])
                strings_after_change.append(rule.split(" -> ")[1])

        self.output_replace_text.delete(1.0, tk.END)
        if len(strings_before_change) == len(strings_after_change):
            output_text: str = change_string(input_text, tuple(strings_before_change), tuple(strings_after_change))
            self.output_replace_text.insert(tk.END, output_text)
        else:
            self.output_replace_text.insert(tk.END, "【エラー】置換前の文字列と置換後の文字列の数が合いません。")


class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(column=0, row=0)
        self["width"] = 100
        self["height"] = 100
        self["padx"] = 10
        self["pady"] = 10
        self["bg"] = "white"


class InputReplaceText(scrolled_text.ScrolledText):
    def __init__(self, master=None):
        scrolled_text.ScrolledText.__init__(self, master)
        self["width"] = 50
        self["height"] = 20
        self["font"] = ("メイリオ", 12)


class RuleReplaceText(scrolled_text.ScrolledText):
    def __init__(self, master=None):
        scrolled_text.ScrolledText.__init__(self, master)
        self["width"] = 25
        self["height"] = 20
        self["font"] = ("メイリオ", 12)


class OutputReplaceText(scrolled_text.ScrolledText):
    def __init__(self, master=None):
        scrolled_text.ScrolledText.__init__(self, master)
        self["width"] = 50
        self["height"] = 20
        self["font"] = ("メイリオ", 12)


class Button(tk.Button):
    def __init__(self, master=None):
        tk.Button.__init__(self, master)

        self["height"] = 1
        self["width"] = 10
        self["font"] = ("メイリオ", 15)

