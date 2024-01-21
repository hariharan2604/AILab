def get_valid_input(message, min_value, max_value):
    while True:
        try:
            user_input = int(input(message))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Input must be between {min_value} and {max_value}. Please re-enter.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def print_board(left_m, left_c, right_m, right_c):
    print("\n")
    for i in range(0, left_m):
        print("M ", end="")
    for i in range(0, left_c):
        print("C ", end="")
    print("| --- | ", end="")
    for i in range(0, right_m):
        print("M ", end="")
    for i in range(0, right_c):
        print("C ", end="")
    print("\n")

try:
    print("\nGame Start\nNow the task is to move all of them to the right side of the river")
    print("Rules:\n1. The boat can carry at most two people\n2. If cannibals number is greater than missionaries, "
          "then the cannibals would eat the missionaries\n3. The boat cannot cross the river by itself with no people "
          "on board")

    lM = 3  # Left side Missionaries number
    lC = 3  # Left side Cannibals number
    rM = 0  # Right side Missionaries number
    rC = 0  # Right side cannibals number
    userM = 0  # User input for the number of missionaries for right to left side travel
    userC = 0  # User input for the number of cannibals for right to left travel
    k = 0

    print_board(lM, lC, rM, rC)

    while True:
        # Left side to right side river travel
        while True:
            print("Left side -> right side river travel")
            uM = get_valid_input("Enter the number of Missionaries to travel => ", 0, 2)
            uC = get_valid_input("Enter the number of Cannibals to travel => ", 0, 2)

            if uM == 0 and uC == 0:
                print("Empty travel not possible. Re-enter.")
            elif (uM + uC) <= 2 and (lM - uM) >= 0 and (lC - uC) >= 0:
                break
            else:
                print("Invalid input. Re-enter.")

        lM -= uM
        lC -= uC
        rM += uM
        rC += uC

        print_board(lM, lC, rM, rC)

        k += 1

        if (lC == 3 and lM == 1) or (lC == 3 and lM == 2) or (lC == 2 and lM == 1) or (rC == 3 and rM == 1) or (
                rC == 3 and rM == 2) or (rC == 2 and rM == 1):
            print("Cannibals eat missionaries: You lost the game")
            break

        if (rM + rC) == 6:
            print("You won the game : Congrats")
            print("Total attempts:", k)
            break

        # Right side to left side river travel
        while True:
            print("Right side -> Left side river travel")
            userM = get_valid_input("Enter the number of Missionaries to travel => ", 0, 2)
            userC = get_valid_input("Enter the number of Cannibals to travel => ", 0, 2)

            if userM == 0 and userC == 0:
                print("Empty travel not possible. Re-enter.")
            elif (userM + userC) <= 2 and (rM - userM) >= 0 and (rC - userC) >= 0:
                break
            else:
                print("Invalid input. Re-enter.")

        lM += userM
        lC += userC
        rM -= userM
        rC -= userC

        k += 1
        print_board(lM, lC, rM, rC)

        if (lC == 3 and lM == 1) or (lC == 3 and lM == 2) or (lC == 2 and lM == 1) or (rC == 3 and rM == 1) or (
                rC == 3 and rM == 2) or (rC == 2 and rM == 1):
            print("Cannibals eat missionaries: You lost the game")
            break

except EOFError as e:
    print("\nInvalid input. Please retry!")
