from utils import csv_manager

data_file = {
    'column 1': [1, 2, 3],
    'column 2': ['a', 'b', 'c']
}

file_buffer = csv_manager.generate_buffer(data_file, list(data_file.keys()), ',')
