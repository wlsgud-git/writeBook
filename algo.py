n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(str, input().split())))

status = int(input())

# if status == 1:
#     for x in range(len(arr)):
#         printer = ""
#         for y in range(len(arr[x])):
#             printer += arr[x][y]
#         print(printer)    

if status == 2:
    print(2222)
    for x in range(len(arr)):
        printer = ""
        for k in range(len(arr[x])-1, -1,-1):
            printer += arr[x][k]
        print(printer)

else:
    for x in range(len(arr)-1, -1 ,-1):
        printer = ""
        for y in range(len(arr[x])):
            printer += arr[x][y]
        print(printer)
