# While Loop Assignment


print("Task 1: Numbers from 1 to 10")
i = 1
while i <= 10:
    print(i)
    i += 1

print("\nTask 2: Print numbers from 1 to the user's input")


while True:
    try:
        num = int(input("Enter a positive integer: "))

        if num <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            print("Numbers from 1 to", num)
            i = 1
            while i <= num:
                print(i)
                i += 1
            break

    except ValueError:
        print("Invalid input! Please enter a valid integer.")