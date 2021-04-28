if student1Isinfected == "True":
    if student1Class1 == student2Class1:
        if student2SeatNum == student1SeatNum + 1 or student1SeatNum - 1:
            print ("")
            print (studentName2 + " needs to quarentine due to exposure to " + studentName1 + ".")
elif student2Isinfected == "True":
    if student2Class1 == student1Class1:
        if student2Class1SeatNum == student1Class1SeatNum + 1 or student1Class1SeatNum -1:
            print ("")
            print (studentName1 + " needs to quarentine due to exposure to " + studentName2 + ".")


