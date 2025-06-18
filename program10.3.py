try:
    num=int(input("enter a number:"))
    result=10/num
except ValueError:
    print("error:invalid input! please enter a valid number:")
except ZeroDivisionError:
    print("error:division by zero!")
else:
    print("result:",result)
