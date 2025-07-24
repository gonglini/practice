# 개인정보 수집 유효기간

import os 
def solution(today, terms, privacies):

    term_dict = {}
    for term in terms:
        type_, months = term.split()
        term_dict[type_] = int(months)

    def to_days(date_str):
        y, m, d = map(int, date_str.split("."))
        return y * 12 * 28 + m * 28 + d  
    
    today_days = to_days(today)

    answer = []
    for idx, privacy in enumerate(privacies):
        date_str, type_ = privacy.split()
        expire_days = to_days(date_str) + term_dict[type_] * 28

        if expire_days <= today_days:
            answer.append(idx + 1)

    return answer
if __name__ == "__main__":
    today = eval(input())
    terms = eval(input())
    privacies = eval(input())   
    print(solution(today, terms, privacies))
