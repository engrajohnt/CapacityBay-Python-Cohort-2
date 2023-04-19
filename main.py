print("Enter Marks Obtained in 3 terms: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
tot = markOne+markTwo+markThree
avg = tot/3
if avg>=69 and avg<=100:
    print("A")
elif avg>=59 and avg<70:
    print("B")
elif avg>=49 and avg<60:
    print("C")
elif avg>=39 and avg<50:
    print("D")
elif avg>=29 and avg<40:
    print("E")
elif avg>=0 and avg<30:
    print("F")
else:
    print("not allowed!")
    
