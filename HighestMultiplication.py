'''WAP to find highest Multiplication of the given number if the given number 
should be split such that the sum is equal to the given number but it should be highest
product 
'''
def doCalc(num):
    temp = num
    result =1
    while(temp > 3):
        result *= 3
        temp -= 3
    if temp != 0 :
        result = result*temp
    return result

if __name__ == "__main__":
    print(doCalc(9))