
class Person():
    g_num= ""
    personCount  = 0
    currentYear = 2023
    def __init__(self,name,address,telephone,email):
        Person.personCount += 1
        self.g_num = f"G{(str(Person.personCount)).zfill(5)}"
        self.name = name
        self.address = address
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return "Person: G-Number: {}, Name: {}, Address: {}".format(self.g_num, self.name, self.address)
    
    def dupePerson(self, other):
        if self == other:
            return True
        if not isinstance (self, Person):
            return False
        else:
            return (str(self.g_num) == str(other.g_num) and (str(self.name) == str(other.name)))

class Student(Person):
    def __init__(self,name,address,telephone,email,major="",status="", enrolled="", credits=0,qpoints=0):
        super().__init__(name,address,telephone,email)
        self.major = major
        self.credits = credits
        self.qpoints = qpoints
        self.enrolled = enrolled
        self.status = status

    def __str__(self):
        return "Student: {}, Status: {}, Major: {}".format(super().__str__(), self.status, self.major)

    def gpa(self):
        if self.credits == 0 and self.qpoints == 0:
            return 0
        gpa = self.qpoints/self.credits
        return round(gpa,2)
    

    def addGrade(self,gradeletter,credit_num):
        if gradeletter != "A" and "B" and "C" and "D" and "F":
            return False
        elif gradeletter == "A":
            self.qpoints += 4 * credit_num
            self.credits += credit_num
            return True
        elif gradeletter == "B":
            self.qpoints += 3 * credit_num
            self.credits += credit_num
            return True
        elif gradeletter == "C":
            self.qpoints += 2 * credit_num
            self.credits += credit_num
            return True
        elif gradeletter == "D":
            self.qpoints += 1 * credit_num
            self.credits += credit_num
            return True
        else:
            self.qpoints += 0 * credit_num
            self.credits += credit_num
            return True


    def isActive(self):
        if self.enrolled == "y":
            return True
        else:
            return False
        
    def classLevel(self):
        if self.credits < 30:
            return "Freshman"
        if self.credits >= 30 and self.credits < 60:
            return "Sophomore"
        if self.credits >= 60 and  self.credits < 90:
            return "Junior"
        else:
            return "Senior"
        
    def setMajor(self):
        self.major = None
        return self.major
    
class Faculty(Person):
    def __init__(self,name,address,telephone,email,rank,active,teach_load,specialty, yearStarted):
        super().__init__(name,address,telephone,email)
        self.rank = rank
        self.active = active
        self.teach_load = teach_load
        self.specialty = specialty
        self.yearStarted = yearStarted

    def __str__(self):
        return "Faculty: {}, Rank: {}, Specialty: {}, Tenure: {}".format(super().__str__(), self.rank, self.specialty, self.Tenure())
    
    def Tenure(self):
        return self.currentYear - self.yearStarted

class Department(Person):

    def __init__(self,d_code,d_name,capacity,minGPA,univ_student = 0):
        self.d_code = d_code
        self.d_name = d_name
        self.capacity = capacity
        self.minGPA = minGPA
        self.univ_student = univ_student

        self.avgGPA = 0
        self.num_students = 0
        self.directory = []


    def __str__(self):

        return 'Name: ' + str(self.d_name) + ' (' + str(self.d_code) + ') ' + 'Capacity: ' + str(self.capacity) + \
            ' Number of Students: ' + str(self.num_students)
    
    def addFaculty(self, faculty_object):
        if isinstance(faculty_object, Faculty):
            self.directory.append(faculty_object)

        else:
            print("Not in Faculty")

    
 
    def addStudent(self, student):
        if self.num_students >= self.capacity:
            return False, "no more room"
        
        if not student.isActive():
            return False, "not enrolled"
        
        if any(student.dupePerson(existing_student) for existing_student in self.directory):
            return False, "dupe"
        
        if self.d_code == "CHHS" and student.gpa() < self.minGPA:
            return False, "low GPA"
    
        self.directory.append(student)
        self.num_students += 1
        self.univ_student += 1
        self.avgGPA = (self.avgGPA * len(self.directory) + student.gpa()) / (len(self.directory) + 1)
        student.setMajor()
        return True, "added"
    

    


    def isQualified(self,student):
        if not student.isActive():
            return False, "not enrolled"
        
        for in_student in self.directory:
            if student.dupePerson(in_student):
                return False, "dupe"
            
        if self.d_code == "ENGR" and student.gpa() >= self.minGPA:
            return True, "qualified"
        elif self.d_code == "ARTS" and student.gpa() >= self.minGPA:
            return True, "qualified"
        elif self.d_code == "CHHS" and student.gpa() < self.minGPA:
            return True, "qualified"
        else:
            return False, "low GPA"


    def showRoster(self, selection = "b"):
        if selection == 's':
            print(F'Roster for Students in {self.d_name} ({self.d_code}):')
            for student in self.directory:
                if isinstance(student, Student):
                    print(student.g_num + ', ' + student.name)
        if selection == 'f':
            print(F'Roster for Faculty in {self.d_name} ({self.d_code}):')
            for faculty in self.directory:
                if isinstance(faculty, Faculty):
                    print(faculty.g_num + ', ' + faculty.name)
        if selection == 'b':
            print(F'Roster for Students in {self.d_name} ({self.d_code}):')
            for student in self.directory:
                if isinstance(student, Student):
                    print(student.g_num + ', ' + student.name)
            print(F'Roster for Faculty in {self.d_name} ({self.d_code}):')
            for faculty in self.directory:
                if isinstance(faculty, Faculty):
                    print(faculty.g_num + ', ' + faculty.name)

