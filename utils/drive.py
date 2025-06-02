import os
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

def upload_to_drive(files):
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    SERVICE_ACCOUNT_FILE = 'credentials.json'
    
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    uploaded = []
    for file in files:
        file_stream = io.BytesIO(file.read())
        media = MediaIoBaseUpload(file_stream, mimetype=file.type)
        request = service.files().create(
            media_body=media,
            body={'name': file.name, 'parents': []},
            fields='id'
        )
        response = request.execute()
        uploaded.append(response)
    return uploaded