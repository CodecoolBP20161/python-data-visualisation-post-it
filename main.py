import connect_to_db
from company import Company
from project import Project
from status import Status
import image_generator


# establish connection to database
cursor = connect_to_db.make_connection()

# chose an option which picture to generate
option = input('Press key 1, 2, 3 or 4 to select an option: ')

if option == '1':
    # get the appropriate data from the database
    cursor.execute("""SELECT DISTINCT company_name, string_agg(main_color, ', '), count(id)
                      FROM project
                      GROUP BY company_name;""")

    # save each row of the extracted data as an instance in a list
    objects_to_print = [Company(row) for row in cursor.fetchall()]

    # make an image from the instances
    image_generator.generate_image(objects_to_print)

elif option == '2':
    cursor.execute("""SELECT name, main_color, budget_value, budget_currency
                      FROM project
                      WHERE name LIKE '_%';""")

    objects_to_print = [Project(row) for row in cursor.fetchall()]

    image_generator.generate_image(objects_to_print)
elif option == '3':
    cursor.execute("""SELECT name, main_color, status
                      FROM project
                      WHERE name LIKE '_%';""")

    objects_to_print = [Status(row) for row in cursor.fetchall()]

    image_generator.generate_image(objects_to_print)
else:
    print('You should choose option 1 for now, the others are not implemented yet')
