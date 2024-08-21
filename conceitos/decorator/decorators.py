import time
def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()- t1
        print(f'Took {t2} seconds')
    return wrapper

@tictoc
def mostrar():
    print("Pronto")



def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("Hi, I am created by a function passed as an argument.")
    print (greeting)

greet(shout)
greet(whisper)