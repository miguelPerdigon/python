from logging import error
from google.cloud import bigquery


class Bigquery:
    def __init__(self, project_id):
        scopes = (
            'https://www.googleapis.com/auth/bigquery',
            'https://www.googleapis.com/auth/cloud-platform',
            'https://www.googleapis.com/auth/drive'
        )
        bigquery.client.Client.SCOPE = scopes
        self.client = bigquery.Client(project_id)

    def do_query(self, query):
        query_job = self.client.query(query)
        result = query_job.result()
        return result

    def up_table(self, dataset_id, table_id, storage_folder, header, name_file, bucket_name):
        try:
            dataset = self.client.dataset(dataset_id)
            table = dataset.table(table_id)

            job_config = bigquery.LoadJobConfig()

            schema = []

            for field in header:
                schema.append(bigquery.SchemaField(field, 'STRING'))

            job_config.schema = schema

            job_config.source_format = bigquery.SourceFormat.CSV
            job_config.allow_jagged_rows = True
            job_config.allow_quoted_newlines = True
            job_config.encoding = 'UTF-8'
            job_config.field_delimiter = '<'
            job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND

            job_config.source_format = bigquery.SourceFormat.CSV
            uri = 'gs://{bucket}/{folder}/{name}'.format(
                bucket=bucket_name,
                folder=storage_folder,
                name=name_file)

            load_job = self.client.load_table_from_uri(
                uri,
                table,
                job_config=job_config)

            load_job.result()

            return True
        except Exception as e:
            error(str(e))
            return False

    def delete_table(self, data_set, table_id):
        try:
            old_table = self.client.dataset(data_set).table(table_id)
            self.client.delete_table(old_table)

            return True
        except Exception as e:
            error(str(e))
            return False
