def read_file():
    f = open('index.txt')
    p_len = int(f.readline())
    plane = []
    for i in range(p_len):
        value = f.readline()
        value = value.replace('\n', '').replace('.', '1').replace('#', '0').split('_')
        value = list(map(lambda j: list([int(z) for z in j]), value))
        plane.append(value)
    t_len = int(f.readline())
    seats = []
    for i in range(t_len):
        seats.append(tuple(map(int, f.readline().replace('\n', '').replace('left', '0').
                     replace('right', '1').replace('aisle', '1').replace('window', '0').split())))
    f.close()
    return plane, seats


p, s = read_file()
for i in p:
    print(i)


def all_on_board(plane, requests):
    for req in range(len(requests)):
        seats = requests[req]
        print(seats)
        for idx in range(len(plane)):
            if seats[0] == 3:
                if plane[idx][seats[1]] == [1] * 3:
                    print('do replace from 3')
                    break
            elif seats[0] == 2:
                if seats[1] == seats[2]:
                    if plane[idx][seats[1]][:2] == [1, 1]:
                        print('do replace from 2 as, 00x')
                        break
                else:
                    if plane[idx][seats[1]][1:] == [1, 1]:
                        print('do replace from 2 as, x00')
                        break
            elif seats[0] == 1:
                print('pass from 1')


all_on_board(p, s)
