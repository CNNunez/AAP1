from dominoes import * 

tiles = make_tiles(6)
assert(len(tiles) == 28)

m = make_board(3, 4)

assert (check(m, 0, 2, 0) == True)
assert (check(m, 0, 3, 0) == False)
assert (check(m, 1, 3, 1) == True)
assert (check(m, 2, 0, 1) == False)

m[0][3] = 1
m[1][3] = 1
m[2][0] = 1

assert (check(m, 0, 1, 0) == True)
assert (check(m, 0, 2, 0) == False)
assert (check(m, 1, 3, 1) == False)
assert (check(m, 1, 0, 1) == False)


assert (next_empty(m, 0, 0)==(0,0))
assert (next_empty(m, 0, 3)==(1,0))

