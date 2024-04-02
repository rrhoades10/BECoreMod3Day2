
# variable = something
name = "Ryan"

#             parameter
def say_hello(name):
    print(f"Hello, {name}")

#      argument fulfills the position of a parameter
say_hello("Alexa")

say_hello("Edwin")

say_hello("James")

# say_hello(100, 25)

def add_numbers(num1, num2):
    print(num1 + num2)

add_numbers(10, 15)

add_numbers(27, 18)

class Pokemon:
    def __init__(self, name, type_):
        self.name = name
        self.type_ = type_


my_pokemon = Pokemon("Charmander", "fire")
