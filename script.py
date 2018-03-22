# Enter Time and It will greet you
ch = raw_input("Enter Time: ")
if ch<'0000':
    print("Invalid Time")
elif ch<'1200':
    print("Good Morning!")
elif ch<'1600':
    print("Good Afternoon!")
elif ch<'2000':
    print("Good Everning!")
elif ch<='2400':
    print("Good Night!")
else:
    print("Invalid Time")
