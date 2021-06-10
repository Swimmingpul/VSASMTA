from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def download_file(ticker, model_name):
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("creds.txt")

    if gauth.credentials is None:
        gauth.GetFlow()
        gauth.flow.params.update({'access_type': 'offline'})
        gauth.flow.params.update({'approval_prompt': 'force'})
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()

    gauth.SaveCredentialsFile("creds.txt")  

    drive = GoogleDrive(gauth)

    name = f'{ticker}_predictions.png'
    file_list = drive.ListFile({'q': f"'1kxtGrwVl0gscMq79quvISHmXhUg4ZDUZ' in parents and trashed=false"}).GetList()
    if (len(file_list) != 0):
        for file in file_list:
            if (name == file['title']):
                print(file['title'])
                file.GetContentFile(f'{name}')
                break
            else:
                continue

ticker_list = ('AAPL', 'MSFT', 'GOOG', 'GOOGL', 'FB', 'TSM', 'NVDA', 'ADBE', 'INTC', 'CSCO', 'ASML', 'TTD', 'ORCL', 'CRM')

for ticker in ticker_list:
    download_file(ticker, 'SARIMA')
