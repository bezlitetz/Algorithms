def multiplyK(x,y):
    x , y = map(str, [x , y])
    n = len(x)
    if n == 1: #base case:
        x , y = map(int, [x , y])
        return (x * y)
    else: #recursive case
        half = int(n/2) # bcs / creates a float
        a = str(x)[:half]
        b = str(x)[half:]
        c = str(y)[:half]
        d = str(y)[half:]

        a, b, c, d = map(int, [a, b, c, d]) # convert them all at once
        p = a + b 
        q = c + d

        ac = multiplyK(a,c)
        bd = multiplyK(b,d)
        pq = multiplyK(p,q)
        
        abcd = pq - ac - bd

        final = (10**n) * ac + 10**(n/2) * abcd + bd

        return final
    
def main():
    # if we were to make both the same digits long


    x=(input("Enter a number:")) # not converted to int, bcs i can slice a string
    y=(input("Enter another number:"))

    product = multiplyK(x,y)
    print(product)


main()

