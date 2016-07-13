import connect_to_db

cursor = connect_to_db.connect_to_db('krs', '#3porcI.')

cursor.execute("""SELECT DISTINCT company_name FROM project;""")
companies = cursor.fetchall()

cursor.execute("""SELECT company_name, id, main_color FROM project;""")
rows = cursor.fetchall()

print(companies)
print(rows)