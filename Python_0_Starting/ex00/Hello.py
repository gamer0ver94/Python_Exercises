def main():
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    ft_list[1] = 'World!'
    ft_tuple = ("Hello, France!")
    ft_set.add('Mulhouse!')
    if "tutu!" in ft_set:
        ft_set.remove("tutu!")
    ft_dict['Hello'] = '42Mulhouse!'

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)


main()
