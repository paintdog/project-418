import os

test_mode = True

files = [file for file in os.listdir() if file.endswith(".png") and file.startswith("2")]

files.sort()

numbers = [108, 116, 121, 130, 136, 161, 14, 50, 56, 73, 92, 99, 33, 5]

number = 0

for file in files:
    
    if number in numbers:
        number += 1
    else:
        print(file)
        print("{:03d}.png".format(number))

        if not test_mode:
            os.rename(file, "{:03d}.png".format(number))

    number += 1
