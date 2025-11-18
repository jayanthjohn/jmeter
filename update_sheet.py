import csv
import sys
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def main():
    if len(sys.argv) < 2:
        print("Usage: python update_sheet.py <spreadsheet_id>")
        sys.exit(1)

    spreadsheet_id = sys.argv[1]
    sheet_name = "Sheet1"
    start_cell = "B1"

    # Authenticate with service account
    creds = Credentials.from_service_account_file(
        'service-account.json',
        scopes=['https://www.googleapis.com/auth/spreadsheets']
    )

    service = build('sheets', 'v4', credentials=creds)

    # Read output.csv into a list of rows
    with open('output.csv', newline='') as f:
        reader = csv.reader(f)
        values = list(reader)

    # Clear existing data in columns B to Z
    clear_range = f"{sheet_name}!B1:Z1000"
    service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id,
        range=clear_range
    ).execute()

    # Write new values starting from column B
    update_range = f"{sheet_name}!{start_cell}"
    body = {'values': values}

    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=update_range,
        valueInputOption='RAW',
        body=body
    ).execute()

    print(f"✅ {result.get('updatedCells')} cells updated starting from B1.")

if __name__ == "__main__":
    main()
