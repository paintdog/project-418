content = """Chapter;Page"""

content = content.split("\n")
print("{| class='wikitable' width='100%'")
print("! style='width=80 %;' | Chapter\n! style='width=20 %;' | Page")
for line in content:
    if not line == "\n":
        chapter, page = line.split(";")
        chapter = chapter.replace("<b>","'''").replace("</b>","'''")
        print("|-\n| {}\n| style='text-align: right;' | {}".format(chapter, page))
print("|}")
