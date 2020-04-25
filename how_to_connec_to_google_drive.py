from utils.google_drive import GoogleDrive

google_sheet_id = 'it is in the url of the google sheet'
range_google_sheet = "'{}'!A2:J".format('sheet_name')

downloader = GoogleDrive()
result = downloader.download_file(google_sheet_id, range_google_sheet)

for row in result:
    for cell in row:
        print(cell)
