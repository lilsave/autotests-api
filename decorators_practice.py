def make_loud(func):
    def wrapper():
        print(">>> начало")
        func()
        print(">>> конец")
    return wrapper



@make_loud
def greet():
    print("Привет")

greet()

say = greet

say()


def run_twice(func):
    func()
    func()

run_twice(greet)



loud_greet = make_loud(greet)
loud_greet()