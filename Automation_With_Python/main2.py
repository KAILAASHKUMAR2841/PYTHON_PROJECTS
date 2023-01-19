from openpyxl import Workbook
from openpyxl.chart import BarChart3D, Reference

wb = Workbook()
ws = wb.active

rows = [
    (None, 2013, 2014),
    ("Apples", 5, 4),
    ("Oranges", 6, 2),
    ("Pears", 8, 3)
]
for row in rows:
  ws.append(row)

data = Reference(ws, min_col=2, max_col=3, min_row=2, max_row=4)
chart = BarChart3D()
chart.add_data(data)
ws.add_chart(chart,'a9')

wb.save('bar32d.xlsx')