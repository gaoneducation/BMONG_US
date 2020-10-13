from PIL import Image
import glob
from pathlib import Path


class Customize:
    def __init__(self):
        # 색 정의
        self.red = (255, 0, 0, 255), (160, 0, 0, 255)
        self.green = (0, 255, 0, 255), (0, 160, 0, 255)
        self.blue = (0, 0, 255, 255), (0, 0, 160, 255)
        self.pink = (255, 0, 255, 255), (160, 0, 160, 255)
        self.custom_color = self.red

    def colorSwap(self, custom_color):
        # 매개변수에 따라 색상 할당
        if custom_color == "red":
            self.custom_color = self.red
        elif custom_color == "green":
            self.custom_color = self.green
        elif custom_color == "blue":
            self.custom_color = self.blue
        elif custom_color == "pink":
            self.custom_color = self.pink
        else:
            pass

        self.createModifiedSprites("data/Imposter/idle/idle.png")

        for path in glob.glob('data/Imposter/walk/*.png'):
            self.createModifiedSprites(path)

    def createModifiedSprites(self, path):
        src = Image.open(path)
        px = src.load()
        width, height = src.size
        for i in range(width):
            for j in range(height):
                pixel = px[i, j]
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                if pixel == self.blue[0] or (70 < b < 255) and not (g > 220 and b > 80):
                    px[i, j] = self.custom_color[1]
                if pixel == self.red[0] or (70 < r < 255) and not (g > 220 and r > 80):
                    px[i, j] = self.custom_color[0]
        src.save('data/Imposter/temp/' + Path(path).name)


customize = Customize()
customize.colorSwap('red')
