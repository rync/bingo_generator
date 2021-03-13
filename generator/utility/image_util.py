import imgkit
import pandas as pd
import os

css = """
<style type="text/css">

table {
color: #333;
font-family: Helvetica, Arial, sans-serif;
border-collapse:
collapse; 
border-spacing: 0;
}

td, th {
border: 1px solid transparent; /* No more visible border */
height: 180px;
width: 240px;
text-align: center;
}

th {
background: #414141; /* Darken header a bit */
font-weight: bold;
font-size: 92px;
color: #DFDFDF;
}

td {
background: #FAFAFA;
font-size: 32px;
}

table tr:nth-child(odd) td:nth-child(even),
tr:nth-child(even) td:nth-child(odd) {
background-color: #DFDFDF;
}
</style>
"""

footer = "<div style=\"font-size:8px\">{}</div>"

def bingo_table_to_image(table, dest_name="output/bingo.png", table_id=None, format="png"):
    df = pd.DataFrame(table, columns=["B", "I", "N", "G", "O"])

    f = open("output/temp.html", "a")
    f.write(css)
    f.write(df.to_html(index=False)) # Index = false will remove that annoying row header
    f.write(footer.format(table_id))
    f.close()
    
    imgkit.from_file("output/temp.html", dest_name, {"format": format})
    os.remove("output/temp.html")