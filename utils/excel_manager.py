#Desarrollado por el Licenciado Miguel Angel Perdigon Orta
#Correo: miguelperdigon91@gmail.com
#06/09/2018

import pandas as pd
from io import BytesIO
from utils.constant import NORMAL_CELL_STYLE
from logging import error


def generate(data_file_list, name_sheets, header_style=None):
    file_buffer = BytesIO()
    writer = pd.ExcelWriter(file_buffer, engine='xlsxwriter')
    workbook = writer.book

    if header_style:
        header_format = workbook.add_format(header_style)

    for i, data_file in enumerate(data_file_list):
        df = pd.DataFrame(data_file)
        df.to_excel(writer, name_sheets[i], index=False)

        worksheet = writer.sheets[name_sheets[i]]
        df.style.applymap(NORMAL_CELL_STYLE)

        if header_style:
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, header_format)

    writer.save()
    return file_buffer


def read_sheet(path_file, name_sheet):
    try:
        df = pd.read_excel(path_file, sheet_name=name_sheet)
        return df

    except Exception as e:
        error(str(e))
