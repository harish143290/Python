
#slicing [start : end : step ]

s="WELCOME"

print(s[0:3:1]) #WEL
print(s[0:3: ])
print(s[0:3])

print(s[:3:1])
print(s[:3:])
print(s[:3])
print("==============")

print(s[3:7:1])
print(s[3:7: ])
print(s[3: :1])
print(s[3: : ])
print(s[3: ])

print("Print Character Existed Even Positions")
print(s[0:7:2])
print(s[0: :2])
print(s[ ::2])

print("Print Character Existed in odd Positions ")
print(s[1:7:2])
print(s[1: :2])

print("Print Character  in reverse order ")
print(s[-1:-8:-1])
print(s[-1: :-1])
print(s[ : :-1])

print(s[-1:-5:-1])
print(s[-1:-8:-2])

















