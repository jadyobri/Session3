#function for f(x).  returns the answer from x**3 + 8
def f(x):
    number = (x**3) + 8
    return number
    # if(number > 27):
    #     print("YAY!")

#Puts 9 into the function.  The f(9) answer to printed
#If the answer of f(9) is greater than 27, then "YAY!" is printed
def main():
    x = 9
    newnum = f(x)
    print(newnum)
    if(newnum > 27):
        print("YAY!")

# Executes the main program when script is run
if __name__=="__main__":
    main()