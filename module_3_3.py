def print_params(a=1, b="строка", c=True):
    print(a, b, c)
    # print_params(1, 2, 15, "аргумент") - не работает, т.к. 4 аргумента
    # print_params(12) - не работает, т.к. только один аргумент, а должно быть 3
    # print_params() - выводит значения аргументов 1 "строка" True
values_list = [12, "яблоко", False]
values_dict = {"a": 22, "b": "образованный", "c": False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)