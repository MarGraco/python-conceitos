my_list = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

x = 0
while x < 3:
    x += 1
    for i in my_list:
        if i == "Monday":
            print("-----------")
            continue
        print(i)