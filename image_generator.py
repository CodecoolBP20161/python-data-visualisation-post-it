from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

bg_x = 1024 # x coordinate, number of columns
bg_y = 600
bg_map = []
for i in range(bg_x):
    bg_map.append([])
    for j in range(bg_y):
        bg_map[i].append(0)


img = Image.new("RGB", (bg_x, bg_y), "black")
draw = ImageDraw.Draw(img)


font_library = "/usr/share/fonts/truetype/freefont/FreeSerif.ttf"

# font = ImageFont.truetype(<font-file>, <font-size>)


def generate_image(objects_to_print):
    for i in range(len(objects_to_print)):
        # select tag size
        font = ImageFont.truetype(font_library, objects_to_print[i].size)

        # select tag colour
        text_options = {'fill': objects_to_print[i].color}

        # select tag text
        text_content = objects_to_print[i].name

        # save the size of text in pixels
        text_size = draw.textsize(text_content, font=font)

        # draw.text((x, y),text_content,(r,g,b))
        # text(position, text, fill=None, font=None)
        place = get_place(text_size)
        draw.text(place, text_content, **text_options, font=font)
        for i in range(place[0], place[0] + text_size[0]):
            for j in range(place[1], place[1] + text_size[1]):
                bg_map[i][j] = 1
        # for i in range(len(bg_map)):
        #     print(bg_map[i])


    # draw.text((0, text_size[1]), text_content, **text_options)
    # draw.text((text_size[0], 0), text_content, **text_options)
    # draw.text(text_size, text_content, **text_options)

    # img.save('sample-out.png')
    img.show()


def get_place(text_size):
    new_place = random.randint(0, bg_x - text_size[0] ), random.randint(0, bg_y - text_size[1])



    return new_place
