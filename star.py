def star(number):
    if isinstance(number, str) is True or number <= 0:
        return

    longArrete = number*2 +1
    longTotale = longArrete*3

    for i in range(0, number+1):
        print(" "*(longArrete+number-i) + "* "*i)
    print("*"*longArrete + " "*longArrete + "*"*longArrete)

    for j in range(1, number):
        print(" "*j + "*" + " "*(longTotale-2*j) + "*")

    # Construction inversée
    for j in range(number, 0, -1):
        print(" "*j + "*" + " "*(longTotale-2*j) + "*")

    print("*"*longArrete + " "*longArrete + "*"*longArrete)
    for i in range(number, 0, -1):
        print(" "*(longArrete+number-i) + "* "*i)

star('toto')
star(-1)
star(0)
star(1)
star(5)