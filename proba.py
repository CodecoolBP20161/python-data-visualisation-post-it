from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

class PictureDraw():
    list_of_textboxes = []
    list_of_reserved_coordinates = []



    def draw(self):
        img = Image.new("RGB", (500, 500), "red")
        draw = ImageDraw.Draw(img)
        for i in self.list_of_textboxes:
            # font = ImageFont.truetype(<font-file>, <font-size>)
            fnt = ImageFont.truetype("beyond_the_mountains.ttf", i.size)

            text_content = # company name goes here
            text_size = draw.textsize(text_content)
            # draw.text((x, y),text_content,(r,g,b))
            rand_num1 = random.randint(100, 1200)
            rand_num2 = random.randint(100, 700)
            draw.text((rand_num1, rand_num2), text_content, font=fnt, fill=i.color)
            # draw.text((0, text_size[1]), text_content, **text_options)
        img.save('proba.png')


    def add_new(self, color, size, name):
        self.list_of_textboxes.append(TextBox(name, color, size))