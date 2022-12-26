import xlsxwriter

workbook = xlsxwriter.Workbook('write_data.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 1234)     # Writes an int
worksheet.write(1, 0, 1234.56)  # Writes a float
worksheet.write(2, 0, 'Hello')  # Writes a string
worksheet.write(3, 0, None)     # Writes None
worksheet.write(4, 0, True)     # Writes a bool

workbook.close()

###############################
#Unicode data in Excel is encoded as UTF-8. XlsxWriter also supports writing UTF-8 data. This generally requires that your source file is UTF-8 encoded:

worksheet.write('A1', 'Some UTF-8 text')

###############################
import xlsxwriter

workbook = xlsxwriter.Workbook('write_list.xlsx')
worksheet = workbook.add_worksheet()

my_list = [1, 2, 3, 4, 5]

for row_num, data in enumerate(my_list):
    worksheet.write(row_num, 0, data)

workbook.close()

#Or if you wanted to write this horizontally as a row:

import xlsxwriter

workbook = xlsxwriter.Workbook('write_list.xlsx')
worksheet = workbook.add_worksheet()

my_list = [1, 2, 3, 4, 5]

for col_num, data in enumerate(my_list):
    worksheet.write(0, col_num, data)

workbook.close()


####################


For a list of lists structure you would use two loop levels:

import xlsxwriter

workbook = xlsxwriter.Workbook('write_list.xlsx')
worksheet = workbook.add_worksheet()

my_list = [[1, 1, 1, 1, 1],
           [2, 2, 2, 2, 1],
           [3, 3, 3, 3, 1],
           [4, 4, 4, 4, 1],
           [5, 5, 5, 5, 1]]

for row_num, row_data in enumerate(my_list):
    for col_num, col_data in enumerate(row_data):
        worksheet.write(row_num, col_num, col_data)

workbook.close()

##############

The worksheet class has two utility functions called write_row() and write_column() which are basically a loop around the write() method:

import xlsxwriter

workbook = xlsxwriter.Workbook('write_list.xlsx')
worksheet = workbook.add_worksheet()

my_list = [1, 2, 3, 4, 5]

worksheet.write_row(0, 1, my_list)
worksheet.write_column(1, 0, my_list)

workbook.close()
##################

Writing dicts of data
Unlike lists there is no single simple way to write a Python dictionary to an Excel worksheet using Xlsxwriter. The method will depend of the structure of the data in the dictionary. Here is a simple example for a simple data structure:

import xlsxwriter

workbook = xlsxwriter.Workbook('write_dict.xlsx')
worksheet = workbook.add_worksheet()

my_dict = {'Bob': [10, 11, 12],
           'Ann': [20, 21, 22],
           'May': [30, 31, 32]}

col_num = 0
for key, value in my_dict.items():
    worksheet.write(0, col_num, key)
    worksheet.write_column(1, col_num, value)
    col_num += 1

workbook.close()
