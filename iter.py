mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

while True:
    try:
        x = next(myit)
        print(x)
    except StopIteration:
        break
