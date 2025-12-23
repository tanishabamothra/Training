try:
    a=20
    b=2
    print(a/b)
except ZeroDivisionError:
    print("Error")
else:
    print("Division successful")