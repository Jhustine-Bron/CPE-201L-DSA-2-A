numbers = [1,2,3,4,5,6,7,8,9,10]
print("\n-----|Numbers from 1 to 10|-----")
print(numbers)

def num_sum():
     num_sum = sum(numbers)
     print("\nSum of numbers is: ", num_sum)
num_sum()

def index_num(number):
    print("\n-----|Individual numbers:|-----")
    for i, element in enumerate(number):
        print(f"Index {i}: {element}")
index_num(numbers)

def app_num(number):
    print("\n-----|Appending a new item|-----")
    number.append(int(input("New number: ")))
    print("\nUpdated Number: ", number)
app_num(numbers)

def ins_num(number):
    print("\n-----|Inserting Number|-----")
    index = (1)
    value = int(input("enter number:"))
    number.insert(index, value)
    print("\nUpdated number: ", number)
ins_num(numbers)

numbers1 = [5,4,3,2,1]

def rev_num(numbers1):
    print("\n-----|Reversed numbers:|-----")
    reversed = numbers1[::-1]
    print(reversed)
rev_num(numbers1)

def len_num1(numbers1):
    print("\nLength of numbers:")
    length = len(numbers1)
    print(length)
len_num1(numbers1)


