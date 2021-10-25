def find_armstrong():
    three_digit_number = int(input("Enter a three digit number: "))
    if three_digit_number >= 100 and three_digit_number <= 999:
        # convert the number to string, then iterate over each number to perform the algorithm
        cubeSum = 0
        stringified = str(three_digit_number)
        for x in stringified:
            cubeSum += int(x) * int(x) * int(x)
        if cubeSum == three_digit_number:
            print(f"{three_digit_number} is an Armstrong number")
        else:
            print(f"{three_digit_number} is NOT an Armstrong number")
        return
    else:
        print(f"{three_digit_number} is NOT A THREE DIGIT NUMBER")
        return


find_armstrong()
