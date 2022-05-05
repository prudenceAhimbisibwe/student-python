class Student:
    def __init__(self,name,age,classroom):
        self.name=name
        self.age=age
        self.classroom=classroom
students=[
    Student("charity",23,"HopperLab"),
    Student("Mollen",20,"AdaLab"),
    Student("Gumato",19,"AdaLab"),
    Student("Susan",24,"AnitaBLab"),
]
for s in students:
    print(f"{s.name},{s.age},{s.classroom}")
