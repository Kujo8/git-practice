lines = ["Hello", "", "World", "", "Python", "",]

empty_lines = filter(lambda line: line.strip() != "", lines)

print(list(empty_lines))
