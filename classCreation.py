print ("Enter Class Name: ")
className = input ()

print ("How many students are in this class? ")
totalStudents = int(input ()) 


if totalStudents <= 12:
            
    print("")

    print("")
    print("This Is Your " + className + " Classroom:")
    print("")
    print("1  2  3  4")
    print("")
    print("5  6  7  8")
    print("")
    print("9 10 11 12")
    print("")


    print("For any empty seat, enter 'Empty' for all values")


    print("")
    print("Student 1:")
    print ("What is their first name? ")
    studentName1 = input ()
    student1SeatNum = 1
    print("Is this student infected? (Y/N) ")
    student1Isinfected = input()


    print("")
    print("Student 2:")
    print ("What is their first name? ")
    studentName2 = input ()
    student2SeatNum = 2
    print("Is this student infected? (Y/N) ")
    student2Isinfected = input()


    print("")
    print("Student 3:")
    print ("What is their first name? ")
    studentName3 = input ()
    student3SeatNum = 3
    print("Is this student infected? (Y/N) ")
    student3Isinfected = input()
            

    print("")
    print("Student 4:")
    print ("What is their first name? ")
    studentName4 = input ()
    student4SeatNum = 4
    print("Is this student infected? (Y/N) ")
    student4Isinfected = input()


    print("")
    print("Student 5:")
    print ("What is their first name? ")
    studentName5 = input ()
    student5SeatNum = 5
    print("Is this student infected? (Y/N) ")
    student5Isinfected = input()


    print("")
    print("Student 6:")
    print ("What is their first name? ")
    studentName6 = input ()
    student6SeatNum = 6
    print("Is this student infected? (Y/N) ")
    student6Isinfected = input()


    print("")
    print("Student 7:")
    print ("What is their first name? ")
    studentName7 = input ()
    student7SeatNum = 7
    print("Is this student infected? (Y/N) ")
    student7Isinfected = input()


    print("")
    print("Student 8:")
    print ("What is their first name? ")
    studentName8 = input ()
    student8SeatNum = 8
    print("Is this student infected? (Y/N) ")
    student8Isinfected = input()


    print("")
    print("Student 9:")
    print ("What is their first name? ")
    studentName9 = input ()
    student9SeatNum = 9
    print("Is this student infected? (Y/N) ")
    student9Isinfected = input()


    print("")
    print("Student 10:")
    print ("What is their first name? ")
    studentName10 = input ()
    student10SeatNum = 10
    print("Is this student infected? (Y/N) ")
    student10Isinfected = input()


    print("")
    print("Student 11:")
    print ("What is their first name? ")
    studentName11 = input ()
    student11SeatNum = 11
    print("Is this student infected? (Y/N) ")
    student11Isinfected = input()


    print("")
    print("Student 12:")
    print ("What is their first name? ")
    studentName12 = input ()
    student12SeatNum = 12
    print("Is this student infected? (Y/N) ")
    student12Isinfected = input()

    print("")
    print("This Is Your " + className + " Classroom:")
    print("")
    print(studentName1 + " " + studentName2 + " " + studentName3 + " " + studentName4)
    print("")
    print(studentName5 + " " + studentName6 + " " + studentName7 + " " + studentName8)
    print("")
    print(studentName9 + " " + studentName10 + " " + studentName11 + " " + studentName12)
    print("")

    print("")
    print("What would you like to do?")
    print("")
    print("Scan Class (1) | Exit (2)")
    action = int(input())
    print("")

    if action == 1:
        if student1Isinfected == "Y":
            print(studentName2 + " needs to quarentine." )
            print(studentName5 + " needs to quarentine.")

        if student2Isinfected == "Y":
            print(studentName3 + " needs to quarentine." )
            print(studentName1 + " needs to quarentine.")
            print(studentName6 + " needs to quarentine.")

        if student3Isinfected == "Y":
            print(studentName2 + " needs to quarentine." )
            print(studentName4 + " needs to quarentine.")
            print(studentName7 + " needs to quarentine.")

        if student4Isinfected == "Y":
            print(studentName3 + " needs to quarentine." )
            print(studentName8 + " needs to quarentine.")

        if student5Isinfected == "Y":
            print(studentName1 + " needs to quarentine." )
            print(studentName6 + " needs to quarentine.")
            print(studentName9 + " needs to quarentine.")

        if student6Isinfected == "Y":
            print(studentName5 + " needs to quarentine." )
            print(studentName7 + " needs to quarentine.")
            print(studentName2 + " needs to quarentine.")
            print(studentName10 + " needs to quarentine.")

        if student7Isinfected == "Y":
            print(studentName3 + " needs to quarentine." )
            print(studentName6 + " needs to quarentine.")
            print(studentName8 + " needs to quarentine.")
            print(studentName11 + " needs to quarentine.")

        if student8Isinfected == "Y":
            print(studentName4 + " needs to quarentine." )
            print(studentName7 + " needs to quarentine.")
            print(studentName12 + " needs to quarentine.")

        if student9Isinfected == "Y":
            print(studentName5 + " needs to quarentine." )
            print(studentName10 + " needs to quarentine.")

        if student10Isinfected == "Y":
            print(studentName6 + " needs to quarentine." )
            print(studentName9 + " needs to quarentine.")
            print(studentName11 + " needs to quarentine.")

        if student11Isinfected == "Y":
            print(studentName7 + " needs to quarentine." )
            print(studentName10 + " needs to quarentine.")
            print(studentName12 + " needs to quarentine.")

        if student12Isinfected == "Y":
            print(studentName8 + " needs to quarentine." )
            print(studentName11 + " needs to quarentine.")

    if action == 2:
        exit()







