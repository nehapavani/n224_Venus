first_number = [8, 12, 6, 20, 10]
second_number = [2, 3, 3, 4, 5]
num_problems = len(first_number)

def calculate(type):

    score = 0
    for i in range(num_problems):
        print(first_number[i], end = " ")
        if (type == "M"):
            print(" * ", end=" ")
            correct = first_number[i] * second_number[i]
        else:
            print(" / ", end = " ")
            correct = first_number[i] / second_number[i]
        print(second_number[i])
        answer = int(input("Enter your answer:"))
        if answer == correct:
            print("Correct")
            score += 1
        else:
            print("Incorrect")
        print()
    return score

print("Math Quiz")
type = input("Select (M)ultipliction or (D)ivision:")
score = calculate(type) * 100 / num_problems

print("score: " + str(score) + "%")


if __name__ == "__main__":
    make_candy()