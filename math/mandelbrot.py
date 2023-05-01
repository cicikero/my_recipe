from PIL import Image, ImageColor

# マンデルブロ集合の計算
def mandelbrot(c, max_iterations):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iterations:
        z = z*z + c
        n += 1
    if n == max_iterations:
        return 0
    else:
        return n/max_iterations

# 画像の生成
def generate_mandelbrot_image(width, height, zoom=1, x_offset=0, y_offset=0, max_iterations=1000):
    img = Image.new("RGB", (width, height), color=ImageColor.getrgb("black"))
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            # 座標の計算
            cx = 1.5 * (x - width / 2) / (0.5 * zoom * width) + x_offset
            cy = 1.0 * (y - height / 2) / (0.5 * zoom * height) + y_offset
            # マンデルブロ集合の計算
            color = int(255 * mandelbrot(complex(cx, cy), max_iterations))
            # ピクセルの描画
            pixels[x, y] = (color, color, color)

    return img

# 画像の保存
def save_image(img, filename):
    img.save(filename)

# メインプログラム
def main():
    # 画像の生成
    img = generate_mandelbrot_image(800, 600, zoom=1, x_offset=0, y_offset=0, max_iterations=1000)
    # 画像の保存
    save_image(img, "mandelbrot.png")

if __name__ == '__main__':
    main()
