from os import environ
from logging import error

from googleapiclient.discovery import build
from google.oauth2 import service_account


class GoogleDrive:
    def __init__(self):
        SCOPES = [
            'https://www.googleapis.com/auth/spreadsheets.readonly',
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/documents.readonly',
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive.readonly'
        ]
        # you have to set a environ variable with the path token.json
        # the token is generated from GCP (google cloud platform)
        token_path = environ['GOOGLE_APPLICATION_CREDENTIALS']
        credentials = service_account.Credentials.from_service_account_file(token_path, scopes=SCOPES)
        self.service = build('sheets', 'v4', credentials=credentials, cache=False, cache_discovery=False)

    def download_file(self, file_id, google_sheet_id):
        try:
            sheet = self.service.spreadsheets()
            result = sheet.values().get(spreadsheetId=file_id, range=google_sheet_id).execute()
            values = result.get('values', [])
            return values

        except Exception as e:
            error(str(e))
