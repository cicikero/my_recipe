# 必要なモジュールをインポート
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Gmail APIのスコープを設定
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# 認証情報を取得する関数
def get_credentials():
    # credentials.jsonが存在するか確認
    if os.path.exists('credentials.json'):
        # credentials.jsonから認証情報を生成
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        # ユーザーに認証を要求し、トークンを取得
        credentials = flow.run_local_server(port=0)
    else:
        # credentials.jsonが存在しない場合はエラーを出力
        print('credentials.jsonが見つかりません。')
        return None
    
    # token.pickleが存在するか確認
    if os.path.exists('token.pickle'):
        # token.pickleからトークンを読み込み
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    
    # トークンが有効か確認
    if not credentials or not credentials.valid:
        # トークンが無効な場合はリフレッシュ
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            # トークンが存在しない場合はエラーを出力
            print('トークンが見つかりません。')
            return None
        
        # トークンをtoken.pickleに保存
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)
    
    # 認証情報を返す
    return credentials

# Gmail APIのサービスを取得する関数
def get_service():
    # 認証情報を取得
    credentials = get_credentials()
    # サービスオブジェクトを生成
    service = build('gmail', 'v1', credentials=credentials)
    # サービスオブジェクトを返す
    return service

# 「すべてのメール」から最新の100件のタイトルを取得する関数
def get_all_mail_titles():
    # サービスオブジェクトを取得
    service = get_service()
    # メッセージリストを取得（最大100件）
    results = service.users().messages().list(userId='me', maxResults=100).execute()
    # メッセージIDのリストを取得
    messages = results.get('messages', [])
    # タイトルのリストを初期化
    titles = []
    
    # メッセージIDごとにループ
    for message in messages:
        # メッセージIDを取得
        msg_id = message['id']
        # メッセージ本体を取得（メタデータのみ）
        msg = service.users().messages().get(userId='me', id=msg_id, format='metadata').execute()
        # メッセージのヘッダー情報を取得
        headers = msg['payload']['headers']
        
        # ヘッダー情報ごとにループ
        for header in headers:
            # ヘッダー名がSubjectであればタイトルとしてリストに追加
            if header['name'] == 'Subject':
                titles.append(header['value'])
                break
    
    # タイトルのリストを返す
    return titles

# メイン関数
def main():
    # 「すべてのメール」から最新の100件のタイトルを取得
    titles = get_all_mail_titles()
    
    # タイトル
    for title in titles:
        print(title)
    
# メイン関数を実行
if __name__ == '__main__':
    main()