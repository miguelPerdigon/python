from utils import excel_manager

data_file = {
    'column 1': [1, 2, 3],
    'column 2': ['a', 'b', 'c']
}

data_file_list = [data_file]
name_sheet_list = ['Sheet Test']

file_buffer = excel_manager.generate(data_file_list, name_sheet_list)
