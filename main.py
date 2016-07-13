import connect_to_db
from company import Company

# establish connection to database with 1. database name, 2. password
cursor = connect_to_db.make_connection('krs', '#3porcI.')

# chose an option which picture to generate
option = input('Press key 1, 2, 3 or 4 to select an option: ')

if option == '1':
    # get the appropriate data from the database
    cursor.execute("""SELECT DISTINCT company_name, string_agg(main_color, ', ') id
                      FROM project
                      GROUP BY company_name;""")

    # save each row of the extracted data as an instance in a list
    company_list = [Company(row) for row in cursor.fetchall()]
    print(company_list[1].name, company_list[1].color)

else:
    print('You should choose option 1 for now, the others are not implemented yet')