data = [
    """Testing preconditions in a constructor when calling another constructor
This note has to do with calling one constructor from another ---for example, in A1, calling the first constructor from the second constructor.
You don't have to read further if you are not calling one constructor from another.

      Rule: Within a constructor, a call on another constructor
      cannot appear in any place except as the first statement.

This means that if you decide to have constructor 2 call constructor 1, the assert
statements for Preconditions cannot be at the beginning of constructor 2;
they must come after that call of constructor 1.

That is OK.

HOWEVER! Note that that if a call on constructor 1 does some assert-checking of Preconditions,
you don't have to repeat them in the rest of constructor 2.

You'll be seeing constructors calling constructors in class VERY soon.""",
    """What to do for A0
After going through the lecture slides and attending today's lecture, I'm still confused about what we need to do for A0. """,
    """A limerick in honor of Gries
There once was a man named Gries
Who earned his doctorate overseas.
  "For what" you enquire?
  An ALGOL compiler.
(That's a language whose syntax gave birth to C's.)

But these days "the Gries" teaches Java.
How that happened is quite a long saga.
  He's retired twice
  ---Wouldn't that be nice?---
He re-returned because teaching's his nirvana.

Our pairing is no coincidence
In fact it makes perfect sense:
  My alma mater, Miami,
  Gave him an honorary degree
Impressed by his 58 years of experience.

So here's to a great spring semester
As we study OO together!
  Watch out for memes now and then
  About 2110
And about David Gries, our professor.""",
    """This week's recitation for those who can't make it
For those who can't make it to recitation this week because of the snow storm, will there be any resources posted/what do you recommend we do to keep up?""",
    """AEW or 2111
what would be the main difference between the two and which would you recommend more?""",
    """downloading Java
I downloaded Java and when I put "javac -version" in my terminal, it says "javac 11.0.2". Is this version okay?""",
    """Makeup Recitations - Action Required ASAP (Today)
Student who missed CS2110 first recitation due to weather conditions. 

We are offering 2 makeup sessions on Friday, 1/25, in 310 Gates Hall. 

Please complete the doodle poll to let us know how many students will attend each session.

In addition, if you cannot make either of these sessions please write your name but do not select any of the times.

This way we have an accurate number of students who need to makeup sessions and can offer additional times if needed. 

Please answer the poll ONLY if you need a makeup recitation. 

And please answer today, Tuesday, 22 Jan.

Thank you,

CS2110 course staff """,
    """Eclipse installer claims I do not have Java installed.
Whenever I try to install eclipse it redirects me to a browser and tells me to download Java. When I type java -version into my command prompt it tells me that I already have java 1.8.0 installed though. What should I do.""",
    """Assignment #A0
Learn about the assert statement and practice using Eclipse: a0.pdf

See the course CMS for the due date.


This helpful ppt file about the assert statement comes from Tony Hoare, author of Quicksort (and a lot more): assertearlyassertoften.ppt""",
    """Eclipse Preferences
When I tried to import the eclipse preferences, when I choose Java -> Editor, the pop-up looks different than the one in the tutorial. """,
    """Eclipse doesn't allow me to import preferences
Whenever I try to import the formatting preferences on eclipse, eclipse says that downloading might leave the workspace unstable and inconsistent and asks me to restart. """,
    """About the Quizzes
Will we take the quizzes in the lecture or recitation class or online? Thanks!""",
    """Changing the Parameters of the Main Method
In my recitation session we were taught how to change the String array args parameter in the main method header. What is the practical use of changing this?""",
    """CS 2110 vs ENGRD 2110
Is there any significant difference in which class you are enrolled? Gries said today that Engineers should be taking the ENGRD, but didn't elaborate why. The engineering handbook says that prospective CS majors should take CS 2110, so I wanted to clarify before I switched in student center.""",
    """Discussion Section Attendance
Does discussion attendance count towards our final grades, and does it matter which section we attend?""",
    """Problem installing Java
After installing Java, I do the command java - version in Run, but a PowerShell window opens but then immediately closes before I can see any text on it. Does this mean my Java did not install correctly?""",
    """Procedure for Switching Sections
In the syllabus it mentions that we may switch sections without "permission" and that we should register for the one we attend regularly. May I know how I can register for a different section than the one I am currently enrolled in?""",
    """Problem installing java
I put "java -version" into the terminal but still got "java version 11.02". I also opened the java control panel and for the "update" section it says that it's unable to check for updates and for me to check my internet connection; however, my internet connection works perfectly fine""",
    """Problem with JDK
After installing the Java SE Development Kit, when I do javac -version in the command prompt I keep getting:

'javac' is not recognized as an internal or external command,
operable program or batch file.

I even tried reinstalling the development kit, yet it is still saying the same thing.""",
    """Cornell Cup #Robotics!
Cornell Cup Robotics is recruiting for the Spring 2019 season! We are looking for driven and passionate students interested in creating cool robots and embedded systems. Our past projects have included a functional R2D2 (like the one from Star Wars) and a robot that is able to play RockBand with 98% accuracy. This semester we have two projects: R2D2 and Labo! 
For more information, please attend an information session (Thursday 24 Jan and Monday 28 Jan at 5 PM in Rhodes 571). We are recruiting for our ECE, CS, MechE/SYSEN, and Business/Communications sub-teams. For any questions or to apply, please reference our website or contact ccrt@cornell.edu. All students are welcome to apply!""",
    """#WICC: Women in Computing at Cornell
WICC is reaching out to students.

Go to their social, check out their interview classes in the image below.

If for some reason you can't see the image-pdf-file, here it is to click on: WICCSP19.pdf""",
    """Error when running Greetings.java
When I tried to run the program "Greetings.java" I got the following error:

must declare a named package because this compilation unit is associated to the named module 'Demo'

I solved this by deleting "module-info.java". Why is this and should I worry about it?""",
    """HW #1
The pinned post says we need to submit to the four parts on CMS, but I see only one place to submit. Is it okay to submit all four questions in one txt file?""",
    """Creating Files in Eclipse
I am unable to open any files in eclipse or create any new projects. I have attached the following image of my screen. Is there any way I can open my editor so that I can type code? """,
    """DIS This week
Are there discussion sections this week?""",
    """Recitation 02: Exception handling
This recitation takes place on 29..30 (Tue..Wed) January.

You have to prepare for it by watching some videos or reading, as follows.

 

1. Visit JavaHyperText and click on the link "Exceptions" in the top navigation bar. You get this webpage:

 

              http://www.cs.cornell.edu/courses/JavaAndDS/exceptions/EX1.html

Watch that video or just read the pdf file. We went over this in Lecture 02.

 

2. Click the link at the top right: "2. The throwable object". Watch the video in Java and read the page.

 

3. Click the link at the top right: "3. Catching and propagating thrown objects". Watch these videos:
     (a) YES: The try-statement.
     (b) NO: Don't watch the video using the try-statement to return a value in an array.
     (c) YES: Using the try-statement to read from the keyboard.
     (d) YES: Propagation of a thrown object.

 

4. Click the link at the top right: "4. The throw statement".
Watch the the first video on the page, about the throw-statement. There is no need to watch the second video.

There is no need to look at parts 5 or 6.


5. On Monday by noon, a short quiz, Quiz 1, will be placed on the CMS. Do it before Midnight.

 

6. Go to recitation and do the problem set. It will be placed in the pinned note on Recitations/Homeworks in advance of recitations.""",
    """AEW/2111
Would you reccomend doing both 2111 and aew or do you think just one will suffice?""",
    """submitting A0
How do we export A0 as a java file?""",
    """Invite a teammate
There is no invite button on the submission page for A0 and A1. Does that mean we should work on them individually? Or is there another way to invite a teammate?""",
    """Ipv4stack error
Whenever I run something, there's a "Picked up _JAVA_OPTIONS: -Djava.net.preferIPv4Stack=true" error, does anyone know how to fix this?""",
    """About the Definition of Evaluation
Must an evaluation return something? Can that be a criterion of determining whether the code is an evaluation or an execution?""",
    """My installed JRE is eclipse


Hello, I was working on A0, and when I got to the last part about configuring the JRE, I realized that my JRE isn't Java 1.8.... I'm not sure how a JRE can be eclipse though... If anyone could help that would be great! :)  Is it also possible if I could just configure this "eclipse JRE" as specified? Thanks!""",
    """Permanently enabling assert statement executions
Is there a way to turn off assert statement executions for one file / run after you've permanently enabled their executions? """,
    """Statler Auditorium is at full capacity
Should we expect to sit on the ground during lecture? I arrived before class started and couldn't find a single seat in the auditorium...""",
    """Teammates submission
How do we declare teammates and do we only submit one homework?""",
    """compiling
I saw today when you were using dr java that you had to compile before the class could actually function properly. Is this something that we have to do in eclipse as well?""",
    """Do we have syllabus uploaded?
Hi all,

I would really appreciate if anyone can let me know where I can find a syllabus online.""",
    """CMS
What happens if we upload to cms twice? Will only the last submission be counted?""",
    """Question in page 15 of lecture 2 slides


It says method "area" is in the object. It gives people an impression that the actual code of method "area" is stored in the object C@6667 on the memory.

But actual code of method "area" should be stored in the class C file and whenever object C@6667 needs to use the method, the program refers class C file to find the method "area".

I don't know how to better phrase this sentence. My attempt would be "The method is in the class C and a class C object has (access to) this method".""",
    """Switching Discussion Section?
I may need to move my discussion section to another time to make room for a required class that would overlap.

Should I swap the section with another on studentcenter, or should I speak with someone to make that change?

My apologies if this has been answered already.""",
    """Cornell Chimes Competition!
Do you want to play the Chimes at the top of McGraw Tower?

Become a Chimesmaster. Info sessions are given in the image below.
If for some reason you san't see the image, here it is as a pdf file: Competition2019flyer.pdf""",
    """Just enrolled for the class, but CMS does not show the class?
I just enrolled in this class, but I still don't have access to CMS. """,
    """A0
I get the error "Error: Could not find or load main class a0.A0" when I try to run the program. What's the problem?""",
    """Makeup Recitation
I'm at G01 Gates Hall for the makeup recitation but no one is here. Is it not happening?""",
    """Fixing Eclipse so that assert statement are aways executed in Windows?
This is my first time using Eclipse on Windows. How do I find menu item on Windows?""",
    """Where can I find assignment?
Hi, can anyone tell me where can I find our A0 and A1. Thanks so much.""",
    """A0 enabling assertion
I followed the directions for permanently enabling assertions, but just to test turning it on/off temporarily, I followed the directions for 'turning assert-statement execution on/off for one run'. I deleted -ea from VM Arguments in the Run Configuration window, but the assert statement was still executed (same output as before). I don't know if it matters, but why might it be doing this?""",
    """Code style in hypertext
Where should I find code style to click on Java hypertext?""",
    """Join the #Daily #Sun
The editor of the Daily Sun has asked us to post the image on joining the Daily Sun.

Two info sessions will be held on 5 Feb. and 6 Feb.

If you can't see the image, click this link: Daily_Sun_Recruitment_Slide.pdf""",
    """JUnit Tesing On E.java For Recitation 2
Are we expected to do JUnit testing on E.java for Recitation 2 before submitting it?""",
    """CMS Access
I enrolled in the class yesterday morning (1/27) and have not been enrolled in CMS yet. How do I go about this since the deadline for the initial assignments and quizzes is round the corner?""",
    """Exceptions: Part 3
I'm having trouble with the section called: Using the try-statement in reading from the keyboard. There is some given code, but I have issues when trying it myself.""",
    """Quiz 1 Followup
To be clear, did the post another student made titled 'Quiz 1 Confusing Format' show the proper way to read the question? His question was never answered because he said nevermind but I am still in the dark as to whether that was the proper way to format the question being asked.""",
    """E.java
Are we supposed to be opening e.java in eclipse? I took python last semester and I'm not sure why it keeps opening on atom for me""",
    """exception handling resources
I am working on Q1 right now and on JavaHyperText it says "there is a tutorial and problem set on exception handling" but I haven't been able to find these.  Where are these tutorial and problem sets located? Thanks!""",
    """Discussion Section
I am wondering if there is only one discussion section that I can attend (which is the only one with no time conflict with my other courses) and it is full and closed now, can I registered other section and attend the closed section?""",
    """Auto-formatting on save
By default, eclipse will not format your files automatically on save. You need to enable it by navigating to the following...

Preferences --> Java --> Editor --> Save Actions --> Preform Selected on Save (Check) --> Format Source Code (Check).

I also recommend organizing imports on save but that is up to you.""",
    """Not enrolled in CMS
Hello!

I enrolled in this class yesterday, and I just enrolled in Piazza today. However, I do not seem to be enrolled in the CMS for this course. Is this something that happens automatically, or so I have to register somehow because I was late to enroll?  As for missed assignments, is there anything I have to submit that is not posted on CMS?

Thank you""",
    """Catching all exceptions
In section 3. Catching and propagating thrown objects of the reading for the recitation assignment, a way to catch all exceptions, or even all throwables. Would there be any scenario where this would be useful? It seems that we would want to make our catch statements as narrow as possible.""",
    """JUnit
were we supposed to already have created a JUnit testing class?""",
    """How do quizzes work?
I did not do q1 because the notification from cms about it being available became lost in a sea of emails. I genuinely did not know that it was an assignment I had to complete. 

I do not want to miss another quiz in the future so how exactly do I find out when they are released? Do I just have to check Piazza and CMS everyday? Did I miss something?""",
    """Due Dates for Assignments
I noticed that the due dates for A0 and A1 are different on the course webpage and on CMS. Is CMS accurate or should we go by the dates on the course site?""",
    """In class demos
I noticed that on the course website under lecture notes, there are demo titles like "C.java" or "demoTime.zip" after the link to lecture notes. Is it possible to upload the demos so we can play it around? Thanks!""",
    """New Formatting Preferences
For recitation we had to make a mini hierarchy in a comment block. With the new formatting preferences, it is extremely irritating and impossible to get the indents to stay put upon saving. Can I just briefly and clearly explain the answer instead?""",
    """Question 5
In my code, for some reason, an if statement that determines if the user types DONE never evaluates to true. I tried testing it by first printing the string that is read from the user and then trimmed, and it prints DONE. Yet, a boolean expression equating the string to "DONE" never evaluates to true. Does the readline() and trim() functions change some aspect of the string that make this occur?""",
    """Where can I download the formatting preferences from?
Same as above.""",
    """A1 assert statements
Let's say this.name = n;

Should I assert n != null before i assign it to name, or should I assert name != null afterwards?

The example seems to be asserting with name but is it bad to assert only after setting name = n?""",
    """Class invariants
When writing the javadoc comments before each field, should we just copy and paste from this section or are we allowed some liberty (as long as the invariant is accurate to these descriptions)?

In addition, should we assume that the invariant for number of PhD advisees is that it is an int >= 0?""",
    """About the E filename
I just have a quick question concerning the work on Java for the second recitation assignment. I saved my work for the problem set but I have it under a different class name rather than the class name E. I was having some technical issues with the java file that was provided for us to get started, but I was wondering if it is okay to have the work from the second recitation saved in a different class name like "Second_recitation". Would we get points off if we used a different class name other than E for this recitation assignment?""",
    """A1, Step 5: How to create PhD objects for advisor1 and advisor2 (JUnit Test Cases)
My partner and I are confused on how to create PhD objects for advisor1 and advisor2 for our JUnit Test Cases in Group A.""",
    """Adding Advisees
In group B, when setting advisor p, and adding advisees to p, how can we access the original number of advisees in p and add on to that rather than the PhD instance we are adding advisors to?""",
    """Error from my file



I see this error and it says "insert "}" to complete class body"; but I think I already inserted the basket. Why is this the case?""",
    """Should setAdvisor2(PhD p) increase the number of advisees of p?
At the beginning of group B, the assignment mentions

"methods setAdvisor1 and setAdvisor2 must change fields of both this PhD and its new advisor in order to maintain the class invariant,"

which seems to imply that setAdvisor2 should change the number of advisees. Immediately after this, the bolded important note mentions

"In setAdvisor1(p), p gets a new advisee, so p’s number of advisees increases. Do not mistake the number-of-advisees field for the number of advisors. There is a difference,"

without reference to setAdvisor2. To clarify, should setAdvisor2 also increase the advisee count?""",
    """? : operator for group D in A1
Can we use ?: operator in areSiblings function of group D method in A1?""",
    """Type of setAdvisor1(PhD p)
What should the time of this method be? And also what does (PhD p) mean?""",
    """Group C Testing
For Group C testing, when it says, "This will require first creating two PhD objects using the first constructor..", does the "first constructor" refer to the one where both adviser 1 and 2 are unknown (first constructor we write)? Do we have to test both of the new constructors we write in Group C?""",
    """Testing group B
What value should I set to test setAdvisor1? More precisely, what is type PhD? How should I do to test it?""",
    """Eclipse preference


When I tried to use the Eclipse preference and view "compiler" or "Installed JREs", I can only see "editor" tab here.

Is this a problem with the Eclipse installation?""",
    """Recitation Problem 5
Is the method supposed to terminate if the user types DONE at any point or only in between rounds of two numbers? If I typed 2 then DONE, should it terminate or print 2?""",
    """Assert statements
Hello, are we allowed to use assert statements in our PhD class to enforce the preconditions?""",
    """Inquiry for A0
Hi! My A0 file is said to be JAVA File, but when I open it it is opened in Notepad. Is it okay to submit to cms in this form?""",
    """HW
Where can I find the classes Time and TimeTest?""",
    """Constructor Chain
When making the other two constructors, can we link them to the first constructor using the "this(...)" keyword and add the additional code for the new arguments?""",
    """How to tell how long a line of code is?
I know it is supposed to be around 80, but how can I tell if it is at 80 or not on Eclipse?""",
    """Primitive Number Types
Is the main difference between a byte, short, int, and long how much space each type takes up (as well as the different ranges) ? For example, is 100 stored as a byte the same as 100 stored as an int, except that it takes up less space? Why does it take up less space/how does this storage work? I'm coming from python and I find this feature of java confusing/ I don't really understand why its a thing and how it works. Any clarification would be appreciated.""",
    """Problem running JUnit tests
I followed the directions on the a1 pdf for creating the PhD test cases, as well as the testing class examples from the lecture slides. However, when trying to run the the test, I received an error, "No tests found with test runner 'JUnit 5'." How do I fix this problem?""",
    """How to declare a field of type PhD?
Do we have to create a new PhD object? or is it simply something in the format PhD p as written in the assignment?""",
    """Tests
I downloaded the files for the homework and only changed them by adding a test case, but for some reason there seems to be a bunch of problems with the test file. Not sure what's going on/what I did wrong (see pic below) :""",
    """A1 Assert
I'm on part 1 of 5 and was wondering, it says to use assert statements, can I use if statements instead? I'm trying to check if the string is empty or not.""",
    """gotAfter
For this method specification, do we still return true if the PhD students have the same year and month? Thanks!""",
    """Assertion
Is there a website that displays all the built in functions in eclipse?
Specifically, I'm looking for a function to check that string is not empty.""",
    """How to compare two PhD objects
One of the constructors of PhD class has precondition that "adv1 and adv2 are different". Since we need to check preconditions using assert statement, how do we know if adv1 and adv2 are not equal? Should we redefine equals() from the Object superclass? Thanks!""",
    """Question on constructor
This is a general question. I am confused about why we are writing so many constructors for the class. What is the difference of these constructors and what are they used for?""",
    """A1 Assert Statement for Constructor
I'm adding my assert statement for group A, and I'm wondering if there's an equivalent to != for type int. In other words, is there a way for me to check whether or not the user actually entered a month and year, and that what they entered is type int? Or can I just assume that the user entered the correct number of parameters, and that the parameters are of correct type?""",
    """gotAfter method
For this method, what variable should I use as the thing to be compared with p? For example, if I want to compare the year of one PhD with the year of p, I know that the year of p is p.year, what should the other be and why?""",
    """Lecture Videos
Where can I go to access lecture videos from last year? Having a hard time finding the videos on the course website.  Thank you.""",
    """Accept invitation after the assignment is submitted
My partner send me an invitation on CMS before our work is submitted. Is it OK if I accept the invitation on CMS after my partner submitted our work?""",
    """Evaluate Expression Statement in JAVA
Hi, did anyone make notes about the example of evaluation of java statement that showed on Tuesday's class? I was not able to find that in the sldies.""",
    """Group C: Changing advisee numbers?
For the constructors in part C, we assign specific advisors, so we are, in turn assigning additional advisees to adv1 and adv2.

Should these constructors increment the "advisees" fields for adv1 and adv2 (as the setAdvisor methods did)

I would think so, but the assignment does not say to do so.""",
    """Testing our assert statements in A1?
Are test cases for our assert statements necessary?  Or are they just recommended?""",
    """[ACSU x WICC] Mock Technical Interviews Opportunity
In preparation for the upcoming career fair season, ACSU and WICC will be hosting a mock interview event!

Time: Saturday, February 2nd&Sunday, February 3rd, 10:00am - 5:00pm

Location: Rhodes 400, 402, 405, 408, 412, 572-- Go to Rhodes Undergrad Lounge (Rhodes 411) first and an officer from ACSU or WICC will tell you which room to go to.

You can check out the event on Facebook:

Interviewees should sign up at:

You will be able to sign up for a 60 minute time slot, during which you will work through a technical interview problem with your interviewer and receive feedback afterwards. There are a limited number of spots so make sure to sign up as soon as possible! Please sign up for only one spot at this moment. Students who are interested in webdev or UI/UX interviews should contact Rishi Bommasani (rb724@cornell.edu) or Julia Chang (jjc438@cornell.edu) directly and specify your needs.

Interviewers should sign up at:

We are currently looking for experienced students to help out with the event as interviewers. You can sign up for as many slots as you like.

If you cannot make your signed up slot, please email Rishi Bommasani (rb724@cornell.edu) or Claire Cui (yc2296@cornell.edu) at least 24 hours before your assigned slot.

Have fun interviewing/being interviewed!""",
    """== vs. .equals in areSiblings()
Should we be using .equals() to compare advisers or ==? == is used to check if they point to the same object. If they have the same advisor, the pointers should be pointing to the same advisor object. However, if we use .equals() we would only be comparing an attribute of the advisor. 

Thanks""",
    """Testing Assert methods
When we come to testing assert methods, can we make a new testing method for testing all the assert statements or should we do them in testing methods A,B,C, and D?""",
    """A1 JUnit test
When we are writing the testing methods in JUnit test, can we use assert <boolean statement> or we have to use assertequals as mentioned in class? Also, what is the difference between these two?""",
    """Test Cases
Can we add more test cases to each of the groups than the instructions specified?""",
    """Dr. Java
I don't understand how to use Dr. Java. When you close the application it becomes a terminal and I do not know how to get it back. I am using MacOS.""",
    """Do we store the date as its own class or as a string?""",
    """no TA
Did the location for Office hours change? I can't find the TA""",
    """Recitation question 5
How are we supposed to execute a return statement when we are dealing with a procedure?""",
    """Preconditions on fields?
In our PhD class, is it necessary to write a precondition for the field name, as is done with methods?

name (a String). Name of the person with a PhD, a String of length > 0.""",
    """test cases
Are we allowed to use the examples given on the a1 pdf for our test cases?""",
    """Testing Group D
Are we allowed to use AssertTrue? If not, how do we run a test case on booleans?""",
    """A1 Group A variable declaration
Is it okay if we assign default values for the advisor1 and advisor2 to null and advisees to 0 in the declaration statement?  Or should we do this in the constructor?""",
    """Is working with a partner best practice?
I don't have a partner and am well into assignment 1.

Am I setting myself up for failure by working solo, or do people still do well without working with someone?

Thanks!""",
    """areSiblings(null) returns NullPointerException
If I evaluate areSiblings(null), when I try to access the advisor of p, I get a null pointer exception. I have read @94, which says that instead of throwing an exception, the code should just return false. Normally, I would run an assert statement in this code or a try catch loop, but it says in the instructions not to use any conditional statements, and there is no precondition saying p cannot be null. Is there another way to get around this?

Edit: my partner just came up with an idea and said that because java has short circuit evaluation, we could put p != null at the beginning of each boolean expression so that if p was null, the program would never try to evaluate p.advisor1. This worked, even though it's very redundant.""",
    """JUnit 4 or JUnit 5 Testing?
On the JavaHyperText page about testing assert statements, the page discuss how to use JUnit 4 and JUnit 5 testing. Which should we use for this project? """,
    """Preferences not accounting for
I updated my preferences by carefully following the instructions on piazza and checked them over multiple times, however when I save the comment with the <br>'s it still saves like this:""",
    """Testing Aresiblings
Should we test A.areSiblings(null)?""",
    """efficiency in test cases
Is it necessary to make the class PhDTest as efficient as possible, or is some repetition acceptable within the class, i.e. creating more PhD objects than absolutely necessary?""",
    """Number of Advisees
Can I create a method to increment the number of advisees for an instance of PhD? Or should I simply increment using the statement <instance name>.advisees += 1?""",
    """Eclipse Preferences not working correctly for Group D Testing
I'm trying to create the function gotAfter(PhD p) and i've coded something that looks like this: 

return (A > B) || (A == B && C > D ); 

but the parentheses are disappearing around the groupings which changes the meaning of what i'm trying to do. It changes to: 

return A > B || A == B && C > D; 

What should I change in my preferences to fix this? I've followed the preferences formatting carefully according to the eclipse preferences document and piazza post.""",
    """increment advisees - private?
I've seen other piazza answers suggest incrementing advisee number using object.advisee, but isn't this field private?""",
    """Test Procedure
I'm confused about the following requirement A1 instruction. “Does each procedure have a name that gives the reader an idea what the procedure is testing so that a specification is not necessary?". Does it mean that we could give each test procedure(include several assertEquals( ) sentences) a name instead of GroupA or GroupB?""",
    """Conceptualizing Siblings
What makes two PhD objects intellectual siblings? I thought that it meant they shared a first advisor, but from the a1 handout it sounds like they are the same PhD object. Can anyone offer some clarification?""",
    """Group B: Testing PhD Object for Advisor 1
When I try to test Group B methods, I'm not sure what to put on the field for the first advisor. I know that it's a PhD object but what kind of value do I put on there?""",
    """Testing the Assert statement
In the JavaHyperText, the assertThrow statement is described as “If the program catches ‘Assertion Error’, it will pass, and if it doesn’t the program will not pass. So, does not passing this statement means that our assertEquals have no Assertion Error and is good to go?""",
    """Formatting preferences
Is line wrapping at 120 characters something that needs to be done? Every time I break a line and save, Eclipse just puts it all on one line again""",
    """80 character rule
The specification for areSiblings, "

Return value of: p is not null and this PhD and p are intellectual siblings. " is over 80 characters without a <br>. Does that mean it is ok that it is slightly over 80?""",
    """A1 conditionals
In reading the instructions I read that we are not allowed to use if statements, conditionals, or for loops. Does a ternary count as a conditional?""",
    """Cornell Data Science Project Team
Interested in Data Science --want to learn about that and the Cornell Data Science Project Team?

Take a 1-credit course, starting this coming Wednesday, as indicated in the image below.

(If you can't see the image, get the pdf file here: Data_Science_Slide.pdf).

For more information, email.
Jia Jiunn is taking CS2110 right now and asked us to post this information.""",
    """WICC's Mixer to find Programming Partner
Are you having trouble finding a partner with whom to do CS2110 assignments?

Attend the mixer organized for the purpose of helping you find a partner.

It's this Monday, 4 February, 5-6PM for 1000-2000 level courses, in the
Gates 3rd floor lounge. Come!

It's organized by WICC: Women in Computing and Cornell.""",
    """Bug when writing testGroupA


I don't really understand what this means""",
    """Making setters for other fields in PhD.java
is it ok for us to have setters for fields like name, year, etc so that we can alter values in PhDTest.java without accessing private variables?""",
    """Resubmit Homework 1
If we got a 0 on homework 1, how do we submit to get a 1?""",
    """Number of advisees class invariant?
If the number of advisees is never given by the user, so there is no real constraint, then are we allowed to declare the field equal to 0, or can we just leave it with no set value upon declaration, so it would be null?""",
    """PhD p= new PhD();
if i try to make a new PhD object using PhD p= new PhD() shouldn't it work? My PhD constructor has the (int m, int y, String n) as parameters but shouldn't creating a new PhD object with nothing in the parentheses just result in default values? (I am trying to test my constructor from group A)""",
    """AssertThrows Confusion
Hi,

I'm confused about AssertThrows. In the example, it says that the body creates a new object of class P. Does that mean that I can only test objects? In order to test all the assert statements I wrote in class PhD, do I just create a new object of the PhD class in assertThrows?""",
    """setAdvisor1()
When we call setAdvisor1(PhD p) on a PhD object, this object receives a new advisor, p, and p gains one more advisee. Do we need to create a setter to change the number of advisees or can we just increment p's advisees by 1 within the setAdvisor1(PhD p) function?""",
    """setter in constructor
can we call a setter in a constructor? ie calling setAdvisor1() in the new constructors that we make?""",
    """precondition for setAdvisor1 method
when the precondition says "the first advisor is unknown", does this mean that we check: assert this.advisor1 == null? Or do we also need to consider situations when this person already has an advisor1 and we are changing it?

Thanks!""",
    """precondition for areSiblings
is there not supposed to be a precondition for areSibilings? can we still add assert statements ie one for making sure p and the object we are calling the method on are not the same""",
    """Testing assert statements
Is the assignment asking us to only test assert statements for constructors or for all of the assert statements?""",
    """testing asserts
if we test to make sure assert statements are working, do we try values that falsify the assert statement, in other words, are we supposed to be getting an error in our J Unit test?""",
    """Eclipse has no "remove redundant modifiers" and "remove redundant semicolons" options
I wanted to set my eclipse according to the preference. But in Additional saved action -> unnecessary code, there's no "remove redundant modifiers" and  "remove redundant semicolons" options. So I could only activate 11 (instead of 13) save actions. What should I do? Thanks a lot!""",
    """Accounting for date of PhD attainment
Must we account for the fact that a PhD holder (realistically) should not have an advisor who got their PhD on a date after them?""",
    """Why should A.areSiblings(null) return true?
Why would we want to say that a PhD and null are siblings?

The spec for areSiblings says that p should not be null (pg 6), but then on pg 7 it says that A.areSiblings(null) should return true. ?""",
    """Comments on test cases
Should we include comments in our test cases to clarify what each block of assert statements is testing?""",
    """Save preferences
When I define a method, I’m using “return this.<name of field>”

When I then save the java file on eclipse, eclipse gets rid of the “this” and makes the definition just “return <name of field>”.

Are my preferences incorrect?""",
    """Need to use getter to access year and month of p?
In the function gotAfter(), to access the private variables inside p, do we need to use getter methods or can we directly access its variables?""",
    """type inquiry in java
Is there any function that can return the type of a variable as a string?""",
    """A1: Deduction by grading program
I'm confused by this step:

If a method spec does not have a Precondition, do not put an assert statement in its body. If a method spec does have a Precondition, do put appropriate assert statements in its body.

Given that we're supposed to test assert statements for the preconditions in another test constructor, what does this mean?""",
    """Assignment due dates
Where can I find the due dates for the assignments?""",
    """A1: Testing Assert Statements
I'm not sure what the second item underneath the JUnit Testing web page is in the Java Hypertext.""",
    """Issue with first constructor call
I am getting the warning 'PhD cannot be resolved to a type'. When I try to search this message, it usually refers to the path being incorrect or the class being compiled incorrectly. It seems like my path is fine, and the constructor in PhD.java was checked by a TA and seems to be all good. So I am not sure what is wrong. Here is a screenshot of my file path and the line that has the warning if that helps.""",
    """Precondition for areSiblings(PhD p)
For function: areSiblings(PhD p), is "p is not null" the precondition? For other functions, preconditions are listed clearly, but none precondition is listed for areSiblings(PhD p). However, it says that: Return value of: p is not null and this PhD and p are intellectual siblings. So, I feel confused about the precondition for areSiblings(PhD p).""",
    """Default Package
Hi, I have problems with default package when create class. I don't know how to make default package appear?""",
    """test procedure
The directions say:
Does each procedure have a name that gives the reader an idea what the procedure is testing, so that a specification is not necessary?

Does this mean we should change our procedure names from something like testGroupA to something that helps us assess what we are testing?""",
    """assert type
Should we put in assert statement to make sure the field are the right type (string, int etc.)""",
    """testing q.gotAfter(p)
When testing gotAfter with q and p having the same month and same year, can we use the same object in the test or should we create 2 separate objects with the same month and same year?""",
    """returning advisor
When we return the advisor of the PhD should we return the name of the advisor?""",
    """Length of Name Discrepancy
In Part 3, when declaring the field name, the spec says it should be "a String of length > 0", but when making the constructors in Part 5, the precondition says the name "n has at least 1 char" (meaning it could be a single character. Which one is correct?""",
    """Test case for Group B
When testing Group B, do we need to test Group A again if we create two new or more objects using the constructor in A?""",
    """Creating the same object
When we create two new objects, if they have the same values for the field, is it adequate to say they are the same object? or they are actually two different objects that have the same information?""",
    """Constructor in Group C
Can we use the setters in Group B to set the advisor in the constructor in Group C?""",
    """Test Cases
Are the provided test cases for gotAfter() and areSiblings() sufficient for full credit, or are we expected to come up with more of our own? If so, are we graded on how comprehensive our test cases are, or just on the functions themselves?""",
    """Duplicate parameter ae
I am getting a "Duplicate parameter ae" error message when trying to name an assertion error for a try-catch block. I haven't named anything ae except in Recitation 2. How do I fix this?

edit: never mind I'm dumb and forgot a bracket""",
    """Set self as advisor
The preconditions for the set advisor methods do not prevent a PhD object from setting itself as its own advisor. This sounds like an error. I assume this should not be the case.

However, we are also not supposed to change the preconditions. What should we do?""",
    """Test case for Group C
We are supposed to first create an object using Constructor in Group A and then use the two new constructors to add the information of the two advisors into the object. But are we supposed to test whether the object with the advisors' information has the same m, n and y with the first original object?""",
    """Test Cases
We have been told to "Test the methods in the group thoroughly" in section 5. Does this mean that we add more test cases than we're told? For instance, for testGroupA do we add more than just 6 assertEquals statements? Or does thoroughly testing simply mean that we use the same 6 assert statements but keep changing the values to see if it works or not?""",
    """Run configurations
How do you choose which project to run when you click the run button? My Eclipse runs E.java from Recitation 2 when I click it, and I don't know how to change it to a1.""",
    """areSiblings()
Is it necessary that the advisor number also matches i.e. adv1 == adv1 or adv2 == adv2?

Or are they siblings even if they have same advisors but one is adv1 for one and one is adv2 for the other?""",
    """Assert Statements
Is there a difference between a field being unknown versus being null? I'm trying to write assert statements, but I'm not quite sure how to check that a field is known/unknown.""",
    """Assignment 1
Because number of advisees should be under complete control of the program, does this mean we make the access provider for advisees private?""",
    """Creating a new line in Assert Statements
I know that our code is not supposed to be more than 80 characters per line. However, one of my assert statements runs more than 80 characters. I keep trying to put half of it in a new line, but whenever I save my project, Java automatically puts it back into one long line. How do I fix this?""",
    """Comments in Tests?
Should/can we add comments (or specifications) to the test procedures to clarify more specifically what each one does?""",
    """Order of fields in constructors
The constructor example in goAfter has its name field first, then month and then year, but the order is different in the original constructor. So we have changed it because it was producing an error in the program. Is that fine?""",
    """additional files
Are they're any additional files we have to download besides the three pdfs in the original A1 post?""",
    """Testing assert statements requirements
If we do not test the assert statements at all will we lose any points. I feel like the asserts are fairly straightforward.""",
    """assert testing
If we have put the assert statements in functions like setAdvisor1() and if the whole function is passing the test cases, it means that the assert statements are correct. Do we still need to test separately for these assert statements?""",
    """Suggested Timetable
My question for assignment 2 is: will there be a suggested timetable like in assignment 1?

Something like this:



I understand this may be a bit much to ask, but it was nice knowing how long the assignment should take (on average).

Thanks in advance!""",
    """Late for lunch with professor
Hi, I see on the piazza note that we need to be there at 11:45am. However, my class doesn't end until 12:05pm. Can I go afterwards?""",
    """Rectangle.java is now up on Piazza !
Sorry for the delay!""",
    """String methods only?
In a2, are we only allowed to use String methods or can we use anything in the API?""",
    """"Case Where l=1"?
In the to do list for recitation 3, it says that we should fix the first constructor for the case where l=1. Does something go wrong in this case? What are we supposed to fix?""",
    """StringBuilder in A2
Can I use java.lang.StringBuilder and it’s functions for A2 instead?""",
    """Int to Double Problem
In the recitation 3 assignment, in trying to test the area with an assertEquals statement, we are getting an error because Java can't cast int to Double, and visa versa. How do we remedy this?""",
    """R3 Clarification
The recitation 3 instructions weren’t very clear to me. Will we need to submit to CMS or not? If so, when will it be up on CMS?

Also, the instructions for R3 posted on piazza are rather vague. I attended section but am still unclear what exactly to do other than generally create a test class and test the specifications. Any help/clarification would be appreciated.

EDIT: Just saw todo was added to instructions.""",
    """Recitation3 file upload
There's only a place to upload the Rectangle.java file. Aren't we also supposed to upload the JUnit test file?""",
    """R3 is whack
I'm in my recitation right now and no one has any idea what is going on. The instructions are very vague (far from recipe format), the program apparently requires the usage of AssertThrows (which was not only never taught but not referenced on the Java Hypertext) and we are all stuck on what we need to do and how to even do it. 

Was wondering if the Pizza gods could provide some clarification for what is required on this assignment. 

Thanks :)""",
    """Recitation 3 questions
I assume we'd need to throw an exception when the parameter of setLength or setWidth is negative (in order to truthify class invariants), right?

Also, I don't understand why there's a need to test the equal case when testing constructor public Rectangle(double l).""",
    """R3 when l or w == 0
The specification says to throw an exception when length and width are negative. What should happen if either are zero?""",
    """Spacing Preferences
Whenever I try to save changes in Eclipse, it keeps adding spaces after my variable assignments

even though all of my Save Action preferences match those shown on the pinned Piazza post

(so for example, int a= 5 becomes int a = 5). In the Save Actions preview window it shows this

happening sometimes and not others:

How do I stop this from happening?""",
    """Recitation 3
I'm wondering how to use constructor 1 in constructor 2 , because I can't set width=null，right？

And what does the fix shadowing mean in the setWidth and setLength?""",
    """A2 isMidSame method
Should s = "1234123" return true or false? The specification makes it sound like it should be true, but the test cases do not cover such a case.""",
    """Confusion on recitation instructions
what does "test positive, negative, zero, equal" entail?""",
    """Throwing an exception
Is there a certain type of exception we are supposed to throw if either l or w are negative?""",
    """Error Using assertEquals in Recitation 3's Rectangle Test
I was able to use assertEquals without error for all the tests up to the tests for getArea, where I am getting the error "The method assertEquals(double, double) is ambiguous for the type RectangleTest"

What does this mean? Why am I only getting an error in the tests for getArea when it worked fine in the tests for every other method?""",
    """stringbuilder class for A2
Are we allowed to use the string builder class in this assignment?""",
    """Adding "import static org.junit.jupiter.api.Assertions.assertEquals;"
I was trying to use assertEquals for testing, and it didn't work until I typed in 

"import static org.junit.jupiter.api.Assertions.assertEquals;"

up at the top. What exactly does this do, and when do I have import stuff like this in general?""",
    """"Double" v. "double"
So when we first define the fields "l" and "w" I notice that "Double" is used. I changed this to "double", but that causes an error for "w" since I assign "null" to w in various instances. Am I not supposed to change "Double" to "double" up here, or am I supposed to handle this error some other way?""",
    """Repeating assertion
While working on Group C (2 constructors), do we need to assert the precondition?

I am using this() and setadvisor() so preconditions should be taken care of there. Do I need to assert them again in group C?""",
    """Checking whether or not width is null in test cases
Since we have hidden the width field, and getWidth( ) is supposed to return the length when the rectangle is a square, how should we check to make sure that width is null?""",
    """This
If we did A1 without using "this" in the second and third constructors, is it ok?""",
    """dupCaps
Are we allowed to use a loop to implement dupCaps?""",
    """Using setWidth( ) to assign a square a value for the width field
Should I prevent the user form using setWidth( ) to change a square rectangle's from null to a value, when the value they want to set is the same as the length already defined?""",
    """Should <br> be automatically deleted when copying specs? When I copied mine everything looks right except <br> is still in the spec.""",
    """Width
When width is null, should our Width getter return null or the length of the rectangle (since technically, if width is null, the rectangle is a square and the length IS the width).""",
    """A2 (atLeast2)
In the comment, it is said that s.index0f() may take time proportional to the length and we should not call the method several times. 

So is the function s.indexof() not allowed in this part?""",
    """Assertion Question
When we assert areSiblings, the preconditions states p cannot be null and we asserted as such. However one test case provided has p as null and so it be impossible not to get an assertion error. How do I resolve this?""",
    """Constructor in Rec 3
In the second constructor, do we call the first constructor using this? I'm doing that and there's an error saying the constructor Rectangle() isn't defined""",
    """making sure advisor is unknown
Should we check to make sure the advisor are unknown?""",
    """Assignment1
Do we make constructors have access modifiers too?""",
    """Assignment1
Do we need to make any assertions in the getter methods?""",
    """Testing Squares
I am confused about how to test the square in condition 1 and how to make width null for this spec?""",
    """# of Assert Tests
Hi! In Step 6, the instructions ask us to test the assert statements. I've only gotten to 14 assertThrows statements, but the instructions say there should be 16-24. For cases where I wrote, for example, assert a > 0 && a < 10, I used two assertThrows statements so I don't think not fully testing the assert statements (of which I have 11) in PhD.java was my problem. Is anyone else having a similar problem? Do people have more than 14 assertThrows statements? If so, any suggestions on what I may have done wrong?""",
    """gotAfter method
In the instruction i understand that we aren't allowed to use an if statement to check to compare between years and months, but are we allowed to use an if statement in the method at all?""",
    """Method nextLowerCase char as int?
In the hint of the nextLowerCase method, it is said that "Principle: Avoid the use of int constants for characters."

Are we not supposed to use the int value of char to, say, find out if a char is a lower case English letter or use operations on int to convert it to the next one? The static method isAlphabetic() from class Character or other similar methods don't work since they regard, e.g., å as an alphabetic character.""",
    """Renaming from Phdtest to PhDtest
I accidentally named the test class Phdtest, and it is not letting me rename it to PhDtest (which it says in the rubric will lose points). Is there a way to do this?""",
    """Consultant/office hours
Some of the consultant/office hours on the calendar doesnt have a room number. Will the room number be posted when it is known?""",
    """Where to change numAdvisees?
We put the numAdvisees as a private static int directly under the public Class PhD. But we could not figure out where to put numAdvisees = numAdvisees + 1. Where should we put it?""",
    """Java Doc
Do we need to write down the return type (for example: the returned value is int) in Java Doc?""",
    """Equality of Two PhD Advisor
Can one PhD's advisor1 is equal to the advisor2?""",
    """Swap Discussion
Although it is past add deadline, is it still possible to swap recitation sections?""",
    """2111
I've gone to all the sessions for 2111 on wednesday so far and I am still confused how this works. Do we learn new material in advance?""",
    """Assignment 1
By convention, I know that when using assert equals, you put the expected output first in the parenthesis. Will we get points off if its not written like this.""",
    """Problem understanding A1 guideline
I have some problem understanding a part of A1 guideline.

The guideline says

 Did you write one (and only one) test procedure for each of the groups A, B, C, and D of step 4 and perhaps another for assert statements? Thus, do you have 4 or 5 test procedures? Does each procedure have a name that gives the reader an idea what the procedure is testing, so that a specification is not necessary? Did you write all the test cases as required in the discussion of each group above?

So does it mean we need to write another test procedure to test all assert statements? Do we need to do what we did in recitation this week (like all those assertThrow stuffs)? and also do we need to change procedure name from GroupA to something like testingConstructors?""",
    """setWidth( )
When user use setWidth( ) to set the width equals to previous long, should it set width=null, or still set width = previous long? If it set width = previous long, does it break class invariant?""",
    """groups for recitation
are we allowed to work with people outside of our recitation section?""",
    """AssertEquals Parameter Order
When we test with our assertEquals() statements, will we get points taken off for switching the order of the two parameters. i.e. assertEquals(whatever we test, expected) versus assertEquals(expected, whatever we test)""",
    """Assert statements for A1
Hi, is it OK if we write less than 16 assert statements since we refer to the first constructor when we define the second constructor, and we refer to the second constructor when we define the third constructor? Thanks!""",
    """Throwing an Exception vs. AssertionError
For Rec3, the constructor specs say to throw an exception if l or w is negative, and if l is negative. Is there a difference between throwing an exception in my code if these values are negative and using assert statements to allow an AssertionError to be thrown? Should we throw the exception ourselves or just use assert statements to create an error when the values are negative?""",
    """Private Advisees
Because advisees is private, do we need to add a setter method to add 1 to advisees in setAdvisor1 and 2? Otherwise we can't access the private attribute of the PhD parameter, right?""",
    """R3 Negative
The instructions say to fix the constructor to handle negative numbers. Does this mean fix it to create a rect object or fix it so that the test procedure runs without failure?""",
    """setLength
Neither the instructions nor javadoc say for setLength to not allow negatives. Is the code supposed to just accept negative values, going against intuition?""",
    """setLength() and setWidth
When I set my length and width, it's allowing me to input negative numbers even though I have my assertions for my constructors in place.  Am I missing something?

Many thanks""",
    """Are we allowed to add the 80 characters line?
Not sure if adding the 80 characters line to A1 is allowed or not in terms of formatting.""",
    """A2 dupCaps() testcase "Å"
When I was doing dupCaps(), I used the method toUpperCase() for every character in the string and the method considers the character "Å" an uppercase character and spits out "Åå" instead of expected "Å". What should I do?""",
    """Can length or width be 0?
According to the preconditions, l or w just has to not be negative. What about 0? Is it allowed to be 0?""",
    """Assert input type
Do we need to enforce/ assert the input type for the constructors? For example, do we need to assert that the month and year are ints and the name is a string since the parameters already defined their types?""",
    """Test without constructors
How do we test getLength() and getWidth() without using the constructor?

If we don't use the constructor to create a new Rectangle object, we cannot use getLength() and getWidth() methods.""",
    """Excess Test Procedures
Will we be penalized for writing more test procedures than necessary?""",
    """Testing getArea()
When using assertEquals() to test the method getArea(), I got this error message. 



assertEquals() works for all my tests before. So I don't really understand what this error means.

Thanks!""",
    """The Format of Test Procedures
I added print statement in the test procedures, shall i delete them when submitting, or can i comment them?""",
    """A2 atLeast2() clarification
Do overlapping appearances count?  I.e., should atLeast2("ababa", "aba") return true or false?""",
    """assignment2
Hi, Im having issues making Junit5 available. So on the document for assignment 2, I'm following the first option in part 7 of the instructions. when it says to say that we want Junit 5, does this mean we should click "New Unit jupiter test" at the top. Also for this what should I do for my source folder...""",
    """grading for recitation?
Hi, I was wondering if the recitation assignments are graded on correctness or completeness?""",
    """object partition?
What does object partition mean in today’s class?""",
    """Testing Assert Statements A1
I read item 2 for junit testing and am still confused on how to test the assert statements. Are we supposed to test that the statements themselves work by verifying it correctly throws an exception when needed (and doesn't when it shouldn't)?""",
    """Bottom up Rule in arrays
Hello, 

In lecture just now, Prof Clarkson mentioned that by the bottom up rule in following case, toString() in Cat partition would be called.

However, doesn't the cat partition have "blinders" on because the array stores objects of type Animal? 

Therefore, by this logic, wouldn't the toString() method in Object be called instead? 

Thank you!""",
    """Different rules applied
In today's lecture, we talked about two cases, the first one being when the bottom up rule applies(toString case), and the second one being the compile time rule applies(purr case). Why are these two different? Is it because toString is built in?""",
    """Test Groups A1
Should the test procedure names be something more specific than testGroupB() so specification isn't needed? For example, could the Group B test procedure be named testSetters()?""",
    """Line Formmatting
Our Boolean expression goes over the 80 char limit but autoformatting does not allow us to split the line up into multiple lines""",
    """second constructor
so when we test the second constructor in Rectangle.java, does width remain null (Double default value)? or should we set the width to length?""",
    """where to find document for 2111
Hi, I cannot find the link to the lecture demos for 2111. Could someone post it? Thx!""",
    """A1 superclass constructor
Should we be using a super() constructor for the later versions of PhD objects with advisors? Thanks!""",
    """dupCaps: return s
Are we allowed to make a new string and append to it? or does return s imply that we must edit the original string and return it?""",
    """Comments in A1
can we add our own comments to our code that help us understand what’s happening ?""",
    """A2: atLeastTwo()
Can we use indexOf() and contains() in atLeastTwo() in assignment A2?

Thanks!""",
    """== and .equals
Can we say something like this: if a == b, then a.equals(b) is definitely true?""",
    """sortToSame()
For the sortToSame() function, do we have to import arrays in order to use its methods?""",
    """Can we create more than one Test procedure to test different parts of the Rectangle class?
Can we create more than one Test procedure in RectangleTest.java to test different parts of the Rectangle class? It would make the code much more easy to read and debug.""",
    """Classes not in default package
I was told that my I did not put the two classes in the default package; they are in package a1. I thought I followed the instructions correctly, so I'm not sure how to fix this. Any ideas on how to put them in the default package? Would I have to create a new project that is in the default package and then copy and paste my code into there? This is what my package explorer looks like right now:



Thank you!""",
    """Can length of a rectangle be null?
Can length of a rectangle be null? I see that length is of type Double. 

Also, why does getArea() have a return type of Double instead of double? Is it possible for the area of a rectangle to be null?""",
    """Test constructor positive
In the TODO.txt, we are asked to test constructor 1 and 2 when they take positive values. When they don't throw an exception, how do we write test cases? Can we use getLength() and getWidth() to do that?  If so, wouldn't that be the same as how we test the getters?""",
    """questions about string
How do I get a specific character of a string? For example, I would like to get the third character from a string, how could I do this?""",
    """method dupCaps
How should I find conventional A...Z from a string? Is there a method for this?

Also, should I look into loops to write this method?""",
    """Searching for partner
Is anyone looking for a partner right now?""",
    """Recitation 3 Problem
I'm getting this error when I try to make an object using the constructor.

The constructor Rectangle(double,double) is undefined. 

How do I fix this?""",
    """r3
should we be able to set the length or width to a neg value?""",
    """Recitation3 constructor 1
In case that l = w (or one of them is negative), should we return width = null?""",
    """Test for setLength
I created a square case in the test for setLength(), but whenever I run it, it always says NullPointerException. What might be the problem?""",
    """how to change default from atom to eclipse
Whenever I open java files my computer opens them in Atom. How do I change the default IDE to Eclipse?""",
    """testIsCatenated

Why does testIsCatenated not have a green/red bar when we try to test it (everything else seems to have a green check mark next to it)?""",
    """Non ASCII characters
Should I assume that the instructors will only test ASCII characters, when I'm implementing duCaps?""",
    """WICC Women in Computing at Cornell
WICC First General Body Meeting on 12 February (Tuesday)!!

5:30 in Gates G01""",
    """Assertion vs exception
In recitation 3, when the method specification says “throw exception…”, would it be alright if we used assert statements? 

When these statements are false, an exception of AssertionError will be thrown right?

Can we use exceptions and assertions interchangeably?""",
    """IsMidSame()
When you say that the characters on either side of the the middle character must be the same, you mean that they must be the same letter but that case doesn't matter, correct? (Based on the fact that there are no test cases to test something like "Aba", I'm assuming it doesn't matter, BUT I wanted to double check).""",
    """Range
Does Java have a range function like python?""",
    """sortToSame
Could some one please give another hint on how to do sortToSame? I have look through the methods and cannot find an way to implement them according to specification. Thanks!""",
    """isCatentated
For the function isCatentated do we have to use a loop?""",
    """isMidSame() clarification
The specification suggests that we are allowing non-palindromes to be true. For instance, "12312" has the same characters on either side of the middle character, as does "1234213" - both of fit the specification as something to be returned true. In other words, there is no requirement in the specification that the characters on each side be ordered in a particular way.

Am I reading this correctly? Thanks in advance.""",
    """Loop Comments in A2?
Do we have to include comments/annotations around our loops as shown in the videos/examples in the Java Hypertext section on loops and loop invariants? (Will we still get full credit if our code works and we don't include this?)

Thank you""",
    """isMidSame
In the isMidSame function should a string input of just a space count as true? A space adds length to a string so I believe it technically counts as a character, but I am unsure from the method specification how I should handle it.""",
    """Recitation
My partner submitted recitation 3 before I accepted the group request. What can I do about this?""",
    """error in first line of module.
Hello,

In every module I write in eclipse, I get an error saying: Must declare a named package because this compilation unit is associated to the named module a1.

I looked up previous Piazza posts on this, with the answer being that I need to change my compiler level to 1.8. I did that, yet I am still getting this error on the sidebar. What could be the problem?""",
    """A2 dupCaps
For this function, do we have to insert lowercase letters into the orignal string, or can we use other methods(e.g. make a new string and add the elements to it) to achieve the same result? In other words, does the insert mean we have to do insert in our function, or does it just mean the result that we need to achieve, but not the only way to solve this problem?

Thanks!""",
    """Solutions?
Hi, I was wondering if we would get a standard solution for each recitation assignment after the due date so that we can know if we made any mistakes and what to pay attention to during review?""",
    """nextLowerCase method
I'm confused about this principle for the method: "Avoid the use of int constants for characters."

Does this mean you aren't supposed to cast characters into its int representation? If so, I don't understand another way to complete the method.""",
    """A2 for loop in dupCaps
Can i use for loop in A2.dupCals()?""",
    """Could String be a null object in A2?
Could the String potentially be a null in A2?""",
    """findShort
Are we allowed to use isCatenated in findShort for more than just checking the criteria?""",
    """ismidsame
i feel like i am overcomplicating this method, do i have to turn the substrings into an array to compare them?""",
    """Recursion
I was wondering if we were allowed to use recursion on the method isMidSame?""",
    """prevchar
may i ask why we should avoid using int constants for characters in prevchar?""",
    """isMidSame unnecessary analysis?
Would it be considered unnecessary to have a condition for the case where there's only 1 element in the string? I'd like to just preface my if statement with an s.length() == 1 || (general condition) , to cover the case with 1 element. Is this an efficient way of doing this or am i missing some kind of tactic?""",
    """comparing arrays
I found the method for comparing two arrays, but why using array1.equals(array2) cannot properly compare two arrays?""",
    """Assignment to a simple variable
I have watched the video, but still do not really understand the purpose of the information in the assignment to a simple variable. Is it basically that since we know the post-condition and execution statement, we want to construct a pre-condition that will not be false?""",
    """Max line length
When I save my file, eclipse formats some of my if-else statements so that the if statement is one line. This makes my return statement go over the 80 line limit, but in my Eclipse preferences I have set that the maximum line width should be 100. Is this fine?""",
    """isCatenated
Can i use recursion in this method?""",
    """recitation 3
Do we need to do the homework pdf file on recitation 3's URL link?""",
    """Eclipse Issue
Something suddenly happened with my Eclipse, I'm not sure why I can no longer drag the rec4 and rec4 test into my folder. also, in the past, if i clicked file, new, it gave me the option to create new java project but now it doesnt.""",
    """Efficiency concerns for atLeast2
So in the comments for atLeast2, it mentions that using contains() and indexOf() are inefficient. Does that mean we shouldn't use these in our solution? if so, where might I find a method that is more efficient?""",
    """method findShort
when I write s.substring(0,k), Java returns me the entire string s. Why is this the case?""",
    """Mental Health Makeathon
The Cornell Design & Tech Initiative is holding a Mental Health "Makeathon" on 16-17 Feb.

Read the image shown below to find out what it is about. Take Part! Sign up!""",
    """How does indexOf work?
Assuming that s1 is contained in s, when you use s.indexOf("test"), does java search the entire string, or only up until the first instance. 

In the case that it only searches up to the first index, could we then use indexOf again, except with a substring of the second half of s?""",
    """Practice Problem
the question said the first part is easy but i got stuck after getting, x=B and C=t. what are we supposed to do next""",
    """sortToSame
Just out of curiosity, why can't we convert the string to an array of strings and sort that?""",
    """atLeast2 indexOf() vs lastIndexOf()
I noticed that in other Piazza posts, you said to think of a way to only use indexOf() once. Would lastIndexOf() be considered the same as indexOf()?""",
    """Do we have to do sortToSame in five lines?
I have slightly more than five lines---is this ok? In other words, what does the instruction "Method sortToSame uses a loop or recursion and doesn’t follow the instructions" mean? What situations may be considered as "not following the instructions"? Thanks""",
    """Clarification on "unnecessary case analysis" for nextlowercase?
What does it mean when it says "avoid unnecessary case analysis like the plague"? I'm not sure how to create a function that does not involve checking each character of the string for case that satisfies the given parameters... thank you!""",
    """Can we use StringBuilder in A2
Hi, can we use StringBuilder in A2?""",
    """Cannot invoke sort() on the array type char[]
I am trying to use sort() in the following way: random_array.sort(), but Java is giving me the following message: 

Cannot invoke sort() on the array type char[]

The documentation seems to suggest this should work, what am I doing wrong?""",
    """A2 asserting preconditions
Do we need to assert preconditions on A2, and going forward?""",
    """a2 Test


Hi When I run the test file. It looks like this. 

and I can not find the failure trace.""",
    """a2 ascii tables
are we allowed to use ascii table values for functions like nextLowerCase and dupCaps? i have heard different things from different people so i just want to confirm. thank you!""",
    """Missed Quiz 2
Will late submission be accepted? If not, will any of the quiz sores be dropped?""",
    """Do we need to insert comments for A2?
Assuming our functions aren't overly complex?""",
    """Abstract class vs interfaces
Can interfaces have fields?""",
    """Running late to 11am OH
Hi all,

Due to the weather condition the bus to campus has been delayed. I might be 10-20 mins late for my OH. Sorry for the inconvenience!""",
    """nextLowerCase and dupCaps
For method nextLowerCase(String s) and dupCaps(String s), should we simply edit and then return s, or should we return an edited copy of s without changing s itself?""",
    """Lecture 6 Equals methods
In the Equals methods for points and animals, the argument is cast up to an object. Why is this necessary? The getClass method can be used even for subclasses of the Object class such as the Animal class and Point class right?

Why not just leave the argument in its original class throughout the entire equals method?""",
    """Question
When I use charAt and append it to a string, it works. But shouldn't this give me an error since charAt gives a character so I would be trying to append a character to a string?""",
    """How could I cast the char to String?""",
    """assert vs. assertEquals
I don't understand the difference between using an assert statement vs an assertEquals method call.  Is one preferential over the other, and if so in what cases?  

Say I am testing whether the method call two() returns 2.

assert 2 == two();

assertEquals(2,two());""",
    """abstract class methods
could you create a method in an abstract class that is not abstract? and that subclasses could refer to by doing super.() ? or can an abstract class only have abstract methods.""",
    """A2 Method 2
Do we have to return a modified version of the same string object itself or can we make a new string that is a copy of the original string object with the required modifications?""",
    """isCatenated
Would a test case such as isCatenated("bbb", 3)  and isCatenated("abcdef",6 )  be true?""",
    """SortToSame
In the last test case of method sortToSame why would the result be false? Since the sorted arrays both end with 'v'.""",
    """Can we use break in our loops?
For findShort, the only way we were able to get our code to compile was using break. Is this allowed/fine, or are we supposed to try not to use break?""",
    """Character class methods
While A2 aims to familiarize with String class methods, it is fine to use Character class methods right? 

For example, can I use the toLowerCase method of the Character class instead of that of the string class?""",
    """how could we say that two array are equal to each other?""",
    """Using libraries in program
Are we allowed to use the StringUtils library in our code?""",
    """Is it important to comment explanations for our code?
I know the assignment is straightforward enough that graders will be able to eventually tell what is happening, but are we still expected to add non-javadoc comments to explain any non-obvious blocks of code we might have?""",
    """Can you process a string backwards in a for loop?""",
    """Coding for edge cases
When coding for edge cases, such as when the input is an empty string, and having the code do something specifically for them be considered as "violating the spirit of the assignment"?""",
    """sumDif test cases required?
do we have to add test cases for sumDif, the pre implemented method, to A2Test? I'm not sure if I understand the comments there.""",
    """arrays
Can you compare arrays with just == or do you need to use the method?""",
    """atLeast2 overlap
This doesn't actually apply to any of the test cases but suppose I wanted to see if "abab" appeared twice in "ababab". Would this return true as in the middle ab is counted twice or false as in every occurrence has to be completely separated with no overlap.""",
    """atLeast2
although u said we should note how long indexof will take, are we still allowed to use it? can we use indexof and lastindexof:?""",
    """TODO for function dupCaps is blank
TODO for function dupCaps is blank. Are we supposed to complete it?""",
    """TODO for dupCaps
What are we supposed to write in the TODO section for dupCaps? Should we explain what we did in the function?""",
    """A2 regex?
Are we allowed to use regular expression for assignment a2?""",
    """The difference between A=B and equals(A, B)
Hi,

I feel confused of the difference between A=B and equals(A, B) when A, B are String, Arrays or something else. Are they the same?""",
    """Assignment 2
So I know with this assignment as long as we pass all test cases we are fine... I just want to make sure that I didn't do too much case analysis and I won't get points off.

For example, is it okay if for at least 2, that I check for s.length()==0 and s1.length()==0

and then do the rest ..""",
    """dubCaps
my code is converting weird characters like Å to lower case versions and adding it to the string, causing it to fail the test case: assertEquals("Å", A2.dupCaps("Å"));

How should I handle this, I thought isUpperCase only applied to letters A..Z.""",
    """dubCaps: What happens if the letter next to an upper case is the lower case version of that letter?
I think there's a contradiction in the specifications of dubCaps and the JUnit test. In the specifications, it says that the string 1Z$Bby should return 1Zz$Bby. In other words, if a capital letter (in this case, B) has the lowercase version of itself next to it already, we don't add another lowercase version of this letter. I wrote my code to follow this rule. But in the test case, one of the statements asserts that 1Z$Bby should be 1Zz$Bbby, which would suggest that we do add another lower case, even if one was already in the correct position in the original string. Am I missing something? Which one is it supposed to be?""",
    """assert A2
Do we need to add assert statement in A2 to make sure it follows the precondition?""",
    """A2 isCatenated
I’m not sure I understand isCatenated. Can you do it with only one for-loop?  

Many thanks""",
    """SortToSame Array Import
If we choose to import class Arrays, should the import statement be the very first line of the program? Or should it go somewhere else?""",
    """junit being less detailed?
I'm not sure what happened, but I must have accidentally changed a setting for the Junit testing. My results used to run through each test, and give me detailed information on what errors occurred and where they occurred. Now, the test just stops on the test that does not succeed without giving information on which assert statement fails or continuing to the other tests.

I've attached a picture of the problem.""",
    """When will assignment three be released?
Same as the header""",
    """findShort
Do you suggest doing substrings manually for length 1-3 before going into a loop. And is a while loop on the right track for this method?""",
    """what about the timeSpent method?
public static double timeSpent= -1;

do we need to add something?""",
    """Junit Test neither passed nor failed?
I'm trying to write one of the methods for assignment two, but when I run the program the green or red bar that indicates whether the program fails or is running properly doesn't load all the way. It's about 3/4 the way green, but then it doesn't say whether the method I am currently writing is wrong or right. Why is it doing this? What could I have done wrong?

Thanks!""",
    """Forgot to Put Net Ids and Time Spent in A2?
My partner and I just realized that we forgot to add our net ids and time spent into our A2 file. We are trying to decide whether or not we should resubmit a file with our names/time spent on it and take the 3 point late penalty. Will we be deducted points for forgetting out NetIDs and time spent? And if so, how many?""",
    """Where can we find A3?
Where can we find A3?

Thanks :)""",
    """Got points deducted for not installing Eclipse preferences
I got 3 points off for A1 for not installing eclipse formatting, but I followed all of the instructions on the website - is there any way to verify this to get these points back?""",
    """Using getter method size() in toStringR()
Is using size() in toStringR() appropriate? I saw in the directions for A3, we are not allowed to access the field  size, however, I was unsure about use of the method. Thank you!""",
    """Can the value of a Node be null?
If so, what should its toString() in DList look like?""",
    """Test Case "stuck"
We were testing the first three todos - and the test were working perfectly (as in they tested whether stuff were right or wrong).

However, after we tested a case where we appended value null, the test cases suddenly stopped working even if we commented or removed the newest test case.  

The testing screen looks like this (it is stuck!) - and doesn't progress or move from there""",
    """Late Submissions
Hi, I forgot to include the amount of time I spent on a2. Will I lose points if I resubmit now? If so, how many points?""",
    """Forgot to accept group request and submitted A1
I forgot to accept my group member's request and submitted A1, so I have a score for the assignment but my group member does not.

Is there any way I can fix the damage I have done? Her netid is in the A1 submission.

Sorry for the inconvenience.""",
    """assignment
Im having trouble creating a for loop with a given variable. For example if we are given the number 3 and want to run the for loop three times can't we just make it so that that variable must always be greater than or equal to 0 and then subtract that variable by 1 every time... i don't know how to write this though with a variable that we are given.. I've looked online but the examples are slightly different""",
    """Answering the 4 Loopy Questions
In the third Loop Invariant video in Java Hypetext (LOOP03), we go through an example on how to answer the 4 loopy questions. The video answers the question using a symbolic method:

I would like the ask whether I can use a box/rectangle diagram like the ones we learned in recitation to answer the loopy questions in general (such as questions in prelims or while programming), or is the symbolic method preferred/more rigorous/better?  I find it much much easier to understand loops with boxes! Thank you!""",
    """Could we appen/preappend null?
In the method append or prepend, could we use null as a parameter?""",
    """Method pretend
It states that we have to add the value v. Does this mean that v is a separate node that we have to insert or am I misunderstanding this?""",
    """Test getNode()
Should we the getNode() method by comparing the Node's value?""",
    """Formatting Preference Deduction for A2?
If we get points deducted for improper formatting in A1, will we still get points deducted for A2 also? Since we submitted A2 before we realized that our formatting preference is not right?""",
    """Quiz 3
Question 2 c and d are the same option""",
    """ToStringR()
When we test toStringR(), variable last is always null despite having multiple nodes in our list. Why is it?""",
    """Quiz 3
Just checking, but is b an array?""",
    """Question about loop invariants
What is the main difference between the two codes here? Why does the latter require doing s= s+k-1 but the first one only requires s=s+k?""",
    """question 4 of quiz
I'm very confused on the effect of incrementing k first or last. In the video lecture, the sum example increments k last, but the minimum exercise increments k first. How do I determine order?""",
    """asserting delete preconditions
the precondition for method delete states that the node is in the linkedlist. However, the method specs states that the method must be in constant time. But, there is no way to check if a node is in a linkedlist using constant time. How do we test the precondition then?""",
    """Time Spent on A3
Do we know the average time spent on A3 from last semester or is there somewhere we can find it?""",
    """Override
I'm a little bit confused about slide page 7 in Lecture 7. Why the subclass may forget to override area()?""",
    """Question 3, Quiz 3
Is it possible that we are indexing through negative indices in this question? I am not sure what Java's protocol i s on negative indices, but I know they are allowed in Python. Essentially, I am wondering if there are any reasons why choice (a) (h!=0) could be an incorrect loop condition.""",
    """How do we submit answers for Quiz 3?
 How do I submit my answers?""",
    """Using .isLetter() on a String
I was doing some extra practice with Strings using a website I found. My code passes all the tests except the one in red. Does anyone know why this is? I assume it's because the code is counting '2' as a letter, but I thought isLetter() would be false on a number. Am I misunderstanding how it works?""",
    """How do you initialize a DList with nodes already in it in it?
I want to make a non-empty DList for my JUnit test, but I don't understand how to initialize the List with some nodes already in it.""",
    """prepend testing
How do I create a linked list that is not empty so I can test the function?""",
    """testing prepend
I get an error message saying that The method assertEquals(int, int) is ambiguous for the type DListTest. How can I test whether the value of the first node is equal to an integer?""",
    """Asserts
Just to be clear, there will be no penalty if none of the preconditions are enforced with assert statements?""",
    """determining if node n is in the list
I'm having problem with understanding how to determine whether node n is in the list.
Do I have to check all of the nodes to see whether the three fields match the fields of node n? Can that process be constant time?""",
    """Did quiz but forgot to submit
I finish the quiz and forgot to submit. I submit it at 12am just now and it was due at 11:59pm. Would it still be consider late?""",
    """Loop Invariant
I'm confused as to why to get an empty array for m..k-1 we would set k=m. Wouldn't that create an array of -1 values?""",
    """For prepend, how do we create a new node?""",
    """open loopProblems.docx
how do we open loopProblems.docx, everytime i open it, it opens up in text editor and the entire formatting goes wrong""",
    """Recitation ppt
Where can we find the ppt for recitations? Thank you!""",
    """Recitation 5 loop questions submission
My docx file turned out to be 127kB which is larger than the maximum allowed size of 100kB for the CMX submission, what should I do?""",
    """Quiz
When will grades be up for quiz 2 and 3.. maybe I'm looking in the wrong place?""",
    """Prepend Question: first and last
In Todo 2 we are asked to add a node to the start of the list, which theoretically means we just create a new node and assign it as the first value in the list.

However, what if the list is empty? Would the first (and only) Node in this last also be last?

Simply:

When I add a new node to an empty list, is it both the first and last value, or is last null?

Thanks!""",
    """method delete
The precondition that n is a node and that it may not be null are the same or do we have to check both in a different way?""",
    """TA OH
Are there no office hours right now? On the course website it says there are until 2:15""",
    """Package error
When I open up the skeleton file in eclipse i get an error with the package linkedlist: 

"The declared package LinkedList does not match the expected package".. is the package not suppose to be default?""",
    """sortToSame instructions clarification
The A2 handout states that points can be deducted from sortToSame "if it uses a loop or recursion or does not follow instructions."  The hint in the assignment skeleton says that sortToSame can be implemented in 5 lines using String and Arrays methods.

Does this mean I will get a 0 on sortToSame if my solution is more than 5 lines (but uses the specified methods)?""",
    """My Eclipse is not highlighting my code
Hi!

I'm starting to work on A3 but my code is not highlighting correctly. 

What should I do to fix this?

 

Thank you,""",
    """Does getNode() just return the object name of the node and not the value of the node?""",
    """method insertBefore
For the method insertBefore(E v, Node n), do we need to consider the condition that n is the first node (so the it will be working like method prepend)? Thanks!""",
    """office hours
Will there be office hours during February break?""",
    """"Takes constant time"
In assignment 3, many of the methods we write say that the method takes constant time.

This may be a basic question, but what does "takes constant time" mean in this case? Does that mean it keeps updating the size of the list?

Thanks!""",
    """a3 empty list case
What should getNode, delete, and insertBefore do if the list is empty?""",
    """Test Cases
Do we only test for the methods we write?""",
    """Prelim 1 Offerings
Can we take both 5:30 and 7:30 exams?""",
    """Testing with only strings
Is it alright if instead of testing with only integers, we only used strings in our test cases? 

Thanks!""",
    """delete and insertBefore
In assignment 3, the methods delete and insertBefore take constant time, but require "scanning through" the list to find where node n's location is in the list.

I think I know how to do this using loops, but I'm having trouble figuring out how to write this method and have it take constant time.

Could I get a hint as to where to start? Would I be able to utilize a method from the Java API for LinkedList, or am I missing something.

Thanks!""",
    """Inner Classes
Can an outer class (ex. DList) access the private fields of it's inner class (ex. Node) without using a getter?""",
    """Test Cases
Are duplicate test cases ok? We won't lose points for accidentally having several test cases that test the same thing right?""",
    """Brackets
Will we lose points if we format using brackets?""",
    """rec5
Do we have to have any formal code in question one for 3.) Does the repetend go towards termination?
it doesn't look like there is anything we can write from the picture to show that it does go towards termination?""",
    """Consulting/TA OH
Will consulting/TA Office hours be open this weekend and during break?""",
    """getNode testing
How should we  test getNode? should we compare the values of the node?""",
    """c.length
Why is it that c.length doesn't have the () parenthesis? I thought in java it should be c.length()""",
    """Accesessing the list within prepend
What is the syntax for accessing the attributes of the list we are manipulating in prepend?""",
    """Empty Linkedlist
Can a linked list be empty?""",
    """Delete
When we delete Node n, do we have to change the prev and next variable in Node n to null?""",
    """Class Node
Since Node is an public inner class of DList, why can't I declare variables of type Node in the JUnit Test?""",
    """Prepend
I know that for this method we have to create the new node of value v and add it to the front of the list, changing the size and prev and next values for the other nodes in the list. However, I can’t seem to figure out the syntax for actually adding the new node to the list.""",
    """Append
For the append method, how do we access the last non-null node? Using last.prev() results in an error because last is null. Can we use iteration even if its constant time?""",
    """quiz solutions
Will the solutions to the quizzes on cms be posted?""",
    """Vet School #Hackathon
The Vet School is holding a Hackathon!

They are looking forward to interacting with students on 5 interesting challenges in the following areas:

 

crop or livestock production
controlled environment agriculture
sustainable ag/environment – water, pesticides, greenhouse gasses
small holder farms in developing countries
consumption - food waste, food safety
Students from all disciplines and colleges are encouraged to participate and will have the opportunity to:

choose a challenge
work in highly inter-disciplinary teams
interact with corporate sponsors
win cash prizes (criteria: novelty, social impact and market readiness of team solutions)
meet new friends and colleagues
Look at the image below. If interested, sign up!""",
    """Null
If I prepend null to a list, is toString supposed to return "[null]"?""",
    """toStringR
If our linked list has three nodes with, for example, the first value 4, second null, and third 8, should toStringR return [8, ,4] or [8,4]?""",
    """Delete Node in Constant Time?
I'm having a really hard time writing a function that removes a node in constant time. If there is a LinkedList with 10 items for example, I believe there is no way to remove a node that is "located at the 5th index". I could only write a loop through the list that checks for next() starting at first or prev() starting at last and checks if this value == n that must be deleted. This would be proportional to the length of the list though, not constant time. Or am I not understanding something about running times of functions?""",
    """test
For the testing, I have only tested the string. Should I test int for each methods?

Thanks""",
    """A3 Preliminary Readings
Hi! Under the "Inner Classes" section on page 2 of the a3 handout, it says to look at the slides for the 17 Feb. lecture, but those don't exist (17 Feb was a Sunday). I'm just wondering which are the correct slides we should look at, and if the 19 Feb slides referenced in the "Generics" section were also incorrect. Thank you!""",
    """late submission on recitation
cms wont let me submit recitation late, does this mean that I get a 0?""",
    """Deleting only node
Hi!  If we wanted to delete a node that was the only node in the linked list, would we just set its value to null?  I understand what to do for all the other cases (changing prev and next or just one) but this case in particular confuses me as to what I should do.""",
    """example of prepend
i am sorry but after reading the comments, i still didn't know what prepend(E v) supposed to do.

1. what is "add value?" Is this supposed to acted like += for String and int?

2. what is "the front of list"?""",
    """Testing for constant time
Should we write a test method that check's whether our methods in DList are running at constant time?""",
    """Testing getNode()
How do you compare the pointers to the nodes?""",
    """testing assert statements
If we add assert statements to some methods, do we need to test them too?""",
    """First equals Last?
When working with doubly linked lists, if the size of the list is 1, should the field first in the header point to the only node in the list while the field last points to null, or should both fields point to the only node in the list?""",
    """Testing the time Complexity
Is there any way that we can use to test the time complexity of our methods? I think it would not be possible to know whether our method is constant time or linear or quadratic by simply looking at our test's run-time (since most of the test cases and method calls can be done within 0.01 sec and this time-elapse is not enough to find out the complexity).""",
    """Testing thrown exceptions
Page 3 of the handout says, "If a method is supposed to throw an exception in certain cases, you must test that it is thrown properly. Look at JavaHyperText entry “JUnit testing” for information on how to do this."

I was wondering if I was missing something because none of the 6 methods I wrote threw an exception.""",
    """Postcondtions
Do we need to have written pre and postconditions in the comments for all of these methods in A3?""",
    """Test prepend
Should we test the case for null and the case that the type might not be integer?""",
    """NullPointerException when testing prepend
We were testing prepend and we keep getting a NullPointerException when we try to assign the new node to first.prev. Are we doing something wrong?""",
    """Difference between "String" and 'string'
From what I can recall, one is a reference type and one is a primitive type, but I'm unsure of what exactly this means. In A3, I have to use DList<String> not DList<string>, why is this?""",
    """A3 method 5
If there is only one node in the list, and I delete this node, should the rest of the node be null or empty?""",
    """Previous pointer in prepend
When writing the prepend method, how do we change the "previous" pointer of the first node to the new first node?

I tried first.prev= first; before changing the first node to the new one, but it didn't work.""",
    """How to test getNode() to see whether or not we are checking from the right direction?
While I understand that we can test getNode() using pointers, how would we go about testing whether or not we have found the node from the right direction and therefore are satisfying the spec?""",
    """Assert precondition
What does it mean to test that n is a node of the list in the precondition? Is it enough to just say it is not null?""",
    """first field
when looking at DList.java, I see when the private field first is declared, but how does first actually get the first node of the linked list?""",
    """Testing for append
Do we need to include tests for toString and toStringR in the tests for append?""",
    """Problem returning node value in getNode
My getNode function currently returns the object name instead of the value of the node.  I was wondering how to fix this since we can't return val as val does not store a node.""",
    """No grade for A0?
I don't know why I still don't get a grade for Assignment 0--is that normal or should I do anything for this situation? Thanks!""",
    """Testing if it's constant time
Hi,

I saw in class that the professor showed whether something is constant time by using print statements. In this case, how do we test if our code is constant time? Is it testable or is it something that we just have to know from our code?""",
    """Delete
when deleting, should we also take into account the possiblity that there could be two or more identical nodes in the Dlist?""",
    """Getters vs directly calling attributes
I noticed that in both DList methods and Node methods, there are getters for retrieving attributes such as size, first, last for DList, and prev, value, next for Node. Does it matter if we use the getter methods via prev(), for example, vs directly retrieve them via prev? Is one better practice than the other?""",
    """Time of toString
The comments of toString say that toString "takes time proportional to the length of the list," but is this actually true? Since we are looping over the list, and in each pass we append an item to res (which takes res.length+1 time about), do we not end up with something proportional the square of the length of the list? Or am I missing something?""",
    """Quiz1
If a statement not in a try-block throws an object, to where is it thrown?

What was the answer to the quiz question above?""",
    """Method Delete: Determining Whether or Not Node n Is in the List?
As far as I can tell, testing the precondition that the node we want to delete is in the list will take linear time. So can we just assume that the user abides by this precondition? Do we need to worry about testing it? """,
    """Super
Given that Cornellian is a subclass of Person, which is a subclass of Object and that each class contains the method toString(), would calling super.super.toString() in Cornellian use the toString() method in Object? Or are we not allowed to call super twice?""",
    """Setting out-of-scope nodes to null
In C++ I had to set deleted nodes to null--do we have to do this in Java or is this done automatically by the Java garbage collector?""",
    """Testing for getNode
How do we compare two nodes? Should we just use value or test all fields (value, next, prev) or is there a way to compare two nodes directly?""",
    """Type of the linked list
Is it correct to think that in the linked list, the value of every node in one list doesn't have to be the same type? If so, do we need to convert the value to a certain type before adding it in the list?""",
    """Eclipse Error
i have been having Issues with eclipse, it seems as if it isn't recognizing any issues with my code or even working at all. For example if i were to input something like "gdSASHGD"  i would not receive any errors or warnings.""",
    """CS F10 #3c
Why can't the parser handle the left Clause in Clause, et Clause? I read some wikipedia on LL and Recursive Descent Parser, but do not have a full understanding yet.""",
    """assert statement in DList
For precondition in DList, do we need to write assert statement? 

If we do, for delete method, how can we check that n is a node in the list but still take a constant time?""",
    """[CS department x ACSU] Research Night
The CS department and ACSU are hosting a Research Night on Thursday, February 28 at 5:30 outside of Gates G01. Come join us to learn about the amazing research being conducted at Cornell CS and the current projects of our grad students spanning areas like programming language, machine learning, distributed systems, and complexity theory. If you are interested in undergrad research, there will be opportunities to discuss and join new projects. If you are already involved in undergrad research or are considering grad school, this is an excellent opportunity to learn more! Food will be served!""",
    """Testing pre-written methods
Should we be testing all the pre-written methods in the skeleton? (first(), last(), value() etc)""",
    """delete() and insertBefore()
Hello, I have a question about calling the nodes.

From my understanding, delete(n) works so that it deletes node n. But how do you get node n? Am I suppose to just go through all the nodes using next() and prev()? Same idea for insertBefore()?""",
    """Recitation 6
Will there be Wednesday recitation this week?""",
    """Code Coverage for Assert Statements?
In several of my methods, I used assert statements. I included statements that should throw assert errors and statements that should not in my test code. However, for some reason, when I test my code coverage, all of my assert statements show that one branch is missing. Is there something special I need to do to fully cover assert statements? I've read through the Java hypertext page on code coverage and I'm still unsure.""",
    """Asserts
This is in the A3 directions:
For example, if a method must take constant time, don’t put
in an assert statement that case the whole list to be examined.

Doesnt a for loop that checks every element in the list still take constant time?""",
    """Testing prepend
for some reason i am receiving a "NullPointerException " when I try to test the method prepend. Specifically, it occurs at the line where I try to prepend a value to a Dlist object after creating one""",
    """Office Hours 2/26
Are there still office hours this evening despite it being break?""",
    """Is there 2111 class on Wednesday?
Hi, I want to know will we have 2111 class on Wednesday? Thx""",
    """Type of Node
Does it matter what type we put inside of the diamond braces when declaring DList both in the main class and the JUnit testing class?""",
    """Recursion?
Are we allowed to use recursion on a3?""",
    """Ambiguous Assert Calls
Why do we have to suddenly specify the type of values we are comparing when using assertEquals?

We did not have to do this even when using getters in A1. Is the reason related to the value() method in the Node inner class?""",
    """Question
When I copy and paste the two methods for testing that are on the document we are given, I get errors. For test constructor  I get "syntax error, insert .class to complete argument list" and "syntax error on token, invalid character byte expected".

Did I do something wrong..? Im confused""",
    """insertBefore when n is first
For the case that n is first in the list, can we use the method prepend inside insertBefore, or are we expected to write out a method similar to prepend?""",
    """Loops
Do you need to use loop(s) in more than one method in this assignment?""",
    """Calling Node constructor in DListTest
How do I call the Node constructor in DListTest? As in, what needs to come before it in order for me to call it? I've tried just assigning new DList<String>.Node(p, v, n) to a variable of type DList<String>.Node but it is not working""",
    """Delete, first node
My partner and I are confused as to how to delete the first node in delete. We drew the diagram as suggested in the program specification and tried to change the pointers accordingly. However, the case where the first node is deleted does not work and the list still contains the first node after calling delete. Our code works for the other cases, i.e. deleting from the middle of the list or the end of the list. How should we go about fixing this?""",
    """Confused about testing
If we were to have a list, and prepend "Sampson" (the example test you gave us) and then prepend and empty string "", would tostring and to stringR return "[,Sampson] and [Sampson,]??""",
    """Linked Lists
For clarification, values in linked lists must have the same type right? Like if the first value is an int the second value must be an int?""",
    """insertBefore
For method insert before are we supposed to create a new node to store the value v or just alter the existing previous node to contain value v?""",
    """Code Coverage
Do we need to get 100% code coverage for a3? Shall we disable the assertions once in a while so that all branches of assert statements would be covered? I don't understand why there are two branches for the class title either.""",
    """A3 getNode testing null
Based on the precondition for the get node method, I am not sure how to test so that the method returns null?

Thanks""",
    """Question
Where can I find the answer to the loop invariant quiz/an explanation?""",
    """Where can I find the fields and methods of class Node?
Hi,

For Assignment3, where can I find the fields and methods of class Node? I'm doing method2. When I need to initiate a new Node, I don't know the constructor of Node.

Thanks.""",
    """NullPointerException for method delete
In the test procedure for the method delete, we added a test case for the situation where the list has only one node left.

We keep getting a NullPointerException error after deleting that one last node at the line of code 'll.delete(n);', but we are sure that n is not null

Could someone explain how to fix this?""",
    """Do we need to test methods in Node class?
There are a few methods in the Node class that are not covered by the DListTest.java, such as prev(). Do we need to test them to achieve a 100% test coverage? 

Also, do we need to test the first(), last(), firstNode(), lastNode() in DList.java? They are also not covered by the test cases. Thanks!""",
    """Should I test the time for getNode( )?
Hi,

For testing getNode( ), should I test whether the time is proportional to min(h, size-h)?

Thanks.""",
    """How can we test the time?
How can we test if the time is constant or proportional to something? Thabks""",
    """What's the difference between first.next.prev and first.next.prev()?
Hi, 

I don't know whether first.next.prev and first.next.prev() are the same. Could you please explain it?

Thanks.""",
    """assert n != null constant time
Hi, just confirming... assert n != null would take constant time correct? it seems like it would but I am not sure if there is some special rule or something.

Thanks""",
    """A4 Due Date
I know it hasn't been released yet but when would A4 be due? 

Would it be due on March 7?""",
    """Testing
For some reason my test case does not test assertion errors with assertThrows. Is there any way I can fix this?""",
    """Will points be deducted if we have not tested assert statements?
In the instruction, it says that it's our decision whether to test preconditions with assert statements and do it if we want. So, will points be deducted if we have not tested assert statements?""",
    """for the answer to A2
I want to ask if we will get the answer to the assignment?""",
    """FYI, I think something is wrong on CMS for A1
Nothing wrong with mine, just thought I'd notify instructors of this.""",
    """How to test getNode() ?
I have been thinking really hard about how to go about testing getNode() method. Can I prepend node to a new DList and use toString since we already tested prepend and toString or do I compare the values if I know exactly what is in the list while testing?""",
    """how to create new Dlist that is not empty for testing getNode?""",
    """Can we insert null as value of node?
Same as header.""",
    """Max size for uploading to cmsx?


We got this error when trying to upload to cmsx. We saw the max size of the file should be 100 kb but our files are like 3 and 9 KB. What is the problem here?""",
    """What does "C basic steps" refer to
In the beginning of lecture, what did the "C basic steps" exactly refer to when creating a new String object?""",
    """Too many test cases
I decided to test all of my methods with both a DList of Strings and a DList of Integers. Is it possible to get points off for too many test cases? (they all pass)""",
    """Testing for exceptions thrown
In the assignment guidelines, under "What to do for this assignment", there is an instruction saying we must test any exceptions we throw in our methods. 

Assuming we did not use assert statements, we do not have any exceptions thrown in our methods, so this instruction is confusing. Can someone please clarify what specifically it is referring to?""",
    """Test cases for every type
Do we need to write test cases for linked lists of different types (String, Integer, Double, etc.) or is just testing linked lists of one type sufficient?""",
    """Null Node
In append and prepend, v can be null. Size is defined as the number of nodes in the linked list. Should size only increase if v is not null in these methods because null is not a Node object?""",
    """how could I said about the assert of --n must be a node of this list;
for the delete method;  if I just write assert n != null is enough?""",
    """Difference between an object and a data structure
What is the difference between an object and a data structure? They seem very similar.""",
    """testing toStringR
if I need to test toStringR how do I create a set of linked Nodes within the test method?""",
    """public static void main(String[] arg){}
I am wondering what this is and when I should use it.""",
    """do I need to assertThrough : throw an exception if n is not in the list?""",
    """Can we use Node class getters prev() and next() in testing?
Not to test the getters themselves, but if we would like to reference b.firstNode().next() or b.lastNode().prev(), where b is a DList. Also, in general can we use the getters of inner classes in JUnit testing?""",
    """A3 testing
Do we have to test String, Int or other types or is it okay to test only one?""",
    """Question about a constant algorithm
Would an algorithm with only if statements and assignment statements be considered constant? I am asking because the amount of steps it would take would depend on if the if statement was true or not. For example, if the if statement was true, it would go through 4 lines of code to be complete, else it would only go through two. Would this still count as constant?""",
    """Loop invariants in projects
Are we required to write loop invariants/preconditions/postconditions for all loops we write in projects?""",
    """deleting last node in DList
I am testing the case in which n is the only node in the list for the method delete. Based on the class specification, it seems that an empty DList, when initialized, has first and last set to null. I tried this in the method and got a null pointer exception. I also tried making sure nothing is pointing to n, and that didn't work. I have drawn the diagrams and I'm still not sure what I'm missing.""",
    """delete method specification
Hi there, I would like to make sure I understand the specification for the delete method correctly. It says "remove the node from the list". What is a more formal definition for "a node is removed from the list?" If the node being deleted has prev or next pointing to the other node, and that node is somewhere in the DList, does that imply the node being deleted is not fully removed? I am confused. I set the next and prev of the Node being deleted to null so that it would have no relation with other Nodes ever after; However, it is not something clearly stated in the specification. As we are not supposed to implement anything that is not to fulfill the specification, I am feeling abysmally hesitated. If I should not do that, I will delete some relevant test cases as well. It is really a big move. Please help!""",
    """Asserts and Testing
If we do choose to do assert statements, do we need to test them in JUnit?""",
    """insertBefore() and delete() precondition
Why is the precondition for insertBefore and delete that n is not null? If we have a list [1, null, 2], why can't we delete or insert a node before the null node?""",
    """Testing using DList
So I know its up to us to decide whether we want to test with more than one type, but are we required to at least test DList<Integer>? We used DList<String> for all of our tests...""",
    """toStringR()
For the method toStringR, I do not understand what they mean by the extreme case to watch out for, when two empty strings are there in a linked list. Do I just test this case or do I need to handle it in the code. Thanks.""",
    """Using List class methods from Java Docs
This may be an obvious question, but are we allowed to use any of the methods from the List class on the Java Docs API? A lot of them seem relevant to the methods we're trying to write.""",
    """Forgot to Write How I felt about project
I submitted A3, but i forgot to write how I felt about the project in the comment section. Would points be deducted?""",
    """Testing
Just to be sure, do you have to test the methods that you don't write, such as first() and last()?""",
    """Forgot to put name and time stamp on A3?
Which one is worth more - handing in the assignment late or not putting your name, netid, time spent and how you thought the code was?""",
    """Loop Invariant Practice
A few lectures ago, it was mentioned that there is a website on which we can practice developing algorithms through invariants.

What is that website?

Thank you!""",
    """Error Message
No enclosing instance of type practice is accessible. Must qualify the allocation with an enclosing instance of type practice (e.g. x.new A() where x is an instance of practice).

this is the error message that eclipse notifies me. Why this error was made and is there any example that this error will be raised?""",
    """Static fields
I'm currently reviewing static fields and am a little confused as to where the static fields are stored. Say in the example in lecture 4 [slide 21], field numObs is not located in the object. Where then is this field? Is there a separate class only folder that stores the static field numObs?

Thanks!""",
    """Why is Quicksort/Mergesort Runtime O(n log n)
In last lecture mentioned the Quicksort/Mergesort runtime is O(n log n). Why is the max depth is (log n)? If want to express how many times need to partition into two, the expression should be log2 (n) with log having a base 2 not 10?""",
    """5:30 vs 7:30 exams from pervious years
I was looking at some of the past exams to study for the upcoming prelim. Are there any fundamental conceptual differences between the 5:30 and 7:30 exams from past years? Are the differences just in details rather than concepts?""",
    """recitation this week
Is there recitation this week?""",
    """Conflict Schedule
If we submitted the cms conflict form, do we go to the time slot we selected?""",
    """Where do I find practice prelims?
I've looked all over the piazza and have seen some people referring to practice prelims with solution keys, where are these located?""",
    """Fall 2017 Short Answer (b)5
The expression i < 3 is evaluated exactly 4 times during execution of this loop:

for (int i = 0; i < 3; i=i+2) i=i-1;

Could someone give me a step by step rundown of why this is true?""",
    """Fall 2017 Short Answer e
Basically it gives a bunch of class declarations that extend each other and implement interfaces. Then, the problem tries instantiating the objects.

How do you know if you get a run time versus a compile time error?""",
    """Which exam do I attend?
This seems like a silly question.  My netid begins with "RL". 

It seems like "L" as a second letter is not in either range, since one goes to K and the next starts at M and L is between K and M.  Did "L" get skipped?""",
    """Spring 2017 OO e


What exactly is happening when g1 is set as g2?""",
    """methods sheet
will there be a sheet of useful methods that we can use as a reference on the exam? (this was something that happened in 1110 and I am not sure if it was just specific to that class)""",
    """Demo in class
Where could I find the recursionDemo of lecture recursion2 on website? It seems that there is no link towards the demo after lecture pdf.""",
    """Fall 2017, 5:30 - Short Answer b part 4
"The space for a local variable that is declared in the body of the loop is allocated whenever the loop body is executed and deallocated when the body finishes" - false

Why is this statement false? I thought that once the loop is over, the local variable can no longer be referenced so the memory of the local variable is deallocated. Where is my misunderstanding?

Thanks!""",
    """Tree
What does Tree <T> do?""",
    """Fall 2017, 7:30 Short Answer 2a- Int and Char
2a asks us to evaluate the expression: (int)'a'==(char)'a' ,and write its value.
The answer is true, but I don't understand why. I thought (int)'a' produced 97, and (char)'a' produced 'a'. Is it because both are in the same memory location?""",
    """Fall 2016 7:30 Recursion


I just wanted to make sure, would it be correct if I did ((int)s.charAt(0), s.charAt(1)) to convert the character to an int?""",
    """Lecture 5 Slide 7
I'm still confused about the inside-out rule and what the path is for the three numbers to get printed. I also am not sure which numbers get printed. Thank you!""",
    """Casting classes/Abstract classes
I am kind of confused about why this expression is valid and why you would want to do it:

Shape sp= new Circle(5, 10, 2.5);

To me, this means that you are creating a Circle object that has a position and a radius, but sp "views" the object as a Shape object (from what I understand of casting classes). So, if sp "views" the object as a Shape object, why do you give it the radius 2.5 if, on the casting classes worksheet, something like sp.radius or sp.getRadius() would be "syntactically incorrect"?

Thanks!""",
    """Local variables in method calls
Since the second step of method execution is only assigning arguments to parameters, does that mean local variables show up in the frame during the third step, when the method body begins to execute?""",
    """Lecture 12: Time Complexity for Getting Data in Array
In Lecture 12, its says that the time complexity for getting a value from an array is O(1) - so constant time. Why is it that the function get in an array not have to look through the array to get that value? Does it not have to through the array one by one?""",
    """WidthAtDepth: stepwise refinement and appropriate recursive thoughts
INTRODUCTION
People who have trouble with widthAtDepth are probably thinking too much about how recursion works and

not about how we said to understand recursive functions or develop them. Secondly, too many people

are not using what we call stepwise refinement in developing these A4 methods. Were you taught stepwise

refinement in your first programming class? It's a pity if you were not. It is a fairly obvious methodology,

which was first explained in a paper by Niklaus Wirth in about 1972. Everyone sort of uses it,
but being more aware of what one is doing and using it consciously can be a big help.

 

We have three videos on stepwise refinement in the JavaHyperText —look in the top horizontal navigation bars.

We have two videos on recursion n trees. If you have not watched them, stop what you are doing and watch them!


Here, also, we try to get these ideas across to you using two examples and then discussing WidthAtDepth.
You should use the ideas expressed below in developing ALL you recursive methods.
Please read slowly and carefully.

AN EXAMPLE OF STEPWISE REFINEMENT

Suppose I ask you to write this method.

     /** Print the names of the children of t. */
     public void printChildren(BugTree t) { ... }

I do this in stepwise fashion by writing the method body like this:

     for (BugTree child : t.children) {
        Print the name of child
     }

I concentrated on getting the loop right, and to be able to focus on that, I wrote the loop body in English.
Now, I see how to implement the loop body. I end up with this:

     for (BugTree child : t.children) {
        // Print the name of child
        System.out.println(child.root.getName());
     }

I cannot emphasize too much this method of stepwise refinement, of doing one thing
at a time, writing all but what one is concentrating on in English. We may not need it
in this simple example, but in many cases, being methodical and careful like this will
lead you to a correct solution, and with much less trouble than simply hacking around.

 

A SECOND EXAMPLE OF STEPWISE REFINEMENT

Now consider writing the method below, assuming that we can't use children.size.

     /** Print the number of children of t. */
     public void printNumberOfChildren(BugTree t)

Since we can't use children.size, we have to write a loop to count the number of children.
So we write the following. Look! The loop body is in English. Get used to writing what the
loop body is supposed to do in English! Until you have more experience programming and
things go easier.

 

I did do one more step; I put in the line to print after the loop ended.

     int sum= 0;
     //invariant: sum contains the number of iterations executed so far.
     for (BugTree child : t.children) {
        // Add 1 to sum
    }
    System.out.println(sum);

Now we have to implement the loop body --put in sum= sum + 1; .

NOW ABOUT WIDTH AT DEPTH

 

Now consider writing this method.

   /** Return the width of this tree at depth d */
   public int widthAtDepth(int d)

There is a hint in the body:

       // If d > 0, the answer is: sum of widths of the children at depth d-1.

Read the line above carefully!
It gives you a recursive definition of width of the tree at depth d.
All you have to do is translate that definition into Java!
All you have to do is translate that definition into Java!

Once more, for emphasis: All you have to do is translate that definition into Java!

Now, use stepwise refinement to implement the recursive case, just as
we did in the two above examples. Write the loop body in English. Pay attention
to the similarity of this example with the second example above.

After you do that, you have to implement the loop body. Here is where recursion
come in. Do NOT think about how recursion works. That will only confuse you.
Instead: Compare what has to be done ---your English in the loop body---
with the specification of function widthAtDepth and write a recursive call.

It would be nice to get feedback in follow-up to see whether this helped.""",
    """Merge/quick sort
How will merge/quick sort be tested? Should we understand each step well and be able to come up with the algorithm by ourselves?""",
    """Question with Interface and Abstract


why only h.getClass() == Cat.class is true?""",
    """Call frame drawing
Will we be tested on drawing call stack diagrams like these? In other words, besides the horizontal drawings of loop conditions, what will we be tested on in terms of drawing diagrams?""",
    """Question
 The expression i < 5 is evaluated exactly 3 times during execution of this loop: 

for (int i= 0; i < 5; i= i + 1) i= i + 1;

 Could someone please point out why above statement is false?""",
    """[ACSU] Interview Prep tomorrow night
ACSU's first interview prep class will be held this Thursday, March 7 from 8:30-10pm. It is especially for students who have had limited programming background (CS 1110/CS 2110). Students will get the chance to practice and work with each other on a series of coding questions after a short lecture on Lists and Arrays this week.

Come through and bring your friends - snacks will be provided!

Facebook event:""",
    """S18 7:30 #3 Exception handling multiple answers?
For the exception handling portion we are asked to write the input that would produce a certain output. Are there multiple possibilities for this? The answer key for the third part of part a says b(1,"x"), but could any string that is not null work for the answer?

The same question applies to part 4 of question a. if I put b(6,"cat") as an answer, would that be correct? Since it would cause an exception to be thrown at the line 'int z = k / (k-6)' and there is nothing to catch the exception.""",
    """S18 7:30 2(b3) generic type
What is a generic type? What its difference between primitive type? I looked java hypertext but did not completely understand.""",
    """superclass constructor
What if the superclass has a constructor that takes two integer parameters (e.g. # vertices and edge length), and in the subclass you wish to have a constructor that uses the # vertices field. How does you make sure super(int v) in the subclass constructor chooses the first parameter from the superclass constructor and not the second?""",
    """Page A-9
In the review slides, there is something like Page A-9 in the 44th slide. What does this mean?""",
    """JavaHyperText Complexity
Do we have an entry for complexity in JavaHyperText? Thanks!""",
    """interfaces
A class can implement more than one interface, but can an interface be implemented by more than one class?""",
    """Contains method complexity in Binary Search Tree
Early in lecture, we finished discussing searching through binary search trees. The conclusion was that in the worst case, searching takes O(number of nodes) time. Does this mean that the contains method formallys take O(n) time for BSTs?

Basically, is "search" different from contains?""",
    """S18 7:30 2.(b)2
Why it is wrong?""",
    """F17 7:30. 2.(a)1
Why it is true?""",
    """Spring 16 7:30 Q2
For the call m("2"), why would it return an -1? The method call should encounter an Arithmetic exception because of division by 2-2, or 0. I don't see how it would end up in ArrayIndexOutofBounds? I don't think there is anything wrong with arrB[x+1], which would just be arrB[3], which is just 99?""",
    """2017 Fall, 2(f)
I'm a little confused as to how upcasting works. For example, for #4 in this problem, you create an object C (which is a subclass of C1) and then cast it as C1. When you call c.f2(), do you still have access to the methods in class C2? I though that casting it to the superclass C1 would prevent access to C2 methods.""",
    """Generic Types
I am confused on what a generic type is and its purpose. I looked in JavaHyperText and I am still lost.
I was wondering if anyone could explain this!
Thank you!""",
    """When can we apply for TA for 2019 fall?
Miss our best Professor Gries...""",
    """algorithm time
Hi, why time of  k<=n  is n+1 not n?""",
    """Interfaces
I'm still a bit confused about interfaces. Why exactly do we need them? In the hypertext video, there is an example given for a sorting algorithm. The sorting algorithm uses a compare method, and the video says that without an interface, we would have had to have written a different sorting procedure for every different class. However, if we didn't have interfaces, couldn't we just specify in the specs for the sorting method that each type that is sorted must have a compare method? Then, in our code for the sorting algorithm, couldn't we could call this compare method?

Are interfaces just a way to standardize methods that are common to multiple classes? In theory, could we technically not have interfaces, if we just made sure that all classes that need a certain method have it, and that it is named the same in all these classes? ( I hope my question makes sense...)

Finally, interfaces never include bodies for the functions they define, correct? These are defined in the classes that implement the interface, yes?""",
    """empty bags
Why is the product of an empty bag one?""",
    """Static components
To put the keyword static in a method definition means that all the objects of the class will share the function?

But if there is only one copy of it, where is it stored if not in every object created? In other words, how does any created object access this method?

Thanks""",
    """F10 2(g) GUI design? Anonymous classes??
Are we supposed to know/understand GUI design/anonymous classes for this test?""",
    """testing insert
We are trying to test insert(), but we must create a Person to do so, and in looking at Person.Java, we see that one of the parameters is a Network. Do we have to make all of these objects and variables just to create a BugTree? Thanks!""",
    """Static?
Since K2 is a subclass but not inner class of K1. Can I use private for int c rather than static?

And I read Hypertext about getClass() and instanceof but I am still lost in the difference between them...Are they the same when overridding eaqual founction?""",
    """Does the term 'nested class' refer to a static nested class or an inner class?""",
    """QuickSort with logarithmic space
I was looking at the slides for QuickSort with logarithmic space, and I don't see how the larger half of the the partition gets sorted. Would iterative code for this have to be added ? Also, does doing quick sort this way affect the time at all? """,
    """Up to what lecture will the prelim cover?""",
    """Can I use getNode in function depthOf(person p)?
The instructions says that I cannot use the function contains(p) in writing depthOf, but can is it legal to use function getNode to check if p is in the tree?""",
    """parseInt
Should we know what methods like parseInt do?""",
    """private default constructor
In prelim of 2010 fall question 4e,

A class might declare a private default constructor

A. to allow the class to be instantiated only by a static method of the same class

B. to prevent the class from being instantiated entirely
C. A and B 

what's a private default constructor and why the answer is C""",
    """Video for review session?
Just wondering if there can be a video of tomorrow’s review session uploaded?""",
    """Consultant hours
I'm in Rhodes 594, but the consultant isn't here. 

Will they be coming soon?""",
    """prelim1
Will trees be on prelim1?

Also, which lecture will the exam be up to?""",
    """Helper Function
What is a helper function?""",
    """A Frame
On the pdf file 03AFrame, I wonder what the answers are for the following questions.

Learning to infer from knowledge of execution

One learns how a statement is executed because it allows you to draw important conclusions from it. We have

not completed the algorithm for executing a method call, but only its first step. Yet, think of the following. The creation

of the frame for the call creates the parameters and local variables —if the computer is executing the call, it

allocates space for the parameters and local variables. We leave you, then, to answer the following question.

1. When during a call of procedure p is space allocated for local variable t?""",
    """2018 Spring Q2.(f) changing class invariants
Hi, for this question, can I change the class invariants of first and last instead of class Node? Say, I change Node first into something like "the previous node of this node", is that ok?""",
    """prelim1
I am aware that we can use == to compare content for primitive types. However, are we also allowed to use == to compare content with wrapper classes? Such as Integer for int.""",
    """Spring 2018 2/4 II

why do we need to use U. before calling the method? Thank you!""",
    """prelim1 2016 Spring
For question 2a(iii) on Spring 2016, What is the result of m("5"), the solution states execution results in ArrayIndexOutOfBoundsException. Would it also be counted corrected if I put -1 as the answer?""",
    """Casting
We know pet1 is cast up to class Animal, but why isn't pet2 also cast up to Animal?""",
    """prelim1 abstract class
A non abstract class that implements an interface must also implement all methods in that interface. What if it were an abstract class, does it still have to implement all methods in that interface?""",
    """2015 fall 1q
does the answer to q miss class C? Will it be correct if we know that C is the superclass of B, so we could cast B upward to C? Thank you!""",
    """'Hidden' fields and static components
Does the bottom up rule not apply when a subclass has static components and fields that are the same as its superclass?""",
    """default access modifier
I know that there are four different access modifiers but sometimes, when defining a function/ method I have seen that we did not put an access modifier at the beginning. What is the default access modifier?""",
    """2015 fall 2


I am confused about when to convert the char to in, why does c+a+b would convert char'a' to int, but not in other cases? Thank you!""",
    """2015 fall 2b


For (i), can I write s=b[k], i=k?

Thank you!""",
    """18S Q6 Loop invariant
Hi, for this invariant here, it says sizes of c[0...h] and c[t+1...n] differ by at most 1, Why is it not c[k+1,t]?

Similarly, in the while body, the solution compares h+1 and n-t, why are we not comparing h+1 and t-k instead?

Thank you.""",
    """fall 2015 2f


C c=b, does this mean b is cast to C, so it has the perspective of C, but cannot see the toString method written in B (i.e., "I'm a B"). Why does c.toString() print out "I'm a B"? Thx!""",
    """Compile-Time errors vs. Runtime errors
I'm having difficulty determining whether something will cause a runtime or compile-time error. How can I go about doing so?""",
    """S17 3e "g2 = g1"
How come g1 = g2 does not throw any error in part g), but g2 = g1 does in part h)?""",
    """Linked List
Will we be tested on LinkedLists?""",
    """Sp 17 7:30 2(a3)
Why (new Integer(2+1)). equals ((Object)(new Integer(3))) is true? How does autoboxing occur in this case?""",
    """S18b 5c Overriding Interfaces
For interfaces, I noticed that this question did not use the @Override statement when implementing the interface's methods (Circled in blue below). I have seen interfaces have been overridden before, so should we Override our interfaces? I also saw in further research that Java 6 and 7 started the @Override with Interface. I just wanted to clarify.""",
    """Sp 17 2(b)
I understand that since A is an abstract, you can't have multiple instances of it so the expression new A() is illegal. However, I don't understand why "since m() is an abstract, class B is illegal because it doesn't override m." Why is that statement true?""",
    """Spring 2018 5:30 PM Q6 Loop invariant question with is Royal() and isGuard()
In this question, we need to make sure that size of the two isGuard() is equal. When writing invariant, why we should not make c[0..h] and c[k+1...t] differ by at most 1?""",
    """S18 5:30 Q2 part (d) test cases
What is the difference between a null and an array of length 0?""",
    """Sp 2017 7:30 2(4)
Local variable in a method maintain their value inside of recursive calls to that method.

Why is this false?""",
    """2017Fall Q2d countRepeats
Hi, for this question, should we consider the case when b is an empty array or has only one element? If that's the case, b[1] wouldn't make sense.""",
    """S16 5:30
I have two questions:

1. for part l, what methods of wrapper class should we know for prelim 1?

2. For part m, why interfaces can only have static fields?""",
    """Instances
Are subclasses always an instance of super classes? Why are superclasses not an instance of subclasses?""",
    """S16 5:30 Q1
So null is not necessarily equals to null?""",
    """Upward Casts and the Bottom-Up Rule
If class C2 extends class C1 and I do the following:

C2 x = new C2( ); 

C1 y = x;

Why does y.equals start from C2 looking if ".equals: is overriden? Doesn't y have a C1 perspective?""",
    """S16 5:30 Q1 part (f)
In this case, the field spike is of type Dog, and pet contains a pointer to dog object. Why the assignment is illegal?""",
    """a try block followed by multiple catch block
When a try block follows by multiple catch blocks, if when executing a statement in one catch block again throws an exception, can this exception be caught in any catch blocks of the try block? 

For instance, given this piece of code:

why the answer to the following question is not -1?""",
    """F2015 2e 5:30
For the execution of a procedure call, wouldn't there be no return value to be left on the top of the call stack (different from a function call)? So step 4 of the method call executions would omit the part about the return value?""",
    """Sp 17 7:30 2e
Why does (1) return a run time error and why does 4 return a compile time error?""",
    """static method
Is there a situation where we want a static method to access an instance field?""",
    """S18 5:30 Q6 part (d) writing loop body


when writing the loop body, would it be the same thing to do something like swap(c, k+1, t+1); and then increment k++; and t++ after the swap? (in the if statement for example) or would this cause an out of bounds error""",
    """multiple code solutions
For the coding parts of the prelims, are there other acceptable solutions that aren't in the answer key? i.e. if I make code that works but doesn't match the answer key code, will I still receive credit?""",
    """"E"
is the "E" used in the generics examples <E> needed, or is it swappable with something like <A>?""",
    """getClass() vs instanceof
What's the difference?""",
    """Override and Overload
How can a method be overloaded and overrided at the same time? To override a method, doesn't the method have to have the exact same parameters?""",
    """SP 18 5:30 Q6D
In the answer key, it says that that the loop guard is while(t<n). Why wouldn't the loop guard be while(t<=n)? Don't we want to take the value at the nth position into account?""",
    """Java Collections/Linked Lists
I have the following two questions pertaining to Java Collections/Linked Lists.

1.) I know that if one wants to make a new array list, one could write the following code:

ArrayList<Integer> al=  new ArrayList<>();

One could then prepend and append values to this empty ArrayList. However, if I know that I want to append 10 values to my Array list, is there a way to do this without out writing a loop (for example, for a new array one could write Int[] a = new [] {1, 2, 3 } )

2.) Are linked lists part of the java collections framework? And if so, is the code that we wrote for A3 already part of the framework?""",
    """Spring 18 Q4 b
In Spring 2018's prelim question 4 b),

can we access "parent.co" directly since co is a private field and parent is another object?""",
    """Static vs Non static
To what extend do we need to understand the "static vs non static" listed in the study guide?""",
    """2017 Fall Q5b override equal
For this question, why is "Assignment as= (Assignment) asgt" necessary?

I looked at JavaHyperext and if I'm understanding it right, getClass only outputs true if the two objects have the same class in the bottom partition. So why do we need casting here?

Thanks!""",
    """Sp 17 7:30 2 (a3)
(double)(double)(int) 5.2 == 5  true
Why is it?
I think it casts from right to left. This, 5.2 is still double""",
    """Loop Invariant
I'm having a hard time understanding the solution to this question. I understand the part about initializing z to 1 being a violation of the invariant given k = m, but what does "the opposite of the loop guard contradicts the invariant" mean?""",
    """Abstract class constructor
Could an abstract class have a constructor? If so, why""",
    """Loop Help (Spring 2016 7:30)


1: How does this violate the invariant?

2: What does the answer mean by opposite of the loop guard?""",
    """White-box testing vs black-box testing
Hi,

I still feel confused about the concept of white-box testing and black-box testing. Could you please explain it? I tried to find them on the slides but I have not found it.

Thanks.""",
    """We don't need to know enumeration types, right?
It's not on the study guide, but I've found it on multiple previous prelim one's, so I want to be sure.""",
    """Object and instance
Is this h an object of object, animal, or cat? Why it has footnote "Animal" at the lower right corner of its box? I'm very confused by this. Thanks!""",
    """Lecture Videos
Are these lecture videos from Fall 2017 still reflective of the content of this course?""",
    """Variables
Why can we store an int in variable of type double but can't store a variable of type char in a String?""",
    """Diamond Problem
What does the highlighted sentence mean? Why is it a syntax error instead of compile-time-error? 

If I do not declare m() in D, then I have to declare m() in B as public. But if I want to declare m() in D instead of B, do I need to declare m() in D as public? Can I declare m() in D as private method?""",
    """fall 2017 2d


I don't understand the first example. Should it return 2? and is the method return the longest repeating number? thx""",
    """Static Methods
What is the purpose of static methods only being able to reference the static components of the class it resides in?""",
    """Constructor assert
When we complete the comstructlr, do we need to write assert statement to assert the precondition?""",
    """sp 17 2.3
Why (double) (double) (int) 5.2 == 5 true? Should it be 5.0 instead?""",
    """getClass() vs isinstanceof
What is the difference between getClass() and isinstanceof()?

Which one do we use when we want to check if object is in the same class?""",
    """Prelim Review Slides
A student reached out to me earlier today for the prelim review slides, so I thought I'd make it available to everyone in the recitation. Please let us know if you have any questions and good luck on the prelim!""",
    """substring
What would the method s.substring(-1) return for any string s? Or for the array, what would be its value at position of -1?""",
    """SP 17 3a 7:30
Why does the use of super.p() could could count the times p() called in H2? Isn't super.p() track to the p() in the super class?""",
    """Copy Array
Pretty sure the answer to this question is no, but I just wanted to double check; we don't have to know how to copy arrays, right? (Asking since you would need to do this for mergesort). And in general, apart from the methods on the study guide, we'll be given any other methods that we might need?""",
    """Does a procedure have a return value in Java?
Is a procedure the same thing as any void method?""",
    """where could I find a visual representation of how method call, while loop, for loops are executed?
The same as the summary""",
    """sp17 5.30
for the true or false question:

q2:  if no constructor is declared in a class, a default constructor is inserted? can you write sth example to help me understand? 

q3: String objects are immutable, so class String has no procedure for changing the value in a String object. but we I see in the javaHyperText, I know it is immutable, but it is also say that "the wrapper class provides functions for manipulating values of the primitive type and may also include a few constants" so it can changing value?

q4: the space for a local variable that is declared in the body of the loop is allocated whenever the loop body is executed and deallocated when the body finishes. this question, the same, can you get an example to help me understand why this is false?

Besides, I want to ask, the problem type we will have in our prilim the same with these uploaded prilim from each years?

Sincerely thanks and have a good week!""",
    """Bottom Up Rule with Fields
Does the bottom-up rule apply for fields or is it strictly for searching for which method to call?""",
    """Sp 16 7:30 1s
If class Dog extends class Animal, and variable Animal pet contains a pointer to a Dog Object, then the statement Dog spike =pet is legal.

Why is this false?""",
    """SP 17 5:30 2d
"A class can extend only one non-abstract class but any number of abstract classes."

Could someone tell me why this is false?""",
    """runtime error vs compile time error
im a little confused about the difference between the two and when one would be thrown versus the other""",
    """fall 16 7:30 4e
I am confused about how they got this answer.""",
    """SP17 5:30PM Q3(e)
Why (e) would result in a compile-time error while (f) would result in a run-time error?""",
    """static variable
Can I declare a variable as private static?""",
    """True/false
Why are C and D wrong?""",
    """Try catch problem
Why won't "six" be printed for sure?""",
    """Fall 2016 7:30 Q3(c)
Why if the type of parameter ob is changed into Grad, the method does not override?""",
    """Runtime error and runtime exception
How can we know when a program will throw runtime error and when a program will throw runtime exception?""",
    """Loop Invariant
Do we need to explain loop invariant in a javadoc comment every time we write a loop?""",
    """Review session?
Do we have recorded video or slides of the review session on Sunday?""",
    """Mean
What’s the typical mean of Prelim 1?""",
    """S18 Q3 7:30
If there is an RuntimeException in the first catch block, the second catch block won't catch it, correct?""",
    """Interface default method
Should we be familiar with this?""",
    """Override equals
When we are overriding equals method for a given class, is there a difference between using getClass() and instanceOf() to check partition at the beginning of the method body? If so, what are some examples that we should use one instead of another?

Thanks a lot!""",
    """Office Hour
I am at Rhodes 596. And is there any office hour going on? I don’t see any person here.""",
    """SP 17 5:30 5 loop


In the while body, after else, is it ok if I add another two line of similar code that checks b[k]?

Thanks!""",
    """4pm OH today delayed
Hello all, I apologize for the inconvenience but I need to push my OH back to 5 pm today (still 2 hours). Sorry!""",
    """interface cannot have a constructor since it cannot instantiated, right?""",
    """Loop guard
Here, why isn't the loop guard while (i<=k-1)? Don't we want the loop to look at the value at the k-1 position?""",
    """I am not ally understand how this execute the number in answer
and what this this(4) mean?

how could we get the answer?""",
    """field
If I don't specify a field as public or private, what will happen?""",
    """depthOf
I currently have my method set up to compute the depth of the entire tree. 

How would I change it to return -1, not the depth of the entire tree, when the method is done?""",
    """SP17 7.30pm 4b


I'm confused about the examples in the specification - shouldn't "1000" be formatted "1 00 0" and "56" as "5 6", or is "1234567" supposed to return "12 34 56 7"?""",
    """docstrings on Prelim
would we be required to write docstrings for the methods that we write on the prelim1.""",
    """Sp 15 1d
I think the default value of Boolean is false. But 1d says that the default value for a field of type Boolean is null. Why is this?""",
    """Equals
I had a general question about equals methods. Consider, for example, the code above for an equals method, which is formatted in the same way that most equals methods seem to be formatted. I understand why we need to cast ob to Roadtest (in this case) before we can compare driver variables (ob might have a variable driver defined in a subclass). But why don't we have to cast "this" to class Roadtest? Isn't it possible that "this" is not of class Roadtest? The only way this makes sense is if we assume that all the subclasses have equals methods defined, which would imply that in a call x.equals(b), x is of class Roadtest. However, I'm not sure if we can make this assumption, and if we can't, there are problems that arise with the code (I think).""",
    """Sp 15 1p
Execution of int x = 54321; byte c = x; will truncate 54321 to an 8-bit number and store it in c. What is the mistake of this statement? I don’t actually understand how this works.""",
    """throw new C()
What does throw newC() mean and should it be a subclass of Exception?""",
    """F17 2D: count repeats
Is there a typo here, or am I missing something? I thought countRepeats was supposed to count the number of occurrences of the first element in the array b, but it looks like it just wants the number of repetitions not including the occurrence at the beginning of the array. The specification didn't help me figure which one was being asked for.""",
    """SP18 5:30PM 2(a)5.


why isn't this S21?

substring(5) of "I love CS2110" should be " CS2110"

and substring(2, 5) of that should be "S21"...?

sorry if this question was asked before, I've scoured the Piazza and couldn't find a similar post. thank you in advance for your time.""",
    """S17 5B: Upwards Casting
For the problem below, how come an upwards cast is needed on argument "asgt"? Why can't we simply compare this.owner to asgt.owner once we verify that they are of the same class (same question for sol)?""",
    """S17 5D: @Override
When we implement abstract methods from interfaces, is the use of @Override necessary, or would it be acceptable if we left that out?""",
    """Array and linked list
What is the advantage of using linked list over array?""",
    """Using super() with interfaces
Hi, I was wondering if you could use super() to initialize fields in the constructor of a class that implements an interface, like you can in a class that extends an abstract class?""",
    """Fall 2017 7:30 2f (2)
In the photo shown, shouldn’t the correct answer for 2 be “execute method in C1”? Since f2 is already declared in C1 and is not abstract.""",
    """2016 sp 3c
Sorry I don't know how to make this image smaller...

In the solution, the variable name is set to be private whereas the variable magicField is set to be protected, why is so?

Besides, is it because the iced and fire wizards have different implementation of the method launchSpell that we make it abstract or is it because we don't want to instantiate the Wizard class?""",
    """Character method
On slide 4 about wrapper classes of the review slides, one of the methods listed is IntCharacter.isletter(). What is the difference between this method and Character.isLetter()?""",
    """17，5.30
why for the problem (g)  the g1=g2 is no error rather than compile-time error?""",
    """values in arrays
I'm a little confused as to why int h = 0 not h = -1 and why k = n not k = n+ 1. Can you please explain?""",
    """Increment operators
What is the difference between "k++" and "++k"? Thank you""",
    """string valueOf


I am deeply confused""",
    """I am not really figure out what this page really mean""",
    """SP15 5.30 4c


If this object is smaller than obj, shouldn't value - obj.value <0 return -1, i.e. shouldn't diff = value - obj.value rather than the other way around?""",
    """17 sp 5:30 2(d) 3
An abstract class cannot have a constructor because it cannot be instantiated

Can someone please tell me why this is false?""",
    """static vs. abstract
What is the difference between static and abstract?""",
    """Compare object to null
When we compare object to null, can we use ==? Thanks""",
    """SP16 .equals
Why is this False? Doesn't .equals compare the values of the two objects?""",
    """2015 fall 5:30PM 3(b)
Can somebody explain this question for me? Thanks!""",
    """Lectures included
Hey, I was just wondering what's the last lecture included in the prelim? Is it Sorting, Trees, Tree traversals, or Priority queues? Thanks""",
    """QuickSort and MergeSort
On the study guide, it says that we should know how to develop " quicksort and mergesort (not the algorithm to merge adjacent sorted segments)". Are these the two algorithms we should know how to develop?""",
    """Fall 17 7:30 Q5
For this question, why do we have to cast object to RoadTest if we are already checking if it belongs to the same class of this? If it doesn't go through the if statement, don't we know that ob is of type RoadTest?""",
    """fall 2017 7:30 5(a) subclass and fields


Does anyone know why we can use super() for the constructor of AnswerKey for answer? When we create instances of RoadTest and AnswerKey, would the fields answers that are in both instances but have different contents interfere with each other? Also, is it correct that if we create an instance of a subclass, a corresponding superclass would not be automatically created? Thank you!""",
    """ArrayList
Do we need to know how to implement code for ArrayList?""",
    """Spring 2015 recursion
Is it OK if I don't put a return statement on the red line?""",
    """Sp17:#3
Just a quick question on try and catch blocks. If the catch block has a superclass of the instance of the thrown exception from the try block and not the exact class, will it still enter the catch block? Is this essentially an upward cast? Thanks!""",
    """fa 14 Q1 1(t)
why this is incorrect?? Thanks!""",
    """Fall 2015 5:30 Q1
Why the following statement is true, and in general, how static/non-static method and static/non-static field interacts?""",
    """S16 5:30
Is this statement illegal because assign pet to spike is a downcast?""",
    """SP2015 Q1(h)
Why this statement is FALSE?

If you do not put an access modifier on a method declared in an interface, you can access that method only from classes in the same package""",
    """Partition algorithm for Quicksort
Referring to variable names as in the lecture slide:

Q. Why, when b[j+1]>b[j], do we swap b[j+1] and b[t], why can't we simply do j=j+1 and continue forward? (I know we would need another loop which would increase complexity, I just don't understand why we are performing this swap, as in what exactly is it doing?)""",
    """Memory Allocation
Is there a JavaHyperText reading that i can use to learn more about when space is made during method calls and creation of objects?""",
    """Fall 2015 1.e
If This is a procedure call, why does the last step say "leaving return value on the top of the stack?"
""",
    """Fall 2015 5b
Why do we need a sperate line for the case n=0; if we erase the first line, I think the function will still return false, as 0%10 != 5.""",
    """Constructor Override
Is it possible for a subclass to override the constructor of its superclass?""",
    """Where to find practice problems proving f(n) is O(g(n))?
It's one of the topics needed for the exam, but I don't where to find problems I can practice with, with solutions. Are there any provided resources I can use?""",
    """Spring 2015 Q1


I thought we could only throw an exception?""",
    """What is the difference between Instance and Class Variable?
In Java""",
    """SP 18 5:30 Q3
For question "What call on b does not print J", if k=5, will there be a RuntimeException at the second to last line? In this way, "J" won't be printed because the program terminates at the second to last line? Thanks in advance!""",
    """SP 17 7:30 3(b)
For this question, when we try to concatinate int numb to a string, why are we allowed to simply do  super.toString() + " " + numb. I thought we have to convert int to string first. Thank you!""",
    """spring 2016 3c protected vs private


In the solution for the new student class they made magicshield protected and name private but then added a getter. Could I have also just made the name field protected? Why was it made private ?""",
    """SP 2017 7:30 3(e) compiletime error


For this question, could someone please explain to me why (c)(f)(h) are compiletime error? They have different interfaces and abstaract classes, but I am confused how JAVA is able to catch this during compile time. Thanks!""",
    """Precondition
When we write recursion, do we assume that the precondition are already met? Thanks""",
    """S16 5:30
Why this statement is true?""",
    """S16 5:30 Q3 part(c)
For the instance variable of Student Class, why magicShield is declared as protected, but name is not declared as protected?""",
    """default values
What types have default values and when do they have them and what are their default values?""",
    """instanceof vs getclass
In order to get the class type of an object, which method should we use?  instanceof <Class> or getclass.()""",
    """Room and Time Assignment
Hi, can we access to the assignment of room and time of prelim 1. I want to make sure that I have enough time to take the next prelim. Thanks""",
    """F17 5(d)
Why is there an @Override in one solution but not the other?""",
    """If a class fails to compile even if it is abstract, how do we answer?
For example, for 2c in Prelim 1 SP18 5:30, Boat2 doesn't compile even if we make it abstract.
Do we put it under both "Which classes need to be abstract in order to compile?" and "Which classes will fail to compile even if they are abstract?"
Or do we only put it under "Which classes will fail to compile fail to compile even if they are abstract?"
""",
    """sp 18 7:30 Question #5a this
When completing the body of constructor in class Athlete, why does ONLY country need "this" in front of it? Why not name and athleteID?""",
    """Statistics for past exams
I am just wondering if we could check out the statistics for past exams so that I would decide if I should do more practice to reach the standard.""",
    """Compile Time Versus Runtime Error?


In the above question, why is part 4 a compile-time error rather than a run-time error? In general, is there a rule we can use to determine the difference?""",
    """complexity
will complexity ever be uploaded into JHT before the prelim?""",
    """fields of an abstract class
when i practice coding, i found that the field of an abstract class did not need to be instantiated in its subclass, why?""",
    """FL 16 7:30 1(b) loop condition


Does anyone know why we do not need k!= t+1 in the loop condition? Thanks""",
    """SP 18 5:30 3a
For the last question where it asks, "What call on b will result in a thrown exception?" could an answer along the lines of (5,"hi") work? Since at the end of the program, z would be k/0 and the arithmetic exception would never get caught.""",
    """CMS feedback
I received a grade for A3 but can't view the feedback, not sure if this an individual problem or if graders need more time.""",
    """Accessing private fields of super class
Can a class access its superclass's private fields by using the phrase super.fieldname or does it need getters for that?""",
    """complexity
in terms of complexity, is it correct that (n) is slower than (log n) but faster than (n log n)?""",
    """Fall 16 7:30 4(e)


I am really confused by this question. I am not sure why 1 is printed since field p is private and call on main happens separately from the class. I also do not understand why q in the furst print statement is 5 since we do not have variable q in the main method. 

For the second print statment, I also do not understand why c.p is 6 since c.p is assigned as 1, and we cannot access the private field. It seems that in the first print statement, q is the same as the return q, but in the second statement, q is the same as the private field or the assigned variable in main. This also confuses me. Thank you!""",
    """SP 17 2D: Local Variables
"Local variables are uninitialized." What exactly does this mean?""",
    """crossing out Integer
My eclipse crosses off the new Integer(2) statement, and is it normal??""",
    """16Sp 7:30PM 2(a)(ii)
Why is this an ArrayIndexOut of BoundsException since I though if a number divide by zero will give an ArithmeticException? Thanks""",
    """Fall 16 7:30 3(c) Override equals
@988

Sorry for making the previous thread long.  

However, I am still confused as to why we cannot cast Object to Grad and what it has to do with override. 

JavaHyperText says that

@OverrideAn annotation that is placed on a method that is supposed to override a method in a superclass or interface. It's a good idea to use it, for it tells you there is an error if the method doesn't actually override another method, perhaps because of a typo.

However, I do not see how casting here is going to create an issue. Thanks""",
    """Confusion in blinders vs. bottom up rule
Suppose we create an Animal array and store a reference to a Cat object in a[0]. If we try to execute a method that is in Cat and not in Animal or any of the classes above animal like purr we get an error. However if we try to execute a method that is in both Cat and in Animal, the version of the method in Cat will be executed. This seems inconsistent. Can someone explain this in a nice consistent way?""",
    """casting
I don't really understand this sentence in java hypertext. Can anyone explain it?""",
    """S16 5:30 q3a private int
Good Evening,

In the OO programming part of SP16 5:30, the first question asks you to write a function called launchSpell() for the class FireGateStudent. I am confused as to how, in the solutions, this function is allowed to access the private int magicShield from variable opponent. Wouldn't that not be possible as the variable is private?





*I have removed some of the code from the photo to make it more focused.""",
    """pen or pencil
Should we use pen or pencil for tomorrow's exam?""",
    """fall 17 5b


While writing equal method for solution, why we use sol as parameters but not (Assignment)sol when calling the super method? 

I thought the super method would return false if we use sol as parameter, as Assignment and Solution are not the same class.""",
    """SP18 Q1


Why is the first one false but second one true? They are all creating different objects aren't they?""",
    """sp 2016 7:30 1 (k)(p)
(k)The Java expression Integer.valueOf(1234) == Integer.valueOf(1234) can evaluate to false. is true. However, I though  Integer.valueOf(1234) will evaluate to integer1234, and eventually we will be comparing two integers. Why is this not allowed? 

(p) Suppose d and f are variables of type Object. If d is null, then d.equals(f) will evaluate to true if and only if f is null.is False

I know that if the .equals is not overriden, then it is the same as ==. In this case, we have one object is null, in order to make .equals true, shouldn't we make the other object to be null as well? Since in this case there is no longer any pointer to consider? Thanks""",
    """Recursion Example
Can you please give an example of this recursive function without a conditional expression? Thank you very much!""",
    """fa 2017 5:30 2b
The space for a local variable that is declared in the body of the loop is allocated whenever the loop body is executed and deallocated when the body finishes. 

Why is the statement false?""",
    """superclass method
If we have a subclass A that extends B, then in A to call a method that is inside B, do we need to write super.method(), or we can just write method() ?""",
    """Interface
Why do we need @override when writing a method in a class under the interface?""",
    """Interface and extends
If we know A extends B and B implements interface I1, does it necessarily mean A also implements interface I1?""",
    """sp 2017 7:30 2(e)
Why is the answer for (1) run-time error? where is the error there? Also why is (4) compile-time error?""",
    """Fall 2017 5:30
Why i<5 is not executed for 3 times?""",
    """runtime exception vs arithmetic exception
Is arithmetic exception a subclass of runtime exception?""",
    """2013 fall
By assertion statement, does it mean the assert statement or javadoc? 

I thought assert statement is also called at run-time? Why A?""",
    """Why both p1 and p2 for dnf are O(g)?
I think P2 should be faster than P1?

Since we may need two swaps for P1 and only one for P2, why they are both O(g)? Thanks!""",
    """F17 7:30 3e and similar questions


What are the general guidelines for questions like this one, when declarations will produce a compile-time error as opposed to a run-time error? Also, what would happen if in part (g), the last line was instead: g1= g2;""",
    """Lec14 Poll 1
Which of these are valid heaps?""",
    """CTRR and Override
This page said the cat partition was blind to v[0]. Yet I thought v[0] could still call toString() in Cat partition, right? Because v[0] could call toString() in Object partition and it has been overridden by toString() in Cat partition. So will this method in Cat partition be strictly bind to v[0]?""",
    """S17 3.(c) Overriding method equals
For writing equals method, when do we use getclass to compare objects and when do we write instanceof. In this particular question, can we also use getClass()?""",
    """time complexity
If we want to insert an element to a double linked list, it takes O(n) time, but if we know we want to insert an element to the, say, 11th of the double linked list( we already know which position to insert), is it O(n) or O(1)?""",
    """fall 2017 7:30 Q2 part f
As shown in the powerpoint, the subclass partition is blinded when upper cast happens. Then why in part f, C1 c = (C1) new C2; can still access methods in C2?""",
    """ArrayList
Hi, where can we find information about ArrayList? I looked at JavaHyperText for array bit there is no detailed description of ArrayList. Am I missing something?""",
    """I still do not understand why the initialization & loop guard isn't correct.""",
    """Sp 16 7:30 2 (ii) exception handeling


For this question, I know there would be an exception, but why is there a -1? I thought after thrown an exception, since nothing is caught, the exception will bubble until terminate. Thanks""",
    """Object Casting
Since the type of v[0] is Animal, shouldn't the pointer returned by new Cat(5) have been casted to Animal, allowing v[0] to only access fields and methods in class Animal or Animal's superclasses? Thank you""",
    """space complexity
What is space complexity and why does it differ from time complexity?""",
    """sp 16 4 (b) autocasting


Why do we not need to case n/10 in get into (int)? Thanks""",
    """Instanceof
I havent been able to find an example of instanceOf used on an object where it is asking if an object is an instance of a partition below it rather than above. If I were to say, if s is some Shape(), s.getClass() instanceOf Circle.class, would this return false? I expect it to be false because s which is a Shape Object does not contain a partition Circle. Is this reasoning correct?""",
    """Prelim Location
Hi,

Is the prelim location announced yet?""",
    """selection sort


the minimum of b[i] is pseudo coded (from lecture slides).  what would the actual code to find the smallest value in b? or is there a method we could use? and would this take constant time?""",
    """Instanceof & getclass
to find whether an object is in the class C, when should we use getClass and when should we use instanceof?""",
    """17 Spring 2(e) vs. 16 Fall 4(e)


I'm quite confused by these two problems. For the first image, a.x returns 3 instead of 2. Does that mean the field variable x is changed to 3? For the second image, why is the c.p in the first print statement 1 instead of 3. Shouldn't that be 3 according to the logic of the first image?""",
    """Casting down is run time exception and not compile time?
I was just wondering why when you cast something like an animal to a cat you get a run time error. I understand this is not possible as the object does not have a cat partition, but why is it not compile time. How do we differentiate between the two?""",
    """fall 2017 7:30 PM 2(b)
"If the first statement of a constructor you write is not a call on another constructor, a default constructor call is inserted."

The answer says True. But is this only true if the constructor is in a subclass of another class, or true for all constructors?""",
    """S17 5:30 Q2 short circuit evaluation
In this case, k is not given. How can we know k!= 0 is false?""",
    """fall 2016 5:30 3 C.m(1)
Why does the code stop at "5:"? Why does it not continue down to the next runtime exception catch?""",
    """difference between
What's the difference between r, npe, and re in catch block?""",
    """S18 7:30 2(c)II
For this question, class Dress3 contains " public Dress1 makeSimilarDress( ) ". Is it also an error? Because class Dress1 doesn't contain a method named makeSimilarDress.""",
    """sp17 7:30 3(e) (h)


I know that the first two assignments are valid, but I don't quite understand how to view h2=h1 in (h). Is it wrong because we're viewing h1 from the perspective of J1?""",
    """SP2017 5:30 3c. instanceof and getClass
can we use getClass here instead of instanceof?""",
    """Scope question
The space for a local variable that is declared in the body of the loop is allocated whenever the loop body is executed and deallocated when the body finishes. false

Space for a local variable declared in an if-statement is allocated only if theif-condition is true. false

Is this because all local variables within a method call have space allocated for them when the method call is executed, no matter what part of the body they're in?""",
    """Fall 2016 5:30, Q1(d)
I don't quite understand how the variables p and c.q are being updated before each println statement. Writing it out, I am getting inconsistent results.""",
    """SP16 5:30 1. why is it false?""",
    """Exam Logistics
Please take a moment now to confirm your assigned room for the first prelim:

For students taking the exam in Rock 201 Schwartz Auditorium, please use the back entrance of the auditorium. After entering Rockefeller from East Ave, do not go up the stairs; go right and follow signs to "201 Schwartz".

Momentarily, we'll be freezing the Piazza for the duration of the exam.

Best of luck!""",
    """SP16 5:30 2.a.
how do you execute it?""",
    """compile time vs. run time error
What is the difference between compile time and run time error and how can we tell the difference between them?""",
    """Dutch flag
Is the dutch flag algorithm we covered in class on any of the lecture slides posted? I've been searching through them one by one and can't find it and was wondering if it was posted or not.""",
    """Using Set methods in equals()
We cannot use the equals() method in Set for our equals() method in BugTree.

Are we allowed to use the containsAll() function in Set?

Or should we limit ourselves to for loops and if statements?""",
    """Grades
When will the prelim grades be out roughly?""",
    """Insert
For the insert method, does the specification mean that we have to create a new BugTree node for c and assign it as the children of a?

Also, when they say return BugTree whose root is the new child. So do we return the subtree of the original tree after adding the child?

I read the previous similar comment but I still don't understand""",
    """Time for Assignment 4
Hi, first I want to say thank you for including a suggested timetable in the assignment, this does help me pace my work and lets me stay on track.

My question is: How many hours, on average, do people spend on this assignment? I want to make sure I'm putting in enough time every day to do good work.

Thanks!""",
    """Contains method
It says that this "This BugTree contains p iff the root of this BugTree is p or if one of p's children contains p." In the second part, is it asking if the root of one of p's children equals p?""",
    """For contains, can we not just use the getTree method and check if it returns null?
If this isn't the case, can you explain why?""",
    """Equals
In the function equals for A4, it says two trees are equal if just their children sets are equal. Do we not have to check the rest of the tree (i.e. the children's children)?""",
    """Files into Eclipse
I can not get the files into eclipse even though they are showing up in the a4 folder on my computer but not in my Java Directory.
Can I have advice on what to do!""",
    """About the GUI
I just have a quick question about the GUI in the beginning of this assignment. When my partner and I run Bug.java like we are supposed to, as one of the first steps of doing the assignment, before doing BugTree, the assignment said something about a GUI popping up but no GUI popped up on our computer. Could that have been a mistake in installing the files or is that supposed to happen?""",
    """Insert(): adding a child to p
How do you do this without recursion? since children is private.""",
    """BufferedWriter bw= outFn.NewBufferedWriter();
when I am creating the buffered writer for customize webpage I am confused as to what goes in making a new buffered writer? also how do I create a file in my project directory? I understand all the concepts and what I would need to do for customize webpage but I don't know how to code it.""",
    """Running BugTree gui
Edit: never mind, my tree is working fine

I've finished all the methods and everything seems to pass the JUnit tests, so if I run BugTree.java, what should the GUI look like? I'm passing in arguments of 50 5 0.7 0.4 0.1 as suggested in the assignment, and the console is printing out all these names, but the GUI still just shows this. Is there a problem with what I did?""",
    """Answers to prelim1
Are we able to see the answer keys to prelim1?""",
    """Efficiency
Will we be tested for the efficiency of our code? Thank you""",
    """size()
Can we get some guidance on size()? We're recursively calling size, but our code is only able to handle one generation (i.e root and 2 kids) and not the kids of each of the kids.""",
    """TODO8 equal
In the specification it says "If this and ob are not of the same class, they are not equal, so return false". Does this mean ob should be exactly the same class as BugTree? In other words, should we use getClass() or instanceof ?

Thanks""",
    """TODO8 (2) size
The specification says that "their children sets are the same size", does this we should use the size method in TODO2 or does we just check the direct children of the root?""",
    """A4 sharedAncestorOf
Hello,

The comments on sharedAncestorOf mentions that we should not use two parallel for-each loops on the lists of the two bug paths. Can we convert the lists to arrays and then use a nested for loop?

Thank you.""",
    """A4 sharedAncestorOf
It says that no recursion is needed. However, are we allowed to do it with recursions if we prefer?""",
    """bugRouteTo examples
Aren't the examples given in the comment in the function incorrect? How is bugRouteTo(C) null? And is the root included in the list (two examples: one does include and one doesn't)?""",
    """Just failed Prelim 1 :(
I just got 3 SD's below the mean for the exam and I want to know how to improve my grade for this class. I usually study by myself but I would like to study with people to help myself get my questions answered. I did all the practice prelims and studied using Java Hypertext and the PowerPoint slides.""",
    """Question
When is the last day to submit a regrade request?""",
    """Equivalent Letter Grades
Hi, 

Can we be provided with an estimate of what letter grades correspond with our scores?

This would be really helpful since the drop deadline is the 19th and this could help some students decide wether to drop the class or not.

Thank you,""",
    """toStringBrief() compile error
when I run the test cases, insert and makeTree1 fail because there is a compile error for toStringBrief(). the error says "The method toStringBrief(BugTree) is undefined for the type BugTreeTest. what can I do so that the error goes away and the test cases run""",
    """Insert
How can you check that p is in the tree if you cannot use recursion to check through all the children or use the contains method?""",
    """Solutions of the prelim
Have the solutions of the prelim been posted anywhere?""",
    """Contains Clarification
In the tree below, should the contains method only return true if p was A, B, F, G, or H? If not, what would be the possible mix of answers?""",
    """TA name?
A couple of weeks into the semester my discussion section had a switch of TA's. Could someone tell me the name of the TA for the 203 discussion section?""",
    """A4 Precondition
"If a precondition is false, any behavior is acceptable."

Does this quotation on handout means that we do not need to assert any precondition for this assignment?""",
    """WidthAtDepth
For widthAtDepth, if the user passes in a depth value greater than the tree's maximum depth value, should we throw an illegal argument exception?""",
    """bugRouteTo cannot be resolved to a type
I want to call bugRouteTo in sharedAncestorof(), but i failed and there was a such error message.""",
    """Prelim 2 Weight?
Hello!

If we show large improvement in the second prelim and final, how heavily would prelim one be weighted?

**Asking for those who also did not do as well as they would have liked and are motivated to change their study habits**""",
    """Contains Method
Can I use the depthOf method in the contains method? The specs don't say otherwise.""",
    """recitation readings
For the recitation next week, do we just have to read down the linked webpage until it asks us to do the example?""",
    """Throwable/Error
If a statement in a try block throws a Throwable, why is it that the first catch block (Error e) does not catch it but catch (Throwable t) does? If error is a subclass of Throwable, it should inherit the necessary methods to handle a throwable, shouldn't it?""",
    """A4 files
"Cannot copy clipboard into selected elements", did anyone else get this error trying to copy files into the root directory of project a4?""",
    """A4 equals() helper method
Do we need to implement the function using the helper method mentioned in the hints? Is it ok if we don't do it like that? I didn't need to use it to check whether dt1 has any dt2 equal to it. I used 2 nested foreach loops and it works.""",
    """How to check if my java is 1.8?
In the instructions sheet, it says that we must use java 1.8. 

We are still using ecllipse, right?

and how to check the java version in ecllipse?""",
    """What exactly is a bugTree node?
It is a person or another bugTree?""",
    """depthOf
I'm having difficulty with where to begin conceptually with depthOf. It seems as if it's a combination of both the assigned videos, where in one we are looking for some person in the BugTree, and the other where we are trying to count some value (depth). Does anyone agree/disagree with this line of thought?""",
    """bugRouteTo and getParent
Are we allowed to use getParent when coding bugRouteTo? Or is it not allowed?""",
    """bugRouteTo()
Are we allowed to use contains() in bugRouteTo()?""",
    """Contains
Do we have to call contains recursively? Or can we call getTree within the function?""",
    """Do I need to create a linkedlist class for bugRouteTo?""",
    """A4 files
I copied the files into the root file of a4, but in my package explorer, there's nothing in the a4 file and src file. What should i do?""",
    """Accessing an element of children
Is there a way to access the elements of children individually? For example, how do you get the first BugTree in children?""",
    """depthOf()
Right now, my code works for any p that is in the given BugTree - I'm adding 1 upon each recursive call as the depth increases and returning the sum when p is found.

If p is not in the tree, then at the end I'm adding -1 to the sum, and therefore always returning a number greater than -1. How can I avoid that?""",
    """About return statements
For each of the TODO's, there is a "default" return statement(i.e. the return statements provided by you) in the body. Can we delete them, or do we have to use these returns in our functions? Thanks!""",
    """Null argument for getTree
What does getTree do if it used with the argument null?

The specification does not say what would happen. I am curious because I use getTree in the insert method in such a way that it might get called with argument null.""",
    """Is our solution to equals() allowed to use the Iterator method of set?
I've written a mutually recursive implementation to the method, but I could only do it using an Iterator variable in the helper function. Is this allowed? I couldn't figure out how to do it otherwise.""",
    """WidthAtDepth
I am returning an int, but this function keeps having an error saying that I am not returning an int.... I am really confused... ???""",
    """widths of the children at depth d-1
Hi, I have difficulty in understanding of "sum of widths of the children at depth d-1." in the hint of widthAtDepth(). I don't know what is "width of a child"? I know the width at a certain depth is the sum of the nodes in that depth, so in my mind, the width is a concept related to the depth. So what is the width of a child? Thanks!""",
    """Prepending to Linkedlist
The A4 FAQ for BugRouteTo thread states that there is a method which we can use to prepend an element to a list. An orthodox "prepend" method doesn't appear, however there are other methods we could use to add the element to the first index anyway. My question is: if we are implementing BugRouteTo using a linkedlist, can we instead use methods that are declared in class LinkedList rather than interface List?""",
    """children
I have tried rereading the bugtree file and all piazza questions but I am still confused about the children in a bug tree. Does the hashset children field only have children that are direct kids or will it also have grandchildren etc.""",
    """Helper Function
Are we allowed to write helper functions for the methods other than equals? I wrote a helper function for widthAtDepth, is that ok?""",
    """How to test that an Illegal Argument Exceptionalism's his thrown when using insert
We tried using assertThrows, but that hasn't been working.""",
    """getTree in depthOf
I called getTree at the beginning of my depthOf method to check if p is in the tree ( if it isnt return -1) is this invalid? I cannot think of any other way to do it.""",
    """[ACSU] March GBody
Come to ACSU's March GBody to hear undergraduate researchers share their experiences in navigating CIS' research opportunities!

Following the Research Night 2 weeks ago, this GBody can be a good opportunity to understand how to start research, and get in contact with research groups and professors --- especially since most undergrads finalize their research plans for the summer and next semester around this time. Even if you already have an upcoming project, there will be ample insight from the panelists on how to plan your time to optimize research output.

Pizza will be served! FB event""",
    """New prelim statistics
What are the new mean/median/SD given the grading change?""",
    """method bugRouteTo
In my recursive case, if a child dt returns a real list when I call dt.bugRouteTo(c), and I prepend the root to this list, how do I save this to a 'list variable' without creating a new list ? (to return the list)""",
    """bugRouteTo
Why can we not use contains in bugRouteTo?""",
    """Bug didn't disappear after I built the path for lib.jar""",
    """Just lost points on my prelim
I saw today that I've lost points on my prelim since it was graded. What's happening?""",
    """sharedAncestorOf
Can we have two for loops (non-nested) one after the other for the case when 1 array Is longer than the other?""",
    """sharedAncestorOf
Can we use contains in sharedAncestorOf?""",
    """method sharedAncestorOf
When using toArray, do we need to cast it to type Person or can we use it as an object and cast it while returning the person?""",
    """depthOf in widthAtDepth
can i call depthOf in widthAtDepth. it doesnt say i cant""",
    """bugRouteToPerson()
Just wanted to double check. If the call A.bugRouteTo(B) is made, and A is a child of B, the function should return null, correct? Thus in the GUI, if I click on a parent and then a child, I will get the path the between the two (if the bug spread from one to the other). However, if I click on a child and then a parent, I will get Null for the path?""",
    """insert function
while adding child n to p, how do  I make sure that p doesn't already have two children?""",
    """JUnit Testing
If I comment out my test cases for equals, everything works. However, when I uncomment it, my contains() stops working. I have checked the test cases thoroughly and neither of my methods calls each other or are related. How is writing test cases for equals giving me an error it contains?""",
    """Consultant Hours
I'm in Rhodes 596 but there is no consultant here?""",
    """Letter Grades for Prelim 1
Will we be able to get our approximate corresponding letter grade before the drop deadline tomorrow?""",
    """depthOf
Hi! I was wondering how to check whether or not p is in the tree in the method depthOf?""",
    """Keeping track of depth in WidthAtDepth
I've written a method for widthAtDepth that initializes the depth at 0 and then recursively finds the width at depth for the children, until the depth is reached. I tried adding 1 to the depth every time I make a recursive call, but the problem is that the depth is re-initialized to 0 every time the method calls itself. Any advice as to how to remedy this?""",
    """Are we allowed to use getTree() in bugRouteTo?""",
    """DepthOf
I am very confused about the depthOf(). Conceptually how can we check whether a Person p is in one BugTree?""",
    """A4 getRouteTo testing
We went to test our getrouteto, and it said that there was an error in the test program that List cannot be resolved to a type. How can we fix this?""",
    """depthOf
How do we write that p is not in the BugTree without using getTree?""",
    """contains in BugRouteTo
Can we use contains in BugRouteTo? I see nothing saying we can't in the handout but there is a Piazza post saying we aren't allowed to. We are having a very tough time figuring out how to do BugRouteTo without it.""",
    """installation-JUnit testing class
When I try to add the Unit testing class, there is a blue triangle next to test.java created and there isn't a newly added JUnit test case file to be deleted. How should I fix that?""",
    """deadline for submitting regrade request
When is the deadline for submitting regrade request for prelim 1?""",
    """sharedAncestorOf
After finding the correct route of the smallest tree in array form, can we use get() to get the person at the correct index of the list, if it is outside of our loop?""",
    """calling contains(c) in insert(p, c)
can i call contains() in insert() for checking whether p and c in this BugTree or not?""",
    """Equals Clarification
In method equals, is the requirement that for each tree in S1, there is some tree in S2 with the same number of children that in S1? Or with the exact same children as S1?""",
    """Regrades
When it comes to regrades, is it per question or the whole exam? Also are rough letter grade estimates out.. or not yet?""",
    """Creating a Set out of s2 in method equals?
I have written a helper function for method equals, one input of which is a set of Bug Trees, s2. I assume that this set is supposed to include all of the trees in ob. How to a create such a set?""",
    """equals methods for FancyRestaurant

Hi, just wondering about the solution for equals() method.

As super.equals() check for getClass(), ob should be an object of Restaurant.

Thus it would not be an object of FancyRestaurant?

Then we would not be able to check for the number of tables?""",
    """Do We Need to Change Test Code Given to Us?
In checking my code coverage, I noticed that the test code given to us does not fully test the constructors. Are we responsible for adding more test cases for these?""",
    """How do you search for a pinned post?
Sorry, I don't know why but I can't find the pinned post for the prelim grading estimates. I thought pinned posts were at the top of my feed but maybe, I'm just doing it wrong. 

Thanks in advance!""",
    """A5 handout?
On course website, reading/assignment section says A5 is handed out last Thursday. Where is A5 handout?""",
    """bugRouteTo
I am having trouble writing the function bugRouteTo(). It says we are not permitted to use the function getParent, but I can find no other way to access the parent of the root of the bugtree I am recursing through. In other words, once my foreach loop generates new iterations of BugTree, I can no longer access those iteration's root's parent without using getParent of the iteration's root. How can I access the parent of that BugTree's root from the class without using getParent?""",
    """Subtree Width in GUI
I've finished coding all the methods so I wanted to test it using the GUI. In the panel on the right there's a number called "Subtree width". What width is it supposed to be for, because the number I'm getting appears to sometimes not correlate with anything, so I'm assuming I have an error.""",
    """running Bug.java
I finished coding and tested with quite some different cases. However, when I was trying to run Bug.java, the GUI seems very wierd.""",
    """Posting logistics
Can i post actual code on a private post to instructors?""",
    """A5
Will A5 be posted tomorrow? Thanks!""",
    """Questions
Just for clarification, so the post before said that regrades are per question... this means I can't get points off on another question if I request a regrade right?""",
    """really confused
Okay so Im having something really weird happen:

I am testing contains... and when I un comment the commented code below.. it passes and when I leave it uncommented.. it doesn't pass.. these two test shouldn't be impacting each other.. they're different trees?""",
    """insert
should you use the method contains to assert that p is in the bugtree in the Insert method or repeat the code""",
    """sharedAncestorOf nested loops
Hello, our code for sharedAncestorOf uses nested for-loops to traverse the tree backwards. Would this be considered traversing the tree unnecessarily?""",
    """About Downloading DListTestIterable file
I copied the DListTestIterable file into the linkedlist package, but in the package explorer panel in eclipse there's not such a file. I wonder what should i do?""",
    """where to put foreach statement
Where are we supposed to put the foreach statement? Like in which method?""",
    """Condition 2 of Equals
Condition two essentially states you can't have more than one child of the same name within a tree. How do we test this if functionally we can't insert more than child of the same name? By the same logic, do we even need to account for this?""",
    """NullPointerException
My DList.java and the JUnit test class don't have any errors nut I'm getting a null pointer exception while running it, I'm not sure why..""",
    """Questions

even after reading the paragraph on this... I'm confused what toStringBrief is supposed to show... at this point I should have a root(B) with two children (C and D)""",
    """Helper method specification
If we write private helper methods, should they have specifications?""",
    """testing insert
for the test case that you guys gave us... why was dt2 created? why not just use st  and just have a statement where you add another person..""",
    """helper for equals
If we don't use a helper in the .equals function as instructed in the readout, can we still get full mark if it works?""",
    """GUI
When testing the code with the GUI, I saw that the GUI was working perfectly for one tree, wherein it updated depth and width but while testing for the second randomly generated tree, the GUI stopped updating depth and width after the fourth level.

What can possibly cause this anomaly?""",
    """why does it expect something different from what I said""",
    """Checking if children sets are equal
Is there something wrong with just using the equals method defined in Set to check if the children sets are equal. Based on the spec it seems to fit our purpose?""",
    """How does homework late submission work?
It seems that I don't have enough time to finish A4 ontime today, how does the late submission work? How do I ask for extension?""",
    """lost water bottle
I was working in office hours and I think I left my water bottle, for people who are there can someone check:)... its grey""",
    """Need to study better for CS 2110
I failed on my first CS 2110 prelim. How can I study better for the second prelim and the final? I'm learning about data structures, specifically trees, heaps, and graphs. What are some resources to help me learn these concepts and practice using these data structures?""",
    """Code Coverage for A4
For this assignment- to see if we have tested well, we only need good code coverage for the methods we write, right?

In total my code coverage is not high, but its green for all of the code I have written.""",
    """Late Penalty
How many points off if the assignment is late but is under a day late?""",
    """testing equals
So my partner and I are testing equals, and we made two bug trees that have the same root, same size, and the same exact people in order. However, it keeps returning false. Our code works with the initial given code where it tests if two bugtrees that only have one person in them are equal, where it puts out true, but doesn't put true for two new bug trees with the same exact size, class, and people in the tree. What should we be looking into to fix this?""",
    """toArray() method
How does toArray() work? When we called it on the returned value from bugRouteTo() eclipse said that it cannot convert Object[] to Person[]?""",
    """subtree size


Here, I clicked on CHI and it says the size of the subtree is 4.

But shouldn't it be 3? Then which method should I fix? 

Or is it supposed to be 4?""",
    """DepthOf()
can I use getTree function for depthOf?""",
    """Calling size() in equals()
Are we allowed to call size() in equals() in order to check if the set of the children are the same size or is that unnecessary recursion?""",
    """Recover Tree Uniquely


Can someone explain again why we can't recover the tree uniquely""",
    """Heap-order Invariant
Just to make sure I'm reading this correctly, does this say that if isMinHeap, the root will have the highest priority?

And if not isMinHeap, the root will have the lowest priority?



Is this right? Or do I not know how to read""",
    """questions
should our dlist.java go in the package we created (linked lists)... because I got an error trying to put it in""",
    """assignment 5
how do I get JUnit5 on the build path for HeapTest.java ?""",
    """Assignment 5: Estimated Time to Complete
Hi, thank you for uploading a timetable for completing this assignment, this is helpful for pacing.

I do want to ask: How long does this assignment typically take on average? The last assignment was about 6-9 hours (approximately), will this be similar in length?

Thanks!""",
    """Post GUI demo
Is it possible for GUI demo to be posted on the course website? Thanks!""",
    """Iterator method in rec8
First, since I see you are replying "why didn't you ask your TA?" on every student's question, I will address this by letting you know that one of our TAs was out sick today and students had many questions about this recitation so the remaining TA never had time to get to me.

Now, in section today our TA showed us how to automatically create an Iterator method with Eclipse. But the rec8 handout also has an Iterator method we are supposed to copy and paste.

When I delete the automatic one, Java is unhappy. If I change the name of the automatic one to DListIterator and delete the copy and pasted one, Java says 'The method DListIterator() of type DList<E> must override or implement a supertype method'

Which of these should I be using and how do I get Java to like it?""",
    """add
edit: never mind, I didn't read the instructions properly

If you're not supposed to reference b[size], then how do you search for if an element is already in the array? I'm guessing we're supposed to use binary search?""",
    """referencing b[size]
So we're not allowed to reference b[size], but we can still modify it, right? Since add is asking us to add to the array?""",
    """add
What does it mean for an object to have priority p, where p is a double?""",
    """bubbleDown
Right now, my while loop condition checks if comparing b[k] and either of its two children returns -1, but how can I make sure that b[k] does have a child before checking? 

Also, my loop exits when b[k] has no children, but how can I make sure it continues as long as it has at least one child?""",
    """griesHeapifyMax
I am trying to see whether I am understanding heaps correctly.

 

Why should h.bubbledown(0) do anything? Won't the value 0 (with priority 8) already be at the top of the heap, so it doesn't need to be moved around?""",
    """How do I get my iterator to hit the first element of the list its iterating over?
First, let me mention that my partner and I ran out of time during recitation, which is why I am trying to finish the code from recitation now and asking questions here rather asking my TA. 

Our iterator almost works, except that it misses the first element of the list, since it only ever returns the next element of the list. Any advice as to how to fix this?""",
    """No office hours on Saturday March 23, 2019
I will not have office hours on Saturday March 23, 2019 from 10 AM to 12 PM; the calendar reflects. There is usually another consultant who holds office hours during this time however.""",
    """test13ensureSpace
In bubbleUp, it tells us to test test13ensureSpace but I can't find test13ensureSpace in the test file. Is this a typo in the instructions or should see it?""",
    """priority
Does the priority correspond with the value?

For example, in a min heap, will the first element always have the lowest priority and in a max heap, will the first element always have the highest priority?""",
    """Method Swap
I'm a little confused. We only have to swap the values of b[i] and b[j] right? The priority has to remain the same?""",
    """JUnit Testing not working
We've completed 5 methods, but for some reason the only methods being tested are test00add() and test01addException() (these two cases are working). Is our testing class set up wrong or is it our code?""",
    """Want to attend the Grace Hopper Conference?
CIS, Engineering, WICC (Women in Computing at Cornell), CS, and IS are sponsoring awards for students in computing-related areas to attend the Grace Hopper Conference in Orlando, Florida, October 4-6, 2019 (Wed. through Fri.). This conference is the largest celebration of Women in Computing.

Full award covers conference registration, hotel accommodation (in a shared room), and travel up to $1500.  Submit your Application (https://cornell.qualtrics.com/jfe/form/SV_3I8ronniw2rayxv) by Wednesday, March 27th.

Applications must include your unofficial transcript and a short essay (max 2,500 characters) about your involvement with and interest in promoting women in computing. Examples include your experience with teaching computer science to girls, being a TA, and working on a project or app to empower women. Priority is given to those enrolled as undergrads at Cornell in fall 2019.

While we will coordinate the awards, the various sources of funding have slightly different rules.

For the college level awards, you need to be a CS or IS student in A&S, Engineering or CALS, or an Engineering college student with technology interest. Students with an overall GPA of at least 3.0 or an in-major GPA of at least 3.2 will be preferred.
For the WICC awards, you need not be a WICC member but you need a second essay (also a max of 2,500 characters) answering the following: How have you been a leader in improving conditions for women in technology fields at Cornell or beyond? What challenges do you see for women in computing, and how do you think attending Grace Hopper will help you enact change at Cornell?
Award recipients will be required to submit a survey after conference attendance.

Students funded from Cornell resources to attend the Grace Hopper conference in past years are not eligible.  

Recipients of the Grace Hopper awards will be announced by Thursday, April 25.""",
    """I cannot use put() to add a value with priority of type double to my hashmap
This is in the add() method. Do i need to convert double p to an integer to the value? Or am I just doing it wrong...?""",
    """recitation 8 iterator test failure trace
I wasn't able to finish in recitation unfortunately. The failure trace shows an expected value of 10, but that it got 9. However, according to the test for DListTestIterable, a value of 9 should never appear. How is this possible? It even says the list is 10..19.""",
    """Both way traversal
In recitation 6, with hasNext() aren't we only checking the traversal in one direction? Do we need to create another function to check the traversal in the forward direction?""",
    """Null
It says we can't check if there is or is not a null value in the heap. But i'm assuming for example in the assertion error for add, we can check for a null value in the Map? Thanks!""",
    """What is the expected time of map.get(v)?""",
    """peek
The specification for method peek() says that we need to throw a NoSuchElementException if the heap is empty. When I'm implementing the method body, it gives a red line when I try to throw this exception. Is this because that I need to fix the method header into: public E peek() throws NoSuchElementException?

Thanks!""",
    """questions
at this point is there absolutely no chance for a regrade for the exam.. I forgot about the deadline.. no worries if there isn't.""",
    """assignment 5
I am working on add and don't know how to check the parent of something before calling on a constructor (to know if it is min or max heap)""",
    """I need a partner who understands heaps well
I honestly do not understand how heaps work in this assignment. I see how the add method is put together from the lecture slides but it does not work here on assignment 5. This class has been moving way too fast and to be real I need someone to work with that understands what is going on with assignment 5 so that I can do better in the class and not have these assigments without taking up too much time from being able to finish assignments in my other classes. Let me know who wants to work with me so that we can finish this assignment as soon as possible.""",
    """A good hint on implementing add
What is a good hint on doing the add method? I have seen how the add method works for heaps with just the value from lecture, but I have no clue about doing it for this assignment. Can anyone give a better explanation of what the add method is essentially doing or a good hint on going about implementing the method? I have done ensureSpace but it is just the add method that does not seem clear to me.""",
    """test15insert()
Do we use test15insert()? Because the comments never say to use it, but it is in the testing file.""",
    """Null Pointer Exception
If map.get(v) returns Null Pointer Exception, what should we do? Are we supposed to check if the value is null?""",
    """Why does the worst case of poll() has time complexity O(n)?
I understand why it has expected time O(log n), but why is the worst case linear to the size of the heap?""",
    """Map has size zero.
I've been trying to get my add function to work and was using the map to check if V was already in the heap. This wasn't working, so I tried to see what the map keys were which didn't work either. When I checked the map size of the heap created in test01addexception it said the map size was zero, meaning there were no elements for me to check the value of. Am I not understanding something, or is there something wrong with the way that maps are being created in my Heap.java.""",
    """size not declared in Heap constructor
Shouldn't there be a declaration saying size=0?""",
    """bubbleDown
This is in the bubble down specification: If there is a choice to bubble down to both the left and right children (because their priorities are equal), choose the right child

Does it have to be that their priorities are equal in order to be able to bubble down to either side? Or just that they have the same compareTo value of -1?""",
    """Problem with testcases
When I uncommented new test and tried to run the test cases, only the first test 01add is run.



Is there anything wrong with my test cases? Or am I using it wrong?""",
    """JUnit Testing Error
I imported a JUnit onto the build path and successfully ran a few test cases, but partway through testing (after uncommenting and recommenting some @Test, I started getting this error:



The source code is showing no error. What should I do to fix this?""",
    """poll test


In this test to check values, wouldn't the HeapValues in mh be out of order compared to the values in c? (because bubbledown changes the order of values in the array) And if that is true, then why are stringB and stringC equal?""",
    """Do we need to use bubbleUp in method add?
Can I use bubbleDown instead? If I use bubbleUp, I have to insert the new element into the first entry of the array, and slide all the other entries over. That seems like a pain. Can't I just insert the new element into the "last" element of the array and bubble it down?""",
    """Data Structure
Why is the time complexity of add in linked list O(1), whereas in an array it is O(n)?

Also, why is get in Array O(1) but get in LinkedList O(n)?""",
    """JUnit not running all tests?
Hi!  After un-commenting some of the bubble down JUnit tests it says that only 7/17 tests are running.  They all pass, however, they do not all run.  I'm not sure what the blue arrow next to the test case indicates.""",
    """Handing in A5
If you hand in a5 during spring break, will it count as only 1 day late, or multiple days late? Also how many points are deducted per day late? Please do not roast me, I am stressed.""",
    """NullPointer
I'm working on implementing add. When I use map.get(v) to determine if v is already in the heap, I'm getting a null pointer exception. Any idea what's wrong?""",
    """bubbleDown
For bubble down, if the heap is a min heap, do we switch the root with the child that has the smaller priority? And so for !min heap, do we switch the root with the child that has the higher priority?""",
    """Spring Break
Will there be office hours over break?""",
    """copyOf method of Arrays
I found this method copyOf in API for Arrays, but what are we supposed to put in the third slot of the parameters? It's a little bit confusing in syntax.""",
    """bubbleUp iteration
When the comment in bubbleUp says to do iteration, not recursion, does this mean we can use a while loop?""",
    """What to consider when bubbling up?
For example, for a minHeap, Should we bubble up if the parent node's value is smaller or the parent node's priority is smaller? I'm kind of confused about that part. thanks!""",
    """Lec18 Poll 1
In what order would a DFS visit the vertices of this graph? Break ties by visiting the lower-numbered vertex first.""",
    """Lec18 Poll 2
In what order would a BFS visit the vertices of this graph? Break ties by visiting the lower-numbered vertex first.""",
    """Midterm course evaluation
The Engineering College is running a midterm course evaluation for CS 2110 through the evening of Sunday, March 31. You should have received an email from Kathy Dimiduk about this inviting you to a Qualtrics survey.  We would really appreciate your feedback on the course!  We want to continue improving it every semester.

Your responses will be anonymized, but we will get a list of who completed the evaluations.  So, to incentivize as many people as possible to give us feedback, we will make completion of the midterm course evaluation worth around 0.5 to 1% of your final grade.  Want an easy grade bump?  Fill out the evaluation!  The deadline is hard, so make sure to do this before leaving for Spring Break.

More than 100 of you have replied already---thanks!""",
    """Test cases for peep()
Why does the test case for minPeek create a max-heap, and maxPeek creates a min-heap? My method fails these test cases because it returns the expected value for maxPeek when test case minPeek is running...""",
    """BubbleUp and BubbleDown
When we write bubbleUp and bubbleDown, do we also need to make sure the invariant for the map is maintained? We found test cases checking the map for bubbleDown but we didn't see it for bubbleUp.""",
    """Finding value at an index
Since we aren't allowed to reference b[k], how do you find the value at a certain index?""",
    """bubbleDown and break
Can I use the break statement in bubbleDown? 

Or would you recommend that I don't use it?""",
    """using bubbleDown() in poll()
Since we are removing an element, the invariant for the heap would no longer be true (the last element would have only one child). Since bubbleDown() has the precondition that the invariant for the heap is true, can we use bubbleDown() in poll()?""",
    """Method swap
I don’t understand what I need to change in the map to keep the invariant true. Any hint?""",
    """Reducing length of map
How do we do this?""",
    """Helper function for BubbleDown
Am I allowed to write a helper function that checks if a node has either no children, a left child, or both left and right children? I know it's not necessary, but the logic for my method without it is getting pretty confusing (~20 lines of nested if's and try/catches) If not, are there any hints that might help to simplify this?""",
    """Lambda function input


Here in the anonymous function, how can java know the input s is an element in the list strs? It was just a random letter...""",
    """poll
I saw the previous thread on poll addressing removing the node from b and how you don't have to. The test script is failing at line 29 where the poll test calls check and sees that the length of b doesn't equal the size of map. How do we pass that assertion error without removing the element from b?""",
    """Regrade
When will A3 regrades be processed? Thanks.""",
    """Are we not allowed to use b[k] in the assignment?
I saw on the a5 instruction that we should never reference elements b[size..]. I'm just confused if it means that we can never use b[k]. And how can we implement swap if we can't access b[k]?""",
    """changePriority
In changePriority, do we need to call bubbleUp or down based on the priority change to rearrange the heap or do we ONLY need to change the double priority value without bubbling?""",
    """testcases not running
I finished bubbleup function and was trying to test it, but the test case seems not to be running.""",
    """swap
I am confused about how we can change the map to keep the invariant true. And how can we get access to the key in the map?""",
    """question
I keep getting a null pointer exception for every single test I run... did i miss something/ actually change something that you can think of?

Sorry I know this is vague and not that helpful I just don't know what I did.""",
    """swap
For the method swap, we are not sure how to update the map. 

We were thinking using replace(K key, V value) to change the values in the map, but i and j are integers, not types K and V.

Is this the right method to use? Or do we have to cast?""",
    """out of bounds error in add
I get an array index out of bounds error when trying to add the value that I want to add to b[size-1], I am confused why I cannot do this.""",
    """Explanation of Expected Heap from test31
Can somebody explain the expected output, shouldn't 1 be the root of this tree to keep the invariant true?""",
    """ensurespace
The whole idea behind ensure space is that we want to allocate space in the array, to make sure that we have room to add things right?

with ensure space, there is a note in the body saying that we should look at Arrays.copyOf in the java api documentation... this copies the array, and the copy has more space right? Just to be clear we don't want a copy though? don't we want the original array?""",
    """size
I am having trouble figuring out where size is actually set to a value""",
    """poll
I am having trouble with this function. For some reason I follow the instructions from the lecture slides yet still the size remains unchanged. Any idea about what might be wrong?""",
    """Bubble Down Problem
I wrote bubbleDown in a way that I think is correct and which passes all of the bubbleDown tests. However, I'm getting errors for methods that use bubbleDown, including poll() and changePriorty(), and it looks to be an issue with the bubbleDown procedure. Is it possible that my BubbleDown function is wrong even though it passed all tests starting with test30 and test31?""",
    """Using get in add
So according to spec add should be logarithmic. Can I still use the get method for hashmaps to see if a certain value is already in the heap as on average its time is constant. Or am I not allowed to do this as in the worst case the time of this can be linear.""",
    """assigning an element at b[size]
Assignment instructions say don't reference b[size] by checking for null elements. Can I use a statement like b[size] = new element and then increment size in the add method or will this result in a big deduction for me""",
    """confused about priorities
I am getting confused on bubble up... just for clarification we want to compare b[k] with its parent and that parents' parent etc... right?""",
    """Poll
For the Poll method
would it be reasonable for us to set (b[size]=null;) ? Because we should be deleting the object from the array.""",
    """"A6
When will A6 be released? Can't wait to play around with GUI :)""",
    """ensureSpace: size 0 case?
If we have a heap of size zero and we want to call ensureSpace(), what should ensureSpace do? Doubling the length of b, as the specification states, still returns an array of size 0. Should I instead increase the length of b to 1?""",
    """GUI Demos
I'm trying to run the GUI demos in eclipse, but it doesn't run giving me an error "editor does not contain a main type."
""",
    """enurespace nullpointer
if value v is in b[k], then map.get(v) returns k but when I try to find the error in my code by tracing and I type
System.out.println(map.get(v)); I get null. When I run test01addException, I get a null pointer exception even though v is already in the heap?""",
    """Copying Array Time Complexity
Would copying an entire array and set it to a variable be linear time O(n) because it goes through every element and copies it or would that be constant time?""",
    """isMinHeap in bubble down
Can we us the boolean variable isMinHeap in bubbledown?""",
    """Finding element v for changePriority
I'm having trouble thinking about how to find the location of element v in the heap while maintaining the time constraint. I believe this is necessary so that you can utilize the bubble functions written earlier. Is traversing the tree the only way?""",
    """Size
What is the difference between mh.size and mh.map.size() ? 

In test12 swap, what can be the reason mh.size stays as 4 but mh.map.size() changes to 5?""",
    """Assert Statement
Should we write an assert statement for bubbledown?""",
    """Poll function
In the poll function, how do we work with map? Considering most of the mappings will change, so how do we change the mappings in map?""",
    """Bubble Up
I'm not exactly sure when I should switch my k and my parent...""",
    """Extra OH Today
I will be over at Rhodes from 11am to 1pm, as well as 3.30pm to 6.30pm today. I will stay longer if I see that there are still people that need help with their assignments at 6.30pm (I will notify on Piazza accordingly), so just come over if you need any help. Otherwise, have a good Spring break!""",
    """About Method Poll
In this method it asks to remove a certain value from the heap, but how is that possible. I thought arrays were immutable and can't have values removed from them?""",
    """Map and size invariants
How do we make sure that our map and size invariants are kept?""",
    """A5- Heaps Testing
If this passes all the given tests, is that good to submit?

Older assignments needed extra tests so I was wondering if we are supposed to do more tests before submitting?""",
    """Testing Off
My testing isn't working. I've continued coding, and my last two functions do not test. When I press a specific test case, it pops up, "No tests found with test runner 'JUnit 5'"

I wish I could come for help, but I've already left Ithaca.""",
    """OH still ongoing
I am still at office hours because there are still quite a few people here asking for help, so if you need any help I will probably still be around for the next hour or so!""",
    """changePriority min-heap vs max-heap
In changePriority, does it make sense to check whether it is a min or max heap before bubbling up or bubbling down, or is there a simpler way to do this?""",
    """map.put
When updating the map, I am getting the error that the key is type E, which can be anything.... including an int, which is what I have put in. I'm just confused as to what I should be putting in instead...""",
    """should we have comments in our code?
will we be graded on comments in our code?""",
    """remove in poll
If remove is linear are we allowed to use it in poll()? Or how else do we remove the last node?""",
    """remove in poll
I tried using remove to only remove the last value at the last position, but it doesn't seem to be working. But if I don't specify the position it seems that it is removing the last value at both b[0] and the last position. I also tried hard coding specific position to see the results of specific test cases but it doesn't seem to be working either. Am using remove in the wrong way?""",
    """A4 Grades: Are grades truncated?
Looking at my grade on A4, I noticed that my points as described in the comments summed to about .6 points higher than the grade I was awarded. Are grades rounded down to the closest integer? Or is this an error for which I could request a regrade?""",
    """JumpStart: Want a summer internship or a full-time job?
Still looking for a summer internship or a full-time job?
Wondering what it's like to work at your dream company?
Sign up and be a part of Jumpstart, where you can RSVP to webinars to
learn more about securing that coveted internship and connect with other
CIS students through a forum!""",
    """Shortest Path Videos
Can someone explain to me why this is true on the third video? It does not seem obvious to me.
Thanks,""",
    """Shortest Path Tutorial
May I know what exactly we should be reviewing on the shortest path algorithm? Are we supposed to review the entire entry in JavaHyperText? Or just part 1?""",
    """Quiz question 2: meaning
What is question 2 of the quiz asking for when it says what the theorem tells us about the given frontier set? I've watched all the videos and understand the algorithm but don't know how to respond to this.""",
    """Far-off set
What exactly is the far-off set, and how is it different from the frontier set?""",
    """Cannot Submit Quiz
On my computer, it says that the server on CMS is currently under maintenance and as a result, I cannot submit the quiz. Is this just an issue with my computer or...?""",
    """Can't get onto CMS
I'm trying to submit my online quiz but the server is getting flooded and I'm not able to submit. What should I do?""",
    """ACSU GBody: Pre-enroll
Time: Monday, April 15th, 5:30-6:30pm
Location: Gates G01


Have questions about pre-enroll? Not sure about what classes to take next semester? Unsure about CS or considering other majors/minors? Come to ACSU’s April G-body to hear experienced students’ perspectives on these questions. Upperclassmen and TAs, come share your insights and help others. Dinner will be served!""",
    """How much do quizzes affect our grade?
If we missed 2 quizzes, how much should we expect our overall grade to go down?""",
    """getNeighbors
In the assignment, the function getNeighbors is protected. Can we change it to public to be used in Paths? Thanks!""",
    """A6 - Estimated Length
Hi, I know that there is no suggested timetable for completing this assignment, but I want to ask:

How long should we plan to spend on this assignment, or how long do people usually take to complete this assignment?

A6 seems like it could be a shorter assignment, or a deceptively long assignment and I want to put in an appropriate amount of time and work.""",
    """Do we have to initialize HashMap info?
The Heap constructor in Heap.Java creates a hashmap, so would we just work with the variable map instead from a5? or do we make a new HashMap<Node, DB> info?""",
    """prelim 2 study guide
When will that be released?""",
    """initializing F
The abstract code says to create F with just v inside it, which I understand since Heap has an add method. But the priority is the distance, right? How do I add v with priority if it's the only node in the heap so far and doesn't have a distance?""",
    """Node f
To find the node in F with the minimum priority, would I have to make the Heap class implement comparator, then do something like Collections.min?""",
    """Generate Graph from Text File
Is there a way to see what map one of the given text files in the maps folder will produce in the GUI to help with debugging?""",
    """Finding the back pointer of f
I am struggling with finding the back pointer of f when I remove it from F and add it in S. I wonder how exactly I can keep track of this.""",
    """Test Cases
Has anyone finished the assignment yet and had trouble passing all the test cases? For some reason, a handful of city pairs are found to have an incorrect shortest path length. I'm sure there is a small issue with my code but thought it was worth asking!""",
    """prelim 2 heapsort
On the study guide, it says we should be able to develop algorithms based on their specs. For heap sort, would that mean knowing how to develop bubble up and bubble down?""",
    """What shortest() returns
I must be missing some important point about what exactly shortest() returns. 

The return type and return stub indicate it should return a List<Node> (implemented as a LinkedList). 

If I read correctly, we are only supposed to implement the data structures F (as a min-heap) and the HashMap.  Neither of these implements List, so where does the list come from?""",
    """Returning the priority value from the heap?
Using the heap, is it possible to return the priority value of a specific value in the heap to get the distance?

Or is getting the distance only possible using the pathsum function?""",
    """Return statement = break statement?
I apologize if this has already been stated in the handout, but I just want to be clear.

The handout states that a break statement is not allowed. However, we do want to exit the loop if the shortest path from v to end has been computed. One obvious way is to add a return statement to return the desired path inside the loop, which causes the loop to terminate early. Does this constitute as a break statement?""",
    """possibly chose wrong file
I was just wondering, is it possible that a grader may not have chosen the newest submission to grade. I just noticed comments that I believe don't apply to my best submission, but they apply to older submissions. I just wanted to ask here before unnecessarily submitting a regrade request.""",
    """Hashmap
I'm very confused about what the hashmap is. I originally thought it represented the settled set S with all the nodes inside. However, I believe the hash map is supposed to contain all nodes in the settled set S and frontier set F. If this is true, then how are S and F distinguished?""",
    """Difficulty downloading a6
I followed the instructions on the a6 page--I downloading the zip file, unzipped it, and dragged the a6 src folder over the src folder in my new Java project. However, I was not asked whether or not I wanted to override the src. As a result (I think), I got errors in all of the files. How can I fix this?""",
    """generics question
Hi,

I'm wondering why the first return statement works, but the second one doesn't.""",
    """HashMap
How do we get the HashMap<Node,DB> with the values for each node of the graph? I understand that we initialize it to be empty but then how do we know the distances and backpointers of each node?""",
    """trees
Should we be familiar with the Java implementation of trees for the prelim? As in the end of this pdf? Or just understand the concept of what it is and its properties?""",
    """4th annual Ivy League Mental Health Conference
Are you interested in advocating for mental health?

Do you want to improve mental health on campus?

Apply to be a delegate to represent Cornell at the Ivy League Mental Health Conference or

host delegates from other Ivy League Universities!

The Conference will take place in Goldwin Smith from 26..28 April.""",
    """Testing not working
I'm trying to test my methods, but every time I press the green arrow to run PathsTester, the gui pops up, and none of the tests run: 



I also checked the configurations, and it says "all methods" in the dialogue box.""",
    """Adding node to S
After we remove f from F, we try to add it to S, but we don't know how to find the distance to create a new DB. How to find the distance?""",
    """HashMap
What should we name our HashMap? Is naming it "map" ok or is there a better name we can give it?""",
    """method main not working
when i try to run the main method in graph.main i keep getting the error: "editor does not contain a main type" i'm not sure what this means

also after dragging src to my project this is what my package explorer looks like, which is slightly different from the image in the a6 pdf, I was never asked whether the directory src should be overwritten or not, not sure what to do""",
    """understanding the relationship between DB and node
i want to really understand what's going on before I code so I am just looking at all of the files right now. In the class DB it says that DB contains information about a Node. When would a DB object get this information and are we creating DB objects? i'm a little confused on this part.""",
    """Finding back-pointer
I know the hashmap stores the distance and backpointer of each node in S and F but how can we actually access this info from the hashmap?""",
    """Class DB in the abstract algorithim
In the lecture slides, class DB is implemented to maintain info about each node's d-value and its backpointer. Why can't we just add fields to the nodes that maintain this information? 

Also, DB is presumably a sub-class of class Node, yes?""",
    """Prefix/Postfix Notation
The prefix and post-fix notation is a part of lecture 13 which goes over Trees. As such, I am wondering if prefix and post fix notation is a part of the Tree topic or is it a short introduction unrelated to Tree (and hence won't be on the exam)?

Thank you!""",
    """Accessing f's d-value?
When I'm in the first if-statement, I want to access the d-value of node f. How do I do that? Simply f.distance doesn't work, and I'm not sure how given the methods we're allowed to use.""",
    """Returning the List?
I finished transcribing the abstract code. Now I want to use my HashMap to return the shortest path. I tried simply calling method path, but I got stuck in an infinite loop. Is this not the way to do it?""",
    """files in a6
we were given a lot of files for a6, which ones would be the ones we should know well/ understand in order to write efficient code?""",
    """Can we put in a map(Node, DB) to keep track of the bkptr of each node?
As the title said""",
    """distance between two nodes
how would i find the distance between a node and its neighbor?""",
    """what should set S be?
I'm just very puzzle should set S be an arraylist or min-heap, and how do we determine what to use?""",
    """ScoreCoeff
I have been trying to write my own test case for this assignment, but I am having trouble building my own map and putting it in JSON form. What exactly is ScoreCoeff? It is included as an array in the test board JSON txt files, but when I print a JSON from the GUI I don't get any information on that for my map. Whenever I run my test case I get an error telling me that my JSON is missing a value. Specifically, I want to test the case where the end node has no edges leading to it.""",
    """Hash Map
Can someone explain why the hash map lookup time is expected to be O(1), but is, in the worst case, O(n)? I don't really understand the worst case.""",
    """Test Cases 70 and 80
When we implemented the algorithm and calculated our paths, our path length was not the same as in the assert statement (expected 76 but was 90 for 70 and expected 112 and was 125), but when we checked the graphs themselves and calculated path lengths by hand, we couldn't get find the shorter method. Is there something wrong with the way we are calculating the shortest path here?""",
    """Polling Nodes with Same Priorities
If the heap has multiple nodes with the same lowest priority, which of the nodes gets polled? 

For example, in the worst case scenario in the following diagram, the polling chooses a path that's not the shortest. In the worst case, it choose Node b instead of Node d. From then on, it chooses Node f and then Node end. This is not the shortest path. How can we know which nodes get polled after Node a and if it's possible to choose.""",
    """a5 solution
I received a 99/100 on a5 so I'm assuming I need to use the instructor solution for a6. Where can I find it?""",
    """How to know if shortest path from v to end has been determined
And what is the appropriate test? I am confused about this portion.""",
    """class DB error.
I am getting an error that says "The constructor int node is not visible".

Am I supposed to make the DB class public?""",
    """All the tests except 70 and 80 work
Why could this be? I am confused about how to proceed.""",
    """Keeping the invariant with Hashmap
So we are using one hashmap to store the backpointers and distance of the nodes in both S and F, but for the invariant to be true, shouldn't nodes in S and F be stored separately? Or did I understand the usage of hashmap wrong?""",
    """tree traversing
In the pdf given in JavaHyperText, it seems the codes for inorder and postorder are the same. How can they be the same? Shouldn't we process left, right and then root in postorder, which means we need to exchange the order of the last two line in postorder?""",
    """Will Balanced BSTs be on the exam?
They were briefly mentioned in lecture 12 towards the ends, but they aren't explicitly stated on the study guide so I am unsure if they are assumed to be part of the tested material.""",
    """Can I find the path inversely?
Since the output is a forward path, can I find the path inversely to simplify the code?

That is, use the endpoint as the beginning.

Will points be deducted?""",
    """Determining if F contains w
I'm having trouble determining whether a heap contains a certain node. I know I can check it see if certain methods throw exceptions, but is there an easier way?""",
    """Should we add "import graphs" to the java file we are submitting, or no?""",
    """adding f to S
To add f to S I understand that it entails adding the node and DB object to info. When creating the corresponding DB object I'm confused as to how I'm supposed to know the distance to input and the backpointer. Any pointers?""",
    """graph coloring
Do we need to know that for the exam?""",
    """How cumulative will prelim 2 be?
I see that the entire Prelim 1 study guide is listed as a topic to study for Prelim 2. Is this more of an observation that Prelim 2 material builds off of Java concepts covered in Prelim 1, or should we expect actual problems on these original concepts similar to those found on Prelim 1?""",
    """questions
We're not supposed to touch class DB right? I have an illegal modifier error? I don't know what I did?""",
    """iterative depth first search
Fall 2017 true false says iterative depth first search does not maintain a stack but a set of visited nodes. The lecture says it's a stack. Which one is correct?""",
    """time complexity of an algorithm


Why is the complexity O(n^2)? I understand the outside loop is n, but why is adding also n?""",
    """Prelim 2 - Relative Difficulty
Hi,

This is a little bit of a weird question but, I want to know how difficult prelim 2 is in comparison to prelim 1.

The mean for Prelim 1 was either a 70 or 76 (depending on which test), are the grades for Prelim 2 typically higher, lower, or about the same?

My apologies if this has been asked before or answered somewhere else.""",
    """BST Insert


In this example, why is September not a child of June? Why is it a child of May? In BST insert, don't we add children from the left?""",
    """planar and nonplanar graphs
I get the definitions, but technically, for nonplanar graphs, can't you always just draw an edge around to avoid all intersections? So how do you determine if something is actually nonplanar or how many edges you need to add to make something nonplanar?""",
    """Expected and Worst Case for Operations: Hashing
on the review sheet I was wondering what are the expected/worst case operations for hashing?
Thanks""",
    """What is a seed?
Does seed just mean the node?""",
    """Did anyone forget car keys in recitation?
Someone left their car keys behind in recitation PHIL 307. I will be here for the next hour. 

Email me if they are yours (om72) and I will make sure to get them back to you.""",
    """Expected time and Worst case time?
What does expected time actually mean? Should it be the optimal time, or teh average time? for example for teh hashing, the expected time is always O(1), but I'm not sure how we can get this conclusion and what does this conclusion is actually saying. Also for the worst case time, how can we know the actual time for the worst case? Do we have methods to calculate, or should we just "think"? Sorry for the so many questions, and thanks for all your help!""",
    """Unable to run the test file as a test.
When I click Run-As in the test file, there are no options, despite my following the steps at the beginning to add the JUnit to path. Am I doing something wrong?""",
    """heap sort algorithm


In this implementation of heap sort, shouldn't it be bubbleDown(c, 0), not bubbleDown(c, j)?

I thought heap sort swapped the root and last node, then bubbled the root down""",
    """Fall 2016 DFS Question


Why does C visit F before it visits G? Shouldn't it visit G first since the weight is less than that of F?""",
    """far off set
If w is not in S or F and you can't check F then w must be in the far off set. How do we check if w is in the FO set or are we approaching it wrong?""",
    """constant time search for load factor
Why is average search time considered constant if the number of probes on average is less than 2? Also why does it follow that linear search time is 2 probes on average?""",
    """Fall 2017 7:30 2a
Why is this false?""",
    """removing f from F
How do I remove an element of a heap?""",
    """time complexity
Why the adjacency list representation requires O(n+e) space? Why are we using multiplication here?""",
    """Fall 2017 7:30 4c


Where are the h and k coming from in the return statement?""",
    """Error in the DB inner class
Why eclipse underlines my DB inner class in red and saying "Illegal modifier for the local class DB; only abstract or final is permitted"
""",
    """Creating new data structures
The handout clearly states we just have to make 1 new data structure (the hashmap for S and F). But, if the parameters don't make the function execute the loop, we will have to return an empty LinkedList! Is it fine if we are doing that or does that count as making a new data structure (since we have not stored it in a variable and are just doing return new LinkedList..?)""",
    """actual pathSum value is always 0
I'm failing all the Map test cases as all of my actual pathSum values are equal to 0 and not the expected. I was wondering if I could get some help on this. Thanks!""",
    """Finding d[f]
I'm confused on how to find d[f]. I understand that it is the priority of the root of the min Heap, but I'm not sure how to access this value.""",
    """Consultant
I am interested in applying to be a CS 1110 consultant for pay and was wondering if anyone knew approximately what the weekly time commitment is like. Thanks""",
    """4/17/19 12:20-2:20 Office Hours Changed
Hi I’m shortening my 12:20-2:20 office hours to 1:20-2:20. I fell and might have slightly hurt my leg on my way out, so I won’t make 12:20. I want to make sure it’s alright so I’m going to get there at 1:20 instead. I’ll make up the time sometime tomorrow. Sorry for the short notice.""",
    """Repeat of sorting/ recursion on prelim2
Since we already had problems on sorting and recursive functions on prelim1 and these topics are reiterated on the prelim 2 study guide, should we expect problems of a similar format (i.e. actually writing a sorting function) on prelim2?""",
    """heap memory
What is a heap memory?""",
    """Spring 2015 exam 1 True and False
This is kind of silly, but I don't really understand what 1.(s) is testing me on: fields have initial values, but local variables do not.

Can I ask for some explanations on this please? Thanks.""",
    """A java window pops up every time when I run the test file
Is this an indicator of any bug?""",
    """Test Cases 50, 60, 70, 80
I checked previous post about failing test 70 and 80, I've updated the priority and I am not sure what is wrong with my code.""",
    """When to use java and when to use english expressions?
For prelims.""",
    """Software on campus computers
My laptop broke down on me today, so I need to work on A6 using the campus computers. Do the Carpenter/Phillips computers already come with the appropriate software installed? And would I need to reconfigure all the Eclipse preferences we went through at the start of the semester each time I use a different computer, provided that I don't get the entire assignment done in one sitting and have to use different computers several times?""",
    """SP 18 5:30 #5


For the Remove function of #5 in the prelim, I don't understand why it's necessary to include s==1 case, why can't we just have s==null and the else. Also for the s==1 case, why don't we directly also decrease the integer part of the map by 1. Why do we only remove the object?""",
    """is distance type int?
Can we assume that the length of each edge is type int? The priority from heap is of type double, but the field dist of class DB is int. That being said, would it be safe to assume that all distances are of type int and perhaps casting the priority value into int?""",
    """Chaining
Could someone please explain how this insertion works from the lecture slides?""",
    """Picking an element of a heap
How do I pick a node from F and store it in a variable?""",
    """complexity


Can someone explain why the second complexity question is n square instead of n? Thanks""",
    """How do I access the first element from a HashMap?
How do I access the first element from a HashMap?""",
    """Review session for prelim 2?
Will there be a review session for prelim 2? If so, when and where?""",
    """checking the value of f and end
what attribute of node f and end do I have to check to be equal?""",
    """Return doesn't terminate while loop
The correct path can be printed. But after return, the while loop doesn't terminate and creates an infinite loop. Is it because of the synchronized keyword in the pathSum method?""",
    """a7 file to work on
So is everything we have to do for a7 in DriverMin.java?""",
    """improved version BFS
In the improved version of BFS, everything we put on the queue is the vertex that we haven't visited so far, right?

So why would we want to check whether the vertex u is visited in the while loop(in red)? Is that sentence necessary?""",
    """a5 grades
Are grades for a5 posted? I can see the average score but my score isn't there.""",
    """Private Constructor
How to I access DB to initialize it to (0, null) since the constructor is private""",
    """placing return statement
I followed the formatting in the dfsWalk tutorial on Java Hypertext, but I'm having trouble placing the return statement. The diver continues moving after coming across the ring. How can I fix that?""",
    """Code Readability
Is it better to create local variables or write something like S.get(fNode) in larger statements (say, an "if" statement)""",
    """Bipartite Graph
Why can bipartite graph has cycle of even length? I thought this kind of graph should not have cycle at all? Also, is there a difference between the concept of "loop" and "cycle"?""",
    """planarity
Does a graph being planar have any significance in terms of things we can achieve if given this property? I get the idea, but why is it important to know this?""",
    """Comment for HashMap
I am confused about how much we need to write in the comments for HashMap. Besides saying which nodes are in the HashMap, are we supposed to add information like the keys, the distances, the backpointers etc?

And in terms of the set F, what kind of comments do we need to put? Is it enough to put “As described in the abstract version of the algorithm in the A6 handout.” as described in A6 handout?""",
    """Lecture slides and sample code files unavailable on course website
I can't seem to download the zip files from 4/16 and 4/18 or the lecture notes from 4/18. Is there an error with the attachments?""",
    """An algorithm being non-deterministic
The subtractive method of finding the spanning tree is a non-deterministic method because we might end with different spanning tree diagram if we pick different edge to delete. Does it mean that whenever the result for some algorithm depends on the intermediate steps taken, then it's a non-deterministic algorithm?""",
    """Does prelim 2 contain Generics?
Does prelim 2 contain Generics in the lecture of April 18?""",
    """Question about SP16 7:30 Prelim2
Hi, for the question 5(b (the last question), I really don't understand any of the 5 problems. Could someone explain the reason for choosing the algorithm over the others for each of the problems? Thanks!!""",
    """Algorithm dance videos
Just wanted to share this YouTube channel I discovered that has videos where they use folk dance to demonstrate algorithms such as Quicksort, Insertion sort, Selection sort, Merge sort, binary search and linear search. Actually helped solidify my understanding of the algorithms to see them like this... plus it's a fun study break.

This one is my favorite: Quicksort with Hungarian folk dance.""",
    """bfs question


Why does D visit E first rather than C? Isn't C a lower letter than E?""",
    """Testing
When I test A6, the test result shows that it passes all the tests. But the GUI does not show up. I was wondering if there is anything wrong with my code or file.""",
    """Peek or Poll
At the beginning of the while loop it okay if we use peek to check if the parent of the minheap is the end node or should we use poll? I feel that using poll when it happens to be the end node violates the invariant since we remove the node from F, indicating that it is a settled node but don't go on to process its neighboring nodes ?""",
    """grace period
how long is the grace period for assignments?""",
    """fa2010 Q1d
In this question, can we answer like this:

The nodes are of type Integer, so we can create a binary search tree according to the value of all the nodes. At the same time, the priority of the nodes can be arranged so that it can be created as a minheap. Therefore the search time can still be O(log n). 

For this question, can priority and the values be different for each node?""",
    """fall 2014 exam 1


Can someone please explain what "tightest bound" means?

Also, In worse-case complexity of removing an item, we take O(log n) time to find it, and another O(log n) time to bubble down the heap. Is this the reason why the overall complexity is O(log n) ?

For worse case of inserting item, we always insert item on the leaf, and bubble it up. Is this the reason why complexity is  O(log n)?""",
    """Common Data Structures
On the prelim review sheet it does not mention knowing the common operations for Queue and Stack should we know them even though it is not listed ( I am referencing number 5 on the handout)? Thanks!""",
    """Forgot names and netid
We forgot to put our names, netid, and time spent at the top of A6. How many points will be deducted?""",
    """prelim
the study guide mentions we should know topological ordering.. should we know the topological sort algorithm""",
    """balanced tree
Why is this tree not considered balanced? Isn't the height for the left subtree 3 and the height for the right subtree 4, which at most differs by 1, the definition of height-balanced?""",
    """dijkstra order of removal


Could someone go through the process of solving this particular question (step by step)? I thought order of removal was edge of minimum distance reachable from the nodes you have already visited.""",
    """Do we have to be able to implement Dijkstra's algorithm from scratch?""",
    """scope of prelim2
is there any file that enumerates all topics covered in prelim2?""",
    """java doc on prelim2 and other style guidelines
are we expected to write down java doc in prelim 2? what other style guidelines we are expected to follow?""",
    """Lectures Explicitly on Exam
I understand that we need to know the material from Prelim 1 as well, but which lectures will be explicitly tested on Prelim 2?""",
    """Difference between Array and ArrayList
What is the difference between the Array and the ArrayList?""",
    """prelim2 covering TreeSet?
When i read the handout for topics in prelim2, i found we were expected to know TreeSet in java but i don't think we have learned this before.""",
    """Spring 2016 5:30 5b: use cases for different algorithms


Can someone explain the answers to these? And the differences between the algorithms?""",
    """sp 2016 5:30 1g: algorithmic complexity true/false
Method m() processes a list of size n using nested for loops. Therefore, the run time of m() is O(n^2)

Why is this false?""",
    """Heap maintains balanced tree
I am confused about the concept that Heap always maintains balanced tree. In the slide below, since for node 22, the heights of its left subtree and right subtree are different, the tree is not balanced, is that correct? But why can we use Heap to manipulate it? 

And also am I right to think that the concept of completeness is not the same as balanced?""",
    """2018 spring 5:30 7f
Why here it's dfs not bfs for the method isProper()? I thought the method traverses each neighbor of a given node which is exactly what bfs does.""",
    """Fall 17 7:30 Q7)#3
In this question, why isn't the answer 0? Isn't this graph already nonplanar since the arrows from b to d and e to c cross?""",
    """updating java
my eclipse had updated my java version to java 9 and uninstalled java 8. Will this matter?""",
    """GUI
In the demo file, BorderDemo.java, when I run the GUI, I'm able to check the radio buttons, but why is this the case if we never added the action listener to the buttons?""",
    """Fall 2017 7:30 Q2C
Why is this statement" A JButton in a GUI must be “listened to” by only one actionPerformed procedure, which defines what happens when the button is clicked." false? Why would a JButton have multiple actionPerformed procedures? """,
    """Dfs
Are we expected to know how to implement dfs recursively and iterative dfs?""",
    """BST complexity
Why does a BST have a time complexity of O(depth) for the get() method? When looking for a element, don't we first see if it's less than or more than the root and repeat that process until we find the element, so we are doing half the search? I thought it would be O(log n)""",
    """Dfs time
On lecture 19 about BFS and DFS, ti says that the time of DFS (recursive) is O(V+E) or O(V^2). I understand why its (V+E) because we might have to visit all the vertices and its edges, but why is it also V^2?""",
    """SP 16, 5:30 2c
In this solution, why do we say list.get(i) takes O(i) time rather than O(n) time?""",
    """SP 16 5:30 4d
Could we have just used if and else statements rather than "return;" in our implementation of add, or is there a specific reason why "return;" is used?""",
    """Fall 2015 prelim2 5:30 Q2 part(a)
Since we should list lower-letter node first, why the order is not ABDCFGE?""",
    """Fall 2016 5:30 2a
After it visits D, why does it go to E instead of C, which would be the smaller letter node in this case?""",
    """Binary Search
Can someone explain why the algorithm below finds the first occurrence of v? I think it finds the last occurrence of v. For example, lets say after one iteration of the loop, b[I] = v. Now lets say during the second iteration of the loop, b[e] equals v again. Well, in this case, I is changed so that e=I, and already we see that b[I] does not refer to the first occurrence of v.""",
    """Fall 2015 5:30 Q1 part d
why g(n) = 2^n is also true?""",
    """Question about Planar Graph
For example, a graph has intersections of edges, however we can move the nodes such that they could be rearranges in positions that do not cause edges to intersect. In this situation, should the graph be considered planar or not? Thanks""",
    """Linked List Complexity
Why does it take time proportional to n to add/remove something from a linked list? Can't we just access the last node directly and set its pointer to the new node we want to add? I understand why it would take time proportional to n to see if a linked list contains a certain value, but I can't piece it together for the other two.""",
    """O(log n) for poll in heap
Why is poll O(log n) for heaps and not O(1) since we are just removing and returning the first element?""",
    """is bubbleUp and bubbleDown stable?
i meant, when i tried to sort the heap once i have bubbleup or bubbledown one node with priority unchanged, is there any case that my heap will change.""",
    """Prelim 2 Review Conflict
According to the study guide, the review is being held on Easter Sunday. Unfortunately, I (along with other students observing the holiday) won't be able to attend due to this conflict. For those of us who are unable to make it since we are not in Ithaca, is it possible to record the event so we don't miss out on the material covered? The last review session was extremely helpful and it would be unfortunate to miss out on this one due to a religious conflict. Thanks!""",
    """Repeated values for hashing
For part i, do we just ignore the second 1 because it's repeated?""",
    """Average time for BSTs
I understand that the worst case time performance for a BST is O(n), but I'm not sure if the average/expected time performance is O(log n) or O(height). 

The lecture slides states O(height) for BSTs, and O(log n) for balanced trees.""",
    """BFS using recursion
Can a BFS be implemented recursively? Or is it much costly to do so?""",
    """QuickSort/ Merge
Should we become familiar with the log(n) space version of quick sort for the exam? Also, I know mergeSort is on the exam, but what about the merge algorithm? (Merge isn't listened on the study guide but I just wanted to double check).""",
    """dfs order


Why would you visit G before F? Doesn't F go before G in the alphabet? Or is this just a matter of implementation?""",
    """algorithm for heapsort
What is the high level algorithm for heapsort? I keep seeing questions on heap sort on the prelims, but they're all very different implementations, and the Java Hypertext entry on heapsort only has pseudocode for bubble up and bubble down.""",
    """O(n) sorting
Is there a comparison-based sorting algorithm that can sort an array in O(n) time?""",
    """Fall 2016 5:30 2(b)


For this question I'm having a hard time understanding why after visiting A, B, and D, the next node visited is E instead of C (going off of the lower-letter condition).""",
    """2017 Spring 5a
For the purpose to check whether the right node or left node is null, can we alternatively write this statement "if (n==null) return true;" at the very beginning of this method?""",
    """need to know minimal spanning trees?
not sure if we need to know this because i dont think it's on the study guide. But for Prim's how do we know which node is going to be the starting node?""",
    """do we need to know Kuratowski's Theorem for planarity?""",
    """quick sort log space
For quicksort log space, we only sort the smaller section. However, wouldn't this leave the larger section unsorted? Thanks""",
    """Hash Functions
Just out of curiosity, I was wondering how hash functions are developed. The example in class hashed based on the first letter of the state, but surely to have truly effective hashing, the hash function must usually be much more complicated. Are there certain hash functions which are commonly used? How does one determine what a good hash function is?

(Presumably, however, if you are storing passwords or something secrative using hashing, you want some super complicated, super weird hash function, because if one knows the hash function, one can "decode" the passwords and get to them?)""",
    """proofs by induction
Do we need to know how to prove using induction? I know the study guide doesn't mention it, but I thought that might be because it is not a direct concept, but instead a method to prove other concepts.""",
    """adding an existing node to heap and BST
What would happen if we add an existing node to the heap and the BST? For BST, I guess it cannot contain two same value, but what about heap?""",
    """dijkstra true false


Why is this false?""",
    """2016 SP 7:30 Q2
Why is the complexity O(i) for remove()? In Java Documentation it says only size, isEmpty, get, set, iterator, and listIterator operations run in constant time. I thought besides moving the last element in the arrayList the complexity is O(1) removing other elements all take O(n) complexity.""",
    """stability of quick sort
I'm a little confused about the stability of quicksort. When i perform the algorithm on my own, when swapping the value at b[j+1] and b[t], my maximum values end up reversing themselves. However, in the lecture slides it shows the maximum values being in the same order as in the original array. how does that work in that way?""",
    """2017 fall 7:30 2(a)
Why do we need a set to maintain nodes that are visited? In the algorithm it seems like we only need a queue. Also can we say "bfs maintains a quene of nodes that are unvisited"? Thanks!""",
    """Slides for Review Session on Sunday?
Can we have the slides from the review session on Sunday?""",
    """Improved bfs
In improved bfs, why do we need to "mark v as encountered"? After we add v to the queue and remove it sometime later, this node v (now it is called u) will fail the if statement condition and thus will not go through the for loop?""",
    """space complexity
Why the expected space complexity of merge sort is O(n) and that for quicksort is O(log n)? What exactly determines space complexity? Is the number of stacks, the number of arrays, the size of the array?""",
    """array vs arraylist vs linkedlist
Could someone please tell me what the differences between array, arraylist, linked list, and list and their complexity regarding operations such as add, search, etc? I am confused because for question 3(b) on 2014FL 7:30, the answer says that add to the end of the arraylist is constant time; however I thought add should be O(n). Thanks""",
    """Are we supposed to know extensions to BST?
Are we supposed to know AVL trees, 2-3 trees etc?""",
    """Review Slides Complexity Problem
In the prelim 2 review slides, there is a question: What is the complexity of the algorithm which multiplies two matrices (N x N) in a naive way? What is the solution to this?""",
    """F18 prelims
Is there any reason the prelim 2s from last semester are not on the list of past prelims on the website?""",
    """Sp 2018 7:30pm - 4(a) a
Why is time complexity for red black tree O(logn)? 

Is it the same for all balanced trees?""",
    """S16 7.30pm 5(a)(ii)


Why does BFS visit d before b? Aren't they both distance 3 away from a? (The question says to visit nodes alphabetically if there is a tie.)""",
    """F17 7:30 6a
In the slides, I remember that seeing that it was possible to make the space complexity of MergeSort O(log n) as well. Was this question intentionally asking for just the efficient version for QuickSort, or is not possible to make MergeSort's space complexity O(log n)?""",
    """DFS/BFS in prelim review slides
My solution to the order of visiting nodes in DFS and BFS is not matching with the order on the review slides. I tried solving the lecture slides one and I go let it right so I'm pretty confident in my solution. 

Is there a mistake in the review presentation?""",
    """F17 7:30 7a3: Making a graph nonplanar
How can we arrive at the minimal number of edges that need to be added to make a graph non planar?""",
    """Sorting
Will sorting be on prelim2? I know we partially covered them, such as insertion sort merge sort Quicksort etc in prelim 1 and although they are on the prelim2 study guide, it's not in the prelim2 review powerpoint.""",
    """BFS
2017 Fall 7:30

One of the true false asks if BFS maintains a queue of nodes that have been visited and the answer is false. Why? I thought BFS did use a queue to do this. Answer says it maintains a set.""",
    """Fall 2017, 5:30, 2b
I was having trouble with the first part of 2b. I understand that the loop is executed n times, but I thought that the add function for array lists was amortized constant time (also stated in java API). Wouldn't this make the complexity O(n)?

From java API, "The add operation runs in amortized constant time, that is, adding n elements requires O(n) time.""",
    """Massaging the Sort


What exactly does it mean to know the "massage" of the sort?""",
    """SP16 5:30 1c
1b and 1c are almost the same. Why 1c evaluated to FALSE?""",
    """Fall 2017 7:30 Q4 part (c)
What is h and k in this case?""",
    """Detect Planarity
To detect the planarity of a graph, could we change the place of a node, apart from changing the shape of edges?""",
    """Fall 2016 5:30 Q2 (a)
Why it goes to E instead of C after reaching D? Isn't the rule saying that should first visit smaller letter nodes?""",
    """FA17 1.c
i was a little confused on this question, and that's what i thought: if the tree was balanced binary tree, then searching was O(log n) or O(Height). Because the question only said "a binary tree", searching would take linear time, right?""",
    """fall 2016 4(d) 5:30


For this question, why does the first statement only check if the first node is equals to e rather than checking the whole tree? Thanks""",
    """Complexity Questions
Will you explicitly ask for the worst time, best time, or average time for complexity on the prelim, or should we assume one of these choices?""",
    """Spring 2016 1(h)
If a graph will have thousands of vertices, each having at most 5 neighbors, you
should implement the graph using a matrix rather than adjacency lists.

Why is this false? Don't you use matrices when there are lots of vertices?""",
    """FA 15 7:30 Q1
"If the value of function equals(Object) in a class depends only on fields b and c, function hashCode() in that class has to depend also on only those two fields."

The answer was true but I thought the only requirement between equals and hashcode was that if two things equal each other they must produce the same hash code. If this is correct then doesn't hashCode() not necessarily have to depend on b and c to produce the same hashcode for two equal objects?""",
    """fa14 2(c)
Should d here be the height h rather than the depth?""",
    """Binary search tree
Can the right and left subtree of BST contain the same value as root? Thanks""",
    """BFS ordering Spring 2016 5a(ii)
When we do the BFS, does it matter which node we write down first if they are in the same depth? For example why is it f then c and c then f?""",
    """Question about Insertion sort and Selection sort
Hi, I'm a little confused what is the best case time complexity for these two sorting algs and also, should the space complexity for them be both O(1) (constant)? Thanks!""",
    """Heap Sort
Is heap sort stable? Also, are the time complexity for best/worst/expected cases all the same for heap sort? Thanks!""",
    """Efficiency for topological sort
In HyperText, the implementation of the topological sort is given, I want to make sure I get this correct:

In terms of efficiency, the first for loop loops through all the possible nodes, which is O(N), and the while loop is executed to check every single edge in the graph, which is O(E), so together, the efficiency is O(N+E), right?""",
    """T/F
The average time complexity to search in a binary tree is (logn), given n is the number of nodes in the tree. 

Why is this false?""",
    """pirority queue
Why is remove and contains linear operation but add log operation? Thanks""",
    """bubbledown
I hear in lecture that we need to know bubbleup but not bubbledown, but I want to make sure. Do we need to know the implementation of bubbledown for the test? Thanks""",
    """Tree


I'm confused because for the in order and postorder of this tree, it seems to be taking a as the root for postorder and b as the root for in order.""",
    """GUI
GUI questions on the Study Guide and Review seem to be only from the 1st GUI lesson and beginning of 2nd. Does this mean we don't have to know all of the functions like capsframe, capslabel etc and Anonymous functions?""",
    """2017 sp 5:30 5(b)


For this question, since a heap is like a tree, which is a set, why are we allowing the same value to appear twice? Thanks""",
    """bubbleDown
when i do the bubbleDown, I first replace the parent with the LEFT children, right?

If the priority of two children are the same, I still choose the LEFT one, right?""",
    """nodes in the order they would be settled by Dijkstra’s algorithm
Will nodes always be settled in the order corresponding to least distance from the initial vertex, v? For example, if the shortest path from v to x was 3 and the shortest path from v to y was 4, would x always be settled before y?""",
    """T/F


Why is Integer a subclass of Object but not String? Is there a place in Java Hyper Text that I can read more about it?""",
    """fa14 3(b)
In (b), why changing the order of inserting would reduce the time complexity to O(n)?""",
    """spring 2016 5:30 3


For this question, i am very confused as to how this is in the order prensented. Could someone please explain to me? Thanks""",
    """balanced binary tree
Is there an exact definition to a balanced binary tree? I saw the slides say that the subtrees of any node should be about the same height. Is there an exact definition to "about the same height"? (within +- 1?)""",
    """fall 2013 t/f question


Is this true because you can have a JFrame with more than 5 components if you implement some other layout manager that is not its default?""",
    """Fall 2015 7:30 2a


I understand that a linear probing algorithm stops searching when something is null, but I don't really understand why that is important here? If we are removing 1, then isn't the space where 1 was available for other values that may be inserted to be hashed into?""",
    """Removing an item from a heap
Shouldn't removing an item from a heap take linear time, since we have to iterate through the entire list to find the item. In a practice prelim, question attached, it says worst case time is O(log n)""",
    """HeapSort Space Complexity
I am unable to understand why the Space Complexity of Heap Sort is o(1). Could someone please help ?""",
    """Time Complexity for computing outdegree of a Node


For this question (fa17b) why is the time complexity to compute the Outdegree for an adjacency list O(n)? I thought that the time complexity for an adjacency list will always be O(1) since class LinkedList has method size() that runs O(1). Furthermore, if implemented using an array of LinkedLists, finding the given node will also take O(1).""",
    """Min Priority Heap
When I did the lab, I noticed that a min priority heap AND a max priority heap had the highest priority as the root. This made sense as it is the value of each node that determines if a tree is a min or max heap, so I figured in a min heap the min value would have the greatest priority, and vice versa. However, on the Fall 2016 5:30 Exam, the question notes that "the value is the priority" and the answer has the min value/priority as the root. Have I been understanding this wrong?""",
    """F 17 2c)


Can someone explain why inserting d alone has multiple indexes?""",
    """F 17 2a)
Help, please""",
    """merge sort stability
lecture slides say mergesort is stable but an exam question says that it depends on the implementation of mergesort. which one is it?""",
    """Fall 2017 Q4(b), 5:30


Can someone please explain the time complexity part?""",
    """FA 16 5:30 - Q2
Is the answer ABDECFG and not ABDCFGE because the edge weghts? Following the lower-letter node rule, one would pick C after D, not E. If it is because of the edge weights is there an implementation of DFS/BFS that takes into account edge weights we can look at?""",
    """Spring 2016 Q3(a) 5:30
I don't understand how this order of addition creates such max-heap. Could someone walk through the process at least for the beginning?""",
    """S 17
For the HashCode, why do we add them together?""",
    """BST
Can binary Search Trees have duplicates?""",
    """Insertion Sort unstable/stable
Can't insertion sort be made unstable or stable based on our choice?""",
    """Spring 2017 5:30 Q5b)
How do we know if this question is talking about a min or max heap?""",
    """F16 5:30 Q 2a
Can you please explain how the last four are traversed? I'm confused as to why E comes before C in the first place. Thank you!""",
    """Visiting nodes
For this method, wouldn't it terminate early if the node you started out with (the very first call) had already been visited? There was no precondition saying whether or not n has been visited.""",
    """2018 spring 7:30 problem 5
For this problem, shouldn't we check whether ob is null or is not an object of class E, and return false for these two cases?""",
    """spring 2016 5:30 dfs


I put C before E since after D, C is smaller than E regarding alphabetical order. Could someone please point out my mistake? Thanks""",
    """spring 2018 5:30 6b


the parameter of this function is an array of files but when creating the variable t we declare that it is type int.  Shouldn't it be type file if we are storing a value from the array in t?""",
    """2010 2q
Shouldn't the sorting order for a priority queue base on the priority instead of the values?""",
    """LinkedList add() for 5b on 2017 Fall 5:30
In lecture 14, it states that a LinkedList add() prepends by putting the new element at the front and is of time complexity O(1). However, in Oracle Docs, it says a LinkedList add() appends the specified element to the end of the list. In my mind, this would take O(n) because it is necessary to traverse to the end of the list. Which convention do we follow?""",
    """Fall 2017 5:30 Problem 3
For a heap sort, the first node in the heap will have to be bubbled down, because it violates the max-heap invariant. However, in the answer manual, the bubble down method bubbles down the element at index k. If k is the maximum of the heap, then why does it have to bubble down? Is it not already the last element of the heap, so it cannot go further down?""",
    """Errors
would you recommend reviewing runtime and compile time error questions......the kind that have shown up on prelim 1 in the past?""",
    """Hashing
Will we be asked to write code for hashing for Prelim 2?""",
    """True false in prelim 2 fall 2017.
The question "Breadth-first search maintains a queue of nodes that have been visited" is false for some reason. Why would this be?""",
    """Linked List on Prelim 2
If given a question with a linked list on prelim 2 will we be told what type of linked list it is (e.g. doubly) or are we supposed to assume it is a doubly linked list as per the default Java implementation?""",
    """2016 SP 2(d)
For this problem, why is the worst time complexity O(log n)? I understand that if we use binary search then the expected time complexity is O(log n), but if we search the array from head to tail wouldn't the time complexity be O(n)?""",
    """shortest-path algorithm
If there are two nodes in frontier set with minimum d values, how should we decide which one to be moved to the settled set first? Thanks!""",
    """spring 2016 7:30 Q3 part a
Why the tree in the picture is created by adding the elements in order? 

What is the order for creating a max heap from a list of values?""",
    """Order in which nodes are removed by Dijkstra's algorithm
What is the best methodology to follow to do this?""",
    """Unbalanced BST
I'm confused on how a BST can be represented as a linkedlist. Wouldn't that mean it is not a binary tree? I understand it is in its unbalanced form, but shouldn't it be called a linkedlist until it is balanced into binary tree form?""",
    """sp16 7:30 1c
Do we need to consider whether the graph is directed or undirected? I chose False since I thought the graph should also be directed.""",
    """Are sorting algorithms like merge sort etc. searching algorithms too?
Are sorting algorithms like merge sort etc. searching algorithms too?""",
    """Coloring
As part of graphs, will we be expected to know how to color a graph as discussed in lecture for the prelim?""",
    """S18 7:30 7c
How can we arrive at the minimum number of colors needed to color a graph to be chromatic?""",
    """Prelim 2 Spring 2016 Q5 part C
Must the graph be directed in order to be able to trace Dijkstra's Algorithm?""",
    """Prelim 2 Spring 2016 Q5 part B
Why the last two elements is db instead of bd?""",
    """fall 2016 1(b) 5:30 hashcode


Can someone please explain why if hascode of two objects are equal, they are not necessarily equal? Thanks""",
    """Hashtable vs hashset
Does anyone know the difference between a hashtable and a hashset. Thanks""",
    """DFS,BFS,shortest path
Does the above algorithm requires no cycles? Thanks!""",
    """Spring 2016 prelim 2 7:30 Q5 part b(v)
In general, when should we use DFS and when should we use BFS to model a problem?

And what properties determine this?""",
    """how much do we need to know about sorting algs?
For which sorting algs do we need to know the java implementation, and for which we needn't? For example, do we need to knw how to write topological sort in java?""",
    """Spring 2016 5:30 complexity


Does anyone know why the worst time for searching a sorted array is O (log n)? I thought if we use linear search, it would take O (n), although binary would take O (log n).

Also (iii), why is the expected run time O(1)? I thought hashing is related to a hashmap, which would take O(n), and hashset is simply a set. Thanks""",
    """Fall 17 5:30 Q4b
Why is the time complexity not O(np + nq). Another person asked this, and I understand that the program will stop when it reaches a the leaf of the smaller tree, but doesn't the program need to check if the other tree is equal? Why would it stop when it reaches the leaf of the smaller tree?""",
    """Greedy algorithm on prelim 2?
Is greedy algorithm on prelim 2?""",
    """Spring 2016 5:30 2(e) BST vs heap


Does anyone know why a balanced BST is better at processing the element in sorted order than heap? Thanks!""",
    """Fall 2015 5:30 1
T F Calculating the depth of a tree always requires examining all of its nodes,

Does anyone know why this is true? I thought if we know the tree is balanced binary, then we only need to look at one branch of the tree. 

Thanks!""",
    """Fall 2017 530
Can someone explain why is the minimal edges needed 3 instead of 2?""",
    """worst case of binary search is O(n) in runtime???""",
    """Time complexity for LinkedList - append(val)
Is the time complexity of append(val) for LinkedList O(n)? Or does it depend on whether the LinkedList has a last-node pointer?""",
    """Fall 17 2b 5:30PM Complexity
How do you figure out a codes complexity? I understand recognizing something at constant time but how you can tell something's O(logn) by just looking at the code. Are there certain rules for things like nested for loops? Or are we just supposed to memorize all the complexities? For example for Fall 17 2b how do you know its O(nlogn)""",
    """Add() for Hashset
Why is the worst case of add() for the hashset be O(n)? Is it because of resizing?""",
    """Binary Tree time complexity
Are the following true:

1. Binary Tree and Binary Search Tree have time complexity of O(n) when searching for a value

2. Only if the Binary Tree or Binary Search Tree are balanced do they have a time complexity of O(log n) or O(height) when searching for a value

Thank you""",
    """FA16 2(a), order visited in by DFS
Why is it that E is visited before C in the DFS? It says in the question that we should list the lower letter nodes first, so if E or C could be visited, wouldn't C be visited first? In the answer key it looks like they had this order and then crossed it out.""",
    """When am I taking the prelim?
I know this is online but the wording is confusing me. If my last name starts with an S am I taking this at 5:30 or 7:30?""",
    """Fall2017 prelim question 2f
Question 2f states this is false: Iterative depth-first search maintains a stack of nodes that have been visited.

Reason being iterative depth first search maintains a set....

Java hypertext says it maintains a stack of nodes.""",
    """LinkedList
For the LinkedList we encounter in the exam, can we infer that, if not specified, is a doubly linked list?

And add() means adding an element to the end of the LinkedList, which takes constant time operation?

Also, does singly linked list preserve the pointer to the last node?""",
    """2017SP b
In b) Why does the priority queue have anything to do with the interface Set? I thought Set only has HashSet, TreeSet, and LinkedHashSet as actual implementation.""",
    """Fall 2014 5:30 1

Does anyone know why it take O(l) time to compute the hashCode? 

Does anyone know how to approach this problem? Thanks!""",
    """Spring 2018 5 collection


In the solution, all the adding and checking functions are written in terms of Map. I thought that we are doing operation on MapBag, which is a set, not Map. Is this because Map is the actual data structure that stores the values in MapBag? Also, are we allowed to use Map since it is only a interface? Shouldn't we use HashMap? Thanks!""",
    """Topic Coverage
Will prelim topics like the different array sorting algorithms and their time complexity be fair game on prelim 2?""",
    """Why is insertion sort always stable?
Should it not depend on my implementation. Rather than checking for less than, I can check for less than equal to!""",
    """F14
My approach: finding the item takes O(n) and removing it takes O(log n). Should I not take into account the finding part?""",
    """complexity


Does anyone know why this is? Thanks!""",
    """Spring 2016 problem 5(b)
For this problem, why should we use BFS for (v)? If we label the weight of each direct bicycle path as 1, can we use Dijkstra's algorithm?""",
    """Spring 2018 5:30 6 CompareTo


Why is the return ob.size-size? I thought it should always be positive when this is larger than ob. Thanks!""",
    """Colorable
Why is a planar graph always 4-colorable?

Suppose: 1 node connected with 5 other nodes, and these 5 edges don't intersect. Then, it's not 4-colorable, right?""",
    """Dijkstra's
Are we expected to know how to implement Dijkstra's in Java from scratch? Thank you :)""",
    """fall 2017 fall 7:30PM (b)2


I'm wondering why we can add a string with an integer. Also, why the time complexity is n^2?""",
    """Merge sort space complecity
For merge sort, we only talked about the array c will take O(n) space, but we did not talk about its space on the call stack. Is that becase the space on call stack is O(log n), which is smaller? Thanks""",
    """2018 spring 7:30PM


Does this have to be a bipartite graph? Can I draw a rectangle-shaped graph?""",
    """DFS questions about weights
Do weights matter with DFS?""",
    """Black and white umbrella left in Statler 185 (7:30)
It's on the podium.""",
    """Will 2111 be held this Wednesday?
I remember after the last prelim 2111 was not held - I just wanted to double check.""",
    """Prelim 2 Grades
Last time the grades came out the day after the exam was given, so I was wondering what the tentative release day for this exam is.""",
    """Do we have recitation today?
Do we have recitation today?""",
    """Grades for/Solution to a6?
I thought that both of these would be posted well before now, but I don't see either. Am I blind?""",
    """Relative weighting of assignments
Are the assignments equally weighted? If not which ones are more heavily weighted? Thanks.""",
    """How can we check our grade?
I got Professor's email but where to find out our grade?""",
    """Didn't get grade on Gradescope
Are we all supposed to get our prelim 2 grades - because mine didn't come out yet.""",
    """CMS prelim grades
On CMS, for the prelim 1 grade, the description says "Prelim 1 (Curved)", however, the grade shown is my raw score, not the curve score. I just want to make sure that this is the case.""",
    """When will solutions for prelim 2 be posted?
Same as topic""",
    """Do we lose point for "ugly" code?
I see that the program needs to run reasonably fast, which isn't a problem for me. But will I lose points if my solution code isn't optimized stylistically as well, such as in a6?""",
    """import LinkedList
Can we import LinkedList in class DiverMin?""",
    """Cannot Run the Program
I follow the instruction given in the handout (but there is not Run -> Configurations, only Run -> Run Configurations), but it always run a6 pathTester. Shown as follow""",
    """coins on every node?
For method flee, we see that there aren't any methods about where the coins are locating. Do we just assume that there is one coins on every node? In other words, does that mean if we traverse more node, then we'll get more coins?""",
    """Error on moveTo: Node must be adjacent to position
I get this error every time I reach the coin. I only use the moveTo method to move to a neighbor, or back to the previous node in my for-loop. 

Any tips on how to figure out what the problem is?""",
    """deadline for regrade requests?
when is the last day to submit regarde requests for prelim 2?""",
    """Running GameState with run configurations
When I run GameState.java with the run configurations with a count greater than 1, every time it runs after the first time it fails to find the ring and produces the message in the console "Your solution to find returned at the wrong location". Additionally the first trial always works, it is only those after it that fail.

The Issue is that I can take that seed that appears to have failed and run it on its own in GUI.java and it's able to find the ring. I know this is not due to my solution taking too much time, as I often will still obtain a bonus over 1 on a seed that had failed. I have also tried increasing FIND_TIMEOUT in GameState.java but that has no effect. Could there just be some bug in my code that only comes through when I try to run multiple trials or is there some greater issue?""",
    """Missing prelim on GradeScope?
If you can't see your prelim 2 on GradeScope, please email Professor Gries immediately.""",
    """When will the A6 solution release?
I used method Node.getExits() for my A6, and I can't find this method at A7Skeleton in class Edge. Should I rewrite my method? And when  will the A6 solution release? It's said solution will be released after Sunday, 21 April, but I can't find where it is.""",
    """Method shortest() in zip file provided is not written
Good afternoon. 

I was just setting up my eclipse project for assignment 7, and the function for shortest path (that we completed in a6 - in class Paths.java) is not fully written on the zip file provided.

In other words, the solution to a6 provided in the a7 piazza note (@1625) that we should be using on the Sewer systems assignment was incomplete. Has it been updated since the late submission deadline to a6 closed? Apologies if I downloaded the incorrect file.""",
    """moveTo
How do we access the moveTo method in FindState if it is an interface? Is DiverMin supposed to implement FindState?""",
    """A7 graded on average score over many trials?
My current solution relies partially on randomness, and although it produces decent average scores (over 1000 runs), it will occasionally do terribly (just as it occasionally does exceptionally well). With such a solution, would my grade be reliant on luck, or is it based off of an average score? It never fails to leave in time.""",
    """Sample Final Solutions
A lot of the solutions to sample finals are not up. Will they be uploaded for us?""",
    """Grundy Number
For 6a in the 7:30 Prelim- why is the answer 4 for Grundy number and not 3? The graph can be colored with 3 colors""",
    """HAPPY BIRTHDAY PROFESSOR GRIES


Happy Birthday!""",
    """The import graph cannot be resolved


I downloaded the solution to A6 to my a7 project folder, but the import statements in the file shows this error. I could I resolve this? Thanks!""",
    """Shortest Path Theorem
Does the theorem in Dijkstra's state that for the node f with minimum d value in the frontier, d[f] is the length of the shortest path from v to f using:

a) only settled nodes (except f - it is in the frontier)

b) all nodes (all paths to f)

I have received various answers about this and wanted to clear up exactly which is the correct one.""",
    """Prelim 2 Curved Score
When are prelim 2 curved scores coming out?""",
    """How do we mark a node 'visited' in dfsWalk in Find()
I don't find a field anywhere to represent it, should we declare a new one in the NodeStatus Class?""",
    """What to do if Min is stuck between two nodes?
During the find state, sometimes Min keeps going back and forth between two nodes without going anywhere else. Any suggestions on how to solve this problem? Thanks!""",
    """Coin values?
I notice that sometimes the coins in the graph are represented by different images, and they seem to have different values. How can we find out the coin value of each type of coin? Thanks!""",
    """Is the miner able to locate coins' positions? Or is it all random?
Random: If you walk over a tile with a coin, you get it, else you don't, tough luck...""",
    """Manhattan Distance
Does the function distancetoRing() return the shortest distance from the current tile to the ring tile, regardless of the unwalkable tile between Min and ring, or will it return the distance of the shortest route? Currently in our program it seems to do the former, but it will lose its meaning in optimizing the pathfinding program in this way.""",
    """getStepsRemaining()
Which class does this method belongs to?""",
    """TA isn't here
Did the TA unofficially cancel his office hours? The website says it's here in Rhodes, but some students and I have been waiting for a long time...""",
    """getExit()
What will this method return when reaches the exit?""",
    """Is time limit running with GUI open?
So I have been running a7 both on GUI.java and on GameState.java, and the time varies between the two, since GUI have a speed limit for how fast the operations are. I was wondering if the time limit of 10-12 seconds is for running on GUI or running on GameState?""",
    """Error during looping getExist
Isn't getExist will return the node to exit?

I just wonder why I had this error:

getEdge: Node must be a neighbor of this Node""",
    """Find
How do you know method find is correct?""",
    """Pass/Fail
Can I switch this class to pass fail at this point in the semester?""",
    """Add
I have a data structure that keeps track of which nodes have been visited through their node status, you are able to do this with every node other than the initial node, how do I add the initial node status?""",
    """Is there a way to get the neighboring nodes of a tile during the flee state?
Is it possible to get information on the four neighboring tiles of a center tile?""",
    """Make-up Office Hours
I am very sorry for those who came for my office hours today and didn't find me there. I had a concert today and was caught up in its preparation for the whole day that I forgot that I had office hours today until just a moment ago. I understand that I have caused a lot of unnecessary wasted time for those who came over to Rhodes specially to get help and I sincerely apologize for that. As such, I will be holding extended make-up office hours tomorrow from 4:30pm to 6:30pm for whoever who still needs help. Once again, I am very sorry for the inconvenience caused by my mistake and I will ensure that such an incident won't happen again.""",
    """Running project
I copied my original project before improving on it, but both files within the projects have the same name (DiverMin). When I try running my project, it keeps running the newer DiverMin.java, but I want to run my original DiverMin file. How do I make sure it is running the older version? Thanks!""",
    """Node and Edge class
Should I add the package game classes
Node and Edge in the solution of A6.""",
    """Why do I always run out of steps?
My strategy for avoiding running out of steps: use a local variable at the beginning of the flee() method to store the total available steps and compare it with the size of my path List before deciding this path is valid. But the steps still run out occasionally, what might be the reason?""",
    """moveTo error after finding ring
after landing on the ring, instead of having the entire map illuminate i instead get this error message-- moveTo: Node must be adjacent to position. could someone help me understand what is causing this error/how to fix? thank you!""",
    """moveTo()
Does moveTo() "teleport" you to the tile specified, or does it walk you back to that tile?""",
    """moveTo() error after landing on ring
I know this has been been asked before, but when we land on the ring, we get an error saying we must try to only move to adjacent tiles. We did add a base case that calls return; if the distance to the ring is 0 after moving. 

Is there another base case we have to consider?""",
    """Modifying shortest()
In getting the miner out of the sewer in the flee phase, do we need to modify shortest() to use it? Or is there a way to use it as is?""",
    """How to access method shortest from Paths.java in DiverMin.java
I'm having a hard time figuring out how to access shortest in DiverMin.java. Aren't public classes available for all other files in the same package?""",
    """Error in find()
In my implementation, Min is able to reach the ring and the method returns at that point, but then I encounter an error saying moveTo: Node must be adjacent to position. Why is this happening considering I reach the point where distanceToRing() returns 0? I did add a base condition which returns if the distance is 0.""",
    """Ring
In our find method, Diver Min travels to the ring but doesn't stop at the ring. Why does it keep on continuing?""",
    """Reaching Neighboring Nodes of FleeState
I saw post @1979, but I'm still lost as how to reach the neighboring nodes of flee-state. Are we supposed to be looping through allNodes with a for each loop?""",
    """FleeState return at wrong location
I am trying to implement fleestate, but it keeps on returning at wrong location despite checking that the current node is equal to state.getexit() the exit node? Can someone point me to the right direction?""",
    """"Good" Scores for A7
Just so we can benchmark a bit and understand how we stack up to the rubric, what is a "good" score on A7 that will let us surpass the 85 point base for a working solution and receive a solid A?

Right now, our average performance over 10000 trials is a score of about 8000. We don't know whether we are lacking and need step our game up, or if this is decent.""",
    """Debug
How do I debug, when the error message says the solution to find returned the wrong location?""",
    """Lecture Slides
When will the slides for April 25th's lecture be up?""",
    """an issue with our diver
So my partner and I are having an issue with our diver. He can move up and left in the maze, but he cannot move right for some reason. Every time the diver hits a corner that would force it to move right, it would simply turn back around to the previous node, but when it does that, it turns to the corner, making it loop infinitely. Any idea why it does that?""",
    """using paths.shortest
How do we actually call paths.shortest in method find()? Specifically, if I want to find the shortest path from the initial node to one of its immediate neighbors, what would my parameters for the method be given that method shortest takes two nodes as its parametrs?""",
    """can't run from GameState
Every time I attempt to run from GameState.java I get an error "Could not find or load main class". What's going on? Thank you!""",
    """implementing the flee stage
Are we expected to make our flee method recursive similar to how we did in the find method?""",
    """current location()
I am confused about returning the unique identifier associated with the current location. I am thinking of returning the id of the location. But how do we get access to the current node Min is standing at?""",
    """DiverMin beginning
Where does the person start at the beginning of the program? For find, do we assume that they are already at the entrance do we have to find the entrance?""",
    """Seeds for simple/small mazes?
Does anyone have recommendations for seeds that produce small/simple mazes so I can move through the maze quicker when debugging? Thanks!""",
    """How to Import Node
What do I need to import in order to use variables of type Node?""",
    """Calculating Steps Needed
I am trying to calculate the number of steps needed. How do I access the edge weights? I only know that getEdges can get the node that is an edge.""",
    """How to get the NodeStatus from FindState
How can we get the node where Min is standing at from the parameter FindState s?""",
    """Code for A7
Is all our code going to be in DiverMin?""",
    """Transitioning from Find to Flee
I return when I am on the ring, but I get an error saying that "my code errored during the find phase." 

Maybe I missed it in the directions, but do we need to write code in order to transition from find to flee?""",
    """prelim #2 weightage
I bombed the second prelim. will be weighed more than the first one?

also what is the aprox. letter grade distribution for prelim #2 lookin like?""",
    """GUI says steps left, popup says otherwise
As I am working on my solution, I am getting an error message that says "my solution to flee ran out of steps before returning". However, under my "steps left" bar on the GUI, it says I still have 11 steps left. What is the discrepancy? My diver has not reached the exit yet.""",
    """Distance
How is distance from the ring calculated? Is distance the number of moves needed to reach the ring or something else?""",
    """Are we allowed to import game.Node and game.Edge for method flee?""",
    """DFS - Recursion or Iterative
It seems that most people are using recursion for the dfs walk. Would it be okay to use an iterative dfs or could that be a hindrance later on?""",
    """Accessing neighbors
While writing a dfs method for find(), I am trying to go through all the neighbors of state and recursively perform dfs on it. The neighbors of state are located in a collection. How can I go through the collection and perform dfs on each neighbor?""",
    """Value of state
when doing state.moveTo(id), does the value of the variable state change as well? i.e. when I do state.currentLocation(), is a new ID given?""",
    """Iterable
I think theres a mistake with Iterable on CMS. It says its out of 100 points, but the high score is a 1.""",
    """distanceToRing()
Does this method return the shortest Manhattan distance to the ring?""",
    """Big Maps
Any seeds that create large maps, please post them here. Good for testing efficiency.""",
    """Finding NodeStatus of Node Min is Standing on
Question title says it all.

How do you find the NodeStatus of the node Min is currently standing on? I want to initialize it into my visited node data structure.""",
    """Number of Steps Per Node
I see that the number of steps per Node is not constant. Is there a way to tell how many steps a certain node will take? If not, is there a set maximum number of steps per Node?""",
    """Acceptable Score?
Very impressed with scores being posted on the board! I have been playing around with different ideas and have gotten up to 27,000 on the specific seed and 13,500 average score over 100 trials. This is much better than the 5000 I got without any sort of optimization. I was wondering how high a score we would need to get for full credit?""",
    """running out of steps
My program runs out of steps for one of the simulations out of thousands sometimes. Is that acceptable?""",
    """Where is the evaluation form?
Same as topic""",
    """Error During Find Phase?
I keep getting an error at the very end of my find phase from method moveTo that says that the node needs to be adjacent to position. I get this error right when diver Min gets to the ring. But, I have a line in my code that returns when diver Min is on a node of which the distance to target is 0. So the code should stop (return) at that point, right? Why am I still getting this error?""",
    """bfs
For the BFS question in prelim2 at 5:30, the precondition doesn't say that the root is visited, it just says that the root is not null, so as the pdf in JHT suggests for dfs, the if statement(if (!f.visited)) should be put inside the for loop(finding all neighbors) instead of outside the for loop. So why the solution put the if statement outside the for loop for finding all neighbors?""",
    """Optimizing Flee
One procedure I attempted during optimizing flee is to check whether the steps needed for the shortestpath from this node exceed steps left. But I got this error message, what does it mean?

Your code errored during the flee phase.""",
    """Time of program
How do we get the time for how long our program takes to run? We are running our program in headless mode, but do not see a time in the output.""",
    """Prelim 2 solution
Where can I find solutions for prelim2?""",
    """ERROR - This compilation unit is not on the build path of a java project.


I have tried re-importing the project several times but it still gives the same error.""",
    """Greedy Paths
Under what circumstance would using a greedy path algorithm that looks at the shortest Manhattan distances to the ring from the neighbors of a node not be optimal? The way we are visualizing it, we can't understand why looking at the shortest Manhattan distance from a node to the ring doesn't just give the shortest path from the node to the ring (since the Manhattan distance is the distance i between two points along the path that can be traveled between those two nodes, and the path is given by the maze). If we were using the distance "as the crow flies", the problem with this approach would make sense, but as is, we can't see the issue.""",
    """Expected median grade for final exam?
What would be the possible corresponding letter grade for the median score of the final?""",
    """NodeStatus to FindState
in our recursive bfs call, our parameter type is FindState, but when we iterate through the neighbors of the state, it returns the neighbors as NodeStatus.

How can we convert NodeStatus to FindState so we can use our recursive call on neighbors?""",
    """Seed With No Coins
Hi! Is there a seed number we can use to check if our methods work when there are no coins on a given map? Thank you!""",
    """Getting a Node From its Id
How do I get a node from its id? currentLocation() returns the id, but I can't seem to get the node.""",
    """distance in flee
When implementing the flee, how do we find the physical distance (not the shortest path) between nodes?""",
    """Error in flee phase
Even when I'm making sure that a node is a neighbour of the current node I'm at, it is giving me the error that node must be a neighbor. My if statement goes if (node n is a neighbor of m). As in, it is entering only if n and m are neighbors. Why the error still?""",
    """Steps to move to a node
Are all nodes one step apart? During the flee phase, how do you find how many steps it takes to move from one node to a neighboring node?""",
    """Finding the ring
Are there any cases where there will not be a ring in the graph?  (I assume no but just wanted to check)""",
    """How to Access Number of Steps Left?
When writing the flee phase, is there a way to access the number of steps remaining?""",
    """Descending Order
In Flee, my partner and I were thinking of using a hashmap with keys for IDs and values for distances and want to sort it in descending order. Is there any way/method to sort a hashmap based upon values?""",
    """How to Get Total Run Time
On the scoreboard, people have total time. I was wondering where you can find this. Thanks.""",
    """Our code doesn't seem to add all of its neighbors


The code just stopped here after backtracking when it hit the dead end, because it thinks that the stack of tiles to visit next is empty. But how can that be the case? Apparently it never added the tile that is just left of Min?""",
    """walls as neighbours?
Are the walls included in the collection of NodeStatus? If so, how can the diver tell a wall apart from an open tile?""",
    """Time Limit for A7
The handout says that it should run in 10-12 seconds. To confirm, is this on the fastest mode or at normal speed?

Thanks!""",
    """is the step taken to neighbor node is always 1?
i was a little bit confused about my program and after looking the flee for couple times, i thought the step taken to the neighbor is not 1, right?""",
    """where is headless mode?
i meant, how can i run my program in headless mode?""",
    """Complexity of algorithms
Our solution works in headless mode every time well under the 12-13 second mark, but the time complexity of our flee isn't great. Will we lose points for a solution based on time complexity of algorithms, or is it solely based on scores on specific seeds and the fact that it works every time?""",
    """Do we need to write our name, netID and time spent in DiverMin?
I didn't see any place to comment our names and netIDs.""",
    """Where is getStepsRemaining()?
I cannot find the function getStepsRemaining() in the file. Which file is it in?""",
    """Collections.sort()
Are we allowed to use Collections.sort()?""",
    """Regrades?
Has the period for regrade requests already ended? I'm not sure why I got a particular question wrong and gradescope doesn't have any explanation for it""",
    """Declaration
1. When we create a new Array List, do we need to declare it as private?

2. I have not used Collections.sort for my solution although a lot of students on Piazza seem to be asking about it. It is possible to write an optimized solution without it right?""",
    """Greedy find algorithm
I am confused about how to make a greedy find algorithm. 

How do you determine the neighbor that is closest to the ring and choose to move to that neighbor when you only have access to the distanceToRing of the current position? 

It seems you'd have to moveTo each neighbor to get the distanceToRing of each neighbor to check which is closest to the ring, and this seems inefficient.  Is there a way to get distanceToRing of a node that is not the current position?""",
    """Weightage of Prelim 2
If we are not taking the final, what will be the weightage of prelim2? Will that be 30 percent for prelim 1 and 30 percent for prelim 2? I didn't find any information of that on the course website. Thanks.""",
    """flee state
How do we know if our implementation of fleestate is good enough (able to get full credit)?""",
    """Grading
Approximately what raw score on CMS for the entire course is a B?""",
    """Creating a greedy algorithm
How I am supposed to create a greedy algorithm that goes to a NodeStatus neighbor with minimum getDistanceToRing. Should I create a new sorting function to sort the collection of NodeStatus objects? Or should I define a comparator class for comparing NodeStatus objects on the basis of getDistanceToRing(). I'm really confused.""",
    """distance during find phase
is there any way to find the manhattan distance along the graph to the ring during the find phase instead of using distanceToRing() that only gives the manhattan distance along the grid (which is really inefficient in most of the cases).""",
    """total weighed score on cms?
Hi, I saw this "total weighed score" on cms, is this weighed score for the course or just for prelim 2? I also see a "prelim 2 curved" on cms, so I'm a bit confused.""",
    """How can you determine if a node has a coin to pick up
I need some help finding out how I can determine if a neighboring node, or tile I think, has a coin to pick up, any good suggestions?""",
    """Average Coins/Bonuses?
I finally having a working and optimized code, but my score is quite a bit lower than those posted on Piazza. I manage to collect coins quite efficiently, but I often miss the bonus from the find phase. So I'm wondering: should our program be such that we always get a bonus from the find phase?""",
    """"Reasonably High Score"
Our program isn't as optimized as some of our peers (for the seed on @2017, we only got around a score of around 49000). Can we get an idea of what score will achieve an "A" level program?""",
    """Problem with graph.Node vs. game.Node
I'm having some trouble with converting graph.Node to game.Node. @2074 says to convert everything to game.Node, but it just seems to create endless errors within both Paths and Heaps. Is there something I can do to fix them?""",
    """What is the max number of lines of code for a function?
will we get points deducted for having a long function?""",
    """Tiles and Nodes
I am a little confused on this point. Is it correct that all nodes have a tile connected to them, but not all tiles are connected to a node?""",
    """"eclipse
Eclipse won't let me open the zipped file... it won't let me open any file actually... and I don't know why.. did anyone else have this issue?""",
    """When will Final Review be posted
And also will there be review sessions for final?""",
    """How to run flee on the same graph?
same as topic, I'm not sure how to find if my optimized flee is better than the original one.""",
    """Creating nodes
in creating nodes during the find phase,  we want to know what tile we’re on to construct it.

But we can’t do that without knowing our tile, given the constructor- how can we construct an accessible data structure to use for our search?""",
    """moveTo Error during flee phase
Hello,

I'm trying to optimize the flee phase, but I'm encountering an IllegalArgumentException stating that the Node must be a neighbor of this Node. This occurs when the amount of remaining steps < the shortest path distance from the current node to the exit, which is my signal to exit my coin search and head for the sewer exit. The error is happening at the line after the recursive calls in the DFS, where we move back to the current node, but I had a similar procedure in my find DFS that did not error like this.""",
    """Failure on One Map?
My code works for every map except for seed 7691522310995151633, on which is runs out of steps before returning. I can't find an error, and I have no idea why it would be failing for only one out of 100 maps.What could be causing this?""",
    """Doesn't return once DiverMin reaches exit.
I had my simple implementation working and I did not need to return when I reached the exit. Now with my coin grabbing algorithm when it reaches the exit it does not return. I shouldn't have to do anything else once the exit is reached right?""",
    """marking a location visited
When implemented dfs walk, I know that we want to mark a tile visited, to reference that later.. I know that when implementing dfs before, we've used a stack... can I use that here? or should I look into using a different data structure?""",
    """Coin Values
How many different types of coin values are there? We are creating a list with one of each type of coin value and were wondering if there was a way to know how many different types there were for initializing the size of the list.""",
    """confused with "steps left"
It seems that each tile/node subtracts a different amount of steps from the steps left. Is there a way to calculate the amount of steps that would be lost if we move from one node to another without actually moving to that node?""",
    """Help with troubleshooting
I'm trying to troubleshoot my find method and I've recognized that when I print out node values of my neighbors they aren't exactly the ID's of my neighbors when I click on them in the GUI (even when I plug the ID's through a hexadecimal -> decimal converter). Is there some hashfunction or something that I'm missing that would help me with troubleshooting?""",
    """Find Ring method return to the initial tile if failed
In the handout, it says if a dfs walk doesn't return the ring, it should move back to the initial tile. Should this be done within the dfs walk method or the method calling the dfs? I don't really get the point why we need to come back. Any hints?""",
    """problem with seeds for testing
I'm not sure I'm getting the correct map when I run the program with a seed as an argument. For example, when using the seed that should give a map without coins, I'm still getting a map with coins. What could be the issue?""",
    """neighbors() clarification
Does the neighbors() method in FindState always return a collection of between 1 and 4 NodeStatus objects, depending on how many walls the currentNode is surrounded by?""",
    """Course evals
Have course eval "grades" been factored into the weighted grade on CMS yet?""",
    """How to access the neighbors in Flee
How can we access the neighbors of the current node in the flee state.""",
    """assignment 7
So Im now passing my data structure through my helper function so that I am keeping track of the visited nodes when I recursively call on the neighbors of a tile....

Currently I am keeping track of visited nodes with a hashset... but ik others aren't doing this... can someone explain why not to do this/why this is a bad idea?""",
    """checking distance
I have a base case that checks if distance to is 0 and then I return if this is true.. shouldn't this end the search once I find the ring? This isn't the case though and I don't know why.""",
    """a7 worth
what percent of our grade is a7 worth??""",
    """solutions for some years do not exist
Some of the given final exams, S18 F17 F16 S16, do not have solutions. Is the solution going to be post recently or there are just no solutions exist for these years?""",
    """Paths
When calling shortest path in the flee phase... I am confused on how I can actually iterate over these nodes and move along the shortest path""",
    """add method in Heap
Can we add new methods, additional to the 8 method we've already written before, in Heap?""",
    """for each
in a collection is there any way to compare to the item that follows it/ before it?

I know that collections don't have indices so I need to convert to some sort of structure? like an array... but the method toArray keeps giving me an error because the array isnt a NodeStatus array""",
    """GameState.java not working
If our code works fast when running GUI, but the GameState.java file is not working, will we be penalized? 

If yes, how much point deduction will we get?""",
    """Accessing neighbors from FleeState
Can we access the current node's immediately neighbors (as a list, etc) from FleeState?""",
    """creating path (List) with given path length
Dijkstra's creates a list of nodes (path) and while making the list, we can keep track of the shortest path length. 

Is it possible to create a path with a given path length??""",
    """Average Scores
May we know what average game score corresponding to what a7 grades?""",
    """Time for program
Does the 12-13 s requirement apply for running with GUI or without? When running with GUI that's slower""",
    """recursive call for flee(FleeState state)
are we allowed to use recursive call for flee?""",
    """Can we import game.tile in Path.java ?""",
    """Greedy Find
I'm working on implementing a greedy find method that goes to the closest neighbor to the ring at every step, however, we come across the case where Min goes back and forth between two adjacent tiles that are equidistant from the ring indefinitely. Any suggestions as to how to fix this issue?""",
    """Seed Score VS average score
Is it better to have a better score on the seed on the leaderboard and slightly lower average (-1000) or a worse score on the seed and a higher average (+1000)""",
    """Only moving once you know where the ring is
Do we have to move as we search or can we run shortest path algorithm in the background and then move straight to the ring after that is done? So are we allowed to use class Node and Tile in the find phase.""",
    """Coin Value
Can we use knowledge of the coin values on each tile to determine the path we take?""",
    """Recursion Trouble
So when I find the ring I return from a recursive call from a dfs method. The problem is all the other calls to dfs are still running and don't know to stop leading to problems. Is there a way to return from all the calls to the specified method that are currently in progress?""",
    """what is Java's Reflection mechanism?""",
    """Do coins have different values?
Do the different coins have different values, and if so, how can i get the value of the coin on a particular node?""",
    """state.neighbor
Does state.neighbor give you a collection of nodes that you cannot walk to? Or does it only give you a collection of nodes that you can walk to. If it gives you a collection of nodes including one's that you can't walk to (like a wall), how do we distinguish that?""",
    """exit node neighbors
Will the exit node in the flee phase always have only one neighbor or is it possible for it to have multiple neighbors?""",
    """Sorting neighbors in increasing distance to ring
In trying to optimize find(), I'm having trouble sorting the neighbors of a node by their distance to the ring. I tried adding all the nodes to a minHeap with their distance as their priorities but then realized that I can't iterate over a Heap.

And for PriorityQueue, I don't know how to pass a comparator as an argument to make sure that the nodes are ordered in increasing distance to the ring. Had the same issue with ArrayList.

How can I create a list of sorted neighbors that I can iterate over for my dfs?""",
    """modified shortest path algorithm
Hi

I'm trying to write a modified shortest path algorithm that gives you the shortest path but without using one specific edge from the start node. Basically I want it to give me the shortest path that I would've found assuming the graph didn't contain the edge between the source node and the specific neighbor I want to exclude. Could someone please give me some advice on how I might modify the existing shortest path algorithm?""",
    """Putting netID in DiverMin.Java
I don't see a spot for our netid's in DiverMin.Java. Am I missing something or do we not need to put our netid's at the top of the document?""",
    """Can we use concurrency in A7?
Say I want to calculate more optimal paths and compare only than only running through one coin collecting path. Can I implement concurrency to make this run quicker?""",
    """grading a7
How is a7 going to be graded? Is the program going to be run on certain/all seeds and how many times is it going to be run? Are instructors going to run just -s or just -n on certain seeds/certain number of runs? What should we be prioritizing when running the program?""",
    """Time requirements Not met
I have an optimized solution for a7 but it takes more than 10 seconds for it to run 100 tests. Should I try to use another solution or is it fine. 

Thanks.""",
    """How to use stepsLeft() if trying to find optimal path
If I am trying to find an optimal path, I cannot move unless I have the entire path returned as a List. But then I cannot use stepsLeft() while constructing this path, as the diver is not moving. I'm really confused on what to do.""",
    """Are we allowed to use Max Heaps for a7?""",
    """Time Requirements
Is the 10-12 seconds per map for running in GUI or in GameState?""",
    """Professor Gries' Last Class
I heard from someone that Tuesday's class was gonna be Professor Gries' last class ever. Is that true? :( """,
    """Headless Mode Taking 84 seconds to run
Hi,

My partner and I are getting really good scores for the A7 assignement. However, in the headless mode, it's taking us 1 minute and 30 seconds to run all 100 maps - which I think is significantly longer than the time required.

Is there any reason why this would be the case? Also, is it possible that it's because my laptop might just be slower?

Thanks!""",
    """submitting A7
When trying to zip package student in eclipse, the zipped folder contains a java project folder, then a src folder, then a student folder. I can't find a way to zip just package student rather than also zipping the directories that lead to student. Has anyone found a way to zip it this way?""",
    """Failure on one map size?
We ran the whole game 500 times, and we ran out of steps 3 times. The map size ranged from 6x6 to 39x39. What could be causing this error?""",
    """a7 submission question
Should the zip file contain .java files or should it contain a folder named student that contains those same .java files?""",
    """time
So currently I have (what I think is) the best way to the highest coin count as possible in a given number of steps, but because I'm doing so many calculations, it takes to long (im over 15 seconds to calculate 100 runs which I'm pretty sure is too long for the time were trying to hit)... is there anyway in java to have it do something after running for a certain amount of time...""",
    """Shortest path with same first and last node
what does calling Paths.shortest(end,end) return? An empty List, or a list with just one element?""",
    """How do we see the time taken in headless mode?
How do we see the time taken to run a map in headless mode?""",
    """edge.length()
Does edge.length() basically return the number of steps needed to move from one node to another?""",
    """Does the average score when running 100 times count 0s for flees that ran out of steps?
As question states""",
    """Keeping Unused Helpers in My Code
If I have written a few helper methods to try out different ways to optimize the algorithm and decided to call only the most efficient one, should I still leave the definitions of the other methods in my code for future reference and/or for grading purposes? What is the more professional approach here?""",
    """Will the exit be returned within method allNodes()?""",
    """how to run the program for 100 times?
to get a total time""",
    """submitting a7 with errors
Our find phase works and is optimized, and we implemented the shortest path algorithm for the flee phase. we worked on optimizing it, and it works on most maps, but there is one out of 100 maps in which our optimization runs out of nodes. would it be better to submit just the shortest path that works every time or the optimized flee that works almost all of the time?""",
    """Inefficiency in Finding All Shortest Paths
My optimization of flee involves traversing through the nodes that hold coins by prioritizing the coin that is closest to Min's current location.

In order to do this, I have implemented a new version of the shortest path algorithm that returns a HashMap holding a shortest path to all nodes, as suggested in the handout.

I then call this method in DiverMin in the helper method getClosestCoin that returns the node with the coin currently closest to Min.

I have to call this method each time Min moves to that node to collect the closest and wants to look for a new coin.

This requires me to calculate all the shortest paths to all the nodes each time Min grabs a new coin, causing my algorithm to be inefficient and the runtime fairly slow (around 35-60 seconds for 100 maps).

How can I make my code more efficient?""",
    """Test randomly stopping
Im running tests in GameState 100 times in one go, and usually the test finishes fine but every 500 or so tests the test just stops. No error message comes up, it just stops mid test and doesn't continue. The last thing it ends on is a print message of the seed for the test and doesn't complete the remaining tests and doesn't show the average. Is this happening to anyone else?""",
    """What is a grace period?
Do we lose points if we submit during the grace period?""",
    """diver gets stuck during flee.
Our diver gets stuck and keeps going back and forth between two nodes until moving a few steps and ultimately giving us an error. We don't know how to fix this. Please help!""",
    """How important are a7 specifications?
Are there any points deducted for poor/no specifications on any method? Do we have to write specifications for everything we add? Are there any extra points for good specifications?""",
    """flee fails
Our code optimizing flee and find seems to work every time on 1000 runs except for 1 or 2 runs where Min does not flee in the prescribed number of steps.  It has raised our avg score by a couple thousand over these 1000 runs.  Would it be better to have this optimized code, or the code that flees 1000/1000 times instead of 998/1000?""",
    """commented methods, specs
My partner and I created a lot of different methods in an attempt to optimize flee but ended up commenting them out and not using them. Is it okay if we leave them in our file submission? also for helper methods that we created, how specific do the specifications need to be, we are not sure how much detail is enough or if we dont need a lot of detail?""",
    """coins() in class Tile
Does the coins() function in class Tile update automatically if the coin is picked up? Thank you""",
    """unused code
Is it okay to leave unused code in the file? (Mainly all the various algorithm attempts that were worse than what I finally decided to use)""",
    """Is the grading cases randomly generated?
Sometimes errors occur in 1/4~5000 maps for random reasons, will the grading test cases be large enough so that it cover all edge cases? Though it is somewhat possible to reduce the speed of the algorithm to 10~12 seconds if someone want to avoid the 1 out of 1000 chance to get caught.""",
    """grade estimates
is there an estimated date for when our approximate course grades will be released? (so that we can figure out if we need to take the final or not)""",
    """Final grades for class
I checked my final grades on Piazza and I saw that my final grade is one standard deviation below the mean. What letter grade would this correspond to?""",
    """Final
Will taking the final most likely raise or lower my grade based on past history?""",
    """Plus and Minus
I’m confused, does your final grade reflect plus and minus as well?""",
    """Why are course grades called tentative if they will remain the same?
If we accept the tentative course grade, it IS our course grade. Why is it then called tentative?""",
    """Final Grade
Is there any good way to approximate our letter grade within the range (whether it’s A- or A or A+) because taking the final depends on even half the letter grade. Also, while approximating can we assume that the cutoff for each half grade is a hard boundary e.g. 88% is A-, A is 90% etc? Thank you""",
    """Final grade affect
Is it fair to say that if you get a better score on the final than your average your final grade (as a percent) will improve?""",
    """a7 optimal solution
I was just wondering what the optimal solution to a7 was, like proximity to coins, coin value, etc?""",
    """S/U Scores
Can students who took the course S/U know their calculated letter grade out of curiosity?""",
    """Grades
What will be the cutoff for a B-? only median scores were shown and my grade is awkwardly in between two grades.""",
    """Consultant Grade
What is the recommended grade for people applying to be CS 2110 consultants? If I am below that grade, should I take the final?""",
    """Past Final Exams Missing Answer
I found that most of the practice final exams on course website have no answer, how can we deal with that?""",
    """Stuck between B+ and A-, should I take the final?
I'm stuck between B+ and A-. Should I take the final? Is it possible to raise your grade to an A?""",
    """2015fall

I'm confused with this question.
If synchronized means that only one thread can run this method at once, then what is the meaning of using wait? How could several threads run the shared method and be in a queue?""",
    """Final S17 Question 2c


I don't see why the third line in the solution is necessary. 

seen.add(p);
I understand that you want to exclude Person p's own pics, but pics are being gathered from people in the Set p.pals which should not include p anyway. 

I don't see why it would be reasonable to assume that a Person contains itself in its own Set of pals, which is the only situation that would necessitate that line.  No technical information was given on how the Set pals was actually populated, leaving us with nothing more than a common-sense definition.  I have never before seen a person included in his own list of friends.""",
    """Thanks for the great semester!""",
    """Practice Final Exam Solutions
Would it be possible to have the solutions a couple more of the past final exams? They don't even have to have explanations - just the answers themselves. If not, I completely understand.""",
    """Answer key for last fall
According to the piazza post, answer key for last fall would be up during this week. When should we be expecting to see the key?""",
    """Questions regarding binary tree
In a true and false question, the statement below is false.

The expected time complexity to search for a value in a binary tree is O(log n), assuming n is the number of nodes in the tree. 

The answer key explains it as "There is no ordering of values in a binary tree."

However, I do not really understand this explanation.  I thought the complexity to search in a binary tree is O(n) since we need to go over every node to find the matching one.""",
    """Worst Case Time of Prepending an Element to an Array List?
What is the worst case time of prepending an element to an array list?""",
    """sp17


I'm very confused with the first question, I can not understand the answer. I though the answer should be b[2] or something like that, since b[1] is 'b'.""",
    """Fall 2018 Practice Final, question 5
Do abstract methods which implement interfaces not need to include the methods specified by the interface? Why can method SUNY in question 5 not implement method graduateStudents() in interface Univ without causing a compile error?""",
    """Review Session Slide?
Will the slides of final review be posted? Thanks""",
    """CMS Accept Course Grade Quiz
If you submit the quiz and accept your course grade, would it still be possible to decide to take the exam on Saturday to count towards your grade? Or is the quiz absolutely final?""",
    """Finals Coding Questions
The third page of the finals overview PDF has a set of code for the different sorting algorithms, dfs, and bfs. 

Is this the level at which we should know how to code the answers on the exam (pseudocode), or are we supposed to how to write the code accurately in Java? For example, the code for insertion sort on the review sheet simply has the line 'Push b[i] down its sorted position in b[h..i]'. 

So, overall, is the Final review sheet an accurate representation of good answers for coding questions on sorting/dfs/bfs on the final exam?""",
    """compareTo
Does compareTo return -1,0,1 or the difference between the two objects?

For example if I had a = 10, b = 8, would a.compareTo(b) return 1 or 2?""",
    """Where Can We Find the Expected and Worst Case Run Times for the Collection Frameworks?
The final exam study guide says you need to know the expected and worst case run time for various methods in the Java Collections Framework. I couldn't really find the answer in the powerpoints or from a decent source online. Would it be possible for you to help me find a resource so I can learn this information?""",
    """sp18


I'm very confused with the answer. For the first part, is 222 counted as ascending? And for the last part, if the function is defined as the answer, then all the test cases should be evaluated to true, while the second one is assert(false, function). How could this pass the test?""",
    """What would happen if you tried to insert a duplicate into a BST?
In a binary search tree, the children must be strictly less than/ greater than the parent. So if we were trying to implement a BST, how would we account for duplicates? Throw an exception?""",
    """What has historically been the mean for final exams?
Are they similar to the means to the prelims? I know the final is curved differently because not everyone is taking it, but I'm curious to see how I'm doing on the practice finals compared to the average scores on the practice finals.""",
    """fall18


I am very confused with the class ArrayQueue on the right. I do not understand what int h is for, and also what does it mean that all indexes mod b.length? aren't those indexes just h+n-1?""",
    """red-black trees?
is it safe to assume these won't show up on the final? i'm pretty sure they aren't on the review pdf, but they've shown up before on previous exams and i just wanted to check.""",
    """Question 2h, fa2018 Final


Can someone explain why it doesn't print b? And why it prints 98? Thanks.""",
    """SP18 Q5a


For first error, it says the constructor calls super(). Does that mean constructor for subclass would automatically calls super()?""",
    """Abstract Data Type vs Class
An ADT is defined as a set of values together with (primitive, or predefined) operations on them, according to the final study guide. This definition sounds very similar to a class. Are all ADT's classes, but not all classes are ADT's?""",
    """fa17 1.d
Why is this O(n^2)? I originally thought it was but while reviewing I researched and found that charAt is linear time. Doesn't this make this O(n) since there is only one loop? Thanks.""",
    """Why this is true?
The try-catch block can be used to handle both Errors and Exceptions. True.

I think we shouldn't catch errors?""",
    """What does register mean?
for example, Threads store x, which is 5, in different registers""",
    """Missing answer for sp 18?
The answer for sp 18 is not complete. Do someone have answer for 3(e)(f)? Thanks""",
    """Fall 2018 Recursion problem
I can't post a photo or else I would... but for the recursion question the answer key has the line:
if (y < yrBorn) return false;

shouldn't it be if (y>yrBorn) return false; because we have a root of a child and it says that the child must be older than the parent... meaning if y was greater than the child's age, y couldn't possibly be the age of any of the parents or grandparents etc...""",
    """hasnext, fall 2018 final question 4
can someone please explain why for the method next() the answer is k=k+1; and then return b[k-1]... if we are setting k to the index of the next value; why would we return b[k-1]?""",
    """spring 2018 final question 1b
the answer for 1bi says that if the digits of i are in ascending order, that the function mystery(int i) will pass the test cases... but the third assert equals statement says that 222 will be true.. & that's not ascending??""",
    """Fall 2017 Practice Prelim Question 4.b.ii
This question asks what the average runtime complexity is of outputting the keys of a TreeMap in ascending order is. The answer key says O(log n). I recognize that this requires an inorder traversal of the tree. But since I need to visit every node of the tree, won't this be O(n)? In general, aren't the expected times of all tree traversals O(n) since they require visiting every node?""",
    """Question about errors
Lets say I have a Class Animal and Class Cat that is a subclass of class Animal. Let's say I said Animal animal = new Animal(); and Cat cat = new Cat();

From my understanding, I can say animal = (animal) cat, because cat is a subclass. 

I cannot say cat = (cat) animal because cat cannot store an animal object.

Is that correct? If it's not, can someone explain why. If it is, what kind of error would it result in; a compile-time exception?""",
    """The final is in Barton Hall?
Where do we go for the final, is it in the main area of Barton Hall, or somewhere else? I'm confused because Barton Hall is a gymnasium.""",
    """Will the final be posted on Gradescope?
... and if so, when should we expect it to be posted? Thanks!""",
    """Do final grades on CMS include +/-?
If CMS says that my final grade is a B, does that mean that it's actually a B, or could it be a B+ or B-?"""
]
