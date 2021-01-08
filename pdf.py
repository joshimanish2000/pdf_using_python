#! /usr/bin/env python3

books_dict = {"Factfulness, Hans Rosling":1, "The Fountainhead, Ayn Rand":2, "Where the Forest meets the Stars, Glendy Vanderah":3, "The Silent Patient, Alex Michaelids":4, "Atlas Shrugged, Ayn Rand":5, "The Rosie Project, Graeme Simsion":6,
"Why We Sleep, Matthew Walker":7, "Sapiens, Yuval Noah Harari":8, "Twenty One Lessons for the Twenty First Century, Yuval Noah Harari":9, "To Kill a Mockingbird, Harper Lee":10, "The Hitchhiker's Guide to the Galaxy, Douglas Adams":11, "Ready Player One, Ernest Cline":12}

books_list = []
for book_name, book_order in books_dict.items():
  books_list.append([book_name, book_order])

from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("/tmp/report.pdf")

from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()

from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
report_pie = Pie(width=10*inch, height=10*inch)

title = Paragraph("A list of books I read or listened to in 2020",styles["h1"])
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
table = Table(data=books_list, style=table_style, hAlign="LEFT")
report_pie.data = []
report_pie.labels = []
for book in sorted(books_dict):
  report_pie.data.append(books_dict[book])
  report_pie.labels.append(book)

print(report_pie.data, sorted(books_dict))

report_chart = Drawing()
report_chart.add(report_pie)
report.build([title, table,report_chart])
