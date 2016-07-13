class Company:

    def __init__(self, sql_output):
        # sql_output should be a tuple
        self.name = sql_output[0]
        self.colors = sql_output[1]