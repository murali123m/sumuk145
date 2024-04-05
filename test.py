def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
    num=7
    int(input("enter fatorial number"))
    if num<0:
        print("sorry,factorial dose not exist for negetive number")
    elif num==0:
            print("The factorial of 0is1")
    else:
                print("The factorial of",num,"is",recur_factorial(num)) 
