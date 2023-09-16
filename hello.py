def addthis(a, b):
    print(f'This is x : {a} and y : {b}')
    try:
        result = a+b
    except TypeError:
        print("Wrong type of input")
        result = int(a)+int(b)
    print(f'This is the result : {result}')
    return result

print(addthis("1", 2))

