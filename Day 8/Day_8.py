# Enter your code here. Read input from STDIN. Print output to STDOUT

phone_book = {}
n = int(input())

for i in range(n):
    name, number = input().split(' ')
    phone_book[name] = number

while True:
    try:
        name = input()
    except EOFError:
        break
    if name in phone_book:
        print(f"{name}={phone_book[name]}")
    else:
        print("Not found")

