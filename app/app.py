from tkinter import *
from tkinter import filedialog, messagebox

from app.gui_widgets import (
    TemplateFileInputWidget, DataFileInputWidget,
    IdColumnInputWidget, RunAppWidget
)

from app.template_processor import TemplateProcessor
from app.utils.utils import is_valid_template
from app.utils.read_excell import get_data_fields_from_excell, is_valid_excell_data


# Constants
FILE_TYPES = [
    ("All Files", "*.*"),
    ("XML files", "*.xml"),
    ("Excel Files", "*.xls;*.xlsx"),
]
WINDOW_TITLE = "Шаблонизатор для метаданных"

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)

        self.template_file_widget = TemplateFileInputWidget(
            self, 'Template file *', self.browse_template_file
        )

        self.data_file_widget = DataFileInputWidget(
            self, 'Data file *', self.browse_data_file
        )

        self.id_column_input_widget = IdColumnInputWidget(
            self, 'ID column'
        )

        self.run_button_widget = RunAppWidget(self, command=self.run_app)

    def browse_template_file(self) -> None:
        """Open a file dialog to select the template file and validate it."""
        file_path = filedialog.askopenfilename(
            filetypes=FILE_TYPES
        )

        if file_path:
            if is_valid_template(file_path):
                self.template_file_widget.set_path(file_path)

            else:
                messagebox.showerror(
                    "Invalid Template",
                "The selected file is not a valid Jinja2 template."
                )

    def browse_data_file(self) -> None:
        """Open a file dialog to select the template file and validate it."""
        file_path = filedialog.askopenfilename(
            filetypes=FILE_TYPES
        )

        if file_path:
            if is_valid_excell_data(file_path):
                self.data_file_widget.set_path(file_path)

                self.id_column_input_widget.input_field.config(
                    values=get_data_fields_from_excell(file_path)
                )

            else:
                messagebox.showerror(
                    "Invalid input XML-data",
                    "The selected file is not a valid XML-data file."
                )

    def run_app(self):
        """Save the parameters and process the template."""
        template_path = self.template_file_widget.get_path()
        xml_data_path = self.data_file_widget.get_path()
        file_name_column = self.id_column_input_widget.get_path()

        if template_path and xml_data_path:
            try:
                template_processor = TemplateProcessor(
                    template_path,
                    xml_data_path,
                    file_name_column
                )
                template_processor.generate_files_from_template()

                messagebox.showinfo("Success", "Template processed successfully!")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to process template: {e}")
        else:
            messagebox.showwarning("Input Error", "Please fill all fields!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
