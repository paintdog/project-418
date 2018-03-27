import re

content = """Chapter;Page"""

content = content.split("\n")

def generate_content_table(content):
    print("{| class='wikitable' width='100%'")
    print("! style='width=80 %;' | Chapter\n! style='width=20 %;' | Page")
    for line in content:
        if not line == "":
            chapter, page = line.split(";")
            chapter = chapter.replace("<b>","'''").replace("</b>","'''")
            print("|-\n| {}\n| style='text-align: right;' | {}".format(chapter, page))
    print("|}")


def generate_improved_table(content):
    print("{| class='wikitable' width='100%'")
    print("! style='width=80 %;' | Chapter\n! style='width=20 %;' | Page")
    for line in content:
        if not line == "":
            chapter, page = line.split(";")
            if chapter.startswith("<b> Part"):
                # <b>Part I: Title</b>;1
                chapter = chapter.replace("<b>","'''").replace("</b>","'''")
                print("|-\n| {}\n| style='text-align: right;' | {}".format(chapter, page))
            elif re.match("^<b>\d* \w+", chapter):
                # <b>1 Subtitle</b>;1
                chapter = chapter.replace("<b>","'''").replace("</b>","'''")
                print("|-\n| \n:{}\n| style='text-align: right;' | {}".format(chapter, page))
            elif re.match("^\d+\.\d+ \w", chapter):
                # 1.1 Sub-Subtitle;2
                print("|-\n| \n::{}\n| style='text-align: right;' | {}".format(chapter, page))
            else:
                print("|-\n| {}\n| style='text-align: right;' | {}".format(chapter, page))
    print("|}")


generate_improved_table(content)
