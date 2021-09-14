'''WAP to find highest Multiplication of the given number if the given number 
should be split such that the sum is equal to the given number but it should be highest
product 
'''
def highest_product():
    number = int(input("enter the number"))
    count = 0
    i=1
    if (number > 1 and number <=100):
        while (number>0):
            if(number%3==0):
                count+=1
            number = number//3
            
    print(count**count)
highest_product()

