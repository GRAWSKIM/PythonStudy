#주석 style1

'''
주석 style2
'''
"""
Doucment String
"""
import random

def lotto():
    """
    Doucment String 주석처리되지만
    함수,모듈,클래스,메서드 등 설명서 작성에 사용
    1~45 사이의 정수 중에서 6개를 무작위로 출력
    :return: <class 'list'>
    """
    #1~45 사이의 정수 중에서 6개를 무작위로 출력
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    return lotto

#print(lotto())

print(lotto().__doc__)
#help(lotto())
