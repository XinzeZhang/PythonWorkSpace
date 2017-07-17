import pyexcel as pe

sheet = pe.get_records(file_name="entry.xlsx")

for row in sheet:
    print(row['event'])
