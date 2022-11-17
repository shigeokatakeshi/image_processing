from PIL import Image, ImageFont, ImageDraw


def main():
    image_path = "./image/konjikido_01.jpg"
    font_path = "/System/Library/Fonts/ヒラギノ角ゴシック W5.ttc"
    font_size = 100  # 文字の大きさ
    text = "平泉最高"
    color = (255, 255, 255)  # 文字の色

    image = Image.open(image_path)
    image = image.resize((1800, 800))
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(image)

    draw_text_width, draw_text_height = draw.textsize("平泉最高", font=font)

    x = int(image.size[0] / 2 - draw_text_width / 2)
    y = int(image.size[1] / 2 - draw_text_height / 2)

    draw.text((x, y), text, font=font, fill=color)

    image.save("image/konjiki.jpg")


if __name__ == "__main__":
    main()
