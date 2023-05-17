# ライブラリのインポート
import numpy as np
import matplotlib.pyplot as plt
import numba # numbaをインポート
import colorsys

# グラフのサイズと解像度
plt.figure(figsize=(6, 6), dpi=100)

# 複素平面の範囲と刻み幅
re_min, re_max = -2, 2
im_min, im_max = -2, 2
re_step = (re_max - re_min) / 1000
im_step = (im_max - im_min) / 1000

# 複素数cの設定
a = -0.8
b = 0.156
c = complex(a, b)

# ジュリア集合を描画する関数（numbaで高速化）
@numba.njit # numbaのデコレータを付ける
def julia(re, im):
    z = complex(re, im) # 初期値z0
    n = 0 # 繰り返し回数
    while abs(z) < 2 and n < 100: # zが発散しないかぎり繰り返す
        z = z**2 + c # 漸化式
        n += 1 # 回数をカウント
    return n # 回数を返す

# 色の設定（HSV色空間）
hsv_tuples = [(x*1.0/100, 0.5, 0.5) for x in range(100)]
rgb_tuples = list(map(lambda x: colorsys.hsv_to_rgb(*x), hsv_tuples))

# 複素平面上の点に対してjulia関数を適用して色を付ける（numpyで高速化）
re_array = np.arange(re_min, re_max, re_step) # 実部の配列
im_array = np.arange(im_min, im_max, im_step) # 虚部の配列
n_array = np.zeros((len(re_array), len(im_array))) # 繰り返し回数の配列
for i in range(len(re_array)):
    for j in range(len(im_array)):
        n_array[i][j] = julia(re_array[i], im_array[j]) # 繰り返し回数を取得

# グラフの表示（matplotlibで高速化）
plt.imshow(n_array.T, cmap="hsv", extent=[re_min, re_max, im_min, im_max], origin="lower") # 配列を画像として表示
plt.axis("off") # 軸を非表示にする
plt.show() # グラフを表示する
