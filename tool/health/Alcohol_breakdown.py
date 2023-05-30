'''
飲酒後にアルコールが分解されるまでの時間を概算するPythonアプリ

仕様:
・標準入力で、体重を指定する
・標準入力で、飲んだお酒と量を指定する
・アルコール量(g) = 飲んだお酒の量(ml) × アルコール度数(%) × 0.8 ÷ 100
・1時間で分解できるアルコール量を計算する。計算式は「 体重 (kg) × 0.1 = 1時間で分解できるアルコール量（g） 」
・選択肢として表示する飲んだ酒の種類、量、含まれるアルコール量は別に定義。定義内容は、酒の種類×単位(本、杯など)
・最後に摂取したアルコール量と分解にかかる時間(時間単位)で表示
'''

def calculate_time_to_breakdown_alcohol():
    weight = float(input("体重を入力してください(kg): "))
    
    # アルコール度数
    alcohol_type = {"ビール": 5, "日本酒": 15, "焼酎": 25, "ワイン": 12} 

    # アルコール摂取単位(ml)
    alcohol_amount = {"ビール": 500, "日本酒": 180, "焼酎": 180, "ワイン": 100} 
    
    alcohol_list = []

    while True:
        alcohol = input("飲んだお酒を選択してください(ビール、日本酒、焼酎、ワイン)。終了する場合は「q」を入力してください: ")
        if alcohol == "q":
            break
        amount = float(input(f"{alcohol}の飲んだ量を入力してください(単位:ビールなら中瓶の本数、日本酒なら合、焼酎・ワインなら杯): "))
        alcohol_list.append((alcohol, amount))

    # 飲んだアルコール量(g)
    alcohol_content = sum([alcohol_amount[alcohol] * alcohol_type[alcohol] * amount for alcohol, amount in alcohol_list]) * 0.8 / 100 

    # 1時間で分解できるアルコール量(g)
    breakdown_alcohol_content = weight * 0.1

    # アルコールが分解されるまでの時間(時)
    breakdown_time = (alcohol_content / (breakdown_alcohol_content))
    
    # 結果出力
    print(f"飲んだアルコール量は{alcohol_content:.2f}gです。")
    print(f"アルコールが分解されるまでの時間は{breakdown_time:.2f}時間です。")

    
#実行
calculate_time_to_breakdown_alcohol()


