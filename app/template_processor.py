import jinja2
from typing import Dict, List
import pandas as pd
import numpy as np
import os

InputData = List[Dict[str, str]]

class TemplateProcessor:
    def __init__(
            self,
            template_path: str,
            data_path: str,
            file_name_column: str
    ):
        self.template = self._get_jinja_template(template_path)
        self.input_data = self._parse_source_data(data_path)
        self.file_name_column = file_name_column

    def generate_files_from_template(self) -> None:
        for idx, params in enumerate(self.input_data):
            processed_template = self.template.render(params)

            file_name = idx
            if self.file_name_column:
                file_name = params[self.file_name_column]

            print(f'{file_name}')

            if not os.path.exists('./outputs'):
                os.mkdir('./outputs')


            save_path = os.path.join(
                './outputs', f'{file_name}.xml'
            )

            with open(save_path, 'w', encoding='UTF-8') as file:
                file.write(processed_template)

    @staticmethod
    def _get_jinja_template(template_path: str) -> jinja2.Template:
        if not os.path.exists(template_path):
            raise FileExistsError(f'Файл {template_path} не найден')

        template_dir = os.path.dirname(template_path)
        template_file_name =  os.path.basename(template_path)

        env_directory = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir)
        )
        template = env_directory.get_template(template_file_name)

        return template

    @staticmethod
    def _parse_source_data(source_data_path: str) -> InputData:
        if not os.path.exists(source_data_path):
            raise FileExistsError(f'Файл {source_data_path} не найден')

        return pd.read_excel(source_data_path).replace({np.nan: None}).to_dict(orient='records')


if __name__ == '__main__':
    template_processor = TemplateProcessor(
        '../input_data/jinja_template.xml',
        '../input_data/pdp_points.xml',
        'pointname2'
    )

    template_processor.generate_files_from_template()