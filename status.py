from project import Project


class Status:

    def __init__(self, sql_output):
        self.name = sql_output[0]
        self.color = Project.to_rgb(sql_output[1])
        self.size = round(sql_output[2]*sql_output[2]*1.5)