if 12 < totalStudents <= 24:
            
    print("")

    print("")
    print("This Is Your " + className + " Classroom:")
    print("")
    print(" 1   2   3   4")
    print("")
    print(" 5   6   7   8")
    print("")
    print(" 9  10  11  12")
    print("")
    print("13  14  15  16")
    print("")
    print("17  18  19  20")
    print("")
    print("21  22  23  24")
    print("")


    print("For any empty seat, enter 'Empty' for all values")


    print("")
    print("Student 1:")
    print ("What is their first name? ")
    studentName1 = input ()
    student1SeatNum = 1
    print("Is this student infected? (Y/N) ")
    student1Isinfected = input()


    print("")
    print("Student 2:")
    print ("What is their first name? ")
    studentName2 = input ()
    student2SeatNum = 2
    print("Is this student infected? (Y/N) ")
    student2Isinfected = input()


    print("")
    print("Student 3:")
    print ("What is their first name? ")
    studentName3 = input ()
    student3SeatNum = 3
    print("Is this student infected? (Y/N) ")
    student3Isinfected = input()
            

    print("")
    print("Student 4:")
    print ("What is their first name? ")
    studentName4 = input ()
    student4SeatNum = 4
    print("Is this student infected? (Y/N) ")
    student4Isinfected = input()


    print("")
    print("Student 5:")
    print ("What is their first name? ")
    studentName5 = input ()
    student5SeatNum = 5
    print("Is this student infected? (Y/N) ")
    student5Isinfected = input()


    print("")
    print("Student 6:")
    print ("What is their first name? ")
    studentName6 = input ()
    student6SeatNum = 6
    print("Is this student infected? (Y/N) ")
    student6Isinfected = input()


    print("")
    print("Student 7:")
    print ("What is their first name? ")
    studentName7 = input ()
    student7SeatNum = 7
    print("Is this student infected? (Y/N) ")
    student7Isinfected = input()


    print("")
    print("Student 8:")
    print ("What is their first name? ")
    studentName8 = input ()
    student8SeatNum = 8
    print("Is this student infected? (Y/N) ")
    student8Isinfected = input()


    print("")
    print("Student 9:")
    print ("What is their first name? ")
    studentName9 = input ()
    student9SeatNum = 9
    print("Is this student infected? (Y/N) ")
    student9Isinfected = input()


    print("")
    print("Student 10:")
    print ("What is their first name? ")
    studentName10 = input ()
    student10SeatNum = 10
    print("Is this student infected? (Y/N) ")
    student10Isinfected = input()


    print("")
    print("Student 11:")
    print ("What is their first name? ")
    studentName11 = input ()
    student11SeatNum = 11
    print("Is this student infected? (Y/N) ")
    student11Isinfected = input()


    print("")
    print("Student 12:")
    print ("What is their first name? ")
    studentName12 = input ()
    student12SeatNum = 12
    print("Is this student infected? (Y/N) ")
    student12Isinfected = input()


    print("")
    print("Student 13:")
    print ("What is their first name? ")
    studentName13 = input ()
    student13SeatNum = 13
    print("Is this student infected? (Y/N) ")
    student13Isinfected = input()


    print("")
    print("Student 14:")
    print ("What is their first name? ")
    studentName14 = input ()
    student14SeatNum = 14
    print("Is this student infected? (Y/N) ")
    student14Isinfected = input()


    print("")
    print("Student 15:")
    print ("What is their first name? ")
    studentName15 = input ()
    student15SeatNum = 15
    print("Is this student infected? (Y/N) ")
    student15Isinfected = input()
            

    print("")
    print("Student 16:")
    print ("What is their first name? ")
    studentName16 = input ()
    student16SeatNum = 16
    print("Is this student infected? (Y/N) ")
    student16Isinfected = input()


    print("")
    print("Student 17:")
    print ("What is their first name? ")
    studentName17 = input ()
    student17SeatNum = 17
    print("Is this student infected? (Y/N) ")
    student17Isinfected = input()


    print("")
    print("Student 18:")
    print ("What is their first name? ")
    studentName18 = input ()
    student18SeatNum = 18
    print("Is this student infected? (Y/N) ")
    student18Isinfected = input()


    print("")
    print("Student 19:")
    print ("What is their first name? ")
    studentName19 = input ()
    student19SeatNum = 19
    print("Is this student infected? (Y/N) ")
    student19Isinfected = input()


    print("")
    print("Student 20:")
    print ("What is their first name? ")
    studentName20 = input ()
    student20SeatNum = 20
    print("Is this student infected? (Y/N) ")
    student20Isinfected = input()


    print("")
    print("Student 21:")
    print ("What is their first name? ")
    studentName21 = input ()
    student21SeatNum = 21
    print("Is this student infected? (Y/N) ")
    student21Isinfected = input()


    print("")
    print("Student 22:")
    print ("What is their first name? ")
    studentName22 = input ()
    student22SeatNum = 22
    print("Is this student infected? (Y/N) ")
    student22Isinfected = input()


    print("")
    print("Student 23:")
    print ("What is their first name? ")
    studentName23 = input ()
    student23SeatNum = 23
    print("Is this student infected? (Y/N) ")
    student23Isinfected = input()


    print("")
    print("Student 24:")
    print ("What is their first name? ")
    studentName24 = input ()
    student24SeatNum = 24
    print("Is this student infected? (Y/N) ")
    student24Isinfected = input()
    



    print("")
    print("This Is Your " + className + " Classroom:")
    print("")
    print(studentName1 + " " + studentName2 + " " + studentName3 + " " + studentName4)
    print("")
    print(studentName5 + " " + studentName6 + " " + studentName7 + " " + studentName8)
    print("")
    print(studentName9 + " " + studentName10 + " " + studentName11 + " " + studentName12)
    print("")
    print(studentName13 + " " + studentName14 + " " + studentName15 + " " + studentName16)
    print("")
    print(studentName17 + " " + studentName18 + " " + studentName19 + " " + studentName20)
    print("")
    print(studentName21 + " " + studentName22 + " " + studentName23 + " " + studentName24)
    print("")

    print("")
    print("What would you like to do?")
    print("")
    print("Scan Class (1) | Exit (2)")
    action = int(input())
    print("")

    if action == 1:
        import scanClassLarge
    if action == 2:
        exit()




