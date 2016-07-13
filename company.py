class Company:

    def __init__(self, sql_output):
        # sql_output should be a tuple of company name and color codes as one string
        self.name = sql_output[0]
        self.color = self.average_color(sql_output[1])
        self.size = sql_output[2]*10


    def average_color(self, all_colors):
        # convert a string of colours to a list of colour strings (give default colour white if none)
        if all_colors != None:
            all_colors = all_colors.split(',')
        else:
            all_colors = ['#FFF']

        r = 0
        g = 0
        b = 0

        for i in all_colors:
            hex_num = i.strip()
            r += eval('0x' + hex_num[1] + hex_num[1])
            g += eval('0x' + hex_num[2] + hex_num[2])
            b += eval('0x' + hex_num[3] + hex_num[3])

        return (round(r/len(all_colors)), round(g/len(all_colors)), round(b/len(all_colors)))

