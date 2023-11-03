def mylen(a):
    if not a:
        return 0
    return 1 + mylen(a[1::2]) + mylen(a[2::2])

def intDivision(a,b):
    if a < 0 or b <= 0:
        raise ValueError("The divisor has to be greater than 0 . ")
    if a<b:
        return 0
    return 1+intDivision(a-b,b)


def main():
    try:
     alist = [43, 76, 97, 86]
     print(mylen(alist))
     n = int(input('Enter an integer dividend: '))
     m = int(input('Enter an integer divisor: '))
     print('Integer division', n, '//', m, '=' ,intDivision(n,m))
    except ValueError as v:
        print(v)
    
if __name__=="__main__":
    main()