#------------------------------------------------------------------------
# IT209_A5_testscript.py - A5 Testscript
#
# Department/Person/Faculty/Student classes


# Testscript suite starts here ---------------------------------------------------        

print('\nStart of A5 Test Script ********************************')

#====================================================================
input('\nTest1. Hit "Enter" to create 15 student, 2 Faculty objects for use in the demo ')

s1 = Student('David Miller', '321 Maple Lane, Vienna, VA',
      '571-285-4567', 'dmiller8@gmu.edu',major = 'Hist', enrolled = 'y',
      credits = 30, qpoints = 90)           
s2 = Student('Bonnie Bonilla', '123 Oak Street, Potomac, MD',
      '301-285-4567', 'bbonilla@gmu.edu',major = 'Math',enrolled = 'y',
      credits = 90, qpoints = 315)
s3 = Student('Chris Squire', '4567 Park Lane, London, UK',
      '425-285-4567', 'csquire8@gmu.edu', major = 'Musc', enrolled = 'y',
      credits = 45, qpoints = 160)
s4 = Student('Tal Wilkenfeld', '423 Outback Way, Sydney, AU',
      '524-485-5674', 'twilkenfeld@AU.gov', major = 'Musc', enrolled = 'y',
      credits = 75, qpoints = 250)    
s5 = Student('Dave Holland', '66 pacific Coast Hwy, Los Angeles, CA',
      '231-44-2596', 'dholland@jazz.net', major = 'CHHS', enrolled = 'y',
      credits = 105, qpoints = 320)           
s6 = Student('John Entwistle', '6 Stable Way, Leeds, UK',
      '416-223-1967', 'johnwho@apple.com', major = 'CSci', enrolled = 'y',
      credits = 15, qpoints = 35)
s7 = Student('Esperanza Spalding', '9122 King Hwy, Upper Marlboror, MD',
      '310-247-1954', 'esperanza@jazzy.org', major = 'ENGR', enrolled = 'y',  
      credits = 65, qpoints = 250)           
s8 = Student('Tim Bogert', '2713 Santa Monica Blvd, Venice, CA',
      '912-333-1968', 'vfudge@yahoo.net', major = 'Hist', enrolled = 'y',
      credits = 45, qpoints = 160)
s9 = Student('Gordon Sumner', '145 Nigel Path, Manchester, U.K.',
      '011-11-0203-2202', 'sting@police.com', major = 'Musc', enrolled = 'y',
      credits = 15, qpoints = 45)           
s10 = Student('Paul McCartney', '422 Hagis Road, Edinburgh, U.K.',
      '481-221-1970', 'paullinda@wings.org', major = 'ARTS', enrolled = 'y',
      credits = 110, qpoints = 275)
s11 = Student('Elizabeth Smythe', '2215 Yonge Street, Toronto, CA',
      '416-676-2983', 'esmythe12@ontario.gov', major = 'ENGR', enrolled = 'y',
      credits = 85, qpoints = 250)
s12 = Student('John McVie', '27 Casino Lane, Monte Carlo, Monaco',
      '011-56-2233-9945', 'johnmac@blues.net', major = 'Hist', enrolled = 'y',
      credits = 45, qpoints = 120)
s13 = Student('Nawt Enrolled', '13 Failed Street, Cantenroll, AZ',
      '320-445-2938', 'nenrolled@gmu.ed', major = 'Hist', enrolled = 'n',
      credits = 45, qpoints = 120)
s14 = Student('Toolow G. Peyay', '1313 LowGrade Drive, Mustwait, NE',
      '678-901-2345','Toolowgpa@gmu.edu', major = 'Undc', enrolled = 'y',
      credits = 20, qpoints = 38)
s15 = Student('Geddy Lee', '320 University Ave, Toronto, Ont',
      '415-922-3835', 'GLee@rush.com', major = 'Chem', enrolled = 'y',
      credits = 58, qpoints = 143)
f1 = Faculty('Amanda Shuman', '3062 Covington Street, Fairfax, VA',
             '571-235-2345', 'gshuman@gmu.edu', 'Assistant Professor', 'y',
             18, 'teaching', 2017)     
f2 = Faculty('A. Einstein', '2741 University Blvd, Priceton, NJ',
             '212-346-3456', 'aeinstein@gmu.edu', 'Professor', 'y',
             6, 'research', 1938)

