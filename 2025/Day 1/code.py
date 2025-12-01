import os

def main():
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "input.txt")

    count = 0
    min = 0
    max = 100
    dial = 50

    with open(file_path) as input:
        instructions = input.read().strip().split("\n")

    for instruction in instructions:
        dial = eval("dial" + instruction.replace("L", "-").replace("R", "+")) % max        
        print(f"{instruction}[{int(instruction[1:]) % max}]: {dial}")
        if dial != min:
            continue    
        count += 1

    print(count)

if __name__ == "__main__":
    main()
