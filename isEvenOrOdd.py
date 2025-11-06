
def main():
    
    
    x = int(input("what's x ? :"))

    if is_even(x):
       print("Even")
    else:
       print("Odd")





def is_even(n):
    '''if n % 2 == 0: #basic
      return True
    else:
      return False'''
    #return True if n % 2 == 0 else False #shorter
    return n % 2 == 0 #shortest

main()
