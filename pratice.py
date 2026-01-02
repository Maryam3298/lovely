n = int(input())
maximum = -1000
minimum = 1000
for i in range(n):
    a = int(input())
    if a < minimum:
        minimum = a
    if a > maximum:
        maximum = a
print(minimum,maximum)        
