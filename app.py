
def addition(args):
    return sum(args)


def subtraction(args):
    # iterate over the whole array and perform substraction
    result = args[0]
    for i in range(1, len(args)):
        result -= args[i]
    return result


def multiplication(args):
    result = 1
    for i in args:
        result *= i
    return result


def division(args):
    result = args[0]
    for i in range(1, len(args)):
        result /= args[i]
    # round the result to 2 decimal places
    result = round(result, 2)
    return result


def calculator(operation, *args):
    if operation == 'add':
        return addition(args)
    elif operation == 'sub':
        return subtraction(args)
    elif operation == 'mul':
        return multiplication(args)
    elif operation == 'div':
        return division(args)
    else:
        return "Invalid operation"
    

if __name__ == "__main__":
    print("\n\n** Welcome To The Calculator App **\n\n")
    while True:
        print("Enter the operation you want to perform: (add, sub, mul, div)")
        operation = input()
        if(operation not in ['add', 'sub', 'mul', 'div']):
            print("Invalid operation, closing the app")
            break
        print("Enter the numbers separated by space")
        numbers = list(map(float, input().split()))
        print(f"The result of the operation is: {calculator(operation, *numbers)}")
        print("Do you want to perform another operation? (yes/no)")
        nextOperation = input().lower()
        if nextOperation == 'no' or nextOperation == "n":
            break
    print("\n\n")
    print("Thank you for using the calculator app")
    print("Regards, Bilal Amjad @thedevelop3r")
    
    
    