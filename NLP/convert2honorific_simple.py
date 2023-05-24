#敬体・常体変換コード　単純置換ベース

def convert_to_honorific(sentence):
    honorific_mapping = {
        'です': 'ます',
        'である': 'でございます',
        'だ': 'です',
        'ですか': 'ますか',
        'でしょうか': 'でしょうか',
        'でしょう': 'でしょう',
        'だろうか': 'でしょうか',
        'だろう': 'でしょう',
        'ない': 'ありません',
        'ません': 'ません',
    }

    for key, value in honorific_mapping.items():
        sentence = sentence.replace(key, value)

    return sentence


def convert_to_plain(sentence):
    plain_mapping = {
        'ます': 'です',
        'でございます': 'である',
        'ですか': 'だ',
        'でしょうか': 'だろうか',
        'でしょう': 'だろう',
        'ありません': 'ない',
        'ません': 'ない',
    }

    for key, value in plain_mapping.items():
        sentence = sentence.replace(key, value)

    return sentence


input_sentence = input('文章を入力してください: ')
mode = input('変換モードを選択してください（敬体: 1, 常体: 2）: ')

if mode == '1':
    converted_sentence = convert_to_honorific(input_sentence)
elif mode == '2':
    converted_sentence = convert_to_plain(input_sentence)
else:
    print('無効なモードが選択されました。')

print('変換結果:', converted_sentence)