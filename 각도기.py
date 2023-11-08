# https://school.programmers.co.kr/learn/courses/30/lessons/120829
def solution(angle):
    answer = 0
    for i in angle:
        if i < 90:
            return(1)
        elif 90<i<180:
            return(3)
        else:
            i = 180
            return(4)
    return answer