import pandas as pd
import os

def is_valid_excell_data(file: str) -> bool:
    return True

def get_data_fields_from_excell(file: str) -> list[str]:
    # Parse the XML
    if not os.path.exists(file):
        raise FileExistsError(f'Data file {file} is not found')

    return list(pd.read_excel(file).columns)
