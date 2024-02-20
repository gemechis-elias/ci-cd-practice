def main():
    try:
        n = input("Enter the Number : ")
        print("|============================================|")
        print("|                                            |")
        print("| FizzBuzz with Docker                      |")
        print("| Input Number : {} => {} ".format(n, fizzbuzz(int(n))))
        print("|                                            |")
        print("|============================================|")
    except EOFError:
        print("No input provided.")
    except ValueError:
        print("Please enter a valid integer.")

 
    
    
def fizzbuzz(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)    

if __name__ == '__main__':
    main()
