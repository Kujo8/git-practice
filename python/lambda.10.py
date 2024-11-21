student = [{"name":"Alice","grade":85},{"name":"Charlie","grade":90},{"name":"Bob","grade":70},{"name":"Diana","grade":65}]

average_grade = sum(s["grade"] for s in student) / len(student)
students = filter(lambda s: s["grade"] > average_grade, student)

print(list(students))
