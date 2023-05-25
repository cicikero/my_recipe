#Open AIのAPIを利用して、文章の要約と詳述を行うコード

import openai

def convert_to_short(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "次の文章を短くしてください。"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    reply = response.choices[0].message.get('content', '')
    return reply

def convert_to_long(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "次の文章を長くしてください。"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )

    reply = response.choices[0].message.get('content', '')
    return reply

# OpenAI APIの設定
openai.api_key = "API Keyを入れる"

input_sentence = input('文章を入力してください: ')
mode = input('どちらに変換するかを選択してください（短く: 1, 長く: 2）: ')

if mode == '1':
    converted_sentence = convert_to_short(input_sentence)
elif mode == '2':
    converted_sentence = convert_to_long(input_sentence)
else:
    print('無効なモードが選択されました。')

print('変換結果:', converted_sentence)