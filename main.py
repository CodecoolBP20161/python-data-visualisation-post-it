import connect_to_db
from company import Company

# establish connection to database with 1. database name, 2. password
cursor = connect_to_db.make_connection('krs', '#3porcI.')

# chose an option which picture to generate
option = input('Press key 1, 2, 3 or 4 to select an option: ')

if option == '1':
    # get the appropriate data from the database
    cursor.execute("""SELECT DISTINCT company_name, string_agg(main_color, ', '), count(id)
                      FROM project
                      GROUP BY company_name;""")

    # save each row of the extracted data as an instance in a list
    objects_to_print = [Company(row) for row in cursor.fetchall()]
    # print(objects_to_print[15].name, objects_to_print[15].color, objects_to_print[15].project_num)

else:
    print('You should choose option 1 for now, the others are not implemented yet')
