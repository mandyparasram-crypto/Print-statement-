print("Enter Marks Obtained in 4 Subjects")
math = int(input("maths:"))
english= int(input("english:"))
Science = int(input("science:"))
Hindi= int(input("Hindi:"))

sum = math+english+Science+Hindi
print("Sum of math,English,Science and Hindi =",sum)

perc =  (sum/400)*100

print(end="Percentage Mark =")
print(perc)

