import os
import csv
import shutil
from tempfile import NamedTemporaryFile


class Academy:
    def display_title_bar(self):
        # Clears the terminal screen, and displays a title bar.
        os.system('cls')

        print("\t**********************************************")
        print("\t***  Welcome to my IT Academy!  ***")
        print("\t**********************************************")

    def get_user_choice(self):
        print("\n[1] See the list of course.")
        print("[2] Register for a course.")
        print("[3] Display students information.")
        print("[4] Update students information.")
        print("[5] Delete students information.")
        print("[6] Refund")
        print("[q] Quit.")

        return input("What would you like to do? ")

    def show_courses(self, filename):
        print("\nHere are the list of courses we offer: ")
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0], row[1])

    def register(self, filename):
        with open('students_info.csv', 'w', newline='') as file:
            fieldnames = ['name', 'roll', 'course', 'is_graduated', 'fee']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            print("Thank you for registering!")

    def display_info(self, filename):
        print("\nHere are the students information: ")
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = [tuple(row) for row in reader]
        print(data)

    def update_info(self, filename, roll, change_column, value):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        fieldnames = ['name', 'roll ', 'course', 'is_graduated', 'fee_paid']
        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            for row in reader:
                if str(roll) == row['roll']:
                    for field in row:
                        if change_column == field:
                            row[field] = value
                    writer.writerow({"roll": row["roll"], 'name': row['name'], 'course': row['course'],
                                     'is_graduated': row['is_graduated'], 'fee_paid': row["fee_paid"]})

                else:
                    writer.writerow({"roll": row["roll"], 'name': row['name'], 'course': row['course'],
                                     'is_graduated': row['is_graduated'], 'fee_paid': row["fee_paid"]})
            shutil.move(tempfile.name, filename)
            print("!!!Successfully updated information!!!!")

    def remove_info(self, filename, roll_no):
        lines = list()
        with open(filename, 'r') as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                lines.append(row)
                if int(row['roll']) == roll_no:
                    lines.remove(row)
        keys = lines[0].keys()
        print(list(keys))
        with open(filename, 'w') as writeFile:
            writer = csv.DictWriter(writeFile, keys)
            writer.writeheader()
            writer.writerows(lines)

    def refund(self, filename, s_id):
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if bool(row['is_graduated']) is True and int(row['roll']) == s_id:
                    print("You have successfully graduated form {} course and your refund amount is Rs.20000".format(
                        row['course']))
                    break


with open("courses.csv", "w", newline='') as file:
    fieldnames = ['course', 'price']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'course': 'Python', 'price': 20000})
    writer.writerow({'course': 'OOP', 'price': 20000})
    writer.writerow({'course': 'Django', 'price': 20000})
    writer.writerow({'course': 'Web Development', 'price': 20000})

with open("students_info.csv", "w") as file:
    fieldnames = ['name', 'roll', 'course', 'is_graduated', 'fee_paid']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Salina', 'roll': 1, 'course': 'Python',
                     'is_graduated': False, 'fee_paid': 10000})
    writer.writerow({'name': 'Sushmita', 'roll': 2, 'course': 'OOP',
                     'is_graduated': True, 'fee_paid': 20000})
    writer.writerow({'name': 'Oppo', 'roll': 3, 'course': 'Django',
                     'is_graduated': True, 'fee_paid': 20000})

choice = ''
op = Academy()
op.display_title_bar()
while choice != 'q':
    choice = op.get_user_choice()

    # Respond to the user's choice.
    if choice == '1':
        op.show_courses('courses.csv')

    elif choice == '2':
        roll = input("Enter your roll no: ")
        name = input("Enter your name: ")
        amt = input("Enter the amount you want to deposit: ")
        subject = input("Enter the course: ")
        op.register('students_info')

    elif choice == '3':
        op.display_info('students_info.csv')

    elif choice == '4':
        id = int(input("Enter your roll: "))
        col = input("Enter column you want to change:")
        val = input("Enter value to change: ")
        op.update_info("students_info.csv", id, col, val)

    elif choice == '5':
        roll = input("Enter your roll: ")
        op.remove_info('students_info.csv', roll)

    elif choice == '6':
        roll = input("Enter your roll: ")
        op.refund('students_info.csv', roll)

    elif choice == 'q':
        print("\nWe hope you found the course for you! Happy Learning!")
        break

    else:
        print("\nInvalid choice.\n")
