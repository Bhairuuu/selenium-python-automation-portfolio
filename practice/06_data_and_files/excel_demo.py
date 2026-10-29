import openpyxl

book = openpyxl.load_workbook(r"C:\Users\Bhairu\OneDrive\Documents\pythonDemo.xlsx")
sheet = book.active

data = {}   # Use 'data' instead of Dict (avoids shadowing the built-in dict)

# Read value
cell = sheet.cell(row=1, column=2)
print(cell.value)

# Write value
sheet.cell(row=2, column=2).value = "Bhairu"
print(sheet.cell(row=2, column=2).value)

print(sheet.max_row)
print(sheet.max_column)
print(sheet['A5'].value)

# Read data for Testcase2
for i in range(1, sheet.max_row + 1):
    if sheet.cell(row=i, column=1).value == "Testcase 2":
        for j in range(1, sheet.max_column + 1):
            print(sheet.cell(row=i, column=j).value)

            # Store Header : Value
            data[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value

print(data)