def sum_list(numbers):
    print(sum(numbers))

def main():
    # write your code below this line
    numbers = []
    numbers.append(3)
    numbers.append(2)
    numbers.append(6)
    numbers.append(-1)
    print(numbers)
    sum_list(numbers)
    numbers.append(5)
    numbers.append(1)
    print(numbers)
    sum_list(numbers)
    

if __name__ == '__main__':
    main()
