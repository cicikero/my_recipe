##敬体・常体変換コード　Open APIベース

import openai

def convert_to_honorific(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "次の文章を敬体に変換してください。"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.6
    )

    reply = response.choices[0].message.get('content', '')
    return reply

def convert_to_plain(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "次の文章を常体に変換してください。"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.6
    )

    reply = response.choices[0].message.get('content', '')
    return reply

# OpenAI APIの設定
openai.api_key = "API Key"

input_sentence = input('文章を入力してください: ')
mode = input('変換モードを選択してください（敬体: 1, 常体: 2）: ')

if mode == '1':
    converted_sentence = convert_to_honorific(input_sentence)
elif mode == '2':
    converted_sentence = convert_to_plain(input_sentence)
else:
    print('無効なモードが選択されました。')

print('変換結果:', converted_sentence)
