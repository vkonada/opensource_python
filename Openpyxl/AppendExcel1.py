# import openpyxl module
import openpyxl

wb = openpyxl.load_workbook("sample.xlsx")

sheet = wb.active

c = sheet['A3']
c.value = "New Data"

wb.save("sample.xlsx")

###################
# import openpyxl module
import openpyxl

wb = openpyxl.load_workbook("sample.xlsx")

sheet = wb.active

data = (
	(1, 2, 3),
	(4, 5, 6)
)

for row in data:
	sheet.append(row)

wb.save('sample.xlsx')


