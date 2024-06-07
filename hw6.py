students = (
    ("Student1",40),
    ("Student2",30),
    ("Student3",50)
)
def function(list):
    max_student = None
    max_score = 0
    for name,score in students:
        if score>max_score:
            max_student = name
            max_score = score
    return (max_student,max_score)
print(function(students))