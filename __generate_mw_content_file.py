content = """Chapter;Page"""

content = content.split("\n")
print("{| class='wikitable' width='100%'")
print("! style='width=80 %;' | Chapter\n! style='width=20 %;' | Page")
for line in content:
    chapter, page = line.split(";")
    print("|-\n| {}\n| style='text-align: right;' | {}".format(chapter, page))
print("|}")