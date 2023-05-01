from PIL import Image, ImageDraw, ImageColor

# ツリーの描画
def tree(x1, y1, angle, depth, draw):
    if depth:
        x2 = x1 + int(depth * 5.0 * angle)
        y2 = y1 + int(depth * 5.0)
        draw.line((x1, y1, x2, y2), fill="green", width=depth)
        tree(x2, y2, angle - 20, depth - 1, draw)
        tree(x2, y2, angle + 20, depth - 1, draw)

# 画像の生成
def generate_tree_image(width, height):
    img = Image.new("RGB", (width, height), color=ImageColor.getrgb("white"))
    draw = ImageDraw.Draw(img)
    tree(width//2, height//2, -90, 9, draw)
    return img

# 画像の保存
def save_image(img, filename):
    img.save(filename)

# メインプログラム
def main():
    # 画像の生成
    img = generate_tree_image(800, 800)
    # 画像の保存
    save_image(img, "fractal_tree.png")

if __name__ == '__main__':
    main()
