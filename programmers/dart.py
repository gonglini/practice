#다트 게임



def solution(dartResult):
    score = []
    i = 0
    while i < len(dartResult):

        if dartResult[i] == '1' and i + 1 < len(dartResult) and dartResult[i+1] == '0':
            point = 10
            i += 2
        else:
            point = int(dartResult[i])
            i += 1

        if dartResult[i] == 'S':
            point = point ** 1
        elif dartResult[i] == 'D':
            point = point ** 2
        elif dartResult[i] == 'T':
            point = point ** 3
        i += 1

        if i < len(dartResult) and dartResult[i] in ['*', '#']:
            if dartResult[i] == '*':
                point *= 2
                if score:  
                    score[-1] *= 2
            elif dartResult[i] == '#':
                point *= -1
            i += 1

        score.append(point)

    return sum(score)

if __name__ == "__main__":
    N = input()
    print(solution(N))


