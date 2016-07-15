from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

bg_x = 1300  # x coordinate, number of columns
bg_y = 700
bg_map = []
for i in range(bg_x):
    bg_map.append([])
    for j in range(bg_y):
        bg_map[i].append(True)


img = Image.new("RGB", (bg_x, bg_y), "black")
draw = ImageDraw.Draw(img)


font_library = "/usr/share/fonts/truetype/freefont/FreeSerif.ttf"


def generate_image(objects_to_print):
    objects_to_print = list(sorted(objects_to_print, key=lambda x: x.size, reverse=True))
    for word in range(len(objects_to_print)):
        # select tag size
        font = ImageFont.truetype(font_library, objects_to_print[word].size)

        # select tag colour
        text_options = {'fill': objects_to_print[word].color}

        # select tag text
        text_content = objects_to_print[word].name

        # save the size of text in pixels
        text_size = draw.textsize(text_content, font=font)

        place = get_place(text_size)
        draw.text(place, text_content, **text_options, font=font)
        for p in range(place[0], place[0] + text_size[0]):
            for k in range(place[1], place[1] + text_size[1]):
                bg_map[p][k] = False

    img.show()


def get_place(text_size):
    taken = False
    new_place = (0, 0)
    while not taken:
        taken = True
        new_place = random.randint(0, bg_x - text_size[0]), random.randint(0, bg_y - text_size[1])
        for m in range(new_place[0], new_place[0] + text_size[0]):
            for n in range(new_place[1] + text_size[1]):
                taken = taken and bg_map[m][n]

    return new_place
