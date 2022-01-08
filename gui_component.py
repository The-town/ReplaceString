import tkinter.scrolledtext as scrolled_text
import tkinter as tk
from typing import List

from replaceRule import change_string, change_string_list
from validate import validate_number_of_replace_rule


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
        button.grid(column=0, row=1)
        button["command"] = self.execute_replace_rule

        self.string_type_check_button: StringTypeCheckButton = StringTypeCheckButton(function_frame)
        self.string_type_check_button.grid(column=0, row=0)

        root.mainloop()

    def execute_replace_rule(self, event=None) -> None:
        input_text: str = self.input_replace_text.get(1.0, tk.END)[:-1]
        rule_replace_text: str = self.rule_replace_text.get(1.0, tk.END)[:-1]
        strings_before_change: List[str] = []
        strings_after_change: List[str] = []
        for rule in rule_replace_text.split("\n"):
            if " -> " in rule:
                strings_before_change.append(rule.split(" -> ")[0])
                strings_after_change.append(rule.split(" -> ")[1])

        self.output_replace_text.delete(1.0, tk.END)
        is_validate, error_msg = validate_number_of_replace_rule(strings_before_change, strings_after_change)
        if is_validate:
            output_text: str = ""
            if self.string_type_check_button.state.get() == "one_line":
                output_text = change_string(input_text, tuple(strings_before_change), tuple(strings_after_change))
            elif self.string_type_check_button.state.get() == "many_lines":
                output_text = change_string_list(tuple(input_text.split("\n")), tuple(strings_before_change),
                                                 tuple(strings_after_change))
            self.output_replace_text.insert(tk.END, output_text)

        else:
            self.output_replace_text.insert(tk.END, error_msg)


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


class CheckButton(tk.Checkbutton):
    def __init__(self, master=None):
        tk.Checkbutton.__init__(self, master)

        self["bg"] = "white"
        self["text"] = "test"
        self["font"] = ("メイリオ", 15)

        self.state: tk.StringVar = tk.StringVar()
        self.state.set("no")
        self["variable"] = self.state
        self["onvalue"] = "yes"
        self["offvalue"] = "no"


class StringTypeCheckButton(CheckButton):
    def __init__(self, master=None):
        CheckButton.__init__(self, master)

        self["text"] = "改行文字列\\nを使い、1行の文字列として置換する"

        self.state.set("many_lines")
        self["onvalue"] = "one_line"
        self["offvalue"] = "many_lines"