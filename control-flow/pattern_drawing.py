size = int(input("Enter the size of the pattern: "))

i = 0
while i < size  :
    j = 0 
    while j < size :
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1