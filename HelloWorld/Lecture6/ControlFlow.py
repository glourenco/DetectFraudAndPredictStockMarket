traffic = "yellow"
distance = 1
if traffic == "green":
    print("go")
elif traffic == "yellow" and distance <=15:
    print("speed up")
elif traffic == "yellow" and distance >15:
    print("slow down")
elif traffic == "red":
    print("stop")
else:
    print("uknown action")

end = 10
start = 3
curr = start

while curr < end:
    curr += 1
    print(curr)

numA = [13,53,2,67,9]
for i in numA:
    print(i*2)