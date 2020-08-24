begin = int(input("input begining: "))
end = int(input("input end: "))

for num in range(begin, end + 1):
    if num > 1: 
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

