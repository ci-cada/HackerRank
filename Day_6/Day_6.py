# Enter your code here. Read input from STDIN. Print output to STDOUT
# we are using _ when we don't have to use the actuall value 
n = int(input().strip())
for _ in range(n):
    st = input().strip()
    print('{} {}'.format(st[0::2], st[1::2]))
