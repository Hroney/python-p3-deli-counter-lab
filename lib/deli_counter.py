katz_deli = []

def line(queue):
    if len(queue) == 0:
        print("The line is currently empty.")
    else:
        statement = []
        for person in queue:
            statement.append(f"{queue.index(person) + 1}. {person}")
        print(f"The line is currently: {' '.join(map(str, statement))}")
    pass

def take_a_number(katz_deli, newperson):
    katz_deli.append(newperson)
    print(f"Welcome, {newperson}. You are number {katz_deli.index(newperson) + 1} in line.")
    return katz_deli

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
    pass

