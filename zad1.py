import sys


def save_students(file_name, students):
    file = open(file_name, 'w')
    for student in students:
        content = ""
        for key in students[student]:
            content += str(students[student][key]) + ','
        content = content.removesuffix(',')
        file.write(content + '\n')
    file.close()


def grade_student(points, students, student):
    if points <= 50:
        students[student]["ocena"] = 2
    elif points <= 60:
        students[student]["ocena"] = 3
    elif points <= 70:
        students[student]["ocena"] = 3.5
    elif points <= 80:
        students[student]["ocena"] = 4
    elif points <= 90:
        students[student]["ocena"] = 4.5
    elif points <= 100:
        students[student]["ocena"] = 5


students = {}
file_name = input("Plik ze studentami> ") or "students1.txt"
for line in open(file_name, 'r'):
    data = {}
    line = line.split(",")
    if len(line) > 4:
        data["imie"], data["nazwisko"], data["liczba_punktow"], data[
            "ocena"], data["status"] = line[1:6]
        data["status"] = data["status"].strip()
    else:
        data["imie"], data["nazwisko"], data["liczba_punktow"] = line[1:4]
        data["status"] = ""
        data["ocena"] = ""
    data["liczba_punktow"] = data["liczba_punktow"].strip()
    students[line[0]] = data
while True:
    print("""    1. Automatycznie wystawić oceny studentom
    2. Wyświetl aktualne dane
    3. Dodanie studenta
    4. Usunięcie studenta
    5. Wysłanie emaila o wystawionej ocenie
    6. Koniec
    """)
    action = input(">")
    if action == "1":
        for student in students:
            if students[student]["status"] == "GRADED" or students[student][
                    "status"] == "MAILED":
                continue
            grade_student(int(students[student]["liczba_punktow"]), students, student)
        save_students(file_name, students)
    elif action == "2":
        for student in students:
            print("\t\t\t\t" + student)
            for key in students[student]:
                print(key + ": " + str(students[student][key]))
    elif action == "3":
        data = {}
        email, data["imie"], data["nazwisko"], data["liczba_punktow"], data[
            "status"] = input("Nowy student(email,imie,nazwisko,liczba punkow,status)> ").split(",")
        data["status"] = data["status"].strip()
        if students.get(email) is not None:
            print("email jest zejęty!")
            continue
        students[email] = data
        grade_student(int(students[email]["liczba_punktow"]), students, email)
        save_students(file_name, students)
    elif action == "4":
        email = input("Student> ")
        if students.get(email) != None:
            students.pop(email)
        else:
            print("Student nie istnieje")
        save_students(file_name, students)
    elif action == "5":
        print("Nie zaimplementowano")
    elif action == "6":
        sys.exit(0)
