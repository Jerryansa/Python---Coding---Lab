<h1>Python Coding Lab</h1>


<h2>Description</h2>
The provided Python code defines a university management system comprising classes for Persons, Students, Faculty, and Departments. Each class encapsulates specific attributes and functionalities relevant to its role within the university structure. Persons are assigned unique "G-numbers," while students can manage grades, calculate GPAs, and determine class levels. Faculty members track tenure, rank, and specialties. The Department class oversees the addition of faculty and students, checks qualifications, and displays rosters. The code sets up a basic system to model a simplified university. It includes features for adding people, managing student grades, and organizing faculty and students into different departments.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Visual Studio Code</b> 
- <b>Python</b>

<h2>Program walk-through:</h2>
<p align="center">
UML Diagram:<br/>
 A visual representation of the system.
<img src="https://i.imgur.com/tEv5wB0.png" height="80%" width="80%" alt="UML Diagram"/>
<br />
<br />
Person Class(Parent Class): <br/>
This portion creates a "Person" class for managing information about people. It assigns unique ID numbers (G-Numbers) to each person and keeps track of the total number of people. The class has a method to display person details as a string. Another method checks if two people are duplicates based on their ID numbers and names. It returns "True" if they are the same and "False" otherwise, with a check to make sure it's comparing two actual person objects.
<img src="https://i.imgur.com/HL9RFEQ.png" height="80%" width="80%" alt="Person Class(Parent Class)"/>
<br />
<br />
Student Class(Child Class):  <br/>
This portion creates a special type of person called a "Student" with extra details like their major, academic status, and grades. The student's information, like their G-Number, name, and address, can be shown as a string. The code also calculates the student's GPA (how well they're doing in their classes) and allows you to add grades to update it. You can check if the student is currently enrolled, find out their class level (like Freshman or Sophomore), and set their major. In simple terms, it helps keep track of a student's academic stuff.
<img src="https://i.imgur.com/KluKT59.png" height="80%" width="80%" alt="Student Class(Child Class)"/>
<br />
<br />
Faculty Class(Child Class): <br/>
This portion is like a digital card for teachers or professors. It keeps track of their name, contact details, rank, specialty, and whether they have a permanent position (called tenure). The card shows all this information in a nice way when you ask for it. It helps organize details about faculty members, making it easy to see who they are and how long they've been working.
<img src="https://i.imgur.com/FzY5ZT0.png" height="80%" width="80%" alt="Faculty Class(Child Class)"/>
<br />
<br />
Department Class(Child Class):  <br/>
This Python code is like a digital system for university departments. It keeps track of details like the department's code, name, how many students and faculty it can have, and the minimum GPA needed for some departments. You can add students and teachers to the department, but there are rules like having enough space and meeting GPA requirements. The code also checks if a student is good enough for a specific department and shows a list of students, faculty, or both in the department. It helps keep things organized for university departments.
<img src="https://i.imgur.com/u8h0oYk.png" height="80%" width="80%" alt="Department Class 1(Child Class)"/>
<img src="https://i.imgur.com/enT5TWO.png" height="80%" width="80%" alt="Department Class 2(Child Class)"/>
<br />
<br />
TestScript:  <br/>
<img src="https://i.imgur.com/VBDLLXq.png" height="80%" width="80%" alt="TestScript1"/>
<img src="https://i.imgur.com/rFLsqSd.png" height="80%" width="80%" alt="TestScript2"/>
<img src="https://i.imgur.com/XtOY2e9.png" height="80%" width="80%" alt="TestScript3"/>
<br />
<br />
 Results:  <br/>
<img src="https://i.imgur.com/MihwZt0.png" height="80%" width="80%" alt="R1"/>
<img src="https://i.imgur.com/260s3Og.png" height="80%" width="80%" alt="R2"/>
<img src="https://i.imgur.com/DIfnH3F.png" height="80%" width="80%" alt="R3"/>
 <img src="https://i.imgur.com/2EmTTOH.png" height="80%" width="80%" alt="R4"/>
<br />
<br />
Conclusion:  <br/>
The provided Python code creates a system for handling information in a school. It keeps track of people (like students and teachers) and departments. Students have GPAs and can be enrolled, faculty have ranks and tenure, and departments have capacities and minimum GPA requirements. The code helps organize and manage these details, allowing for actions like adding students or faculty, checking qualifications, and showing rosters. It's like a digital tool for running things smoothly in a school setting.
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
