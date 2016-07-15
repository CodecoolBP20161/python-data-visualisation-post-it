

class Status:

    def __init__(self, sql_output):
        self.name = sql_output[0]
        self.color = self.color_of_status(sql_output[1])
        self.size = round(sql_output[1]*5)

    @staticmethod
    def color_of_status(output):
        if output == 1:
            color = (255, 0, 0)
        elif output == 2:
            color = (255, 131, 6)
        elif output == 3:
            color = (255, 255, 0)
        else:
            color = (0, 255, 0)
        return color
