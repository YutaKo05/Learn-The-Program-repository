# Fizz Buzz

def solution(num):
    
    # numが３で割り切れる、numが５で割り切れるか確認するだけ
    if num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    
    elif num % 3 ==0:
        return "Fizz"

    elif num % 5 ==0:
        return "Buzz"
    
    else:
        return str(num)