print('\nList of Students anf aculty created----------------------------:\n ')
print('s1=  ',s1)
print('s2=  ',s2)
print('s3=  ',s3)
print('s4=  ',s4)      
print('s5=  ',s5)
print('s6=  ',s6)      
print('s7=  ',s7)
print('s8=  ',s8)
print('s9=  ', s9)
print('s10= ',s10)
print('s11= ',s11)
print('s12= ',s12)      
print('s13= ',s13)
print('s14= ',s14)
print('s15= ', s15)
print('f1=  ', f1)
print('f2=  ', f2)

#==================================================================================
input('\n\nTest2. Hit "Enter" to see the list of 3 Department objects created ')
print('\n\nDepartments established---------------------------------:')
d1 = Department('ENGR', 'Engineering', 5, 3.0)
d2 = Department('ARTS', 'Art and Architecture', 5, 2.5)
d3 = Department('CHHS', 'College of Health and Human Sevrices', 3, 2.75)

print(d1)
print(d2)
print(d3)

#========================================================================================
input('\n\n\nTest3. Hit "Enter" to add s1 - s5, f1, f2 to ENGR Department- print student list\n')
d1.addStudent(s1)      
d1.addStudent(s2)
d1.addStudent(s3)      
d1.addStudent(s4)
d1.addStudent(s5)
d1.addFaculty(f1)
d1.addFaculty(f2)
d1.showRoster()

#==========================================================================================
input('\n\n\nTest4. Hit "Enter" to creat+add  Turing and Von Neuman to ARTS and CHHS faculty, then display their rosters:\n')
d2.addFaculty(Faculty('Alan Turing', '6 Stable Way, Bletchly Park, U.K.',
             '9-56-4955', 'aturing@UK.gov', 'Associate Professor', 'y',
             6, 'research', 1943))
d3.addFaculty(Faculty('J. Von Neuman', '71 Kovaletch Prad, Budapest, Hungary',
             '9-56-4955', 'hvneuman@gmail.com', 'Professor', 'y',
             6, 'research', 1948))
d2.showRoster()
d3.showRoster()

#==========================================================================================
input('\n\n\n\nTest5. Hit "Enter" to add additional students to various departments ---------:')
a, b = d1.addStudent(s6)
print('\nAttempting to add ', s6.name, ' to ', d1.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nDepartment ', d1.d_name, ' student list is now: ')
d1.showRoster()

#=========================================================================================      
input('\n\n\n\nTest6. Hit "Enter" to add two students to the ARTS Department ')
a, b = d2.addStudent(s6)
print('\nAttempting to add ', s6.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d2.addStudent(s7)
print('\nAttempting to add ', s7.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
d2.showRoster()

#========================================================================================
input('\n\n\n\nTest7. Hit "Enter" to add two students to the CHHS Department' )
a, b = d3.addStudent(s8)
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d3.addStudent(s9)
print('\nAttempting to add ', s9.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
d3.showRoster()

#=========================================================================================
input('\n\n\n\nTest8. Hit "Enter" to try adding a student with low GPA to CHHS')
a, b = d3.addStudent(s14)
print('\nAttempting to add ', s14.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

#=========================================================================================
input('\n\n\n\nTest9. Hit "Enter" to try to add a non-enrolled student to the CHHS Department')
a, b = d2.addStudent(s13)
print('\nAttempting to add ', s13.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

#========================================================================================
input('\n\n\n\nTest10. Hit "Enter" to try adding a duplicate student ')
a, b = d3.addStudent(s8)
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

#========================================================================================
input('\n\n\n\nTest11. Hit "Enter" to add s10 to ENGR, s11 to ARTS, s12 to CHHS.')
print('  then print all 3 department student lists')
a, b = d1.addStudent(s10)
print('\nAttempting to add ', s10.name, ' to ', d1.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d2.addStudent(s11)
print('\nAttempting to add ', s11.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d3.addStudent(s12)
print('\nAttempting to add ', s12.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

#=========================================================================================
input('\n\n\n\nTest12. Hit "Enter" to try to add s15 to ARTS, which will fail for low gpa, ')
print('    then add a new course grade of "A"/3 credits to s15, and try the add again.')
print('\nStudent to be added to ARTS is ', s15)      
a, b = d2.addStudent(s15)
print('\nResult of attempt to add ', s15.name, ' gpa: ', str(s15.gpa()), ' to ', d2.d_code)
print('\tis ', a, ', with reson code: ', b)

#==========================================================================================
input('\n\n\n\nTest13. Adding 3 credit course with grade of "A" to ' + s15.name )
s15.addGrade("A", 3)
print('\nStudent profile is now: ', s15)
a, b = d2.addStudent(s15)
print('\nResult of second attempt to add ', s15.name, ' to ', d2.d_code)
print('\tis ', a, ', with reason code:  ', b)
print('\nNote: ', s15.name, ' is now a ', s15.classLevel(), ' with gpa ', str(s15.gpa()))

#==========================================================================================
input ('\n\n\n\nT14Hit "Enter" to see the final list of students and faculty for all departments')

d1.showRoster('s')
d1.showRoster('f')
d2.showRoster('s')
d2.showRoster('f')
d3.showRoster('s')
d3.showRoster('f')

print('\n\n\n***** End of A5 Output **********')