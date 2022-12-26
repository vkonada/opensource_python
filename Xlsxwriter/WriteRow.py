import xlsxwriter

workbook = xlsxwriter.Workbook('write_data.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 1234)     # Writes an int
worksheet.write(1, 0, 1234.56)  # Writes a float
worksheet.write(2, 0, 'Hello')  # Writes a string
worksheet.write(3, 0, None)     # Writes None
worksheet.write(4, 0, True)     # Writes a bool

workbook.close()
