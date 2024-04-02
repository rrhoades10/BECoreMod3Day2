# yes
def add_nums(num1, num2):
    return num1 + num2
# no
def idk(a, x):
    return x + a

# vague labels, vague variable names, vague function

# process customer information
# bad wrong, badong way
def process(data):
    pass

# right way
def process_customer_order(order_details):
    pass

# being aware of spacing and indentation
# def bake_cake():
# eggs = 3
# flour = 1
# sugar = 2
# mix(flour, sugar)
#        add(eggs)


# clean class names
# Object Relational Mapper
# Takes python classes (Models) converts them into SQL tables
# creating a table for a User
class User:
    first_name = ''
    last_name = ''
    email = ''
    username = ''
    user_id = ''

    def __init__(self, first_name, last_name, email, username, user_id):
        pass
     

