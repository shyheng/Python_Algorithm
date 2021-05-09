
def can_play(fn):
    def inner(x,y,*args,**kwargs):
        # if args[0] <= 22:
        clock = kwargs.get('clock',20)
        if clock <= 22:
            fn(x,y)
        else:
            print('out')
    return inner

# 开放封闭原则
@can_play
def play_game(name,game):
    print('{}play{}'.format(name,game))


play_game('shy','zph')
play_game('zph','shy',23)