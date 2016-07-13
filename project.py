class Project:
    def __init__(self, sql_output):
        # sql_output should be a tuple of name, main_color, budget_value, budget_currency
        self.name = sql_output[0]
        self.color = self.to_rgb(sql_output[1])
        self.size = round(self.to_eur(eval(sql_output[2]), sql_output[3]) * 0.004)

    @staticmethod
    def to_rgb(color):
        if color is None:
            color = '#FFF'
        r = int(color[1] * 2, 16)
        g = int(color[2] * 2, 16)
        b = int(color[3] * 2, 16)

        return r, g, b

    @staticmethod
    def to_eur(value, currency):
        if currency == 'USD':
            return value * 0.9
        elif currency == 'GBP':
            return value * 1.19
        else:
            return value
