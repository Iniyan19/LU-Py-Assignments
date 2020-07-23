string = "what we think, we become; we are python programmers."
#find all occurance of sub-string in the string and print index values.
sstring = input("enter a substring to search for in the string : \n")
start =0
result = []
while start<len(string):
    start = string.find(sstring,start)
    if start == -1:
        print(result)
        break
    else:
        result.append(start)
        start = start + len(sstring)

