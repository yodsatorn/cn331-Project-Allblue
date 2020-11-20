from __future__ import print_function
import httplib2
import os, io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None
from . import auth
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.getCredentials()

http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http)


def uploadFile(filename,filepath):
    mimetype = 'image/jpg'
    file_metadata = {
        'name': filename,
        'parents': ['1VJRdUjkR39mXwvGWnsUgd__VrZwjK-B1']
    }
    media = MediaFileUpload(filepath,mimetype=mimetype)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    return file.get('id')

