def calculate_time_to_breakdown_alcohol():
    weight = float(input("体重を入力してください(kg): "))
    alcohol_type = {"ビール": 5, "日本酒": 15, "焼酎": 25, "ワイン": 12} # アルコール度数
    alcohol_amount = {"ビール": 350, "日本酒": 180, "焼酎": 180, "ワイン": 100} # 単位(ml)
    alcohol_list = []
    while True:
        alcohol = input("飲んだお酒を選択してください(ビール、日本酒、焼酎、ワイン)。終了する場合は「q」を入力してください: ")
        if alcohol == "q":
            break
        amount = float(input(f"{alcohol}の飲んだ量を入力してください(単位: ml): "))
        alcohol_list.append((alcohol, amount))
    alcohol_content = sum([alcohol_amount[alcohol] * alcohol_type[alcohol] * amount for alcohol, amount in alcohol_list]) * 0.8 / 100 # 飲んだアルコール量(g)
    breakdown_alcohol_content = weight * 0.1 # 1時間で分解できるアルコール量(g)
    breakdown_time = (alcohol_content / (breakdown_alcohol_content * 10)) # アルコールが分解されるまでの時間(時)
    print(f"飲んだアルコール量は{alcohol_content:.2f}gです。")
    print(f"アルコールが分解されるまでの時間は{breakdown_time:.2f}時間です。")

calculate_time_to_breakdown_alcohol()



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


