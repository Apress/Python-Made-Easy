class MyException(Exception):
    pass

try:
    1/0
except MyException as e:
    print('invalid input')
    print(e)
except Exception as e:
    print('unknown problem')
    print(e)