from HTMLPage.Paragraph import Paragraph
from HTMLPage.Image import Image
from HTMLPage.Table import Table


class Page:
    def __init__(self, title="New Page", background_color="white"):
        self.content = []
        self.title = title
        self.background_color = background_color

    def set_title(self, title):
        self.title = title

    def add(self, element):
        self.content.append(element)

    def export(self, filename="index.html"):
        file = open(filename, "w")
        file.write(
            f'<!DOCTYPE html>\n'
            f'<html lang="en">\n'
            f'<head>\n'
            f'  <title>{self.title}</title>\n'
            f'</head>\n'
            f'<body style="background-color:{self.background_color};">\n'
        )

        for element in self.content:
            file.write(f'  {element.export()}\n')

        file.write(
            f'</body>\n'
            f'</html>'
        )

        file.close()
