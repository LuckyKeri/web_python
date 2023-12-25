# Функция декоратор 
def dec(f_arg):
    #функция обертка
    def wrapper():
        #доп. функуциональность 1
        print("before")
        #вызов целевой функции
        f_arg()
        #доп. функциональность 2
        print("after")
    return wrapper

#новый синтаксис
@dec
# Целевая функция
def func():
    print("Hello!")

#старый синтаксис
# func = dec(func)

# вызов функции
func()