#2016년
import os 

def solution(a,b):
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date =['FRI','SAT', 'SUN', 'MON','TUE','WED','THU']
    total_days = sum(days_in_month[:a-1])+(b-1)
    return(date[total_days%7])

if __name__ == "__main__":
    a,b = map(int,input().split())

    print(solution(a,b))
