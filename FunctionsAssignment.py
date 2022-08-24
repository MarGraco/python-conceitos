def user_dictionay(firstname, lastname, age):
    created_user_dictionary = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return created_user_dictionary

solution_dictionary = user_dictionay(firstname="Eric", lastname="Roby", age=32)
print(solution_dictionary)