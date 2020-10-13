def matreshka(n:int=5):
    """ Разворачиваем матрешку n-раз"""
    if n == 1:
        print("Матрёшечка")
    else:
        print("Верх матрешки - {}".format(n))
        matreshka(n-1)
        print("Низ матрешки матрешки - {}".format(n))

matreshka()

