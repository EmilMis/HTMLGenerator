class Paragraph:
    def __init__(self, align="center", font="Times New Roman", color="Black", size="5", content="empty paragraph"):
        self.align = align
        self.font = font
        self.color = color
        self.size = size
        self.content = content

    def export(self):
        return f'<p align="{self.align}"><font face="{self.font}" color="{self.color}" size="{self.size}">{self.content}</font></p> '
