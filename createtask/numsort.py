def adFunc(a, val):
    for i in range(val -1):
        for j in range(val - i - 1):
            if(a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

def deFunc(a, val):
    for i in range(val -1):
        for j in range(val - i - 1):
            if(a[j] < a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

while True:
    a = []
    val = int(input("Please Enter the Total Elements : "))
    for i in range(val):
        value = int(input("Please enter the %d Element : " %i))
        a.append(value)


    answer = input("Would you like to sort these numbers in ascending (A) or descending (D) order? ")
    if answer == "A":
        adFunc(a, val)
        print("The List in Ascending Order : ", a)

    elif answer == "D":
        deFunc(a, val)
        print("The List in Descending Order : ", a)

    final = input("Run again? (Y/N) ")
    if final == "Y":
        continue
    else:
        print("Bye.")
        break


if __name__ == "__main__":
    adFunc(a, val)
    deFunc(a, val)