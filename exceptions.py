class JustMinorError(Exception):
    pass 
x = 2
try:
    print(x/0)
    raise JustMinorError ('check through ur all work again')
    '''if not type(x) is str:
        raise TypeError('this is character not numbers')'''
except NameError: 
    print('enter a proper for your variable')
except ZeroDivisionError:
    print('use your senses')
else:
    print('that\'s all there is')
finally:
    print('it\'s a free way')