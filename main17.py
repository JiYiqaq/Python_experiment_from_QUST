from PIL import Image, ImageDraw, ImageFont

def set_watermark(image_path, text, outfile):
    # 打开图像文件
    im = Image.open(image_path).convert("RGBA")

    # 创建字体对象和绘制对象
    font_path = "msyh.ttc"
    font_size = 50
    im_font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(im)

    # 获取文本的边界框
    bbox = im_font.getbbox(text)

    # 计算文本的位置
    x = im.width - bbox[2] - 10
    y = im.height - bbox[3] - 10

    # 绘制文本
    draw.text((x, y), text, fill=(255, 0, 0), font=im_font)

    # 保存图像
    result = im.convert("RGB")
    result.save(outfile, "JPEG")

if __name__ == '__main__':
    set_watermark("绿色麦田.jpeg", "水印", "output.jpg")
