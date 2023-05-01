class Table:
    def __init__(self, dimx, dimy, data):
        self.dimx = dimx
        self.dimy = dimy
        self.data = ["-"] * dimx * dimy
        for i in range(len(data)):
            self.data[i] = str(data[i])

    def export(self):
        exp = '<style>\n    table, th, td {\n      border:1px solid black;\n    }\n  </style>\n  <table style="width:100%">\n'
        for i in range(self.dimx):
            exp += "    <tr>\n"
            for j in range(self.dimy):
                exp += f"      <th>{self.data[i*self.dimy + j]}</th>\n"
            exp += "    </tr>\n"
        exp += "  </table>\n"
        return exp