user_dictionay = {
    'username': 'codingwithroby',
    'name': 'Eric',
    'age': 32
}

'''user_dictionay["married"] = True
print(user_dictionay)
print(user_dictionay.get("username"))
print(len(user_dictionay))

user_dictionay.pop("age")
print(user_dictionay)

user_dictionay.clear()
print(user_dictionay)'''

'''del user_dictionay'''

# apenas pega as keys, sem os valores
'''for x in user_dictionay: 
    print(x)'''
# pega as keys e os valores
'''for x, y in user_dictionay.items(): 
    print(x, y)'''

user_dictionay2 = user_dictionay
user_dictionay2.pop("age")
print(user_dictionay)