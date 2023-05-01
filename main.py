from HTMLPage import *

page = Page(title="portfolio")
page.add(Paragraph(size=12, content="Hello, my name is EmilMis"))
page.add(Image(filename="cattons/sleepycat.jpg"))
page.add(Paragraph(size=7,
                   content="I do some stuff, sometimes",
                   align="left"
                   ))
page.add(Table(3, 3, ["something here", "some numbers here", 1, "haha, the rest is empty"]))
page.export("document.html")
