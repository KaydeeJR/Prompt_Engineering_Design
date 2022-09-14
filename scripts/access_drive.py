""" TODO: Change Spreadsheet ID
    The file accesses my drive folder and fetches an Excel file"""
from __future__ import print_function

import os.path
import sys
import shutil
import io
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']
SPREADSHEET_ID = '19N_K6SnIm0FylD2TBs-5y3WeSgdveb3J'

# path to credentials folder
my_path ="D:\\10XAcademy" 
os.chdir(my_path)
path_to_module = os.path.abspath(os.getcwd())
if path_to_module not in sys.path:
    sys.path.append(path_to_module)

def main():
    """Access sheets API.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                my_path+'\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    # Connect to the API service
    return build('drive', 'v3', credentials=creds)

def FileDownload(service, file_id, file_name):
    """
    # Download excel file from GDrive
    # https://docs.google.com/spreadsheets/d/19N_K6SnIm0FylD2TBs-5y3WeSgdveb3J/edit#gid=293715615
    """
    request = service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
          
    # Initialise a downloader object to download the file
    downloader = MediaIoBaseDownload(fh, request, chunksize=204800)
    done = False
  
    try:
    # Download the data in chunks
        while not done:
            status, done = downloader.next_chunk()
            fh.seek(0)
            print(status)
            # Write the received data to the file
            with open(file_name, 'wb') as f:
                shutil.copyfileobj(fh, f)
            print("File Downloaded")
            # Return True if file Downloaded successfully
            return True
    except:  
        # Return False if something went wrong
        print("Something went wrong.")
        return False


if __name__ == '__main__':
    FileDownload(main(), SPREADSHEET_ID, os.getcwd()+"\\Prompt_Engineering_Design\\data\\example_data.xlsx")