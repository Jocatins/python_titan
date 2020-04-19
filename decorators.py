def smile_dec(func):

    def func_wrap():

        print('*smile*')
        func()
        print('*smile*')

    return func_wrap

@smile_dec

def question ():
    print('can you fuck me twice')

@smile_dec

def answer ():
    print("okay babe, I'll do anything for you")
question()
answer()
