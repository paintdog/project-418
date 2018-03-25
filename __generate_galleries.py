import os
import webbrowser

PATH = "./png/"


# __style__.css
css_file = """body {
    background: DimGrey;
}

a:link {
    color: White;
}

a:visited {
    color: LightGray;
}
"""


# index.html
html_page = """<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<h2>{title}</h2>
{content}
</body>
</head>"""


html_pic = """<!DOCTYPE html>
<html>
<head>
    <title>{page}</title>
    <link rel="stylesheet" href="style.css">
    <script>
      document.onkeydown = function(evt) {{
        evt = evt || window.event;
        switch (evt.keyCode) {{
          case 37:
            back();
	    break;
          case 39:
            forward();
	    break;
        }}
      }};
      
      function back() {{
	 window.location.replace('{back}')
      }}

      function forward() {{
        window.location.replace('{forward}')
      }}
    </script>
  </head>
  <body>
    <header>
      <p style="text-align: center;"><a href="{back}">Back</a> | {content} <a href="index.html">Index</a> | <a href="{forward}">Forward</a></p>
    </header>

    <div>
      <img src="{image}" width="100%" style="display: block; margin-left: auto; margin-right: auto;" />
    </div>

    <footer>
      <p style="text-align: center;"><a href="{back}">Back</a> | {content} <a href="index.html">Index</a> | <a href="{forward}">Forward</a></p>
    </footer>
  </body>
</html>"""


def generate_content_page():
    with open(os.path.join(PATH, "__content__.txt"), "r", encoding="utf-8") as f:
        w = f.readlines()

    table = []
    table.append("<table width='100%'>")
    table.append("<tr>")
    table.append("<th style='width: 80%;'>Chapter</th>")
    table.append("<th style='width: 20%;'>Page</th>")
    table.append("</tr>")

    table.append("<tbody>")
    for line in w:
        if ";" in line:
            table.append("<tr>")
            headline, page = line.strip("\n").split(";")
            try:
                page = int(page)
                table.append("<td><a href='{:04d}.html'>{}</a></td>".format(page, headline))
                table.append("<td style='text-align: right;'><a href='{:04d}.html'>{}</a></td>".format(page, page))
            except ValueError:
                table.append("<td><a href='{}.html'>{}</a></td>".format(page, headline))
                table.append("<td style='text-align: right;'><a href='{}.html'>{}</a></td>".format(page, page))
            table.append("</tr>")

    table.append("</tbody>")
    table.append("</table>")
    with open("content.html", "w") as f:
        f.write(html_page.format(title="Content", content="\n".join(table)))
    

def generate_html_pages(path = PATH):
    
    pics = [file for file in os.listdir(path) if file.endswith(".png")]

    # index.html
    with open("index.html", "w") as f:
        content = """<div style='column-count:8; -webkit-column-count: 8;-moz-column-count: 8;'>
                       <ul>
                         {}
                       </ul>
                     </div>"""
        content = content.format("\n".join(["<li><a href='{}.html'>{}.html</a></li>".format(pic.split(".")[0], pic.split(".")[0]) for pic in pics]))
        f.write(html_page.format(title="Index", content=content))

    # style.css
    with open("style.css", "w") as f:
        f.write(css_file)

    # content.html
    if os.path.isfile(os.path.join(PATH, "__content__.txt")):
        content = "<a href='content.html'>Inhalt</a> | "
        generate_content_page()
    else:
        content = None    

    # pic.html
    for i, pic in enumerate(pics):

        if i == 0:
            back = "index.html"
        else:
            back = "{}.html".format(pics[i-1].split(".")[0])

        if i == len(pics) - 1:
            forward = "index.html"
        else:
            forward = "{}.html".format(pics[i+1].split(".")[0])

        filename = "{}.html".format(pic.split(".")[0])

        with open(filename, "w") as f:
            f.write(html_pic.format(content=content, page=pic.split(".")[0], back=back, forward=forward, image=os.path.join(path, pic)))

    webbrowser.open("index.html")
    

if __name__ == "__main__":
    generate_html_pages(PATH)

