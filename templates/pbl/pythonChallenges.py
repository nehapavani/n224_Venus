age1=int(input())
age2=int(input())
def swap(age1, age2):
    if age1 > age2:
        temp1 = age1
        temp2 = age2
        age1 = temp2
        age2 = temp1
        return age1, age2
    print(swap(age1, age2))

if __name__ == “__main__“:
    swap(age1, age2)



