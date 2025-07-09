#문자열 나누기

def solution(keymap, targets):
    answer = []
    for word in targets : 

        if len(set(word) - set(list(''.join(keymap)))) : 
            answer.append(-1)

        else : 
            cnt = 0
            for w in word : 
                get_cnt = min([key.index(w)+1 for key in keymap if w in key])
                cnt += get_cnt
            answer.append(cnt)                
    return answer

if __name__ == "__main__":
    keymap = eval(input())
    targets = eval(input())
    print(solution(keymap, targets))

