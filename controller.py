from dominate import document
from dominate.tags import *
from dao import select


def index():
    res = select()
    main_content = div()
    with main_content:
        h1("Hello world")
        for item in res:
            img(src=item[0], alt=item[1])
    return main_content
