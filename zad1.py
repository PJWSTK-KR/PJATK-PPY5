import sys

students = {}
for line in open(input("Plik ze studentami> ") or "students1.txt", 'r'):
    data = {}
    line = line.split(",")
    if len(line) > 4:
        data["imie"], data["nazwisko"], data["liczba_punktow"], data["ocena"], data["status"] = line[1:6]
        data["status"] = data["status"].strip()
    else:
        data["imie"], data["nazwisko"], data["liczba_punktow"] = line[1:4]
        data["status"] = ""
        data["ocena"] = ""
    data["liczba_punktow"] = data["liczba_punktow"].strip()
    students[line[0]] = data
while True:
    print("""1. Automatycznie wystawić oceny studentom
    2. Wyświetl aktualne dane
    3. Dodanie studenta
    4. Usunięcie studenta
    5. Wysłanie emaila o wystawionej ocenie
    6. Koniec
    """)
    action = input(">")
    if action == "1":
        for student in students:
            if students[student]["status"] == "GRADED" or students[student]["status"] == "MAILED":
                continue
            liczba_punktow = int(students[student]["liczba_punktow"])
            if liczba_punktow <= 50:
                students[student]["ocena"] = 2
            elif liczba_punktow <= 60:
                students[student]["ocena"] = 3
            elif liczba_punktow <= 70:
                students[student]["ocena"] = 3.5
            elif liczba_punktow <= 80:
                students[student]["ocena"] = 4
            elif liczba_punktow <= 90:
                students[student]["ocena"] = 4.5
            elif liczba_punktow <= 100:
                students[student]["ocena"] = 5
    elif action == "2":
        print(students)
    elif action == "3":
        data = {}
        email, data["imie"], data["nazwisko"], data["liczba_punktow"], data["ocena"], data["status"] = input("Nowy student> ").split(",")
        data["status"] = data["status"].strip()
        students[email] = data
        pass
    elif action == "4":
        pass
    elif action == "5":
        pass
    elif action == "6":
        sys.exit(0)
