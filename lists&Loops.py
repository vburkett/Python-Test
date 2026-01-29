students = []
done = False
while not done:
    name = input("Enter student name: ")
    if name == "":
        done = True
    else:
        students.append(name)

students[1]="Jen Carrey"

for name in students:
    print(name)