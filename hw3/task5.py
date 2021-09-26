def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
         print('Error: division by zero!')
    else:
         print('The results is', result)
    finally:
         print('Goodbye world!')
         
         
print(division(2,2), division(2,0))
