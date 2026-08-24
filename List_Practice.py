Student_list = ["Nahar","Kohin","Tanzeel","Abrar","Sayem","Habib","Tanvir","Junayed"]

print(Student_list)

print("\n"+Student_list[3])
print("\n"+Student_list[-2])

print("\n")
print(Student_list[3:])

print("\n")
print(Student_list[-2:])

print("\n")
print("Nahar" in Student_list)
print("Kohin" not in Student_list)
print("Saydad" in Student_list)

i = int(input("\nGive an index to find : "))
print(Student_list[i])

print("\n")
i = 0
while i<7:
    print(Student_list[i])
    i = i+1
