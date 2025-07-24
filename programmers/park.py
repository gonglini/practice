# 공원산책
import os 

def solution(park, routes):
    grid = [list(row) for row in park]
    h, w = len(grid), len(grid[0])

    for y in range(h):
        for x in range(w):
            if grid[y][x] == 'S':
                cy, cx = y, x
                break
    dir_map = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }

    for route in routes:
        d, n = route.split()
        n = int(n)
        dy, dx = dir_map[d]

        ny, nx = cy, cx
        valid = True

        for _ in range(n):
            ny += dy
            nx += dx
            if not (0 <= ny < h and 0 <= nx < w):
                valid = False
                break
            if grid[ny][nx] == 'X':
                valid = False
                break

        if valid:
            cy, cx = ny, nx

    return [cy, cx]


if __name__ == "__main__":
    park = eval(input())   
    routes = eval(input()) 
    print(solution(park, routes))
