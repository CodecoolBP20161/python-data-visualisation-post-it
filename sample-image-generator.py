from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from main import company_list
import random

img = Image.new("RGB", (640, 640), "black")
draw = ImageDraw.Draw(img)
font_library = "/usr/share/fonts/truetype/freefont/FreeSerif.ttf"
# font = ImageFont.truetype(<font-file>, <font-size>)


for i in range(len(company_list)):
    # select tag size
    font = ImageFont.truetype(font_library, 10*company_list[i].project_num)
    # select tag colour
    text_options = {'fill': company_list[i].color}
    # select tag text
    text_content = company_list[i].name
    # save the size of text in pixels
    text_size = draw.textsize(text_content)
    # draw.text((x, y),text_content,(r,g,b))
    draw.text((random.randint(0, 555), random.randint(0, 555)), text_content, **text_options, font=font)



# draw.text((0, text_size[1]), text_content, **text_options)
# draw.text((text_size[0], 0), text_content, **text_options)
# draw.text(text_size, text_content, **text_options)


#img.save('sample-out.png')
img.show()