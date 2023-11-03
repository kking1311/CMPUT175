def reverseDisplay(a):
  if a<0:
    raise ValueError("Enter a positive integer")
  if len(str(a))==1:
    return a
  else:
    return int(str(a%10)+str(reverseDisplay(a//10)))

def sumdigits(a):
    if a<0:
      raise ValueError("Enter a positive integer")
    if a == 0:
        return 0
    return (a % 10 + sumdigits(int(a / 10)))
def main():
 try:
  number = int(input('Enter a number:'))
  print(sumdigits(number))
  number = int(input('Enter a number:'))
  print(reverseDisplay(number))
 except ValueError as v:
  print(v)
main()