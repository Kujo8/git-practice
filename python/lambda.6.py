ages = [ 15, 22, 18, 25, 14, 30, 17, 21]

valid_ages = filter(lambda age: age >= 18, ages)

print(list(valid_ages))
