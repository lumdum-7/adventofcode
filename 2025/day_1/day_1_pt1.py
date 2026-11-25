
start = 50
password = 0

with open("2025/day_1/input.txt", "r", encoding="utf-8") as file:
    for line in file:
        print("start: " + str(start))
        command = line.strip()
        print("command: " + str(command))
        units = int(command[1:])

        if command[:1] == 'L':
            units = units * -1
        elif command[:1] == 'R':
            units = units * 1

        print("units: " + str(units))

        command_sum = start + int(units)
        print("command_sum: " + str(command_sum))
        mod = command_sum%100

        if mod == 0:
            start = 0
            password += 1
        elif command_sum < 0 or command_sum > 100:
            start = mod
        else:
            start = command_sum

        print(password)
        print(start)
        

        
        