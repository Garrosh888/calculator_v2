class Data_button():
    def __init__(self,title,function,type):# title - это что написано на кнопке
        self.title = title
        self.function = function
        self.type = type

dictionary_buttons_type = {
    "S2A": "aziz",
    "0": "number",
    "1": "number",
    "2": "number",
    "3": "number",
    "4": "number",
    "5": "number",
    "6": "number",
    "7": "number",
    "8": "number",
    "9": "number",
    "+": "operation",
    "-": "operation",
    "×": "operation",
    "÷": "operation",
    "С": "clear_all",
    "⌫": "clear_last",
    "=": "equal",
    ".": "point"
}
