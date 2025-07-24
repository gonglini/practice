def solution(mats, park):
    rows = len(park)
    cols = len(park[0])

    mats.sort(reverse=True)

    for size in mats:
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                can_place = True
                for x in range(size):
                    for y in range(size):
                        if park[i + x][j + y] != "-1":
                            can_place = False
                            break
                    if not can_place:
                        break
                if can_place:
                    return size
    return -1


if __name__ == "__main__":
    mats = eval(input())
    park = eval(input())   
    result = solution(mats, park)
