'''def my_name(name1, name2):
    print(f"Hello {name1} {name2}")

my_name("Steve", "Jobs")
'''

'''def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)

print_numbers(lowest_number=3, highest_number=10)'''

'''def multiply_numbers(a, b):
    return a * b

solution = multiply_numbers(10, 6)
print(solution)

def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)

number_list = [1, 2, 3, 4, 5]
print_list(number_list)'''

def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_time):
    current_tax_rate = .03
    return cost_of_time * current_tax_rate

final_cost = buy_item(50)
print(final_cost)