print("")
print("Student 1:")
print ("What is their first name? ")
studentName1 = input ()
print ("What is their first class? ")
student1Class1 = input ()
print ("What is their seat number? ")
student1Class1SeatNum = int(input ())
print (studentName1 + " sits in seat " + str(student1Class1SeatNum) + " during " + student1Class1 + " first period.")
print("Is this student infected? (True/False) ")
student1Isinfected = input()


print("")
print("Student 2:")
print ("What is their first name? ")
studentName2 = input ()
print ("What is their first class? ")
student2Class1 = input ()
print ("What is their seat number? ")
student2Class1SeatNum = int(input ())
print (studentName2 + " sits in seat " + str(student2Class1SeatNum) + " during " + student2Class1 + " first period.")
print("Is this student infected? (True/False) ")
student2Isinfected = input()


if student1Class1 == student2Class1 & student1Isinfected == "true" :
    if student1Isinfected = "True":
        if student2Class1SeatNum == student1Class1SeatNum + 1 | student1Class1SeatNum -1:
            print ("")
            print (studentName2 + " needs to quarentine due to exposure to " + studentName1 + ".")
    if student2Isinfected = "True":
        if student1Class1SeatNum == student2Class1SeatNum + 1 | student2Class1SeatNum -1:
             print ("")
             print (studentName1 + " needs to quarentine due to exposure to " + studentName2 + ".")
