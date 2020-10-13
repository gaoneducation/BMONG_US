from PIL import Image


def colorSwap(custom_color):
    # 색 정의
    red = (255, 0, 0, 255), (160, 0, 0, 255)
    green = (0, 255, 0, 255), (0, 160, 0, 255)
    blue = (0, 0, 255, 255), (0, 0, 160, 255)
    pink = (255, 0, 255, 255), (160, 0, 160, 255)

    # 매개변수에 따라 색상 할당
    if custom_color == "red":
        custom_color = red
    elif custom_color == "green":
        custom_color = green
    elif custom_color == "blue":
        custom_color = blue
    elif custom_color == "pink":
        custom_color = pink
    else:
        custom_color = red

    src = Image.open("data/Imposter/idle/idle.png")
    px = src.load()
    width, height = src.size
    for i in range(width):
        for j in range(height):
            pixel = px[i, j]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if pixel == blue[0] or (70 < b < 255) and not (g > 220 and b > 80):
                px[i, j] = custom_color[1]
            if pixel == red[0] or (70 < r < 255) and not (g > 220 and r > 80):
                px[i, j] = custom_color[0]
    src.save('data/Imposter/custom/idle.png')
