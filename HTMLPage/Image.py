class Image:
    def __init__(self, filename, alt="image", align="center"):
        self.filename = filename
        self.alt = alt
        self.align = align

    def export(self):
        return f'<img src="{self.filename}" alt="{self.alt}" align="{self.align}">'
