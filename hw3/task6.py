def summ(a,b):
    return a + b

def power(a,b):
    return a ** b

def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
         print('Error: division by zero!')
    else:
         print('The results is', result)
    finally:
         print('Goodbye world!')
            
print(summ(1,power(2,division(3,0))))





Error: division by zero!
Goodbye world!
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-28-74df98ce439e> in <module>
     15          print('Goodbye world!')
     16 
---> 17 print(summ(1,power(2,division(3,0))))

<ipython-input-28-74df98ce439e> in power(a, b)
      3 
      4 def power(a,b):
----> 5     return a ** b
      6 
      7 def division(a, b):

TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'NoneType'
