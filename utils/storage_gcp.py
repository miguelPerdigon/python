from google.cloud import storage
from logging import error


class Storage:
    def __init__(self, project_id_gcp, bucket_name):
        client = storage.Client(project_id_gcp)
        bucket = client.get_bucket(bucket_name)
        self.bucket = bucket

    def up(self, buffer, folder, file_name, content_type='text/csv'):
        try:
            file_blob_name = '{folder}/{file}'.format(folder=folder, file=file_name)

            blob = self.bucket.blob(file_blob_name)
            blob.upload_from_string(buffer.getvalue(), content_type=content_type)

            if self.bucket.get_blob(file_blob_name):
                buffer.close()

        except Exception as e:
            error(str(e))

    def delete_folder(self, folder):
        try:
            blobs = self.bucket.list_blobs(prefix=folder)
            self.bucket.delete_blobs(blobs)
        except Exception as e:
            error(str(e))

    def delete(self, folder, file_name):
        try:
            self.bucket.delete_blob(folder + '/' + file_name)
        except Exception as e:
            error(str(e))

    def download(self, segment_name, folder, file_name, path_download):
        blob = self.bucket.blob(segment_name + '/' + folder + '/' + file_name)
        blob.download_to_file_name(path_download)

    def download_buffer(self, folder, file_name):
        blob = self.bucket.blob(folder + '/' + file_name)
        buffer = blob.download_as_string()
        return buffer
