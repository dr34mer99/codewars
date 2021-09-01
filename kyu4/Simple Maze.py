'''
Kate constantly finds herself in some kind of a maze.
Help her to find a way out!.

For a given maze and Kate's position find if there is a way out.
Your function should return True or False.

Each maze is defined as a list of strings,
where each char stays for a single maze "cell". ' ' (space) can be stepped on,
'#' means wall and 'k' stays for Kate's starting position.
Note that the maze may not always be square or even rectangular.

Kate can move left, up, right or down only.

There should be only one Kate in a maze.
In any other case you have to throw an exception.

Example input
['# ##',
 '# k#',
 '####']
Example output
True

Example input
['####'.
 '# k#',
 '####']
Example output
False
'''


def wyplaszcz(lista):
    ret = []
    for x in lista:
        if type(x)==type([]):
            for y in wyplaszcz(x):
                ret.append(y)
        else:
            ret.append(x)
    return ret

def has_exit(maze):
    b = [maze[0] , maze[-1]]
    b.append([j[0] for j in maze])
    b.append([k[-1] for k in maze])
    b[0] = list(b[0])
    b[1] = list(b[1])
    b = wyplaszcz(b)
    if ' ' in b:
        return True
    else:
        return False

maze = ["########",
        "# # ## #",
        "# #k#  #",
        "# # # ##",
        "# # #  #",
        "#     ##",
        "########"]
print(has_exit(maze))