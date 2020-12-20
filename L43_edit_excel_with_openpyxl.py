import openpyxl
wb = openpyxl.Workbook()
print(wb)
print(wb.get_sheet_names())
sheet = wb.get_sheet_by_name('Sheet')
print(sheet)

#change or add to cells
sheet['A1'] = 42
sheet['A2'] = 'Hello'
# to save from memory to a file
import os
os.chdir('/Users/btdrew')
sheet2 = wb.create_sheet()
print(sheet2)
print(sheet2.title)
sheet2.title = 'sheep'
print(wb.get_sheet_names())
wb.save('example234.xlsx')
