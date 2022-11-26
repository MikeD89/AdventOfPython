from aocd import get_data, submit

data = get_data(day=1, year=2015)


def count_character(character):
    return data.count(character)


def print_data():
    print(data)


open = count_character("(")
closed = count_character(")")
print(open - closed)

#submit(open - closed, part="a", day=1, year=2015)

a = 0
for index, i in enumerate(data):
    if i == "(":
        a += 1
    else:
        a -= 1

    if a == -1:
        print(index)
        break

submit(index+1, part="b", day=1, year=2015)
