try:
    num=int(input("enter a number:"))
    result=10/num
    print("result:",result)
except ValueError:
    print("error:invalid input!please enter a valid number")
except ZeroDivisionError:
    print("error:division by zero!")
