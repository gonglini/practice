#가장 많이 받은 선물

import os 

def gift_point(g, i):
    return sum(g[i]) - sum(list(zip(*g))[i])


def solution(friends, gifts):
    answer = 0
    l = len(friends)
    m = {}
    g = [[0] * l for _ in range(l)]

    for i, friend in enumerate(friends):
        m[friend] = i

    for gift in gifts:
        a, b = gift.split(" ")
        x, y = m[a], m[b]
        g[x][y] += 1

    garr = [0] * l

    for i in range(l):
        for j in range(i+1, l):
            a, b = g[i][j], g[j][i]
            if a>b:
                garr[i] += 1
            elif a<b:
                garr[j] += 1
            else:
                i_gp = gift_point(g, i)
                j_gp = gift_point(g, j)
                if i_gp > j_gp:
                    garr[i] += 1
                elif i_gp < j_gp:
                    garr[j] += 1

    answer = max(garr)

    return answer


if __name__ == "__main__":
    friend= eval(input())
    gift = eval(input())
    print(solution(friend, gift))
