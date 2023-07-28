import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from config import SPREADSHEET_ID, NAME_LIST, SCOPES, CRED_PATH, TOKEN_PATH


class GoogleAPI:

    def __init__(self):
        self.path_to_cred = CRED_PATH
        self.path_to_token = TOKEN_PATH

    @property
    def service(self):
        creds = None
        if os.path.exists(self.path_to_token):
            creds = Credentials.from_authorized_user_file(self.path_to_token, SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.path_to_cred, SCOPES)
                creds = flow.run_local_server(port=0)
                self.create_token(creds)
        return build('sheets', 'v4', credentials=creds).spreadsheets()

    def create_token(self, creds):
        with open(self.path_to_token, 'w') as token:
            token.write(creds.to_json())

    def create_(self):
        spreadsheet_ = self.service.create(body={
            'properties': {'title': 'TABLE_SUMMER'},
            'sheets': [{'properties': {'sheetType': 'GRID',
                                       'sheetId': 0,
                                       'title': 'MAIN_LIST',
                                       }}]
        }).execute()
        return spreadsheet_.get('spreadsheetId')

    def append_data(self, data: list):
        """writing data after non-empty fields"""
        self.service.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=f'{NAME_LIST}!A1',
            valueInputOption="USER_ENTERED",
            body={'values': data}
        ).execute()
