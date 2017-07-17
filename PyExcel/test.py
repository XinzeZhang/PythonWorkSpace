import pyodbc as pysql

conn = pysql.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=localhost;'
    r'DATABASE=AccountingEntry;'
    r'UID=sa;'
    r'PWD=1231'
)
cursor = conn.cursor()
table = 'create table entry\
(\
    entry_id    char(10)    not null,\
    entry_event varchar(max)   null,\
    entry_answer    varchar(max)   null\
)'


cursor.execute(table)
cursor.commit()
if cursor.tables(table='entry').fetchone():
    print('yes it does')
