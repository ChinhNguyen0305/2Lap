def draw_tree():
    picture = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]

    for l in picture:
        for number in l:
            if number == 0:
                print('', end=' ')
            else:
                print('*', end='')
        print('')

def draw_many_tree(number):
    i = 0
    # for c in range(number):
    #     draw_tree()
    while i < number:
        draw_tree()
        i +=1
draw_many_tree(5)