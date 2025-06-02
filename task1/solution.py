def strict(func):
    def wrapper(*args):
       # print('test')
        #print(args)
        #print(list(func.__annotations__.values()))
        #for el in func.__annotations__.values():
        #   print(el)
        for el in args:#,list(func.__annotations__.values())[:(len(args))]:
            i=0
            #print(type(el))
            #print(list(func.__annotations__.values())[i])
            if type(el)==list(func.__annotations__.values())[i]:
               pass#print('dobre')
            else:
                raise TypeError('Неправильный тип переменной')
            i=i+1
        return func(*args)
    return wrapper

@strict
def sum_two(a:int,b:int) ->int:
    return a+b

@strict
def contain_ultimate_answer_to_life_the_universe_and_everything (a: str) ->bool:
    if '42' in a:
        return True
    else:
        return False

@strict
def sum_two_float(a:float,b:float)->float:
    return a + b

@strict
def bool_test(a:bool)->bool:
    return a

print(sum_two(1, 2))
try:
    print(sum_two(1, 2.4))
except Exception as e:
    print(e)
try:
    print(sum_two(5.6, 2.4))
except Exception as e:
    print(e)
try:
    print(sum_two(1.9, 2))
except Exception as e:
    print(e)
try:
    print(contain_ultimate_answer_to_life_the_universe_and_everything('It is 42'))
except Exception as e:
    print(e)
try:
    print(contain_ultimate_answer_to_life_the_universe_and_everything(42))
except Exception as e:
    print(e)
try:
    print(sum_two_float(4.5,5.6))
except Exception as e:
    print(e)
try:
    print(sum_two_float(4,5.6))
except Exception as e:
    print(e)
try:
    print(sum_two_float(4.0,5.6))
except Exception as e:
    print(e)
try:
    print(bool_test(True))
except Exception as e:
    print(e)
try:
    print(bool_test('True'))
except Exception as e:
    print(e)