from tkinter import *
from tkinter import ttk

class BaseWidget(Frame):
    def __init__(self, parent: Tk):
        super().__init__(parent)
        self.pack(pady=10, fill='x')
        self.grid_columnconfigure(0, weight=1, minsize=110)
        self.grid_columnconfigure(1, weight=2, minsize=250)
        self.grid_columnconfigure(2, weight=1, minsize=80)

    def add_label(self, row: int, column: int, text: str):
        label = Label(self, text=text)
        label.grid(row=row, column=column, padx=10, sticky='w')
        return label

    def add_entry(self, row: int, column: int, width: int = 40):
        entry = ttk.Entry(self, width=width)
        entry.grid(row=row, column=column, padx=5, sticky='ew')
        return entry

    def add_button(self, row: int, column: int, text: str, command: callable):
        button = Button(self, text=text, command=command)
        button.grid(row=row, column=column, padx=10, sticky='e')
        return button

    def add_combobox(self, row: int, column: int, values: list, width: int = 20):
        combobox = ttk.Combobox(self, values=values, width=width)
        combobox.grid(row=row, column=column, padx=5, sticky='w')
        return combobox



class FileInputWidget(BaseWidget):
    def __init__(self, parent: Tk, label_text: str, command: callable):
        super().__init__(parent)
        self.label = self.add_label(0, 0, label_text)
        self.text_input = self.add_entry(0, 1)
        self.button = self.add_button(0, 2, 'Browse', command)

    def get_path(self) -> str:
        return self.text_input.get()

    def set_path(self, path: str) -> None:
        self.text_input.delete(0, END)
        self.text_input.insert(0, path)


class TemplateFileInputWidget(FileInputWidget):
    pass


class DataFileInputWidget(FileInputWidget):
    pass


class IdColumnInputWidget(BaseWidget):
    def __init__(self, parent: Tk, label_text: str):
        super().__init__(parent)
        self.data_fields = []
        self.label = self.add_label(0, 0, label_text)
        self.input_field = self.add_combobox(0, 1, self.data_fields)

    def get_path(self) -> str:
        return self.input_field.get()

    def set_path(self, text: str) -> None:
        self.input_field.delete(0, END)
        self.input_field.insert(0, text)


class RunAppWidget(BaseWidget):
    def __init__(self, parent: Tk, command: callable):
        super().__init__(parent)
        self.button = self.add_button(0, 2, 'Run', command)
