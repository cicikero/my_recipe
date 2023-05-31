import re

def extract_matching_parts(file_path, regex_pattern):
    with open(file_path, 'r') as file:
        text = file.read()
        matches = re.findall(regex_pattern, text)
        for match in matches:
            print(match)

# テキストファイルのパスと正規表現パターンを指定します
file_path = 'path/to/your/file.txt'
regex_pattern = r'<([^>]+)>'

# 関数を呼び出してマッチする部分を抽出し、出力します
extract_matching_parts(file_path, regex_pattern)
