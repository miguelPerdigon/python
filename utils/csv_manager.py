import pandas as pd
from io import StringIO
from logging import error


def write(raw_data, header, path_file, sep, with_header=True):
    try:
        df = pd.DataFrame(raw_data, columns=header)
        df.to_csv(path_file, encoding='utf-8', sep=sep, header=with_header, index=False)

        return True
    except Exception as e:
        error(str(e))
        return False


def generate_buffer(raw_data, header, sep, with_header=False):
    try:
        file_buffer = StringIO()
        df = pd.DataFrame(raw_data, columns=header)
        df.to_csv(file_buffer, encoding='utf-8', sep=sep, header=with_header, index=False)

        return file_buffer
    except Exception as e:
        error(str(e))
