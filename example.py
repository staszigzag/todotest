def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        func()
        print('Выходим из обёртки')
    return wrapper

@decorator_function
def xxx():
  print('hello world')

xxx()