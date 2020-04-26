from utils.storage_gcp import Storage
from utils import csv_manager

data_file = {
    'column 1': [1, 2, 3],
    'column 2': ['a', 'b', 'c']
}

file_buffer = csv_manager.generate_buffer(data_file, list(data_file.keys()), ',')

storage_manager = Storage('project_id', 'bucket_name')
storage_manager.up(file_buffer, 'folder_name', 'file_name.csv')
