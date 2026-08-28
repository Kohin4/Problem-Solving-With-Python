student_id={
    233064 : "Tanzeel Ud Dowla",
    241001 : "Sheikh Kohinoor Rahman Dipu",
    241002 : "Junayed Ahmed",
    241003 : "Rashedul Karim Rafi",
    241004 : "Ashikur Rahman Chowdhury",
    241017 : "Iftaher Sayem"
}
print(student_id[241001]+"\n")

for x in student_id:
    print(student_id[x])

print("\n"+student_id.get(241017)) 
print("\n"+student_id.get(241006,"Not Found"))
