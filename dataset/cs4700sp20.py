data = [
    """Gradescope Issues
I tried to add 4700 to my Gradescope classes using the code shown in class, but it seems the code enrolled me into the Fall '19 session of the class. Am I doing something wrong?""",
    """Textbook Link
I tried using the link to the textbook on the course website but it doesn't seem to be working. Anyone else having this issue?""",
    """Question about Overleaf template
I tried to click the link of Overleaf template in the hw pdf but it shows that page cannot be found.""",
    """HW1 revised to correct some typos
Some typographic issues got introduced when the file was put into Overleaf. They've now been fixed and have been uploaded onto the website.""",
    """Clarification of ⊢ meaning
Problem 5 of the homework asks you to say whether False ⊢ True. I'm wondering if the ⊢ thing (both in this subquestion and throughout problem 5) is used here to mean "there exists a proof tree for False ⊢ True" or more generic entailment, like "every interpretation satisfying False also satisfies True"; maybe I'm misunderstanding the question but I feel like assuming either of those interpretations might change my answer. If it's meant in the sense of "there is a proof tree for this," should we assume we're using the meta-logic system that was taught in 2800, or does it not matter? """,
    """textbook comments should just be typos
I just learned that the draft copy that we're using is the one that's just about going to the publishers.  That's good for this semester's 4700 - you don't have to deal with as rough a draft as has previously been the case.  That means the only feedback that you give through the 4700 website that makes sense at this time are typos.""",
    """full info on Tuesday's Karma Lecture
The information about the first Karma Lecture speaker hasn't been posted on the CS colloquium website yet, so here it is for those who might be interested:

The Principal-Agent Value Alignment Problem in Artificial Intelligence

Dylan Hadfield-Menell

UC Berkeley

Tuesday, January 28, 2020

11:40am - 12:40pm

Gates G01

Much of our success in artificial intelligence stems from the adoption of a simple paradigm: specify an objective or goal, and then use optimization algorithms to identify a behavior (or predictor) that optimally achieves this goal. This has been true since the early days of AI (e.g., search algorithms such as A* that aim to find the optimal path to a goal state), and this paradigm is common to AI, statistics, control theory, operations research, and economics. Loosely speaking, the field has evaluated the intelligence of an AI system by how efficiently and effectively it optimizes for _its_ objective. This talk will provide an overview of my thesis work, which proposes and explores the consequences of a simple, but consequential, shift in perspective: we should measure the intelligence of an AI system by its ability to optimize for _our_ objectives.

 

In an ideal world, these measurements would be the same -- all we have to do is write down the correct objective! This is easier said than done: misalignment between the behavior a system designer actually wants and the behavior incentivized by the reward or loss functions they specify is routine, it is commonly observed in a wide variety of practical applications, and fundamental, as a consequence of limited human cognitive capacity. This talk will build up a formal model of this value alignment problem as a cooperative human-robot interaction: an assistance game of partial information between a human principal and an autonomous agent. It will begin with a discussion of a simple instantiation of this game where the human designer takes one action, write down a proxy objective, and the robot attempts to optimize for the true objective by treating the observed proxy as evidence about the intended goal. Next, I will generalize this model to introduce Cooperative Inverse Reinforcement Learning, a general and formal model of this assistance game, and discuss the design of efficient algorithms to solve it. The talk will conclude with a discussion of directions for further research including applications to content recommendation and home robotics, the development of reliable and robust design environments for AI objectives, and the theoretical study of AI regulation by society as a value alignment problem with multiple human principals.""",
    """Notation for questions 5E
In figuring out whether is satisfiable, I'm confused about what the symbol means. If I'm remembering right,  the symbol is like the if/then relationship, and can be evaluated in a particular interpretation, but I thought that the symbol was a statement about a relationship across all interpretations, sort of like ⊨? Only I thought that "satisfiability" was a question of whether there exists a particular interpretation where a given proposition evaluates to true, so how do we reason about satisfiability when the proposition is making a statement about the relationship of A and B across all interpretations? Or, is that question asking, can there be an interpretation satisfying A∨B given that the A→B relation doesn't necessarily hold across all interpretations?""",
    """Course Schedule with Textbook Reading
Could the course schedule that lists the lecture topics and associated textbook readings be posted in advance of the actual date? I would greatly appreciate it so that I can get ahead with readings and have an idea of what we are learning before entering class. """,
    """lecture 2 slides updated
Just FYI, I've updated the slides for Friday's lecture to provide a bit more detail on the missionaries and cannibals formulation that I zipped through at the end of the lecture.""",
    """Jupyter Notebooks Primer Session
Prof. Hirsh mentioned that there would be a Jupyter notebooks primer session. Does anyone know when it's gonna happen? I know the professor said the date would be mentioned on the site but i don't know where on the site to look.""",
    """HW 1
How much detail should I give in my responses for this homework? For example, for Question 5 do I need to justify my answers?""",
    """"Give exact formula" in Question 4?
Not really sure what the stipulation "Give the exact formula" entails for question 4. I feel like the answer is pretty straight forward and isn't really contained in a "formula".""",
    """Lecture 3 slides
Could the slides from today's lecture please be posted? Thank you!""",
    """Piazza authentication
Basically, I have to re-login every minute to use Piazza.

When I click on piazza questions in the list on the left to view them, I get a popup saying: "This site says... please authenticate", and the question doesn't open.  

I can refresh the page, which redirects me to the Piazza login.  After logging in, I can use Piazza for about a minute before the "please authenticate" nonsense resumes.  At this point, I can refresh and login again, and the cycle continues.

I have used Piazza for other classes in the past on the same computer with the same web browser without this issue.

If anyone experiences or knows of this issue, please let me know!""",
    """HW1 Question 3d
It asks for the depth-first traversal order, but there are three possible ways to traverse a binary tree depth first(preorder, inorder, and postorder). Since we've already been asked about inorder and postorder traversal, I assume this question asks for the preorder traversal order?""",
    """median grade
What is the median grade for this course?""",
    """Jupyter Primer (now includes presentation!): Friday 2/14 at 5pm in Gates G01
How to View The Presentation:

1. Download Jupyter_Intro.ipynb

2. Download iris.csv

3. Go to https://colab.research.google.com/notebooks/intro.ipynb#recent=true, click 'Upload', and upload the downloaded file. Voilà!

There will be Jupyter notebooks primer lesson starting at 5pm in Gates G01 on Friday 2/14 (this is the rescheduled time!); it will take less than an hour.

If you haven't encountered Jupyter before, this primer will help you with the programming assignments throughout the semester.

----------MORE DETAILS------------------------------

We’ll be introducing Google Colab, an online Jupyter Notebook environment with cool features like:

No issues with Python installation
Saving to Google drive, great backups, and good version control
Access to Google’s GPUs (!)
Easter eggs?
We’ll also present some important Python libraries/concepts that may make the programming assignments easier, and are generally good to know.
Bring your laptop!
If you’re already familiar with Jupyter notebooks, feel free to come and explore Colab/Python!""",
    """Problem 1 B
For this probability problem, I got very closed expected value of money for both player and cannot show a significant difference in scale of 100. In other word, in scale of 100, both player will have the same amount of money remaining. May I know if that is expected, please?""",
    """Can we submit Hw1 solution as scanned written pdf?""",
    """Does Hw1 count towards our grade for the course?""",
    """Question 5C
The expression for 5C on the homework pdf is:

However, on the overleaf template, the expression for 5C is:

I was wondering which format of the question is correct.""",
    """hw1 2A
In 2A, are x and x bar referring to the same thing? If not, f(x) is not even about x. 

Thanks!""",
    """hw1 problem 4c definition of number of comparisons
Should number of comparisons be the number of elements that need to be compared to or the actual number of comparisons that need to take place? Currently having the debate about this because in an actual Java implementation you might compare a number to see if it's equal to the one to check for and if it's not then see if it is less than in order to decide between traversing the rest of the left or right side of the tree. Whereas in OCaml, you could use a single comparison that results in a GT, LT, or EQ output that could then be matched against, so that it would be only one comparison operation.""",
    """Necklace left at Office Hours
A necklace was found at office hours today. If you think it might be yours, please email me at and I can return it to you.""",
    """Question of 4C
How can we give an exact formula when all we know is that the tree is balanced. Can we assume that it is balanced to the point that the depth h = log(n). Red black trees are considered balanced as well but don't have that height necessarily. Or should we just introduce a variable h and do it in terms of that?""",
    """Question 5 notation
I have seen other questions on this and have looked at the answers, but I am confused on the difference between |= and ->.

They seem to mean the exact same thing. Is that the case or am I missing something?""",
    """Problem 1A on Homework 1
For the random variable, should I be considering a continuous or discrete distribution?""",
    """Hw1 2A
I'm not sure what does the wi refer to in the partial derivative. Does that mean we are taking teh derivative for every w component in the w_bar vector, or we only take the partial derivative of one specific wi(i.e., i refer to a number, like 0).""",
    """HW1 Grades & 2800 coverage of logic
I learned today that 2800 didn't cover logic last semester (even though it's supposed to be).  As a result I will be computing your grade on HW1 both with and without question 5 and give you the higher of the two.  (Gradescope will show your grade including question 5.  We will be computing the max offline so you won't see it online.)""",
    """HW1 Question 1 different on template
I'm not sure if I'm missing something, but I haven't seen anyone else ask about this.

As of right now, this is the PDF linked to on the CS4700 course page:

This gives Problem 1 as being on "Probability", with 3 parts worth 5 points each.

However, the Overleaf template linked in the PDF, which was also linked here on Piazza in another post, has Problem 1 as being on "Hill Climbing" and is a single question worth 15 points.

Which "Question 1" should we answer? The PDF, or the Overleaf template?""",
    """Exam Conflicts
Where do we submit our notifications for exam conflicts?

Thanks!""",
    """Course Schedule Readings
Are the readings listed for each lecture supposed to go with that lecture or the next lecture? It seems like the material covered in the last two lectures or so is a day behind the listed reading sections.""",
    """Auditing this course
I wanted to know if I can audit the course. I could see that it is written there's no official auditing for this course. But I was able to see enrollment was open for auditing this course. I have a huge workload and want to learn about AI as well. I wanted to know what I should do.""",
    """Rescheduling Professor Office Hours
Professor Hirsh's office hours today are cancelled and will need to be rescheduled.""",
    """Homework Solutions
I was wondering if there will be solutions for any homework problems in this class?""",
    """HW1 Grades Released + HW2 Released
Homework 1 has been graded and grades are now available on Gradescope. Regrade requests will be open until Monday 2/10/20 at 2:15 PM. The grade that you see on Gradescope does not account for possible grade adjustments for the logic section. Attached below are some statistics and the distribution for HW1.

Additionally, Homework 2 has been released on the course website and is due on Monday 2/17/20 at 11:59 PM. Late submissions will be accepted up to 48 hours late for a 50% deduction.

Friendly reminder, please do not submit any handwritten assignments. Any hand written submissions will receive no credit :(""",
    """HW 1 1A solution - standard deviation of X
I have simplified the solution answer to the std dev of X this way: 



Is this wrong because we are considering the interval FROM a TO b?""",
    """Hw1 Q2 A Solution
Would it be possible to upload the detailed solution for Hw1 Q2 A as well ?""",
    """HW2 Q3 Clarification
For 3a, can (3,1) be swapped around? For 3b, can (8,6) swap with (3,1)? For 3c, what is the starting city point and can it be swapped around by the hill climbing operator? """,
    """HW2 Q2––how to handle cycles?
I got a lot of questions about this in office hours, and the instructor's answer here clarifies a bunch:

In drawing our expanded graph, how should we handle cycles? For example, starting with the initial state we can move 9 to the left and then back to the right. In this situation should we draw the initial state node again as a child of the state with 9 shifted to the left, or just draw an arrow pointing back to the initial state node? Should we draw these cycles at all?""",
    """HW 2 Overleaf Template
For some reason the HW 2 overleaf template isnt properly formatted for me.

Even though I have just made a direct copy of the original template through overleaf, and the original template does have proper formatting when viewed through the Overleaf editor. Does anyone know how I might resolve this?""",
    """HW2 Q3C do we need to draw out all possible states?
So, the left R value must be positive as the optimal solution has least number of crossings. And the right R value must be negative as the optimal solution has most number of crossings. But do I need to find exact bound values? Like for example, using the hill climbing operator the left state can be transformed to a state hypothetically where there are 4 crossings but the loop length is much less than the current optimal solution loop length which means that R value must be calculated. For example in the solution say f = 28+2R. Then there can be a state where f = 10+4R. Hence R value will need to be calculated; so do I need to consider all possible states that can be formed from hill climbing operator?""",
    """2/5 updated lecture slides
Could the last few slides from yesterday's lecture please be posted? Right now they're missing from the presentation that's already uploaded on the course website. Thank you!""",
    """Class, Jupyter Session & Office Hours Cancelled Today
Class and office hours are cancelled today. Saturday office hours remain scheduled for now.

Jupyter primer session tonight also cancelled. It will be rescheduled for sometime next week; we are waiting on room availability.""",
    """HW2 Q1B Heuristic Function
Is there any particular reason that there is no h(s) for the initial state? Given that we know h(T)=0, is the initial state forbidden from having a value, or does it just not matter for the question?""",
    """HW2 Q3C City Locations
Are the city locations in the two paths of 3C meant to be the same as those at the beginning of problem 3? They're all the same except the paths of 3C have a city at (6,4) while the original has a city at (6,5).""",
    """Q2 DFS
When branching for DFS does it matter which order of moves we chose for the level we are at? Or should we try to follow some order like left, right, up, down? The question doesnt lend itself to a particular order like the examples given in class and in the book.""",
    """Difference in space requirements of DFS vs BFS
Hello. I remember Prof Hirsch going somewhat into depth about the memory requirements of DFS vs BFS (O(bm) vs O(b^d), respectively), but now I'm reviewing the material and am having trouble conceptualizing why this is the case. Can someone reiterate it?

My current understanding is that for BFS, we traverse by levels at a time, adding the levels and all of their successors into memory before we continue. This means we add b things per level up to level d, so b^d. My trouble is with explaining the complexity of DFS.""",
    """Do we have slip days ?
Do we have slip days for homework?""",
    """Rescheduled Jupyter Primer Session
The cancelled-due-to-snow Jupyter primer session has been rescheduled for 5pm this Friday (2/14) in Gates G01.

As a reminder, please bring your laptop to the session.

Materials will be posted for those who are unable to attend.""",
    """About hw1 regrade
For question 4C, my solution is floor(log(n))+1, where floor(log(n)) means the number of nodes except leaf node and +1 means we include the comparison for the leaf node. May I know why it is wrong, please?

Also, it has passed the regrade deadline for 15 mins, may I know if I still can regrade for this question?""",
    """Friday 2/14 replacement lecture Wed at 3:30
As I explained in class today, I won't be able to give my 4700 lecture on Friday so I'll instead give the lecture later in the afternoon this Wed and will record it so you can watch it offline. However, I misspoke in class and said the lecture would be at 2:30. It's actually at 3:30 Wed, in Gates G01.  Please come to the live lecture if you're able, so I won't be stuck lecturing to an empty room and you won't be stuck watching a recording of someone lecturing to an empty room.""",
    """Getting "Page not found error" on Overleaf template for HW 2 linked in PDF
Can someone post a link to a working version of it?""",
    """Regarding Q3c -- assume the two maps are optimal
The map on the left actually would have successors, but just assume (wrongly) the two maps are the optimal end results of two efforts of hill climbing with two different rewards. 

Edit: Also, the starting state is the given starting state in part A!

Edit: I see there are a lot of concerns with 3C. To solve this problem, it really is about satisfying the heuristic that the two new maps are more profitable than the original map. Please don't brute force!

Sorry about all the confusion surrounding this problem!""",
    """Office hours 12-1
On the office hours schedule, it says that there are office hours from 12-1 in Rhodes 408, but the TA isn't here. Are there still office hours?""",
    """Question 1b: A* cost
For question 1b, when we report the "cost" of the path found by the A* search, is cost just the addition of the weights of the edges or is it the weights+heuristic values?""",
    """HW2 Q3A clarification
Just to clarify, this question is asking how many states can be generated from this sample solution after switching only two of the cities? Not for the total number of states that this problem can have?""",
    """Question about slide
I'm confused since we didn't change the bound in any part of the algorithm, does that mean we have a fixed constant as the bound? Also, why the recursive call for the DBDFS does not include bound as a parameter?""",
    """Q2 graphs clarification
To clarify, should we keep the nodes that are in open list but not yet expanded in the graph after we first find the solution? Also, if we keep them, is it correct that we only need to label the already expanded(checked) nodes? Thanks!""",
    """Questions 1,2: Showing our work
How much work are we supposed to show for question 2? Right now, I have described the operations, their order and drawn a graph to indicate how I traverse it. And then I have shown the final goal state and drawn the table corresponding to the goal state. Is this enough work or do I need to draw every table representing every node in the my graph?

As a follow-up, what about for question 1? Do I need to show each step in executing the algorithms?""",
    """h(T) question 1
There is no entry for T in the table for the heuristic function. Can we assume it is 0, or is it that when T is added to the open list the algorithm automatically terminates?""",
    """What denotes a path
For question 1 what does "path" formally mean.

Is it the sequence of states the s argument takes in the running of the algorithm

Or is it the result of storing back pointers to the state from which each state was reached in the "optimal" way.""",
    """Question 2
Just to clarify for question 2- we draw out everything that is GENERATED but only label nodes that are EXPANDED?""",
    """Question 2 Drawing out Search Space
Do we need to draw out the whole search space (which is massive) or do we only need to do so until we hit the first goal state. 

I feel like its until we hit the first goal state, but the question says "identify the states that are goal states" which is scaring me.""",
    """Question 1 showing work
Can we just write the path obtained by the algorithm and its cost for (a) and (b). Or do we have to explicitly show each step of the algorithm. If we have to explicitly show each step of the algorithm is there a way that we should be formatting it?""",
    """Q2
For question 2A, it asks us to describe the states of the search problem. In lecture there was a similar problem where there were a series of numbered tiles with one blank space. It was discussed how this problem could be simplified by only focusing on where the blank space moved instead of the all the other tiles. Does this imply that there are only 9 states in the lecture search problem? If so, does this further suggest that the same state of a search problem could be both a goal state and not a goal state? In this example, if the blank tile were in the bottom right corner, the other tiles may or may be not arranged in a manner that yields a goal condition, but any these combinations would be considered of the same state.""",
    """Moving up from initial state - Q2
Is it possible to move up from the initial state in Q2 (resulting in 9 swapping with 5) or is this operation just not possible given this state? Thanks""",
    """Question 3 part C
For the graph on the left, shouldn't it be impossible to reach that state from hill climbing. As swapping (6, 5) and (3, 6) would clearly lead to a better result regardless of what R is. 

I also wrote a program to do the hill climbing procedure and regardless of what I set R to be I cannot generate the graph on the left.""",
    """Order of numbering Problem 2
In what order do we number the states for number 2.

In the order in which the states are traversed?

Or in the order in which they are added to the open list (order in which they are generated)?

In the case of the order in which they are traversed, should we just not number the nodes that are generated but not traversed?""",
    """Error in Notes for DBDFS
In the notes there is an error in the algorithm for DBDFS. Recursive calls don't mention the bound so the code would not compile. This is of special note for the HW because I was wondering if a node is expanded if it is at the deepest position (Expanded but not further traversed).""",
    """3A confusion
Are we supposed to answer with how many states there are in the whole search space, or how many states can be made by expanding the initial state.

Also do we count states that are a different order of vertices as different, or do we count states with distinct cycles as different, in other words are states that can be achieved by shifting considered identical? (This concern only applies if the answer is supposed to be how many are in the whole search space)""",
    """Question about the presence of cycles in HW2 Q2
I am wondering about how cycles are ever present given our search algorithm. We never visit a state that has already been visited, so why would this appear in our search space more than once?""",
    """Question 3b
For "drawing", are we supposed to draw a graph with swapping (8,6) with other vertices as an operator, or are we supposed to draw the resulting state as a path diagram like the example below?""",
    """Page not found for slides link from 2/3
In the course web, all of the lecture slides link after 2/3 is shown "page not found", but previous slide (before 2/3) can be shown.""",
    """Figures for HW Q2
Can we neatly hand draw the search space and scan into Latex for Q2? Seems like doing this in latex would take way too much time.""",
    """Do we get to drop our lowest homework grade?
I don’t think this was mentioned on the website and just wanted a clarification.""",
    """Can we use drawings for questions that do not require a diagram, but to show work?
I understand that in question 2 that we need to use a computer generated graph, but for question 1, since the question doesn't explicitly ask for a graph that returns the required paths, can we attach a picture of a drawing to show our work?""",
    """5-6 PM Office Hours Not Changed
The office hours I'm holding today (Monday, February 17) that are listed at 5-6 PM will in fact be held at 5:30-6:30 PM. There should still be a TA in the office hours room at 5 PM. Sorry for the change and the late notice! 

The professor I had a meeting with got sick so office hours will be at the regular 5-6 PM time.""",
    """Is it okay to go to only part of the karma lectures?
I want to attend these lectures but they seem to all be at the same time and I have a class 40 minutes into all of the,. Is it okay to go to just the first 30 or so minutes of these lectures and still say you attended the lecture?""",
    """Creating unlabeled nodes using the graph editor
I understand that we are supposed to label nodes in the order they are "visited", and we are supposed to include but NOT label nodes in the open list.

I have been using this graph editor linked in the assignment, but I cannot find a way to create a node without a label.  Does anyone know of a way to create unlabeled nodes using this editor, or will I have to scrap this and use a different system?

Thanks!""",
    """How should we represent F(s) in Q3 part B?
Should we leave our answers with square roots or should we approximate and round? Thanks!""",
    """Evaluating g(s) for a node with multiple paths to it
I am a bit confused about what value g(s) gives. Say we have a state A which has successors B and C. Say f(B) < f(C), so the BestFS is run on B. Say the successors of B are C and X and Z. Now in this case, does g(C) return the sum of the weight on the edges A-B-C or does it simply return the minimal sum of weights of edges from start state (A) to C (equivalent to returning the weight of edge A-C)?  

I believe in this case, weight A-B-C is returned, but if when we were at state A, f(C) had been less than f(B), then going forward this g(C) would have been recorded (A-C) and any other evaluations requiring g(C) would choose the minimum evaluation (A-C, assuming this one's less than A-B-C). Correct me if I'm wrong please.""",
    """hw 2 question 2
I realized one thing that might be causing confusion with question 2 concerning the numbering.  In the slides for Lectures 2 and 4 I numbered each node by the order in which recursive calls to the search method take place.  Thus, for example, the first call is to the root, so it gets #1.  This is not about whether its successors are generated, just simply that it's the first call to the search method.

On the other hand the homework is asking you to number nodes by the order in which they are *expanded* - when a node's successors are generated.  This is not the same numbering as was depicted in the lecture.  The question is asking you something different.""",
    """Grad School DeMystified event
For those interested:""",
    """lecture slides not loading?
Many of lecture slides links don't seem to be working. Can this be fixed. Thanks!""",
    """HW2 Grades Released
HW2 grades have now been released on gradescope. We encourage you to review your assignment and the course regrade policy. Solutions are posted on the course website.

If you believe there was a grading error in accordance with regrade policy, you may submit a regrade request through gradescope until March 2nd at 2:30pm.

Also of note for those who submitted late: grades in gradescope do not reflect the 50% late penalty, although it has been added to our grading records.

Statistics:
Maximum: 35.0
Mean: 28.55
Median: 30.0
Standard Deviation: 5.8""",
    """Office Hours Over Break
There will be a handful of office hours held over break, please check the course calendar. If you are around, this is a great time to ask any questions about course material!""",
    """Question 3C solutions
The solutions only give the values for R_l and R_r. How were these calculated?""",
    """HW 3 not loading
Edit: It works right away if you use safari.

I just tried to open the HW 3 pdf (in chrome) and it is not loading. Is anyone else having this issue?""",
    """HW3 Overleaf Link
To allow for a secondary access point to the assignment, the read only overleaf copy of HW3 can be found here:""",
    """Homework 3 Missing from Website
see title.

The homework was there right after class, but I looked at the website a few minutes ago, and it seems that Homework 3 has gone missing.""",
    """HW 2 3C solution explanation?
I am still very confused about this question's solution. 

I knew one must be positive and one negative, but how exactly did these numbers come out?""",
    """Unifying two different variables
Following the algorithm below, I am still confused whether unifying two different variables is legal (i.e. UNIFY(x, y) = UNIFY(f(x), f(y)) != FAIL). If so, could we write [x/y] or [y/x] either way? 

Can anyone answer this?""",
    """12pm office hours today
I'm just wondering if 12pm office hours are still happening in Rhodes 406 today? There isn't a TA in the room yet.""",
    """formulating domino tiling problem as constraint satisfaction problem
I was reading the book Artificial Intelligence: A modern approach and came across this problem that I found interesting. 

Anyone would like to kindly provide some ideas on how to work on this problem?""",
    """What counts as pruning
Question 2 of the homework asks us what relationships between a...h make no pruning possible––say we're looking at the rightmost child of a node, and it fulfills the inequality that would normally result in the parent node being pruned (like it's  a max node and this child is greater than Beta). Since it's the rightmost child, though, this doesn't actually save us any steps since we would have stopped after that child anyway. So does this count as "pruning"?""",
    """HW 3 4B - "3 people per group" to CNF?
I am having a lot of difficulties trying to encode this rule in CNF. 
Here is what I have so far, as a sum of products, where abc represents the combination of 3 in which students 0, 1, 2 are in a group. I want to convert ALL of this to CNF, yet is there an easier way to encode this problem in general? This step seems WAY too tedious and difficult to do.""",
    """User study from Prof. Snavely's lab
Two PhD students from Prof. Snavely's lab at Cornell Tech, Wenqi and Zhengqi are conducting a user study for their research project. The project is about synthesizing realistic light fields from internet photos, with potential applications in AR/VR. They are seeking participants for an online user study, which takes around 10 minutes to finish.
Please help out if you have the time, the online form is here:""",
    """Question 3 HW3 alpha/beta clarification
I just wanted to confirm how we're supposed to report values of a and b for pruned edges in the graph in question 3 of HW 3. In the code on the lecture slides, a/b values are updated after the code checks whether the current value is greater than b (at a max node) or less than a (at a min node).

If we are at some maximizing node X with children Y and Z, where the current value of b = -10 and a = −inf, and child Y is checked first and has value -5 (greater than b), then we should prune the edge X-to-Z, as I understand pruning. And the value of b should be reported as -10 in this case, since that's the value of b at the time this edge was pruned. But what should we report the value of a as? Should it be −inf, since the code returns before X can update a to the value of Y, or should it be -5, since that's what X would have updated α to be after checking Y?""",
    """Should question 4 code go in a file with all the other release code, or in its own .py file?
The .ipynb file just says to download it as a .py. Does that mean we should write all of our code in jupyter notebooks and then download the whole things as a .py file and upload that? Or should we make a new .py and only put the code relevant to question 4 in it?""",
    """Variable vs. constant notation
I was curious about the notation in this class for variables vs. constants. I'm under the impression that variables are lowercase, and constants are uppercase.

For instance, in the lecture slides UNIFY(P(x,A),P(y,B)) has x,y as variables and A,B as constants? Is this correct?""",
    """Question 2, do we need to find the minimal set of inequalities
Do we need to find the minimal set of inequalities that guarantee what the questions state in order to receive full credit?""",
    """HW 3
3 Things:

1. Should we leave in print statements? (ie. will graders be using our print statements to check if our generator is correct)

2. Just to check, 4b is creating constraints for all 7 days of a week, and 4c is creating constraints to get 10 different weeks?

3. How long do solutions generally take to execute? I timed mine to be 3 minutes, but I also don't think I can get rid of any of my constraints.""",
    """4B modeling
How do we visualize our code to check whether we are creating proper groups? Right now I'm getting a huge list of a bunch of numbers ranging from 0-1000 when I call return on get_model()""",
    """Contents of Prelim
Is it possible for us to know which topics the prelim will cover?""",
    """Ok to have Helper functions in 4b and 4c?
I am just wondering if it's ok to have helper functions outside of the functions sol_4B( ) and sol_4c( ) like how the Sudoku tutorial had different functions for each constraint? It makes the code cleaner. Thanks!""",
    """HW3 4B 840 truth values instead of 105
If my understanding is correct, I should be getting 105 truth values in 4B. However, my solution is giving me 840 truth values. I know my constraints are probably off but is there an obvious reason why this is happening?""",
    """Values of a...h containing infinities
Should we assume that a...h are finite only or can they include infinity? I am just having trouble in parts where I should evaluate something like B <= val, where val = +infinity, B = +infinity. If a...h can contain infinite numbers, then should we treat +infinity = +infinity? Thanks""",
    """Submission for hw3 python
Hi,

I am wondering for the submission of .py file, should we only include the necessary code to run sol_4B and sol_4C? And are these 2 functions supposed to be without any arguments?

Thank you!""",
    """Resolution Procedure
So when reviewing lecture slides on resolution, I encountered this slide:



Line 2 is completely ignored, and so () is reached. But why can line 2 just be ignored?? Doesn’t this result in (my v mo) rather than ()?""",
    """Resolution with disjonctions and conjunctions
How does one go about applying resolution to statements of the form
p or a1 or ... or an
not(p) or b1 or ... or bn
with a negated goal of form c1 and ... and cn
What I'm not sure about is the conjunctions""",
    """hw3 4c: what is considered "hard coding"?
The instructor answer to @133 says that any output by the SAT solver will be accepted as long as it is not hard coded. How strict is this definition of hard coding? For example, if we add a constraint that says that student 1 must be in group 3 on day 2 in every solution, would that be accepted?""",
    """Lost iPad in OH
someone left their ipad at office hours tonight.""",
    """Questions for Lecture 12 slides


I am not sure why (my^mo) is ignored in this case.""",
    """hw3 4b output format
Is there a particular format we should output our solution for the scheduling problem? Currently, I have it stored like 

day1 [[group 1], [group 2], [group 3], [group 4], [group 5]]

...

It outputs one possible solution to the problem. It also runs quite fast, so I'm confused why it doesn't take the 3 min that others have previously asked.

Also, to be clear about the problem statement: "no two shall walk twice in a group".

This means that once a pair of students (i,j) walk together, then they can't walk together on any other day or group right?""",
    """Prelim Review Session Information
Prof. Hirsh will be holding two review sessions for the prelim:

Friday, March 13th at 4:30pm in Gates G01
Monday, March 16th at 9:00am in Hollister B14
Additionally, a reminder the prelim will start promptly at 7:30pm on March 17th in Baker Lab 200.""",
    """4c How different do schedules for weeks have to be?
Is having just one group in one day in one week different from another week enough for a "different" schedule?

(While other days and groups remain similar)

When I add my print statements, it's hard to find the nuance, but the difference still exists.

Will 4c be auto graded? Or should we make it easy for TAs to spot the difference?""",
    """Online Option for prelim?
Will the virtual instruction notice today affect the prelim? Is there an online prelim option?""",
    """Time to Find Solution hw3 #4
In the homework under question 4C, the hint says that:

"If you don't get an answer for a minute, that often means your constraints are too hard"

Is this talking about solving for a single solution or all ten?""",
    """.py submission
Does our .py file need to contain all the code from the sudoku walkthrough or is it okay if we copy pasted all relevant code for the actual problem to a separate file? 

Also should each solution create a local solver instance or should there be a global solver instance. Or does it not matter.""",
    """hw 3 4C output
How should we output the groups for each day/week? Assuming that an autograder grades, i want to make sure that the formatting is correct""",
    """Q3a Clarification
Do we iterate the algorithm step by step and show the values step by step, or do we need to just show the final product (values after all steps?""",
    """Are we allowed to import modules for 4C?
I've imported the random module to help with 4C - is that allowed?""",
    """hw3_4b
How to use clause to get the number of people in a team to be >=3? Since clause is OR, I'm super confused how can we select a combination and then get the number of true elements to be >=3.""",
    """Exam and Corona Virus
I'm scared for my life for this Corona Virus and am sure a lot of students are too, and may be leaving campus early because of this. All of my other exams have switched to virtual instruction and virtual exams as precautions, and I personally do not feel safe taking this exam in person. Is it possible for an accommodation to be made for other students who are also in my situation?""",
    """HW3 - no late penalty
I've heard from a few students that Cornell's response to the COVID-19 crisis impacted their ability to effectively finish up homework 3.  As a result I'm going to waive the late penalty for submitting homework 3.  If you have already submitted the homework you will be able to resubmit if there are changes you'd like to make given the additional time.""",
    """Updated: Testing Virtual Office Hours Tonight
There will be office hours happening from 5-8pm available both in person as normal in Rhodes 405 and online. 

This is the first test of virtual office hours for us, so they will likely take longer and likely be buggy to set expectations. Please see the course schedule for the Zoom link to join office hours. Recommendations for how to engage with virtual office hours will be posted here later this afternoon.

Some procedures for virtual office hours as we test them out:

We will be using the Zoom waiting room; the TA will use their discretion to add/remove students from the video chat
We are also using authentication; you need to sign on with SSO and use your NetID login for Cornell
Please familiarize yourself with the Zoom interface before joining (Raise hands, screen sharing, etc.) and ideally download the app
Please keep your video on if possible, but mute at all times unless you are speaking (headphones help!)
Please use common sense about your attire/location/what's on your shared screen/etc. to maintain a learning environment on the call
Please be patient with your TAs: this is their first time doing this as well.""",
    """prelim prep questions
I've just uploaded a list of prep questions for the prelim.  You can find them on the course web page under the bullet for Prelim, or directly at""",
    """Concern about Performance on Midterm
The last few days have been really stressful for all of us. The upcoming days I anticipate will be worse for a lot of us. I am genuinely concerned that I will do horribly on the upcoming midterm because of everything that's going on. I am guessing at least a couple of students share the same fears. I was wondering if the grading for this midterm will be fair taking these extenuous situations into account. I think any reassurance of the fact that the staff will be accommodating of our stress will be great. Ideally, I think a lot of us would prefer not having the midterm in just a couple of days but I understand that that might not be an option. I'm just looking for any sort of assurance that we will be evaluated fairly on this midterm. Thanks!""",
    """Reschedule Prelim
How can I reschedule this prelim? I originally didn't have to reschedule it, but then the coronavirus pushed back some of my prelims from this week to next week. Now I have three prelims within 48 hours.""",
    """Course Status Update
This is the same as what was just emailed out to all students.

---------------------------------------------------------------------------

This email is going out to everyone in CS 4700.  As I mentioned in class yesterday, we're designing the airplane as we're flying it.  I am going to do my best to be responsive to the various ways this is impacting all your lives, both in terms of fears about the virus, and in terms of how the need to leave Cornell has turned your lives upside-down in so many different ways. Please bear with me as we work this out together over the next 2 months.

Here is where I'm at:

- PRELIM: I am cancelling the in-class prelim and replacing it with an online prelim.  It will still be a timed exam.  My plan is to give you a 24-hour window starting Tuesday evening in which you would take it.  I will give you further details once I have them more precisely worked out, but I wanted to give you this head's up both to reassure those who were worried about it and so you can plan accordingly.

- OFFICE HOURS: One of our TAs is doing a trial run of running office hours online.  If that works we'll roll it out for all office hours.  If you go to the course website and click through on the link to office hours each office hour will have the URL you will use as it's "location".

- LECTURES: I will be doing my usual live lecture tomorrow, but will try to simultaneously do it online.  I will send the URL for that once I have it all figured out.  This is an experiment, so I can't guarantee that I'll get it right the first time.  Best-case scenario you'll be able to watch the lecture from the classroom, watch it live online, or watch a recording.  Worst-case... I'll try to fix what didn't work and do it again on Monday.  Either way, the slides will be online as usual.

- REVIEW SESSIONS: This will depend on what happens at Friday's lecturing experiment.  If that works I'll do the Friday review session simultaneously in class and online in the same fashion.  If not, it'll just be in class.  Rather than plan for how Monday's review session will go I'll leave it hanging for now until we see what happens tomorrow.  I'll send the URL for that subsequently as well.

Finally, I know I'm unlikely to anticipate every challenge that each of you is working through with this.  If there's something I've overlooked or that doesn't line up with your own circumstances please let me know.  The best bet is to email to FAI-L@Cornell.edu and put 4700 at the start of the subject, since that makes it easier for me to see it amidst all the emails that are blasting me right now.""",
    """Sodoku 'has to be one symbol that appears in the row'
what is meant by 'has to be one symbol that appears in the row', for adding 

solver.add_clause(in_row)  ?""",
    """HW3 4B
Is it okay if my constraints don't use the propositional symbols for pairs (i, j)? I found that if I try to encode the constraint that no two students walk twice in a group using pairs, my solution doesn't terminate after a few minutes. However, if I encode it using only symbols for individual students, it takes about 20 seconds to find a solution.""",
    """3/11 lecture slides
Could the lecture slides from Wednesday please be posted? Thank you!""",
    """Values of Nodes for 3A
If we come across a node that is unvisited due to pruning, is the value of the node undefined since it is uninitialized? Or is the value of the node +/- infinity?

Similarly, if a leaf is not visited, would the value of the leaf be the numeric value assigned to it? Or would it's value be unassigned since the minimax algorithm never reached that leaf due to pruning.""",
    """Zoom info for today's lecture
I'm appending the full Zoom meeting invite below, but if you're doing it from a browser the short version is to click on.

Logistics for real-time participants:

All remote attendees will be muted by default.  Stay muted.  But you have the power to unmute.  Please be careful not to do so unless called on for a question.
If you are a remote attendee and have a question please send me a message via Zoom's chat resource.  You can do so via a private message to me within chat.  There's a chance I'll miss it if I'm looking at the in-room attendees or the board, so I'll try to acknowledge any chat messages that pop up so you'll know that I saw it.  If a little time passes and I don't acknowledge it please send another message.  (I don't know if this will be necessary - I'm trying plan ahead for contingencies.)
Logistics for offline viewers:

The video will be made available via vod.video.cornell.edu.  I'm still working on the details and will post a followup once I have that live.
I believe the logistics for the review session will be much the same, but I'll post a separate note about that once we make it through today's lecture.""",
    """Office Hours Going Forward
Office hours will be transitioning to virtual over the next two weeks. They will be cancelled over break and resume after break as all virtual. For the next two weeks, please check the course calendar to determine if office hours will be virtual or in person.

Some procedures for virtual office hours:

We will be using the Zoom waiting room; the TA will use their discretion to add/remove students from the video chat
We are also using authentication; you need to sign on with SSO (cornell.zoom.us) and use your NetID login for Cornell 
Please familiarize yourself with the Zoom interface before joining (Raise hands, screen sharing, etc.) and ideally download the app
Please keep your video on if possible, but mute at all times unless you are speaking (headphones help!)
Please use common sense about your attire/location/what's on your shared screen/etc. to maintain a learning environment on the call
Please be patient with your TAs: this is their first time doing this as well.""",
    """Prelim
Given the new updates about classes getting cancelled for 3 weeks, will we still have a take-home prelim next week?""",
    """Suggestion for remote lectures
I think it would help to record audio directly for the remote lectures with a mic pack since the audio was somewhat unclear at times during today's lecture.""",
    """COVID Update
As you've no doubt read, classes are suspended until after the spring break.  What does that mean?

- Nothing has changed with regards to HW3.  I didn't give an extension, I'm waiving the late penalty.  We're in the late submission period.
- The prelim will not happen next week.  I will reschedule it for after April 6.  I don't want to do it immediately thereafter so that people can take advantage of office hours, but I don't want it to drag on too close to finals.  There's a lot I still don't know, and the situation may morph yet again, but to help you plan for it I'm planning to aim for the latter part of the first week of classes after spring break.
- There will be no further lectures until April 6.  They will be online after that.  (I'm glad to have done a test drive today!)
- Office hours will be suspended until April 6.
- There will be no prelim review sessions today or Monday.  I will reschedule them for closer to the exam, when they'll be of more value to you.
If you have any questions or issues, please email me at FAI-L@Cornell.edu and put 4700 at the start of the subject field.
Stay healthy and be safe.""",
    """4A Issues getting Results
If I only run "link_symbols(s, varmap2)" and then solve the model, I get no positive results from model[I]. All 4200 entries are just the negative versions of themselves. What could be going on here?""",
    """Office Hours
Will today or tomorrow's office hours still be in session? I am in need of help on HW 3. I know professor just notified us that OH are suspended, and I just wanted to clarify if this was effective immediately. Thank you!""",
    """4B creating group of 3 constraint
I am trying to approach this problem as suggested in @128, as defining a constraint that a group has at least 3 students and then at most 3. I generate all the combinations of 3 students for a given group first.

My intuition is that if we have students s1, s2, and s3 that is a possible combination of 3 students for a group, and I want s1, and s2, and s3 to be true simultaneously. But to do this, I need some sort of nested conjunction, while add_clause only creates disjunctions. Is there a way to create a clause that is made up of inner nested conjunctions?

Thanks so much!""",
    """HW 3 delayed until April 6 11:59pm
I just went into Gradescope and saw how few students had managed to get it in by the original deadline.  I'm going to change the deadline to April 6 at 11:59pm.  I know that's right after you get back, but at this point you should be far along on your assignments and I want to make sure you have this under your belt in time for the prelim.  Please continue to post questions to Piazza (and hopefully answer those you can), since I don't know the availability of TAs during the suspension of classes.""",
    """karma points for answering questions while classes are suspended
Now that homework 3 is due April 6, many of you will be working on it during the break.  Similarly, the prelim will be later that week, and you have lots of exercises to work on in the meantime, giving those who choose to and who are able to work on them.  However, I'm not sure how the TA situation will shape up over the next 3+ weeks.  Piazza gives me lots of statistics at the end of the semester that I use for karma points, and I'm always particularly appreciative of students who answer Piazza questions.  That is going to be especially so over the next 3 weeks.  I'm going to keep track of Piazza over three next 3 weeks separately from everything else when I figure out karma points.  So aside from being a good citizen at a time when we need lots of that happening and getting good cosmic karma, you will get some positive course karma too.""",
    """karma lectures via zoom
As I've explained, many of the karma lectures are faculty candidates interviewing for jobs at Cornell.  They've largely all been converted to virtual interviews, and so some form of lecture should still be happening - and getting recorded for those who can't watch in real time.  If you're getting bored, or want to feel connected to Cornell and your studies while you're away, or are simply just interested, I'll be posting links when I have them for each lecture.""",
    """today's karma lecture is happening at 11:40am
Use the URL.  It will be recorded and will be accessible even if you can't watch it in realtime.

Speaker: Somil Bansal, UC Berkeley

Safe and Data-efficient Learning for Robotics""",
    """Fun Video
Hey all, this is primarily for the instructors, primarily for Professor Hirsh, this was shared in the CS 4410 Piazza and I thought it was a funny video that you might enjoy and lift your spirits. :)

https://www.youtube.com/watch?v=CCe5PaeAeew

In these coming days, humor is one way to keep up spirits!""",
    """Date for final?
Do we know what date our final will be rescheduled for, given the new dates for finals week? For those of us who could have internships that conflict with the new finals week, will there be an option to take the final earlier?""",
    """Prelim Content and Form
I have some questions regarding the prelim. I'm not sure will it cover more topics because we have pushed it to a later time. Also, will it still be closed book, and will a sample exam be posted on the piazza/course website? I totally understand there are a lot of uncertainties; thanks for any information and all your help!""",
    """Dropping one homework?
While we are transitioning to online platforms due to COVID-19, many of my other classes are increasing the number of dropped homeworks. Will this be the case for this class?""",
    """moving forward in CS 4700 [1 of 2]
Dear CS 4700 students,

 

[To maximize the chance of reaching everyone you’ll get this both in email and on Piazza.  They are identical.]

 

I hope you are all doing well under the new circumstances that you find yourselves in.  I’ve had some time to consider how to adapt CS 4700 to match the unexpected world we’re now in.  I’m going to share the result of my thinking in two notes.  The next note contains details about the course’s operation moving ahead.

 

I’m sending this as a separate note to strongly encourage each of you to take CS 4700 on an S/U basis, and to give you an honest explanation for why.  There are two broad reasons that are, loosely, why grades will be bad and why S/U will be good.

 

From an instructor’s perspective, speaking frankly, grading involves sampling from a noisy signal.  We try to measure your mastery of the material, but noise intrudes in many forms – for example, doing poorly on a test because you had a cold, or you blanked out on the answer to a question, or had bad luck that it hit the material you were weakest on, or you had multiple exams and didn’t have enough time to study adequately for all of them.  (Noise can go both ways, like you lucked out that the test hit the topics you’re strongest on, giving an inflated view of your performance.  I get fewer complaints about this kind of noise.)  For better or worse this noisy sampling process is a core element of how we teach and learn.

 

COVID-19 has us sampling from a much noisier signal.  For example: You were not able to focus on classes before we left because of the turmoil caused in your life by having to leave Cornell on short notice.  You may not have a great situation at home for online learning, whether bad Internet or an annoying sibling or whatever.  You’ve had a multi-week wormhole appear in the middle of your studies, and now need to get back into school mindset and up to speed on >3 week old material.  Online learning might not suit you.  You can no longer easily study with the friends that help you succeed in classes.  And so on.  Add to that the fact that  uncertainty about grades already creates stress, which is itself another source of noise, and it will be worse still now.  We are on our respective sides of a process that will be sampling from a much noisier signal than is usually the case.  Further, this noise is mostly one-sided, more likely to hurt you than to help.  At some level this noise issue is the very reason Cornell is giving you the S/U option this semester.  Your grades this semester might not be the same as they would have been had COVID-19 not intruded in all our lives, having nothing to do with you or your abilities.  It’s about the noise, and Cornell is giving you a way to not have to be hurt by it.

 

Focusing on 4700, I don’t particularly want to be assigning grades in this noisy setting.  I’ve spent the last few weeks thinking hard about how the course should move ahead, and I’ve realized that I don’t have an approach that’s acceptable to me in our current setting for assigning A-F grades to 224 students with the confidence that I’d like.  So I’ve instead decided that I’m going to focus on learning, the reason that I’m in this job in the first place.  The changes that you’ll see in my next note are designed to help students learn within the constraints of our situation, and to assess if people are engaged in the learning process.  This will not be a course designed around an endpoint of giving you a letter grade.  It will be designed as an S/U course centered on teaching a class of students interested in learning about AI and to growing their knowledge of one of the most important forces changing our world.  If you continue to take the class for a grade you will get a grade, as best as I’m able, but you are doing so accepting the heightened noise and stress imposed by this semester’s unusual circumstances and given the form that the class will now take.

 

That’s the reasoning focused on why getting a grade is unwise.  Here’s why I think Cornell’s decision to let you take your classes – required, electives, whatever – as S/U has given you a remarkable opportunity.  Cornell is offering you a semester to enjoy learning without grades being intertwined with that experience.  I’m proposing you embrace it.

 

The suggestion of going S/U may be disturbing at a very basic level to some of you.  You got to Cornell because both learning and grades have been important for most of your life, and they will likely shape where you wind up after Cornell.  However, this semester lets you change that.  I’m asking that think carefully about the idea of school without grades without letting the initial recoil of the concept keep you from doing so.  What might it feel like if you had a semester for learning for its own sake?

 

You’d get to pick what to learn and what’s important to you.  It’s both about devoting yourself to the courses that matter to you without it being about grades, and also, honestly, about courses that you hate and would no longer need to spend as much time on it as you would have.  You get to consider what has happened and is happening in your life right now and decide how to resolve them with the things you want to learn this semester.  You get to make learning choices deliberate rather than grade-centered.

 

There are lots of concerns this might raise for you that might let you quickly dismiss the idea.  Let me address some of the ones that I’ve thought about over the last few weeks, FAQ-style.  I encourage you to contact me if there are others that I haven’t considered.

 

“Could it damage my progress and standing within the CS major?”  No.  Hopefully, you’ll have seen by now the new rules in place for undergraduate CS for this semester.  If you haven’t, please consult https://www.cs.cornell.edu/undergrad/Spring2020FAQ.   An S grade in a relevant class (this semester only) will satisfy all CS core, elective, project, technical elective, and external specialization requirements.  You will furthermore be considered in good standing for the semester if you only have S credits in the relevant courses.  In other words, nothing we’re doing in CS is stopping you.  (While I can’t speak about other programs, I do know that all of our degree-granting programs are similarly assessing how to incorporate S/U grading this semester into their requirements.)
“Could it damage getting into graduate school or getting a job?”  The CS undergrad website states, “Note that the CS department does not know how graduate schools, employers, and so on, will evaluate S grades.”  While accurate, it’s important to realize that just about everyone in college in the US right now is having a weird semester.  Places like MIT are requiring that all courses be switched to S/U.  Speaking for myself and not Cornell, while the note on the website is correct that we don’t know, we can make a pretty good guess.  Everyone reading a transcript will know what this semester was about.  What kind of nut would see an applicant with an amazing record, except for having S/Us for this specific semester, and think less of the applicant because of it?  This won’t be an anomaly on one random transcript, there will be many students from across the US with S/U springs this year.  Again, speaking for myself, in my experience people in positions that read transcripts, whether for hiring or graduate school, know how to read transcripts and will know how to interpret grades this semester.
“I’ve spent my whole life focused on grades!  What you’re suggesting is unfathomable!”  It’s fathomable.  Imagine Cornell had been like MIT and mandated it.  See if you can put thoughts about grades in a box, close its lid, and truly reflect on what your semester would be like if you didn’t have to think seriously about grades this semester.  Make the decision after explicit serious deliberation.
“But I will still need to focus on grades because I might fail the class!”  It’s pretty hard to fail a class at Cornell.  You’re aiming for the equivalent of a C- at worst in order to pass.  Be engaged in learning and I am confident you will do well enough for an S grade.  CS 4700 moving ahead is centered on that premise.
“Grades motivate me to study and learn.  Being honest with myself, I just won’t put the work in to learn unless grades are there to make me do it.”  I suggest you try it anyway and see.  You’ve been given a free pass to try learning this semester without it being about grades.  Life after school has many things we need to do without grade motivation.  See how it fits.
“My parents/family would be furious.”  As before, put these issues in a box and close the lid, and contemplate what you would enjoy doing with your studies, momentarily factoring out the reactions of others.  If you do find S/U grading to be a singular opportunity this semester but you have forces in your life that might react negatively to this decision, don’t hide from it and don’t blindly make the decision that others want you to make without acknowledging it.  Weigh the forces in your life.  If you want S/U grading figure out how to assert to others what you believe is the best thing for you and your studies.  Or decide to go along with what others in your life want even if it contradicts your own views, but do so fully aware that this is what you’re doing without hiding from it.  College is when you go from kid to adult.  This is what life looks like.
 

Finally, I will be teaching you AI regardless of the choice you make.  My goal is to make sure you realize that there is a real choice in front of you.  Don’t go with a grade for CS 4700 or any other class by default because it’s what you’re currently signed up for and getting a grade is your presumed definition of what school means.  Think seriously about what taking the S/U option for CS 4700 (and your other courses) might mean to you for this very strange semester.

 

If you have any questions about this or anything else that I can be of help with, please let me know.""",
    """moving forward in CS 4700 [2 of 2]
Dear CS 4700 students,

 

[To maximize the chance of reaching everyone you’ll get this both in email and on Piazza.  They are identical.]

 

This is the second of the two notes that I’m sending you about CS 4700.  This is the one that has the details of how the course will change.  The other note encouraged you to take the course on an S/U basis.  Whether or not you do so, this describes how grades will be determined.  I will also shortly be asking you to fill in a short survey about your personal circumstances to help me with further planning for the course.  Please fill it out when you get it.  (I know you’re getting similar surveys from others as well.  I apologize that we have no simple way to ask you once across everyone for this information.)  A HTML-ified version of this note will be posted on the course website as well once I complete it.

 

TIME AND TIME ZONES: Whenever I give a time for something for the rest of this semester, such as due dates for assignments, I will continue to follow the local Ithaca Eastern Daylight Zone clock.  This is not because I’m unaware that many of you are scattered across the globe, but because you are indeed scattered across the globe and it’s the easiest way to be clear about times.  You have to do the math to figure out what Ithaca time represents for where you currently sit.

 

LECTURES: All lectures for the rest of the semester will be available both synchronously and asynchronously. 

Synchronous “realtime” lectures:
I will be giving my lectures at the same time as before, MWF 1:25-2:15 EDT.
The first lecture will be Monday, April 6, at 1:25pm EDT.
The last lecture will be Monday, May 11, at 1:25pm EDT.
I will be using Zoom to deliver the lectures.  I will establish a protocol for being able to receive and answer questions.  Details on signing into lectures and how I will operate them will be forthcoming.
Asynchronous “recorded” lectures:
All lectures will be recorded and will be available online.  There are multiple options for doing this, and further details about how and where will be forthcoming.
All slides will be posted, as before.
Attendance: I will assume that all students “attend” class, either synchronously or via recordings asynchronously.  That is the material that all testing will target.
Technology policy: You will now be allowed to have open computers and laptops during lectures.  (Yes, that is an attempt at humor.)
 

ASSIGNMENTS:

How it was:
We had 6 planned homework assignments totaling 30% of your grade, or in other words 5% per assignment.
3 assignments have gone out.  2 are in the past, 1 is still due.
How it will be:
Homework 3 was due just as COVID-19 struck and will still need to be submitted.  The new due date will be Wednesday, April 8, at 11:59pm EDT.
I am decreasing the amount of work imposed by assignments.  There will only be 2 assignments rather than 3 for the rest of the semester.  Neither of them will involve programming.
With 2 additional assignments you will have 5 total for the semester.  Each assignment will be continue to be worth 5% of your grade, meaning that homeworks will now total 25% of your final grade.
I do not plan to change the grading basis for assignments beyond what was listed here.  There will still be a 50% penalty for assignments submitted up to 48 hours late.  There will be no dropped homework grades.
 

EXAMS:

How it was::
You were scheduled for a prelim on March 17, worth 30% of your grade.
You were scheduled for a final exam on May 13, worth 40% of your grade.
How it will be: I do not feel that there is a satisfactory way to move 4700’s traditional exams to an online setting and maintain many of their essential characteristics.  I also do not feel comfortable making you get up to speed on all of the material from the first half of the class for a prelim that must happen only a short while after our return to teaching, particularly with other classes possibly doing the same with exams and other coursework.
I will not be giving a prelim or a final this semester.  I am replacing them with online biweekly quizzes, taking place on Tuesdays and Thursdays.
Details of how these quizzes will be run will be forthcoming, but here are the principles I am seeking to follow:
Quizzes will be accessed via a web browser.
Quizzes will be timed by the platform.
You will be given something like 10 or 15 minutes for each quiz (exact details will be forthcoming).
Each quiz will be available for you to begin within a particular time window (for example, within a 24 hour window), so it can be taken when convenient to you and your time zone.  (Again, exact details will be forthcoming.)
Questions may be multiple choice or short answer, as you might expect for an online platform.
The questions you get will be selected at random from a pool of questions that I will be generating for each topic.
Tuesday quizzes will cover the prior week’s material.  Collectively they are testing the material for the second half of the semester.
Thursday quizzes will cover material from the first half of the semester.  Collectively they serve much the role that the prelim would have but spread it over the rest of the semester rather than in one shot looming soon.  Each such quiz will be about a specific topic – like search methods, propositional logic, first-order logic, etc. - and you will be told the topic in advance.
The first quiz will be on Thursday, April 9, the Thursday after we resume, covering search methods.
The last will be Tuesday, May 12.
The above results in 10 quizzes.  Each will be worth 7.5% of your grade.  Collectively they total 75% of your grade, 37.5% for Tuesday quizzes, 37.5% for Thursday quizzes.
 

FINAL GRADES:

 How it was:
30% homeworks, 30% prelim, 40% final.
I normally subtract 3% from the component of your grade that represents your lowest score, and add 3% to whichever component is the highest.  I announced in class just before classes were suspended that I was changing that to 5%.
How it will be:
Homeworks: 25%, as explained above.
37.5% Thursday quizzes, serving much the same role as the prelim in assessing performance for the first half of the semester.
37.5% Tuesday quizzes, assessing performance for the second half of the semester
I will subtract 5% from the lowest component of your grade and add 5% to the highest component of your grade, but they will now apply to the new three components of your grade.  For example, if your Tuesday quizzes were where you got your lowest score and your homeworks were your highest score your homework percent would go from 30% to 35%, your Tuesday quizzes percentage would go from 37.5% to 32.5%, and your Thursday quizzes percentage would remain at 37.5%.  I will compute this automatically for all students.
Karma points: My prior note about changes to 4700 discussed making the course learning-centered rather than grade-centered.  Karma points were largely a way to make something that you should be doing anyway as interested learners have grade relevance for those who are more grade-centered.  My belief still persists that you should participate in Karma point activities because they are about learning, regardless of whether you take 4700 S/U or for a grade.  It’s now also about pulling together as a community in difficult times in terms of, for example, answering questions on Piazza.  Even so, I am still offering Karma point opportunities moving ahead, in part because the online setting makes it so simple to monitor them.  Some, like Piazza, are as before.  Karma lectures will also be available, only now in online form – which, happily, allows you to now watch them offline.
 

OFFICE HOURS: [UPDATE see @222] We will rely on zoom for office hours and will provide more details about how that will work once we get it all together.  We will also generate a new office hours schedule, and it is my hope that we will be able to offer times that are better suited for people who are now many time zones away.

 

SPECIAL ACCOMODATIONS: For those of you who face difficulties in your studies to which special accommodations are in order (typically documented in a letter from the SDS office) they still apply in the online setting, but it is not always transparent how to respond thoughtfully to them in the new setting.  Should you have any questions about your specific situation as we move ahead, please let me know (fai-l@cornell.edu).  Further, should your new circumstances impose challenges that were not previously a concern I ask that you contact SDS first (https://sds.cornell.edu/about/covid-19-update) – I say this not to avoid whatever issue you might be facing but because I know more about AI than they do and they know far more about accommodations for diverse situations than I do, especially in light of our new circumstances.

 

I have tried to be comprehensive in my thinking about these changes in 4700, but this is new terrain for all of us.  If there is something I've overlooked please let me know - Linus's law (https://en.wikipedia.org/wiki/Linus%27s_law) states that "given enough eyeballs, all bugs are shallow".  you have 446 more eyballs than I do.""",
    """Prep Question Solutions
I'm working through the prelim prep questions (even though there will be no prelim now) just to review the material and make sure I understand everything we've done so far, and I was wondering whether there are solutions to these problems anywhere, since it would be nice to have a way to make sure my answers are on the right track. Thanks!""",
    """MDP's - Placement of Reward Function
While comparing at the Bellman equation with the formula given for active reinforcement learning, I noticed that for active learning, the reward function is outside the summation computing the expected utility of neighboring states. I’m not sure if the placement of this reward function in the Bellman equation makes a difference in the computation of the expected utility/optimal policy of a state. From what I understand, the reward from s to s' is already known and doesn’t really need to be part of the expected utility calculation, and could be placed outside the summation (represented by the bottom equation).""",
    """Question 15 of prelim prep questions
Intuitively, I feel like hill climbing can't possibly be guaranteed to find a truth assignment that satisfies a given boolean equation, since hill climbing generally doesn't guarantee a solution, but I can't think of a counterexample for this question. 

The closest I can get is setting up a boolean equation with truth assignments such that each "child node" will have an equal or smaller smaller number of satisfied clauses (like (A∨B)∧(¬A∨C)∧¬C with initial assignments A = 1, B = 0, C = 1). But would that necessarily cause hill climbing to halt? If you just keep side-steeping in that case you'll eventually get to a solution. Are we assuming that we're using a version of hill climbing that will halt if it can't find a strictly better child node?""",
    """CS 4700 survey of students / Canvas usage
[This note is being sent both by email and Piazza so that I'm confident that I reach all students.  Moving ahead I will rely on Piazza because it allows students to direct their emails to the account of their choice.  Please make sure that you receive the Piazza notification about this note.]

In my earlier note I said that I would send out a survey to learn more about each student's specific situation.  This is the notification of that survey.

First, however, I'll share that there are certain functions, like quizzes and videos, that Canvas is well-suited for and that I'll be using throughout the rest of the semester.  Please go to Canvas and make sure that you can login and see the home page for the course within Canvas.  I will not be using Canvas as the primary platform for the course - my goal is to keep as much as I can unchanged - but you will need to be able to access Canvas throughout the semester.

Second, I will be giving quizzes using Canvas, so I have given the survey in the form of a quiz, so you'll see what that experience is like.  This "quiz" won't be graded.  It's (1) a convenient way to gather information and (2) let's me have you kick the tires of taking a quiz within Canvas.

Third, and finally, please "take" the quiz and fill in your answers as soon as you're able.  I'll be making final arrangements for the course over the weekend and your answers will be valuable as I do so.  I know you are being asked for this information from various Cornell entities, and I'm sorry to be the cause of having to do so yet again, but I won't get this information unless I get it from you directly.

I will send a final note over the weekend with details about how to watch lectures starting on Monday and moving ahead.  I would like as many of you as possible to "attend" the lecture on Monday in realtime.  We've been disconnected for weeks and I'd like to give a more human face to our shared experience teaching and learning about AI.  (I am aware that some of you may be unable to do so, and I haven't forgotten about you, I am hoping that we can find ways to keep all students engaged in the shared experience of this class.)""",
    """Prelim Prep Question 20 (a)
I am completely lost as to how to find U∗(<1,1>) in this question without policy iteration. I feel like I would maybe be able to find UΠUR(<1,1>) with a lot of time and math, but I don't know how to find the optimal value––also, I thought in class that we said that you can't find U∗(s) using math because the max function messed up the linearity of the equations? How are we meant to calculate it here? Did we talk about methods for doing this computation in class? 

Similarly, I'm really confused about how to do 21 (c) and (d)""",
    """virtual class poll and test
I notice that apart from homework, there are "test" and "virtual class poll" on gradescope. Do we need to submit anything for these two categories?""",
    """quiz on April 9
What's the topic of the quiz on April 9?""",
    """potential impact of COVID-19 on your health and those close to you
There is one additional item that I should have included in my earlier notes.  I hope all of you in CS 4700 - and everyone close to you - remain well throughout the COVID-19 crisis.  However, some of you may very well fall prey to the virus.  Some of those who do might be lucky and suffer minimal symptoms, but others might have a serious enough case for it to call into question your ability to get through the course. The same holds true if someone close to you becomes ill from it.

If that happens, I'm pretty confident you won't be alone among 4700 students facing that situation.  I am committed to helping all students who face this challenge figure out a way through the course. If you are continuing in the course with a letter grade that might very well involve getting an Incomplete in the class and we'll arrange a way for you to make up what was missed as soon as is credible.  For those seeking an S/U grade it is quite possible that you would be able to get through the class in the normal timeframe, depending on what is missed - it might very well be that missing the work would drop your grade, but as long as it still remains C- or better you still get the S grade.  This is another very real reason that Cornell has created the broad ability to switch classes to S/U grades, as your insurance policy against you are those close to you getting sick.

If you have any questions that I can be of help with, please let me know.""",
    """zoom link for lectures
Where can we find zoom links for lectures?""",
    """Office Hours Begin Again Monday
With instruction resuming, as will office hours starting Monday. Office hour times have changed to provide a winder time window to accommodate all students. This does mean that, at most times, only one TA will be running hours rather than two. Please therefore be patient and try to make use of office hours that make sense in your time zone. There are some early morning and late night hours (in EDT) that are targeted at students who cannot attend the 5-9pm hours typically due to time zones. 

To join an office hour, the link to the Zoom call hosted by the TA is present in the location field on the course calendar. Not all hours are posted yet; they will be finalized in the next day or so.

During the 24 hours each quiz is live, there will still be office hours. However, TAs will not answer questions about the quiz itself during those periods.

Current procedures for virtual office hours:

We have given TAs guidelines about how to conduct office hours, but they are each empowered to conduct them using what methods/tools work best for them
Most office hours will use the Zoom waiting room; the TA will use their discretion to add/remove students from the video chat
We are also using authentication; you need to sign on with SSO (cornell.zoom.us) and use your NetID login for Cornell 
Please familiarize yourself with the Zoom interface before joining (Raise hands, screen sharing, etc.) and ideally download the app
Please keep your video on if possible, but mute at all times unless you are speaking (headphones help!)
Please use common sense about your attire/location/what's on your shared screen/etc. to maintain a learning environment on the call
Please be patient with your TAs: this is their first time doing this as well.""",
    """Monday's lecture and other updates
Hi everyone,

I'll use this email to give multiple CS 4700 updates:

SURVEY: Only half of you have filled out the survey that I asked for.  Please do it.  Aside from helping me plan the class, it gets you to make sure you can get into Canvas and do quizzes.  If you have a problem connecting to the real quiz and you haven't done this survey I won't be sympathetic.
LECTURES:
All lectures will be delivered via Zoom via Canvas!!!  You will need to login to the class Canvas page, then click on the Zoom item on the left.  You then click on the link for a particular lecture, both to "attend" a lecture in realtime, and to watch the recorded lecture later.
I have set up a fake lecture for Monday 12-1pm EDT, in case you want to make sure you can connect.  It's the first one you'll see on the Zoom page.
I have set up the real lecture for Monday at 1pm rather than 1:25 EDT.  It is the second entry.  Please try to "arrive" a few minutes early.
All slides will be up on the regular course website a little before the lecture, in case you want to follow the slides that way.
Protocols for interaction:
Audio: I've set up these things so that everyone who joins is muted.  Please stay that way.  Do not speak up unless I've called on you to speak, or if you notice that a blaze has started in the room behind me and I'm oblivious to it.
Video: You can choose to attend with video or without.  That might depend on how good your internet connection is, but also on whether you're in your pajamas.  Please don't hesitate to use video - this ain't the same thing as a real face-to-face lecture, but that doesn't mean we can't try to approximate it.  My only request is that what appears on the screen be thoughtful.  It's fine to be dressed comfortably - I will be too - but use reason about what garb (or lack of garb) might be viewed as offensive or disturbing to others.  Same with whatever is in the background, whether real or virtual.
Interaction: I'm going to figure out what works best for fielding questions,so this might change as I/we gain experience with it, but here's my starting point: If you have a question that you'd like to ask live, please go to the chat window and type, in all caps, QUESTION.  You are also free to ask questions in the chat window, and for that matter to answer the questions of others if I haven't gotten to the question yet.  Questions via chat are for short easy-to-state questions, because of its nature.  If you're question is getting long you probably need to ask it by voice.
Trolls: As you've probably heard, there's a thing called Zoombombing.  If some unwanted interloper should somehow find their way into our lecture, the worst thing to do is to give the person any attention, since that's what fuels them.  Just hang on and I'll kill them off.
S/U GRADING:
Deadline change: Cornell has changed its policy and is allowing students to change to an S/U grade basis until May 12, the last day of lectures.  I think it's the right decision, to give maximal flexibility to students.  On the other hand, it might lead some students to think of this as "let me see what my grade is likely to be, and decide then".  It allows you to continue to frame the semester in terms of grades rather than in terms of learning.  Nothing about my argument has changed - I encourage you to take a moment to think very seriously about what going S/U might feel like, thinking of it less as a grading choice and more as a learning choice.  (I'm happy to see that a fair number of you have already made the plunge and changed to S/U!).
Transcript language: I've learned that all transcripts will include the following text with this semester's grades, "During the Spring 2020 semester, the COVID-19 pandemic required significant changes to coursework. Unusual enrollment patterns and grades reflect the tumult of the time, not necessarily the work of the individual.”  Just FYI.
OFFICE HOURS:
Times: Those students who replied to the survey already span 10 different time zones, with some students exactly 12 hours off from EDT.  Our TAs have really stepped up and are offering office hours throughout the week, and some at unusual hours for Ithaca - like 2am on a couple of days, and there may be a few more joining that.  Thank your TAs if you're far from Ithaca and availing yourself of these office hours set specifically to address the global dispersal of our class.
Quizzes: I'll use this chance to inform you that, for obvious reasons, TAs will not be able to talk about quizzes until after the window in which students can take them has ended.
QUIZZES: You are undoubtedly wanting more information about quizzes.  I'm not keeping something from you, it's because I'm still figuring some of it out.  As soon as I nail it all down I'll provide that information.
HOMEWORK 3: One student sent me an anonymous email reminding me that no assignments are supposed to be due April 6 yet I was making Homework 3 due then.  The student apparently missed my note saying that it was delayed until the 8th.  That's fine, there's a lot going on and it's ok to have missed that, especially since it hadn't been updated in Gradescope yet (since fixed).  I have two reasons for mentioning the email.  First, it gives me another chance to say that it's been delayed.  Second, I want to assure the student who sent the email and everyone else: Life's too short and I've been doing this long enough that you're not going to upset me with emails like this.  It could easily have been that I did miss something, and I'd rather you feel comfortable letting me know.  As long as you're polite and thoughtful, as this student's note was.  Emails like this are a good thing, not a bad thing.
Stay healthy!""",
    """today's slides
Because of a change of computer I am having a problem uploading today's slides to the website.  I am attaching them to this post instead.  They will be posted to the website later.""",
    """Videos
For those who missed today's lecture I'm still figuring out the access protocol for students to get to the videos.  I will post something as soon as I do.  (The way I thought it would work is not how it worked.)""",
    """April 9th quiz topic
Will quiz on April 9th cover uninformed search or both informed and uninformed search?""",
    """today's Karma Lecture info
You can attend today's lecture (which starts at 11:40am EDT) via the zoom link.  To belabor the obvious, please make sure you're muted.  (I am still looking into whether past lectures will be available for viewing.)


Practical Algorithms for Trustworthy Autonomy

David Fridovich-Keil, UC Berkeley


Autonomous systems are becoming more and more prevalent; meanwhile, both industry and academia are pushing the fundamental limits of what these systems can do.  As autonomous systems become more sophisticated and tightly coupled to human society, their safety and effectiveness rely increasingly upon accurate modeling and prediction of human behavior. This talk will touch on work at multiple levels of abstraction, including low-level robust control and higher-level confidence-aware human prediction and motion planning. We will focus, however, on a new solution strategy for solving nonlinear N-player general-sum differential games, which arise in many motion planning problems of practical interest. The proposed algorithm is easily real-time, even for moderately large problems. We will discuss the core intuition behind the proposed approach, present convergence and complexity results, and demonstrate it through several examples.""",
    """accessing earlier Karma Lectures?
Could someone help me out with the following?

Go to and see whether after authentication they can access the two post-March-13 lectures that have been recorded. 
Do the same for pre-March-13 lectures at.
These work for me, but my access may differ from CS 4700 students' access.

Please reply here on Piazza, so that only one person need answer (check below to see if someone has already done it).  Thanks!

(If all goes well, the answer is yes, which means past Karma Lectures are available to watch at your leisure.)""",
    """redoing yesterday's lecture for recording - tomorrow 10am EDT
It looks like my using two different machines for giving yesterday's lecture backfired on me.  It correctly recording the session, but it recorded the session on the machine that was doing slide sharing and not the one that showed me speaking.  As a result I will need to give the lecture again so that it gets recorded.  I'm going to do it live so that those who missed it the first time will have a second chance to catch it.  That will be tomorrow (Wed) at 10am EDT.  (I've picked the time so that people in time zones farther away can still watch it in the evening their local time.)

You'll find the link by logging into canvas.cornell.edu, clicking on zoom, then clicking on Lecture 22 (again), CS 4700, Spring 2020.""",
    """HW3 Q4b NoneType error for model
When I add my three constraints and run the model, the model ends up as None. This only happens when I group the first and second constraints together. It runs normally in any combination of the three constraints that does not include both the first and second constraint. I went through all my constraints with multiple TAs who believe the logic to be sound and coding to be correct. How can I fix this error?""",
    """Lecture 8 error?
The textbook says "a = the value of the best (i.e., highest-value) choice we have found so far at any choice point along the path for MAX." Lecture 8 says "a is largest (best) value of all options available to opponent in response to my move thus far," but depicts MIN as the opponent. Is this an error in the lecture?""",
    """4 A and 4B submission
Do we just download the .py file from colab after we are done?  I got the code working in colab, but when i download it, the python code is not syntactically correct when run it my local python interpreter due to the !pip command in front.   

Do you want a working python file or just the one we download from colab?""",
    """Prelim Prep Question 3
Is this question essentially asking for the space complexity of each of the algorithms? I'm not sure if there is supposed to be a difference between the worst case size of the Open list and the worst case space complexity, or if they are the same (O(bm), O(b^m), O(bm) and O(km) for 3a-d respectively)?""",
    """Zoom Link for 9am EST Office Hours Today
Here is the zoom invite for office hours thats happening in ~10 minutes.""",
    """Minimax with or without pruning?
For question 3A, should we be using the Minimax algorithm with alpha-beta pruning capabilities? Or without alpha-beta pruning?""",
    """survey absentees
I have responses from 158 out of 223 now registered in the class.  Thank you to the 158.  But 65 haven't.  Really?  30% of the class?  Are you still in a mindset where I would need to give deadlines and make things count for points in the current circumstances to get your attention?  That's not how this semester in CS 4700 is going to work.  If you are one of the 65 who haven't done it, just go do it.""",
    """new Karma Lecture Thursday
The next CS colloquium relevant to CS 4700 will be tomorrow, Thursday, at 11:40am.  The Zoom link is.

Efficient Machine Learning via Data Summarization

Baharan Mirzasoleiman

Stanford University

 

Large datasets have been crucial to the success of modern machine learning models. However, training on massive data has two major limitations. First, it is contingent on exceptionally large and expensive computational resources, and incurs a substantial cost due to the significant energy consumption. Second, in many real-world applications such as medical diagnosis and self-driving cars, big data contains highly imbalanced classes and noisy labels. In such cases, training on the entire data does not result in a high-quality model.  


In this talk, I will argue that we can address the above limitations by developing techniques that can identify and extract the representative subsets from massive datasets. Training on representative subsets not only reduces the substantial costs of learning from big data, but also improves their accuracy and robustness against noisy labels. I will present two key aspects to achieve this goal: (1) extracting the representative data points by summarizing massive datasets; and (2) developing efficient optimization methods to learn from the extracted summaries. I will discuss how we can develop theoretically rigorous techniques that provide strong guarantees for the quality of the extracted summaries, and the learned models’ quality and robustness against noisy labels. I will also show the applications of these techniques to several problems, including summarizing massive image collections, online video summarization, and speeding up training machine learning models.
""",
    """slides for today's lecture attached
Still can't post things directly myself, so posting them here.""",
    """HW3 late penalty?
On March 12 the instructors waived the late penalty for Homework 3. Now that the due date has changed, is there still no late penalty?""",
    """three questions about logistics
1. Are quizzes on Tuesday and Thursday weekly or bi-weekly?

2. Do we have weekend office hours? I didn't find zoom links for weekend office hours on online office hours calendar.

3. Are there preparation questions for quizzes?""",
    """question of lecture slide
Why we have constraints over a? (I think the equation under two arrows are correct for all the time)""",
    """question about in-class example
For two statements underlined in blue, is R(<1,1>, U, <2,1>) = R(<1,1>) = -0.04?""",
    """Exponential space in terms of depth
Question from the relevant problems for the quiz:

Let m be the depth of the tree.

When doing a DFS don't you need to keep track of the visited nodes so that you don't enter a cycle? When doing this your visited set might be all the nodes if the goal is the last one you hit. This would be exponential in size.

However the answer key says the opposite so I'm wondering where I am wrong.""",
    """How to check 4c correctness
Is there any way we can check to see if the models we come up with are valid on our own?""",
    """Search Questions
1.) Is the root node of a search space considered to be the first state visited. Or do we consider the first node of depth 1 (1 step away from root) visited to be the first state visited. 

2.) Why not check if a state is a goal state as soon as it is generated and before it is added to the open list. Wouldn't this be a useful optimization, as if your are one away from the goal state it guarantees that you go there next. In this context the open nodes have been generated and tested for goal but have not been expanded, while the closed nodes have been expanded (as opposed to the open nodes just being generated). Not to mention that this doesn't even involve doing extra work as the nodes would be tested for goal eventually anyways

3.) The lectures slide ignore the space taken up by the closed set and says we can ignore it because it is a hash table with constant time look up, which makes no sense because that still takes space. How can we ignore the space taken by the closed set and say that DFS space complexity is linear with the max depth when we are keeping track of a closed set? I understand that we could just not keep track of the closed set and allow repetition which would give the desired space complexity, but then the algorithm is not complete as it could run infinitely""",
    """best-first search
In which lecture have we talked about best-first search?""",
    """Question 3c Prelim prep questions


Could someone explain the last part of the solution for this question?

"But this is in terms of k, not m. However, since iterative deepening’s complexity will have visited O(b^d ) if the current iteration goes to depth d, this means k is O(log m). So the answer is O(b log(m))."

Thanks""",
    """Quiz location in canvas
I cannot seem to find the quiz on canvas.""",
    """If time runs out and we don't hit submit quiz will what we have done so far remain?""",
    """today's quiz
Is today's quiz due April 10th at noon?""",
    """S/U grading
If we choose the S/U option, I know all we need is a C-, but does that mean our raw score has to be a C- or our grades have to curve to a C-? I'm just a little concerned after taking the first quiz so was wondering if I should be worried or not. (sorry if this was already answered somewhere) Thank you!""",
    """Quiz Question pictures are not showing
Hi, I cannot see the picture of the quiz question.""",
    """Zoom meeting links missing from zoom page
All the links for future zoom meetings can no longer be seen.""",
    """slides for today
I now have access to the course website, but I haven't had the chance to update it to reflect the new schedule.  I'm attaching the slides to this post, and will later have it up on the website.""",
    """I cannot get in to the class.""",
    """Monte Carlo Lecture Slide 18: Game Statistics in Tree Confusion
I was confused by the numbers in the tree during lecture today. Here is a picture:

In class we said that the white node selects 60/79 because that is the node where white wins the most (so taking the action at the grey node, white has won 60 times out of 79). But then, when we simulate the game and black wins, the grey nodes are updated (by adding 1) but not the white nodes. Why does this happen if the grey nodes are keeping track of the number of times white has won? Or if the grey nodes are keeping track of the number of times black has won, why would the white node select the node where black has won the most, minimizing white's chance of winning?""",
    """Zoom recording for 4/10
Is there a recording for yesterday's lecture? I can't seem to find one under the Recordings tab on Canvas.""",
    """When will quiz results be posted so we get an idea of whether to switch to SU?""",
    """preparation for quiz on April 14th
Do we have preparation questions and solution for preparation questions for April 14th quiz?

If yes, where can we find them?""",
    """lecture 22 page 35
What does the part circled in blue means?""",
    """How long do zoom recordings remain? I heard after 3-4 days it's not accessible""",
    """4B Solution Timeout
For my solution to 4B I was given zero points with the comment "timeout". However, when I run the code I find that I consistently get a solution in under thirty seconds. The answer to question @159 and the HW it͏͏͏self imply that I͏͏͏ shouldn't be penalized for this since I have sufficiently few constraints such͏͏͏ that I get a s͏͏͏olution in well͏͏͏ under a minute.

"If you don't get an answer for a minute, that often means your constraints are too hard"

Shoul͏͏͏d I su͏͏͏b͏͏͏mit a regrade request?""",
    """Grading clarification about Q4 in HW3
Due to the NP-hard nature of SAT problems, we set timeout for a single .get_model() call to be 1 minute (this information is available on piazza and on Jupyter notebook).  We simply don't have the resource and time to finish running every single submission (it's nearly 200 submissions and only a few TAs).  If your 4B solution is taking more than 1 minute to run, what we do is to take a look at your code, if it looks reasonable, then we gave partial credits.  Please only submit regrade requests, when your 4B can finish in a minute and 4C in 10 minutes in your testing.  The assignment aimed for you to generate constraints that can be solved efficiently than just making constraints that return a correct solution.""",
    """HW3 4c partial credit and regrade
If our solution times out but we still have a solution, do we not get partial credit on 4c either? When I interrupt my kernel even after a few seconds, my 4c solution still generates at least 4 solutions. It's just not able to generate all 10 in under 10 mins. I know we are being graded on efficiency but a 0 on 14 for this seems a little harsh if we are being able to come up with a part of the solution and our logic is correct. 

Also the regarded button is disabled on both my homework. Where do I submit one if I need to?""",
    """not having used pair symbols
Were we required to make use of the pair symbols for 4B's pair constraint? (the propositional symbols representing ) I did not make use of these symbols and also didn't use the function link_symbols. The answer to question @185 implied that it wasn't necessary for an acceptable solution.""",
    """Make Up Office Hour 4/12
I apologize that my OH Zoom link for Sunday 3 AM EST was not up in the course calendar.

To make it up, I will hold an OH for the next two hours (5-7 AM EST).

The link is here:

Starting next week, it will be 3 AM EST as usual.

EDIT: the link is updated.""",
    """HW 3 2B Solution
I'm having trouble understanding the second criterion in the solution for 2B. Why is the given criterion

max(e, f ) <= max(a, b) sufficient, and the stronger condition max(e, f ) <= min(max(a, b), max(c, d)) not necessary?""",
    """HW4 Posted on Course Website
HW4 has been posted on the course website. It is due via gradescope on 4/28 by 11:59pm EDT. It covers some topics that will be on Tuesday's quiz, so it is worth looking at early.""",
    """CS 4700 website updated
I have finished updating the course website to reflect the plan for the rest of the semester.  In doing so there's always the risk that I may have inadvertently introduced some errors.  Please let me know if you find any.""",
    """Lecture questions: terminal nodes
Lecture title:  Monte Carlo Tree Search

Page: 25

Question: I am confused about the definition of leaf node. According to the definition, leaf node is state in the game tree that has successors for which no games have been simulated (has one or more “arms” that have never been pulled). In this case 27/35 is a leaf node. However, since it has not been pulled, how can we know the game result? That is: how can we know if this node wins 27 times out of 35 tries?

In other words, my question is: how can we know the result of a game from an non-terminal node?""",
    """Quiz 1 Grades Released
Grades for Quiz 1 have been released on Canvas. Quiz solutions are posted on the course website.

Regrade requests will be accepted for one week until 4/20 at 2:00pm; a reminder that you should only submit a regrade request if you feel that there was an error in grading. 
Canvas does not have an explicit regrade request mechanism. We ask that you add a comment on a question that you feel needs a regrade and a TA will address it. You should be able to go Grades, then click on the name of the Quiz, and then "Add a Comment" in the right menu bar.


Also of note is that the Canvas gradebook will only show a portion of your grade; all assignment grades post regrade requests are maintained offline.""",
    """Open list question
For quiz question 2, if there are no nodes on the open list why wouldn't the search program end?""",
    """Professor office hours
Does the professor have office hours today? I don't see a Zoom link on the calendar.""",
    """Partial credit
It appears that there is no partial credit for quizzes, is this a mandate or will quizzes in the future give partial credit for questions? Thanks""",
    """Quiz 1 Q1 First Possible Question
I do not understand why "The states at level d have no successors generated". Would it not be that in order to reach level d it needs to go through all its successors to reach that level? If it was a linked list this is the order in what I believed it would be visited. Would someone be able to explain why it is not like this?""",
    """Is the quiz out of 22 or 30?
The quiz only has 22 points, but it says out of 30?

Also how do we submit a regrade. The links provided don't seem to apply?""",
    """Quiz 1
I'm not sure how this works so I wanted to ask to clarify things. I took this quiz and got no partial credit and ended up getting a 0. I understand that quizzes are curved, however, many professors do not curve 0's on assignments or tests. I was wondering if this is the case, because as of right now I'm worried that I won't even get the C- needed for an S. Thank you!""",
    """Quiz 2 practice problem solutions not working
the link to the quiz 2 practice problem solutions posted on the website is not working for me. It says "The requested URL /courses/cs4700/2020sp/quiz2reviewsolutions.pdf was not found on this server.""",
    """Possible to Release Tuesday and Thursday Quiz Topics / Review Materials Early in the Week?
I know this is such a new mode of teaching and administering quizzes for both students and TAs/professors.

But, I was just wondering would it be possible to release both Tuesday and Thursday quiz topics / review materials / lecture slides covered on the quiz at the start of each week? I think for Tuesday quizzes it is pretty safe to assume that it will cover the previous 3 lectures (MWF) from the previous week as Professor Hirsh has mentioned. However, because Thursday material is from earlier on in the semester, I think it would be useful to be able to know what topics / lecture slides / review questions we could look over by Sunday or Monday of the week during which we will have the quiz. 

I really liked how Professor Hirsh outlined details for quiz 1 in one of the piazza posts by mentioning that it would cover lectures 2-4 and attached are some practice questions with solutions posted the following day. 

Overall, I think it would be a nice, organized way for students to have access to both Tuesday and Thursday content at the start of the week just so it is easier to plan how we can review material. This was just a suggestion I had, but I understand that these are such new times for us all so it will definitely take a while to get adjusted to the new logistics of the course. Thank you for listening!""",
    """HW3 Stats?""",
    """quiz 2 preparation solution Q2
Based on the answer of quiz 2 preparation questions, should the 2nd and 3rd sentences of question statement be "Arm 1 always gives a reward of 0 on each pull. Arm 2 always gives a reward of 1 on each pull." ?""",
    """How many marks is required for a letter grade A
Since all the hw/quiz have specific marks, what is the total percentage of mark that should be get to receive a final grade A? Or the grade is curved? It is helpful on deciding switch to S/U or not.""",
    """Quiz 2 Material
Am I correct in saying that Quiz 2 will only cover lectures 22, 23, and 24? Along with the clarification at the beginning of lecture 25?

Thanks!""",
    """Typo in MCTS diagram
So there was a little confusion on what the numbers in the nodes meant during lecture, but the prof clarified that the number in the black nodes refers to the amount of times the white node above it won going through it. That made sense to clarify a seeming contradiction, but it seemed to have opened up more contradictions. 

1.) Why is there a number in the root node (or are we to assume it is not a root node)

2.) The diagram says black won so all the white nodes should go up by a win and all the black nodes should take a loss (because the number in a black node refers to the number of wins white had going through it)

Am I missing something?""",
    """Does simulation add nodes to the tree
Does simulation add nodes to the tree or do we only add the node that is one beyond the leaf node and forget about the rest after back propagation to conserve space?""",
    """Question about BFS
According to the answer to quiz 1, it says, for BFS:

If n were an exact multiple of b we’d need n/b nodes on Closed to generate the n nodes on Open. 

I'm not sure why this is not n/(b-1) nodes since after we added b nodes to open we still need to remove one from open.""",
    """Quiz 2 Time
I'm incredibly sorry if this was already asked and answered. I was wondering what time quiz 2 would be released today?""",
    """MCTS on a graph
So it is possible if the game is not really a tree that treating it as such could lead to a lot of duplication. Does MCTS just treat the whole thing as a tree and not worry about it, or does it account for the possibility of getting to the same node from two different states. I don't see how it could do this accounting without fundamentally changing everything but just checking if there is some fancy optimization for real life scenarios where there is more than one route to a node and expansion/simulations from that node would be duplicated otherwise.""",
    """Karma Lectures now up-to-date
The web page listing all 14 past and upcoming Karma Lectures is now up-to-date, reachable off of the course homepage or directly at link.  I will be updating the page with the Zoom URLs for attending upcoming live lectures probably about a day in advance, as soon as I get the URL, and the same with the URL for recordings of these lectures about a day after, as soon as I get the URL.""",
    """4/14 5-6PM OH
I've been waiting for the 5-6 PM OH meeting to start for about 30 minutes, and I'm not sure if the TA isn't online or is with another student. Is there a way to know if the TA plans on starting the meeting? Thank you! """,
    """Confused about Simulation
Can a Node only be simulated before its successors have been generated? So will a node only be simulated at most once? Also there is no zoom link to the office hours right now.""",
    """quiz 3 topic
Where is topic for quiz 3 posted? 

Is quiz 3's topic only informed search or it will include both informed and uninformed search?""",
    """A* Algorithm with Consistency


In lecture 5 (A* Search), slides 68 and 69 show that when h(s) is consistent, we can get rid of a couple steps in the A* search algorithm. I'm having some trouble understanding why that is true. Is it because the definition of consistency factors in costs between nodes?

Any clarification would be greatly appreciated, thank you!""",
    """Practice Prelim 6c
The solution for question 6c of the practice prelim says that the sequence of states visited by hill climbing is: S, A, D G2. 

I thought that the hill climbing algorithm would get stuck at node S because f(A) = 9 and f(B) = 9. Since f(S) = 9 and the hill climbing algorithm from class (lecture 6, slide 34) states that f(new) < f(s), wouldn't the hill-climbing algorithm stop at node S because both f(A) and f(B) are equal to f(S)?""",
    """prelim prep question 6 (d) solution
Why does A* visit B? I had calculated f(B) = 6 + 3 = 9, while f(G2) = 0 + 6 = 6, so would G2 not be the next node visited after D?""",
    """prelim 1 d
1.d.
Question: If breadth-first search is able to find a solution to a search problem, then A* is
guaranteed to find a solution.
Answer: False. h need not be admissible

Does it mean if h is admissible, then A* is not guaranteed to find a solution? If so, may I know why?""",
    """prelim 4
The question and answer are:

Consider a search problem whose state space may contain cycles or be infinite. Imagine
you have an evaluation function f(s) that always assigns to a state a positive integer
value that is less than or equal to 100 (where lower values are better).
Will hill climbing search always halt on such a problem?
- If your answer is “yes”, what is the maximum number of states it will visit?
- If your answer is “no”, please give an example of a search problem where it doesn’t
halt.
Yes. Hill climbing only moves to a new state if there is a successor that has a better
(greater) value than the current state. There are only 100 values that f(s) can take on, so in
the worst case the first state will have value 1, the second value 2, …, all the way to a final
state with value 100. So the maximum is 100.

May I know if the first state should be value 100, the second value should be 99 until the state with value 1 since "lower values are better"? In other words, if the first state has value 1, then there is no other states can be added to open list and the algorithm will directly halt. And the total number of state is still 100.""",
    """quiz 4 6e)
actual cost of an optimal path to a goal state h*(s)

For 6e), is h*(s) = f = g+h = 1+ 2 + 6 + 0 = 9?""",
    """Quiz 2 Grades Released
Quiz 2 grades have been released on Canvas and solutions have been posted on the course website.

The quiz was out of 15 points. The mean score was a 70% with a standard deviation of 3.2. Partial credit was only given on Q3, where you could have gotten 1/2 credit for 1 correct answer.

Regrades will be accepted via Canvas until 10:30am EDT on Thursday 4/23. Please see @289 for how to submit a regrade request.""",
    """Playout nodes
On the slides the definition of a playout is a simulation from a leaf node to a terminal node.

Question 2 asks: In Monte Carlo Tree Search a playout from the root node can fail to reach a leaf node.

How is this not false by definition of playout given that a playout implies we start from a leaf node.""",
    """HW3 Q4 solution released
The solution code for HW3 Q4 is now released on the course website.  Note that it is only an example of making the constraints, and I have seen many other effective and efficient ways in your solutions (good job, by the way!).  If you would like to discuss SAT solvers further, I have office hours from 12-1pm on Saturdays.  Thanks everyone for your efforts working on the problem!""",
    """A Note on Quiz Regrades
Please submit one comment per each regrade request and put the question # at the front of the request. This helps us sort them.

In addition, as there are two quizzes a week and all students have a week to submit regrade requests, please be patient as we address them.""",
    """4/16 8-9 PM OH
I'm waiting for the TA to start the meeting for the 8-9 PM OH, but the meeting still hasn't started. Is the TA planning on starting the meeting anytime soon?""",
    """Prelim prep 6d
Why is the answer S, A, D, B, G2 and not S, A, D, G2 ? You can't get from D to B. Is this a typo?""",
    """Quiz 1: Question 1
One of the options for Question 1 on quiz 1 was: 

"If iterative deepening search runs faster than breadth-first search on a particular problem, then depth-first search will also run faster than breadth-first search on that problem." 

I'm still unable to find a situation in which IDS performs better than BFS, and was hoping for some clarification. Thank you so much!""",
    """Quiz 2 Question 2
Could you explain why "In Monte Carlo Tree Search the branching factor at a leaf node is strictly greater than the number of playouts that have visited the node"?""",
    """HW4: Q4b - Confusion on what "How can you modify f" means.


I'm confused on what "How can you modify f" means.

Is it asking to find an ε where fa > fb, or add some additional term that will make fa > fb for all ε?

Also, are there any limits to how much we can change f? (I would expect that you don't want us to completely rewrite f or cancel out the variables given.)""",
    """HW4 Overleaf Link
Where can I find the overleaf link for hw4?""",
    """Yiduo's Office Hour for April 18 Cancelled + April 19's Extended to 5PM
Hey guys, I woke up with a sore throat so I won't be too effective holding office hour today. I will try to extend my office hours tomorrow to two hours.

Thank you for your understanding!

-Yiduo Ke

Edit: My April 19th's office hours are extended to end to 5PM!""",
    """office hour
Is there an office hour right now? I'm the only participant in the zoom meeting""",
    """Quiz 2 regrade
I just received a Canvas notification about my quiz being regraded even though I haven't submitted a regrade request. My score for the question that was regraded (#3) didn't change, but I'm wondering if this regrade was actually supposed to address the ambiguity in #2 about playouts and leaf nodes?""",
    """Perceptron Learning as Search
I'm a little unsure of why we can consider learning the weights for a perceptron as an example of search. Would the actions be to make the weights bigger, smaller, or the same, and the states a set of of the x_ij values?""",
    """HW4: N(s,a) in double Q-learning
I noticed that the explanation of the double Q-learning algorithm doesn't include the number of times an action was tried as a factor in updating Q or choosing the next action, even though that was in the slides. Should we include N(s,a) in our answer? Thanks.""",
    """giving students grade feedback
One of the downsides of replacing the prelim and final with quizzes is that you no longer have a big-ticket item - the prelim - midway through the semester giving you a sense for how you are doing gradewise this semester.  I know that is making many students uneasy, whether or not they are going S/U.

I've been thinking about how I can give you some feedback to replace what you would usually get from a prelim, and settled on the following: Later this week (either Friday or over the weekend) I will compute two "mock grades" for each of you.  For the first I will rescale your total Tuesday and Thursday quiz scores to 37.5% each, and your homeworks to 25%, and compute what kind of grades you'd get if you performed at that level for the rest of the semester.  I think many of you who are worried about even just passing the class will be reassured by what they see.

However, the quiz form we're using is a blunt instrument, and some of you may feel like you had some bad runs of luck, particularly on questions that are True/False.  First, note that luck is an even-handed force, and the reason for having repeated quizzes is so that it averages out in the long run, both in terms of you potentially doing better moving ahead, and in terms of others having their own bad runs of luck at times when you don't.  To give you a sense for how things might go for the rest of the semester what I'm going to do is compute a second grade for each of you, one where instead of scaling quizzes to 37.5% and homeworks to 25% I will instead replace the missing quizzes/homeworks with the median grades from the first calculation above so that the total score approximates what you'd get if you perform at median class level for the rest of the semester.  I will then assign you a grade using the scale from the first set of grades.  This gives you an approximate answer to, "I thought I was following things but messed up on some quizzes/homework, how much damage will that cause me if I otherwise do decently for the rest of the semester?".

Some students going S/U are worried about even just getting an S.  I am confident that the above exercise will reassure those students.  For those of you still thinking about a letter grade, I'll use this as my latest chance to remind you: If you're the type for whom worrying about grades can be extremely stressful, it must be even more stressful this semester.  The S/U option was introduced precisely because of this.  It is a stress you don't need to experience this semester, on top of all the other stresses that may have been introduced into your life over the last month and a half.  (And I am pleased by how many of you have now made that switch without letting it hang over you for the rest of the semester.)""",
    """Zoom Authorization Error
Zoom isn't letting me authorize my Cornell account; it's saying "log into your Zoom account using this method. Contact your IT administrator for instructions," so it doesn't let me in to the lecture.

Thanks!""",
    """4/20 OH 5pm-7pm
I'm waiting for the TA for the office hours from 5pm-7pm today. I've been waiting for around 10 minutes but I still haven't been let into the meeting room. Are there still office hours today at this time?

Thank you!""",
    """Quiz 4 Practice Question 4
The answer to the practice question 4 for quiz 4 says that one possible way to create a new perceptron after realizing that the labels on the input data would be to use these weights to generate a new set of data and then train a perceptron on this new data. I was wondering if you are randomly generating the new set of data, how would you go about ensuring that the new perceptron would be provably correct?""",
    """Quiz 4 Time Limit Issue
The quiz summary says we have 20 mins to complete the quiz whereas the timer is set to 15 minutes. Not sure if the summary or the timer is wrong.""",
    """Quiz 4 Practice Problem 2
Hello, In the question variable "n" was not declared. Is it supposed to be "d"?""",
    """Quiz 3 Grades Released
Quiz 3 grades have been released on Canvas and solutions have been posted on the course website.

The quiz was out of 20 points. The mean score was a 76% with a standard deviation of 4.4.

Regrades will be accepted via Canvas until 2:30pm EDT on Tuesday 4/28. Please see @326 for how to submit a regrade request.""",
    """purpose of this line in policy iteration


What is the purpose of the if statement? If we are using argmax in the previous line, isn't this always guaranteed to be true?""",
    """Quiz 4 Review Question 3
The solution to this question contains the vector (1,2,5,2,7,9). Where did the first 2 come from? Is it supposed to be (1,1,5,2,7,9)?""",
    """Lecture 27 slide 26 xij
Can anyone gives a more detailed explanation of what xij is used for in Perception Learning Rule here?""",
    """How to keep lectures forever
How can we save recorded lectures? I could go in and screen record every one but that sounds awful and given the recording is already produced, I am assuming there must be some way to download it. How can we download these lectures?? I want to be able to reference these as they're super cool! I realize we can just download the slides but I really enjoy the explanations which aren't always available on slides.""",
    """Quiz 3 Problem 4 Ambiguity
Problem 4 on quiz 3 could have very easily been interpreted in a way where the answer if False.

The question requires you to assume that you don't redundantly add to the open list. Which is especially strange because the question explicitly says

"Assume the search method checks for cycles in the usual fashion, using the Closed list".

Interpreted as that when something is redundantly added, the second time it is taken off it is not re-expanded. (hence using the closed list, which is the implied check in all the algorithms in the notes)

This assumption that the optimization to avoid redundant adding is present also would entail having to maintain a hashset as well as a priority queue to avoid redundantly adding to the open list, making the optimization a trade off between time and space and even less obvious (as opposed to just using a priority queue). 

There are also algorithms in which redundant adding is unavoidable (unless you throw run time out the window) like Djikstra's. Avoiding redundant adding would require searching through the heap when updating distance values on the open list. 

The assumption that such an optimization is present was also explicitly stated in a problem on quiz 1 so the fact that it was not stated here but we were supposed to assume it is strange. (This same issue caused me to lost points on quiz 1).

So to me it did seem reasonable to assume the opposite, and in the way that I interpreted it even though there are n states it is possible that because of redundant adding to the open list that the paths to the goal get over written by redundant nodes and the algorithm fails to find a solution.""",
    """Quiz 3 Problem 4
For this question (specifically, the question on whether a beam search with a beam size equal to n is guaranteed to find a solution), I understand why the answer would be True, if a solution does exist. However, since the question does not explicitly specify that a solution indeed exists, wouldn't the answer technically be false? (In other words, if the given search space does not have a goal state, then wouldn't beam search fail to find a solution, even with a beam size equal to n?)

While taking the quiz, I noticed that the first question did ensure to make this distinction ("Hill climbing might fail to find a solution if one exists"), so I thought that the absence of this information in question 4 was significant. Am I misunderstanding something here?""",
    """Quiz 4
Sorry about posting this here, I didn't want to email the wrong person. I just took quiz 4, however I lost power before submitting (I had all of my answers entered already), how can I go about checking that it was submitted with my answers? Is there someone I can email to make sure before it's due tomorrow? Thanks and I apologize in advance there were crazy storms that took my power out :(""",
    """Link error for quiz 5 review questions
It says NOT FOUND when I click the link for review questions. I am not sure if I am the only person who encounters this problem.""",
    """solution to textbook exercises
Do we have solutions to textbook exercises?

If yes, where are the solutions?""",
    """Are the inputs limited to the range of g
In order to maintain consistency even through the initial input layer, are the inputs (xij's) limited to being between 0 and 1 (or -1 and 1 in the hyperbolic tangent case)? Or do we allow zeroth layer activation (layer corresponding to raw input) to be arbitrary?""",
    """Runtime of neural network computation in practice
I understand that training can take a while, but I was wondering once the network is trained is it quick at outputting on a given input?

For example it was kind of alluded to in lecture but I just want to make sure I understand. In theory if you wanted to run Monte Carlo Tree search on a game, but the search would take a long time per move could you use the tree search to train a network before game day and then just use the network in the actual game. Would the network run faster that MCTS to output a move given a state?""",
    """Homework 3 Problem 3B clarification
In the left-to-right pruning, what is the intuition behind why we prune CC? How do we know, just by looking at BB, that we don't need to check the value of CC at all?""",
    """Question about #2 Quiz3
The question says: "If h(s) is admissible, then max(0, log2 h(𝑠))  is admissible."

I think this is false because when h(s)=0, we get log2 h(𝑠) = log2(0) and this is undefined. However, we cannot have an undefined input to a max function and we cannot know the output of the max function if we have one input to be undefined. Therefore I think we cannot say this function is admissible just because h(s) is admissible.""",
    """hw4q3a
For the Gittins Index calculation, it says that Rt is the random variable denoting the reward at time t. Is this the reward of pulling arm M at time t?""",
    """Double Q Learning use of N(s,a)
Is it unnecessary to use N(s,a) in the calculation of the policy update rule and selection of the next action in double Q learning because we are avoiding bias through having two separate Q functions?""",
    """Epsilon in Double Q Learning
I'm not sure if I'm misunderstanding the hw 4 appendix, but there is no actual epsilon in Double Q Learning. There is only a probability of choosing either to update Q1 or Q2 and then using the sum of both to inform the decision of which action to actually take. Is epsilon meant to be modeled by the alpha learning parameter due to the fact that it's weighting the old expectation vs the immediate expectation?

Also, I'm a little confused about how evaluating argmax a works for a probabilistic action. Would the reward value calculated by argmax be probabilistic for each a during the calculations and the actual result be independent of these reward values?""",
    """Quiz 4 Grades Released
Quiz 4 grades have been released on Canvas and solutions have been posted on the course website.

The quiz was out of 18 points. The mean score was a 75% with a standard deviation of 4.2.

Regrades will be accepted via Canvas until 8:00pm EDT on Thursday 4/30. Please see @326 for how to submit a regrade request.""",
    """Review Question Quiz 5 #11
Wouldn't the smallest game tree for #11 be exactly the same as the solution as question #10, except that the node that was pruned before now has one successor?""",
    """Quiz 4 Question 3
I think I'm still confused about linearly separable data - for the first possible question of #3, why does it not matter to the separability of the data that all points would be labelled +1, since any sum mod 2 either returns 0 or 1 and always satisfies the inequality?""",
    """Quiz drops
So it looks like theres no quiz drops, I was just wondering if this has been considered. I have now missed two quizzes because I get busy and confused with time zones. Seems crazy this would cost 15% of my grade.""",
    """revised slides for today
Just a quick note to let you know that I posted a slightly revised version to today's slides and I'm posting this note to be explicit about what changes there are:

The neurons on the second layer of the figure on slides 5 and 6 go from n+1 to k rather than 3 to k.  (Neurons are labeled by integers, and as I realized during lecture, choosing to use "3" as a placeholder label for the first neuron at that layer could be confusing since "3" would likely be the label of one of the input neurons.)
I added a slide explaining why I used wij as the argument to the activation functions, in response to the question during lecture.
I fixed the typo mentioned in class on slide 23 where the initial subscript should have been j rather than i.
I fixed a typo that I discovered on the same slide while doing this, namely the second loop should go from k-1 down to 2 rather than 1.  (We use the delta term for neurons on the second layer to adjust the weights going from the inputs to layer 2.  We don't need delta terms for the input units themselves at level 1.)
The format of the summations on two of the slides changed slightly, which probably would have been noticed by few, but for completeness I'm mentioning it.""",
    """Multi-armed bandit
Do we compute regret for the initialization steps of the multi-armed bandit problem? If one arm has been initiated and the other one hasn't, do we assume that the initiated arm is the "optimum"?""",
    """Policy Iteration s_t


Does s_t represent the total reward starting from the initial start state, or does it just represent the current state?""",
    """do we calculate regret from expected or observed value""",
    """OH at 1pm?
Are there still OH today at 1 pm? Thanks!""",
    """hw4 N(s,a)
So the lecture slides on Q-learning mention N(s,a), which I understand to just be the number of times you've tried a certain action for a state. However, the appendix in hw4 for question 2A doesn't mention this factor. Should we still include it in our pseudocode for when we calculate the new Q-hat? Also, can we assume that we are given an arbitrary alpha value?""",
    """HW 4 Q1B Excel Sheet
I wanted to know if it would be okay to make an excel sheet to help with calculating values for HW 4 Q1B. Thanks!""",
    """hw4 q3b
So for question 3B, when we do the simulations, we do it only based on the UCB values correct? I got confused because at first I thought the problem gave you the sequence of arm pulls A, B, A, A, A and we had to follow that when doing the simulation.""",
    """HW 4 1B
Hello, I am currently working on the first iteration of question 1B. I have a lot of writing so far, and the entire problem may span over two pages. Is a long answer expected for 1B, or is this a sign that I should find a different approach for this problem?""",
    """Double Q Learning "Sets"
In the Appendix, it says that we "divide the samples into two sets and learn two independent estimates". Does this mean only some values (s, a) will have a Q1, and others Q2? Are we actually dividing up the sample space into sets, or just generating 2 Q values for each element (s, a)?""",
    """HW4 2b
Is this question asking for an explanation of why the optimal policy choosing 5% left action? Or it's just asking for what is the epsilon value? Actually I don't see why the optimal policy would involve some left actions since in the long term, the expected reward of left action is negative.""",
    """2pm Office Hour cancelled
Hello guys. I will have to cancel my 2pm office hour today. Sorry for the inconvenience.""",
    """policy definition
So i'm a little confused on the definition of a policy. Is a policy defined by just the state s and action a? Does the outcome s' state from apply(s,a) matter when considering it a different policy?

For example, if apply(s,a) can give s'_1 and s'_2. Does that count as 2 unique policies, or just 1?""",
    """HW 4, 4A
Should we consider the probability of 'O' to go first is 1/2 or should the symbols be interchangeable (ie the same formation with all X's swapped for O's and all O's swapped for X's).""",
    """5pm office hours - I am not let in still in waiting room""",
    """HW4 Q1B: Cumulative reward
Hi, question 1B asks about convergence which, based on Lec 17, considers cumulative reward. It states that cumulative discounted reward "treats future rewards as exponentially decreasing as t goes to infinity (if R bounded, 0 <= γ < 1)". What is the bound on R?""",
    """Hw4 Q3 Gittins Index
The problem says to use our typical discount factor gamma, are we to suppose a gamma in this calculation?""",
    """delta_i in backpropagation
Why do we need to calculate delta_i in the backpropagation algorithm for every layer below the output layer? Where does its value get used again?""",
    """Quiz 6 Practice Problems
Will there be review questions and solutions posted to prepare for Quiz 6 tomorrow on Lectures 28-30? I couldn't find a link on the course website.""",
    """Lecture 28
Hello, I am a little confused on how xij appeared in the derivative of the Error function. (3rd line)""",
    """MDP PI* for different initial states
Is it correct to say that PI* remains constant even if you change the initial state of the MDP (Assuming all other thing remain the same)? 

I understand the actual value of the policy will change, but it should still be optimal right. I don't know how to go about proving it but it seems intuitive enough that I'm sure someone has.""",
    """miu superscript best - multi armed bandits
miu superscript best = (argmax subscript i)(R subscript i) 

I believe that this is a mistake in the slides. Shouldn't miu be a numerical value that says the expected average reward for pulling the optimal arm? Isn't argmax going to return machine i rather than the expected average reward for pulling the optimal arm?

I believe that this should be miu superscript best = (max subscript i)(R subscript i); correct me if I am wrong. This is on the slide near minute 31 of lecture 23.""",
    """4/27 7-8pm OH
HI, I'm waiting for the TA to start the zoom meeting for the 7-8 PM OH, but the meeting hasn't started yet. Is the TA holding office hours today?""",
    """policy iteration optimality
Does policy iteration provably always converge to the optimal policy? I can see how this would be the case if when evaluating the value of a policy we didn't use the estimates of the utility of the neighbors from the previous iteration, but instead computed the actual utility of the current policy using Gaussian Elimination. And then when it is time to update the policy choose the best action according to a "Q" that doesn't represent acting optimally afterwards but rather acting with regards to the previous policy afterwards. I saw a proof that shows that this would lead to strictly better and better policies.

Theorem: If for every state acting according to pi' and then acting according to pi for following actions leads to greater than or equal long term utility than the utility of pi, pi' must be better than pi (Using a Q that is not for optimal follow up but just follow up with pi)

Intuitively this makes sense and the proof is just unraveling the utility of pi until it becomes the utility of pi' with a bunch of less than or equals in the middle.

So I guess I am wondering how using estimates of not just any policy, but a different policy, can lead to a good estimate of the utility of the current policy in such a way that the policies get better, provably""",
    """Neural Nets Error Confusion
Since we said that delta w is the error of a particular set of weights for an example, can the neural net learning update rule be written in the following way? Is this the same as the neural net learning rule we talked about in class (on the slides)?

I'm confused whether it's true that the error of a state is the sum of errors of its neighboring states. If so, could you please provide an explanation for why it is this way.

I'm also wondering what would happen in a neural net with cycles when calculating the result of the activation function. I'm guessing you wouldn't be able to get a value, since in a neural net with one cycle between two nodes, two variables are expressed in terms of each other in two equations.

Thank you!""",
    """Q learning
1.) What kind of things can Q learning be used on. It seems keeping a table of Q values for every (s, a) pair is very limiting as any complex problem would blow up in terms of space?

2.) Assuming space is not an issue, I was wondering if the following would be a decent adversarial twist to Q learning? One Q learning agent starts in a state and chooses an action. He does not know where this action will take him because he has no idea what move the other opponent will make. The opponent is also a Q learning agent that is doing the same thing. The reward is just some heuristic that evaluates the board state. The two agents just play each other again and again until they both have an understanding of what they should do.""",
    """4/27 slides and recording?
I'm just wondering if there are lecture slides and a Zoom recording for 4/27? I'm looking on the course website and on Canvas, but I'm not seeing any new material. Thank you!""",
    """no Karma Lecture Tuesday after all
Ashia Wilson won't be giving a talk Tuesday.  It will be rescheduled some time next academic year.""",
    """slides for Monday; quiz 6 delayed 4 hours
There was a suggestion during Monday's lecture that I create a graphical version of the Backprop update algorithm.  It was a great suggestion.  So I just spent the last few hours doing that (that's why the slides weren't previously posted).  You can find them off of the website.

However, it was a few hours that I hadn't scheduled into my life, hence here I am at 3:20am posting this note.  As a result, as a one-time thing, I am delaying the start of Quiz 6 by 4 hours.  It will be released at 4pm EDT (instead of the usual 12 noon time).  You will still have a 24 hour window in which to do the quiz.  I apologize for the last-minute change.""",
    """Gittins Index
I'm confused on why we are using a Gittens Index. It just seems like a fancy way of expressing expected value as you can just pull E(R) out of the top sum. Also it doesn't seem like there is any reason to ever use something that is not expected value because if you have all the probabilities then its pretty obvious your policy should just be to pull the arm that has higher expected value. 

Am I missing something?""",
    """Question 4b
I saw another post on this but I still don't know what the question is asking.  

I just solved for epsilon to make node a have a higher value. Is this what was being asked?

If not, what is being asked? Because it seems that node a already can be chosen without changing the function at all (if epsilon is below a certain threshold)""",
    """Clarification about calculating regret
in office hours they told us regret was expected reward from optimal policy - expected reward from ucb policy but in the slides it says it’s N*expected reward from best policy-N*expected reward from ucb. Do we need to multiply by the number of pulls (5 in the case of question 3b) or not?""",
    """HW4_4A
I'm a little bit confused by this because since we have a uniform probability distribution, does this mean that we are just randomly selecting each position and give it a random X or O?""",
    """50% late penalty
There is a 50% penalty for late homework assignments. Does this mean 50% of the total would be deducted, or 50% of points earned? For example, would an assignment worth 10/20 points before the late penalty drop to 0/20 or 5/20 after the late penalty?""",
    """Policy For Single State MDP
In the slides/textbook, a "policy" has been defined as a mapping of states to actions. Therefore, does a policy for a single state MDP only consist of one action? If not, can this policy be defined as a series of moves? For instance, can a multi-armed bandit have a policy that maps a specific time step "N" to an action or must the policy only consist of a single action since there is only one state?""",
    """Notation for logistic gradient update

Hi so in the slides when you use the error value to generate the updated weights the Xij term changes to having a bar in the update step. Does this mean that this term is a vector? I thought that each Xi term is a vector of values so Xij would be the jth value of Xi""",
    """HW5 Posted on Course Website
HW5 has been posted on the course website. This is the last homework for the semester.

It is due via gradescope on 5/12 by 11:59pm EDT.""",
    """Prep for Quiz 7
I'm getting an error when trying to click the review question link for Quiz 7. Could someone check to make sure it's posted? Also, will answers to the review questions be posted before the quiz? Thank you!""",
    """HW5 1a
I'm confused about how to apply the notation taught in class to words. In class we learned that 



Where



i.e., the number of examples in class l where attribute j  has the value at index a.

But in the homework, we have a bunch of examples (sentences) with varying length. Are we treating the first word of a sentence as attribute x¯test,0? So, when we're looking for the probability of very | Politics in 1(a), where "very" occurred in the second position in the test sentence, are we looking for the number of times "very" occurred as the second word in an example sentence with the label Politics out of the total number of example sentences?  This happens zero times and would send our probability to 0, which makes me think I have the wrong idea. 

Alternatively, should we treat each word as its own example? So then we would be looking for the number of times "very" was in a sentence labelled with "Politics" out of the total number of words? The gives me a more reasonable number but it feels too different to what we learned in class.""",
    """Logistic Regression Algorithm (page 5 of Lecture 29 slides)
I'm a bit confused about what xij represents in the algorithm. If I were to simulate the logistic regression algorithm, how would I determine xij from the values of xi?""",
    """Quiz 5 Grades Released
Quiz 5 grades have been released on Canvas and solutions have been posted on the course website.

The quiz was out of 19 points. The mean score was a 80% with a standard deviation of 3.2.

Regrades will be accepted via Canvas until 12:30pm EDT on Thursday 5/7. Please see @326 for how to submit a regrade request.""",
    """Quiz 5 Question 3
In the solutions to quiz 5 provided, for the first of the two possible questions for question 3, the solutions states that 

"G will get pruned if Y ≤ min(max(8,7),max(6,X)) = min(8,X)"

Therefore, to guarantee that G will be pruned regardless of the value of X, shouldn't the value of Y be 1? 

If Y is set to 8, as the solution states, then for any value of X less than 8, the inequality "Y ≤ min(8,X)" would be false and the node G would not be pruned. 

Is there an error in the solutions or am I misunderstanding something?""",
    """Confused by review question 1(g)
I don't quite understand why the answer is false. If P is unsatisfiable, then that means for any assignment of 1's and 0's to its literals, it will output 0. Then, if we negate P, shouldn't all of those 0 outputs become 1 for any assignment of literals, making its negation a tautology?

Or, I also thought of it like, if P is unsatisfiable, then P |= False, which means (not P \/ False) for any truth assignments, which means that (not P) must always be true since False will never be. 

Where am I going wrong? I think it would really help me if I could have an example of a P that is unsatisfiable, but its negation is not a tautology. Thanks!""",
    """Quiz 6 Grades Released
Quiz 6 grades have been released on Canvas and solutions have been posted on the course website.

The quiz was out of 15 points. The mean score was a 40% with a standard deviation of 5.12.

Regrades will be accepted via Canvas until 2:00pm EDT on Thursday 5/7. Please see @326 for how to submit a regrade request.""",
    """Quiz 7 Details
Does Quiz 7 cover propositional logic and first-order logic or just propositional logic?

Thanks!""",
    """Quiz 7 Prep Question #17 (Unification)
I'm sort of confused about unification on this problem; I'm getting {y/G(x), x/F(G(A))}, and can't seem to find where I made a mistake when comparing it with the answer. I'd really appreciate an explanation addressing what I'm doing wrong.

Thanks!""",
    """AlphaGo Movie
While procrastinating, I found a free, really well-made documentary about AlphaGo on youtube. It's not technical, but it was cool to watch the historic match and hear from the people involved with the project.

https://www.youtube.com/watch?v=WXuK6gekU1Y in case anyone is interested.""",
    """Quizzes Time Window
Is it possible quizzes are adjusted to be over 24h? Some people are unfortunate with time zones and don’t get two days to do it. Since sometimes we have things going on on a given day given we are now at home, this presents an unfair advantage to some who instead of having 2 days only really have one because the quiz might start late at night and end late at night, while for people with Ithaca time zones their quiz starts at midday and ends at midday; allowing time to work on the quiz on two different days rather than just one. Not saying 48h but some middle ground that would allow all people to have two different days to take it. Would very much appreciate.""",
    """Lecture 31 Zoom Recording
Hi, 

I am trying to access the zoom recording of Monday Apr 27th's lecture on Canvas, but there doesn't appear to be a recording there (this is for lecture 31). 

I was wondering if we can access it from elsewhere?""",
    """Saturday 12-1pm office hour canceled (this week and next week)
Hi all,

Sorry I won’t be able to make it to the office hour from 12-1pm today and this time next week.  I apologize for any inconvenience this may cause.""",
    """Is the Quiz 5 Question 3 Regrade done?
I wanted to make sure it's okay to submit a regrade request and that the course staff isn't still working on regrading that question. My answer is listed among the "correct" answers but for some reason the question is still being marked as wrong. Should I submit a regrade request or wait? Thanks!""",
    """Yiduo's office hours today moved to Sunday 4pm
Hey guys, 

Unfortunately I really can't make it to my office hours today due to fatigue. I will, however, make up for this by extending tomorrow's OH by an hour to make up for it.

Thank you for your understanding! See you tomorrow! 

-Yiduo Ke""",
    """Citing online textbook
I would like to reference certain sections from draft chapters from the upcoming 4th edition of Artificial Intelligence: A Modern Approach by Stuart Russell and Peter Norvig for a research paper for another class. Since this book is technically not yet published, what would be the correct / best way to cite it? Thanks!""",
    """lecture 31 should now be available in canvas
I apologize that the redone lecture ran longer than a typical lecture (~1:20).  Most of the lecture is a wrap-up of neural net learning followed by a brief intro to Naive Bayes.  The main value is to get a big-picture pulling all the neural net stuff together and a hint at where it goes when used in real applications.  In some sense there is nothing new algorithmically, just big-picture, so you can view it as an optional lecture.""",
    """2B error after forward propagation
Is the error after forward propagation y−a5 i.e. the difference between the expected label y and the actual output value at node 5?""",
    """powerpoint of lecture on May 1st
When will powerpoint of lecture on May 1st be posted?""",
    """Clarification about calculating 1a
I'm confused about calculating the probabilties for 1(a). For P(Politics | a very close race) do we need to calculate the exact value?""",
    """Quiz 7 Solutions Released
Quiz 7 solutions have been posted on the course website. Grades will be released later today.

We're hoping to find any issues/errors with the quiz prior to grades being released, so please take a look at them.""",
    """HW4 Grades Released
HW4 grades have been released on gradescope and solutions posted on the course website. As always, the grade does not reflect the 50% late penalty, which we calculate offline. If you received an extension on your assignment, it will be graded shortly; please be patient.

Statistics are below. You have until Monday 5/11 at 5:00pm EDT to submit a regrade request via gradescope.""",
    """Problem 3B, HW 4
I'm having trouble understanding how the value of 3 for the regret is obtained in the solution. My understanding is that you subtract the policy's reward from the best possible reward and then multiply by N. Does this mean that the best possible reward is actually 6, possibly because you're supposed to include the initialization steps? In my solution I obtained 7 for the best possible reward (the sequence 1, 1, 2, 2, 1), giving a regret of 4.""",
    """Confusion about 2B Gradient and Weight Updates
For 2B in HW 5, the question asks to calculate the gradient and updated value for each weight after the back-propagation part of the algorithm. I talked to some TAs during office hours and we had a few questions.

In lecture, I believe it was mentioned that oftentimes the -2 coefficient that is part of the official gradient formula becomes a part of the alpha (learning rate) when doing weight updates. Because we are given an alpha = 1 in this problem, do we need to take the -2 into account when calculating the actual gradients (the delta_j / delta_i values in the backpropagation algo)? 

Additionally, when actually performing the weight update with w_ij <- w_ij + alpha*a_i * delta_j, does the delta_j gradient value also take -2 into account, or should this value be without -2?

Basically, when calculating gradients, do we need to multiply by -2, and when doing the weight updates, do we multiply by -2 there as well or not worry about it? These are the 2 different cases.

Thank you!""",
    """HW1 1A solution
I am curious why there are 9 unique policies. For each of the 2 states, there are 3 possible actions. So there should be 3*2 = 6 unique policies.""",
    """Q1C: What smoothing parameter should we use?
In the lecture, the slides only mention that the smoothing parameter should be > 0 and is generally <= 1, but no specific value is given either in the lecture slides or in the homework.

So what value should we use for this smoothing parameter in our calculations?""",
    """Quiz 8 Practice
Are there going to be any practice questions for quiz 8? I see there are some for quiz 9 already but I don't see any for quiz 8""",
    """quiz 8 formatting
Just a head's up that the formatting for the questions of Quiz 8 came out a bit inelegantly despite my battle with Canvas to tidy it up.  Make sure to read it carefully.  There is one question with two parts.  You can tell the two parts apart because they each begin with "(5 points)".""",
    """HW5: 1a Possible typo in question.


The background information explains that we are trying to classify the statement "a very close race". However, part A asks for the conditional probabilities of two different statements, and I believe it would make more sense to find the conditional probabilities for the same statement, "a very close race", as we want to find the higher probability of the two categories for that single statement.

So, does 1a #2 have a typo and is supposed to be: P(Not Politics | a very close race) instead of "election"?""",
    """Practice Questions Quiz #8 Question 3b
How did they get 2/4 for the final term of the + category? Wouldn't it be 1/4 since njaj = 0, alpha = 1, Nl = 2, and |Vj| = 2 ?""",
    """Naive Bayes Question
When we calculate the size of Vj for Naive Bayes (slide 22 of lecture 33) would the size of Vj for a sentence be the unique words in that sentence?""",
    """Quiz 7 Grades Posted
Quiz 7 grades have been released on Canvas. Regrades will be accepted until 11:30pm EDT on Tuesday 5/12.

The quiz was out of 15 points; the mean was a 38% with a standard deviation of 4.8

Solutions, as previously announced, are on the course website.""",
    """Quiz #9 Practice Questions
Is the link to the practice questions for quiz #9 working? I can see that it's up but when I click the link, it doesn't pop up. It says the following:""",
    """Finding probabilities when using laplace smoothing
I understand that laplace smoothing won't change the outcome when using argmax, but for problem 1c on hw5, when it asks you to calculate an exact "likelihood," how can you adjust for laplace to calculate an exact probability? I also noticed it's using the word likelihood instead of probability here, is this meant to be a distinction?""",
    """Practice Questions Quiz 9 21a
For question 21a, would the right approach be to set up a system of equations for the utility of each state according to the given policy, and to solve the system to get the value of U(<1, 1>)?""",
    """Practice Questions Quiz 9 22e
For the policy iteration section (part e) of question 22, would the policies for states 1, 2, and 3 converge to clockwise, stay, and counterclockwise respectively?""",
    """Practice Questions Quiz 9 21b
I'm confused about the solution given for the policy iteration in question 21. I feel like you would only get the given values of U_1 if actions were deterministic, but if I apply that assumption to my calculations for U_2, I don't get the values given in the table. Could someone break down the steps being followed/calculations being done in order to produce the values given in the solution? Thank you!""",
    """score estimation
When the estimated grade is calculated, are the lowest two quizzes dropped?""",
    """Quiz 9 delayed 30 minutes
Quiz 9 will be out at 12:30.  I've reconsidered one of the questions and it's taking me longer than I expected to redo it.""",
    """Quiz 9 Prep Questions 21 & 22e, 22c
In the solution for question 22e, I'm confused why we have that U(2) and U(3) are equal to 0 for the row corresponding to the first iteration. Since the policy is of staying in state 2, wouldn't we wind up in state 2 and thus receive a reward of 1, implying that the utility will be 1, and similarly for state 3?

Also, in question 21, I'm wondering why the actions represent a single move (is just "Up" or "Down" for example), as opposed to question 23, where we have that the clockwise and counterclockwise actions consider more than one move (unchanged city & next city) from a state.

Thank you!""",
    """HW5 Q1 clarification
In the definition of tfidf, N is defined as the number of training examples in the training set. Would each phrase count as 1 training example or would each individual word count as 1 training example? Also, would n(w) represent the number of phrases the word appeared in (I.e. n(a) = 3) or something else? Just wanted to make sure I had these clear before doing all of the calculations.""",
    """Another grade estimate?
will we receive another grade estimation before drop/SU ddl?""",
    """hw5 1B
When it says "What would the likelihood be with Laplace smoothing?", do we just give the modified formula for P(w|c), or is it asking for actual values for the statements in 1A (ex. P(politics | a very close race))""",
    """hw5 2B "error"
I'm little confused on what "error" is after forward propagation. 

On lecture 28, it defines Error as the following. So is the error of the output just based on nodes h3 and h4, because they feed into output node h5? Or does the error summation include ALL nodes in the neural net?""",
    """HW5 Q1C P(w|c)
For part C in question 1, for applying the Naive Bayes algorithm, should we be using the form n_jal / N_l  from the slides as the form of estimate for P(w|c) with added Laplace Smoothing, or should we be using the P(w|c) from B with the Laplace Smoothing?""",
    """Average Quiz Score
I understand that it's very difficult to give us new grade estimates at this point right before calculating actual grades again, but would it be possible to tell us the average score for Tuesday and Thursday quizzes to give us some guidance?

As mentioned, the quizzes are a very noisy signal of our performance in the course and it's hard to know where our cumulative quiz scores stand in relation to the class at this point in the semester. If it's not too much work, I think it would be very helpful for those of us still making up our mind about whether or not to take the course pass/fail.""",
    """HW5 Q2 part A
Can we assume alpha=1 in Q2 part A? ( alpha=1 is given in Q2 part B)""",
    """Backpropagation in Problem 2B
After doing backpropagation and updating the weights, the problem asks for the new output after the update. Does this mean I need to run forward propagation again with the new weights?

Also, is the error supposed to be the square of the difference between the desired output and the actual output, as defined in Lecture 28? This is what I saw in @481, but Lecture 31 also refers to the difference (without the square) as an error, and I don't think I've seen the sum of squares formula mentioned since Lecture 28.""",
    """Homework resubmission
I accidentally submitted my homework when I made a mistake on one of my questions. Are the submitted homework graded prior to the due date, or am I allowed to re-submit my homework?

I apologize if this question was already asked, I couldn't find an earlier post on it.""",
    """HW5 Q1C Calculation
I think N and n(w) do not depend on the category, so they will be the same for all categories. In this case, can we drop the lnNn(w) part just to simplify the calculation or we still need to do it?""",
    """Back-propagation concrete example / steps
Hi guys! 

Some of you were struggling on problem 2 of HW 5, especially in applying the backpropagation pseudocode to a concrete example. I made an example with different numbers and stepped through it in the following file. Hope it helps!

-Yiduo""",
    """5/10 2pm OH
Is OH still happening today? I've been waiting for over 20 min but the host still has not started the meeting.""",
    """HW5 Q1b: Laplace smoothing on tf-idf or probability only
Should smoothing affect the way tf-idf is calculated?""",
    """HW5 Q2 B and C
I have two questions about backpropagation:
1. Does it matter whether we update w03, w13, and w23 before w04, w14, w24, or w04, w14, w24 before w03, w13, and w23?

2. Within each group of weights (by group, I mean w05, w15, and w25 is a group, w03, w12, w23 is a group, and w04, w14, and w24 is a group), does it matter which one of the three weights we update first?""",
    """Question 1B and 1C
For Part B it says compute the likelihood. The likelihood of what?

Part B says use Laplace smoothing. What should we use for alpha

Also for Part B, what is our notion of "Laplace smoothing".  Should we just put a + alpha the numerator and a + alpha|Vj| in the denominator of the given probability formula. And if so what is |Vj|? Should we just say |Vj| is 2 (word is present or absent)? Can we choose any formulation we want that provides the affect of starting above 0 and having an affect that diminishes as more data is collected?

For part C are we reporting 4 probabilities?""",
    """Square Error 2B
Should we square the difference between 1 and our error and just use the expression from class, or are we supposed to derive an expression for the updates using an absolute error?""",
    """alpha = 1 in backprop
Wouldn't assuming alpha = 1 make you step in the direction of the gradient giving you the worst possible update. Since in the slide it is written wij <- wij + alpha(ai)(deltaj). And (ai)(deltaj) is the derivative of the error function with respect to wij. So shouldn't either alpha be negative or that plus be a minus""",
    """Question 1 HW 5
For question 1 on hw 5, if V_j represents the presence/absence of a word, does this mean that n in the below equation from class (slide 12, lecture 33) represents the number of unique words in the training set? And each j is one of the words in the training set?""",
    """final course grade date
When will course grades be available? Will they be finalized by the 23rd?""",
    """Conditional Probability Calculation in 1C
I still a little confused about how to calculate the conditional probability P(statement|Politics) in question 1C. I have two different approaches in mind of how to calculate the probability, but I'm not sure which one is correct. 

Approach 1: 

P(This is an example statement|Politics) = P(This|Politics)*P(is|Politics)*P(an|Politics)*P(example|Politics)*P(statement|Politics)

In this approach, I image |V_j| to be the number of unique words in the training set. 

Approach 2:

P(This is an example statement|Politics) =P(w_1|Politics)*P(w_2|Politics)*P(w_3|Politics)* ... *P(w_n|Politics)

were each w_i represents a word in the training set and each w_i is set to 1 if the word exists in the example and w_i is set to 0 if the word does not exists in the example. In this approach, I image |V_j| to be 2 which represent the existence/absence of the word w_i. 

I'm unsure about which approach to use when going through the Naive Bayes algorithm. Any help would be greatly appreciated, thank you!""",
    """Calculating P(politics) and P(not politics)
For many of the calculations in part 1c, they will in include the values of P(politics) and P(not politics). There was much confusion in office hours if P(politics) = P(not politics) = 12/24 since 12 out of the 24 words are in politics and 12/24 words are in not politics, or if P(politics) = 3/5 and P(not politics) = 2/5 as 3 of the 5 examples are politics and the other two are not politics. If someone could please clarify it would be very appreciated as I have heard contrasting things from different TAs!""",
    """clarification on homework 5 #1
I've been trying to block out some time to answer the various questions about questions 1 on the homework, but realize I'll get that done sooner if I post one note explaining things further.  I'll circle back to the various postings later tonight.

There are two things that are different here that in hindsight wasn't spelled out as clearly as they could have been.

To explain, forget about classification for a moment and let's think about probabilities more generally.  Imagine I wanted to know P(D|A,B).  I could use Bayes Rule together with the conditional independence assumption to convert that to P(D)P(A|D)P(B|D)P(A,B).  If there was some other random variable C and we have no information about it it would just be absent from that calculation.

The reason this is relevant is that how we treat words as features depends on what we ascribe to a word being absent from an example.  Is it's value "0" because it's absent, or is it simply a random variable that we have no information about.  If the word is present for an example of some category, it's clearly relevant for that category.  But if it's absent do we simply say we don't know whether it's relevant, or do we say that its absence was relevant to that category rather than conveying no information.

I presented the vector space model using the second of these.  It was a natural consequence of the basic Naive Bayes approach.  To do Naive Bayes in the general case I described, if there were n attributes you ended up doing a product of n+1 terms, P(c)P(x1|c) ... P(xn|c), where each P(xi|c) refers to the value that the particular example that I'm classifying took on.  When I went to text classification I talked about there being as many features as there were words, where they each took on a value 0 or 1.  The absence of a word (that is, that its value was 0) was treated as a term in the product.

The homework intends for you to treat absent words using the first of the approaches above.  The absence of a word gives us know information.  Think of it as "If my example has the word present then I know that word is relevant, but if it's absent it might still be relevant but I don't know because it's absent".  As a simple example, imagine my example had the word "boat" but didn't have the word "ship".  It's likely that "ship" is pertinent because it's so similar to "boat", even though for this particular example the word "ship" didn't occur.  Using this line of thinking the absence of a word isn't a feature with value 0, it's the absence of information about the word for that example.

So how does that change things?  First, it means that when you consider P(c | word1 word2) even if there were other words that might have been there but were not you'd simply be using those two words, resulting in a calculation that multiplies three terms, P(c)P(word1|c)P(word2|c).  Other words don't play a role in it, even if they occur in other examples.  If some other example you want to label has 4 words and you're computing P(c|word3 word4 word5 word6), you'd end up multiplying 5 terms together, P(c)P(word3|c)P(word4|c)P(word5|c)P(word6|c).  Here word1 and word2 would not be part of it, even if they occur for other examples.  (And, because we're using tfidf instead of computing P(w|c) as (#examples of c with w present)/(#examples of c) we compute tfidf(w,c)/(#examples of c).)

Note that this still gives us the problem that led to Laplace smoothing, namely that if you're classifying an example that has word1 but one of the classes you're considering has no examples of word1 you'd get a zero for it.  So we want to use the pseudo-count approach to get past this.  When a feature took on some set of values the denominator would add the size of that set to the denominator (or α times that in the more general form).  What should the corresponding thing look like with this different way of approaching features, where we're only multiplying together probabilities for the words that occur in the document?  The common way to do this is to think of each word as a priori having equal probabilities of occurring for any category.  If there are n possible words that occur across all the messages this means P(word1)=P(word2)=⋯=P(wordn)=1n.  So what we want as a default if there was no data whatsoever is for the probabilities to default to 1n.  This corresponds to having 1 in the numerator and the number of words overall in the denominator.  So, unlike the case from class where we think of the presence or absence of a word both having probability of 1/2, we're treating it as a value which has a 1/n chance of occurring.  So whereas before P(w|c)=tfidf(w,c)N(c), we need to add appropriate terms to numerator and denominator so that in the absence of data we get the 1/n probability.""",
    """HW 5 Problem 3 Notation
I'm a bit confused by the notation in the subscripts; I noticed that part A refers to wic, but part B uses wcj.  I was wondering if the order of the subscripts is supposed to be different here? Also, when summing over classes or features, is using c or j recommended?""",
    """Hierarchical bottom up clustering vs centroid-based clustering
What is the difference between hierarchical bottom up/agglomerative clustering and centroid-based clustering? I'm a little confused because the diagram showing agglomerative clustering in the lecture slides from 5/4 look to me like some sort of centroid-based clustering is happening, where the centroids are updated after each new point is incorporated into a cluster. Thank you!""",
    """Tuesday 9 am office hours
Hi! Are 9 am office hours happening today? It's 9:25 and I don't think the ta has started the meeting.""",
    """HW5 Q1c
For 1c do we use the more complicated version that has the log term (tfidf, given in part B) to calculate the likelihood?""",
    """Quiz 10 Review Question 5
The solutions for question 5 state that only one iteration is required for the algorithm to halt, but the table shows two iterations. Does the first round of assigning points to the closest centroid not count as an iteration? Thanks!""",
    """k-means clustering
Besides time complexity, is it possible there could be a difference in the clusters formed by the k-means algorithm if the algorithm stopped after convergence and if it continued to run even after convergence? Also, is the algorithm guaranteed to converge for any set of examples and initial centroids?""",
    """Quiz 9 Question 2
Hi, I am confused as to how it would be possible for policy iteration to change its policy from the optimal one. Doesn't policy iteration require that if a policy is to be updated then it needs to be a strict improvement upon the previous one?""",
    """k-means clustering (two centroids with same point in space)
Is it possible for two centroids to be the exact same point in k-means clustering? I read elsewhere that k-means is a form of partitional clustering, which does not allow clusters to overlap, so I'm guessing it's not possible, but I'd appreciate if this could be confirmed.

Thanks!""",
    """quiz 10
wait just to verify, the quiz closes at 1 pm on may 13 or at noon or at 4 pm?""",
    """Quiz10 P1
I verified the problem 1 by the link below:

I add four points, and set 4 clusters. The iteration number is more than 1. So the statement must be false.""",
    """Another bug in Q10 P1
According to PreQuiz 10 Question 5, the end after first iteration means following:

there are one update on centroids, thus the answer said there are only one iteration.

but in Quiz10 P1, since there's no update on centroids, it will end in zero iteration. Rather than one.""",
    """5/14 6PM OH
Hi,

I can't get into Liz's OH because Zoom says the host has locked this meeting room. Ashneel's meeting is empty (I am the only participant when I join). How can I get into an OH?

Thanks""",
    """Collin’s OH Tonight Delayed by About 5-10 Minutes
Hi everyone, my office hours will be delayed by about 5-10 minutes. For this reason, I will extend my office hours by 5-10 minutes. And please feel free to reach out to me if you need extra help and now cannot make it to OH tonight, and I can set up another time for later tonight. Sorry for the inconvenience.""",
    """Zoom changes on May 24 and 30
Just FYI:

On May 24 there's going to be a change to all Zoom lectures/meetings/seminars: All such meetings must have passwords, in addition to the usual authentication protocols.  This will not only apply to any new meetings in the future, but will also be applied retroactively. Thus I am told that I need to add passwords to all my past lectures (or else they will be added for me).  That shouldn't affect most students in CS 4700 since the class is pretty much done for students, but I'll nonetheless hold off until the date gets closer, in case the changeover has glitches and interferes with anyone wanting to refer back to the lectures.
On May 30 you will need to use Zoom version 5 or higher for lectures/meetings/seminars.   To update your copy launch Zoom, click on the profile picture at the top right, and click on Check for Updates.  Or wait until May 30 and Zoom will prompt you automatically.
They've also helpfully informed faculty that Zoom will be offering no support to individuals in May and June, so if you run into any problems you will need to seek help from Cornell IT people.""",
    """Census information
Not about 4700, but figured I'd pass it along as general interest.  I'm told that for census purposes you're treated as living where your college is rather than where COVID-19 has landed you.  If you lived on campus for example Cornell submits info about you living there even if you're not currently living there.  More at link.  (I know nothing more about this, this is just a public service announcement.)""",
    """Quiz 9 1a
The 1a of quiz a put forward an example of an non-optimal Q-learning. I'm curious because textbook says Q-learning is always optimal: 

"Q-learning learns an optimal policy no matter which policy the agent is actually following (i.e., which action a it selects for any state s) as long as there is no bound on the number of times it tries an action in any state (i.e., it does not always do the same subset of actions in a state). Because it learns an optimal policy no matter which policy it is carrying out, it is called an off-policy method."

Can someone explain that for me? Thanks.""",
    """Reporting Karma Lectures
Hi, I noticed there was a question about reporting Karma lectures in which this response was given “ I will be sending out a "quiz" asking for this information sometime in the next few days.

[UPDATE]: There is a Canvas survey live which you can use to report karma lectures. It will be available until 5/16 at 11:59pm EDT. You can find it by going to "Quizzes" on Canvas and scrolling to the bottom (it is listed as a Survey).”

I was thinking we would receive notification or an email or an instructor piazza post on this :( I missed this deadline since this was announced as a reply to a post I was not a “part of”. This post might’ve been pinned but we still got no notification of it since it was pinned retroactively on a student post after a instructor response update. Is it possible this quiz be reopened for a short amount of time with an announcement so that all students can be aware of it? 

Thanks""",
    """overall course grades have just been posted in Canvas
If you go into Canvas you will find an assignment called "Overall Grade".  That is your final grade for the class.  Please make sure that if you are taking the class for S/U that you don't have a letter grade, and vice versa.  (It was ultimately something I had to do manually.  I checked it over multiple times, but there's still room for error.)

I am posting the grades now so that you'll have this in time for the May 23 deadline for changing grade basis/withdrawing with a petition.  I suspect the May 23 deadline was picked without the expectation that students would actually have final grades by now, so I won't do the formal grade submission process for a couple of days, just to make sure it doesn't inadvertently get in your way if you do pursue that option.""",
    """explaining answers
There were some questions about whether you have to give an explanation for your answers to the homework questions.

My general rule is that if a question doesn't ask for an explanation you don't need to give one - whether on a homework or an exam.  However, I also always encourage giving an explanation, since if you get an answer wrong the explanation might get you partial credit.""",
    """textbook exercises
Recall that exercises for the textbook can be found in a github repository at link.  Here are some exercises you can try that might be helpful in preparation for the prelim.  (I will post some further questions later today.)  Note that the number of exercises per chapter does not reflect the expected distribution of exam questions but rather simply reflects what I think are good exercises.  (I was hindered in the case of some chapters - particularly MDPs and Reinforcement Learning - by exercises referring to figures that were not present.)""",
    """academic integrity in difficult times
I'm not sure how widely this has been distributed, but the university released a new academic integrity statement in light of our reliance on online teaching and assessment this semester.  You can find it at link.

At some level you already know what it says.  You know when your behavior is admirable and when it is not.  My responsibility is to be clear about where the boundary is, much of which is already laid out on the original course website.  I will continue to do my best to do so as we move ahead.  For example, you may wonder if quizzes are open or closed book and notes.  I don't know yet, I still need to come up with some of the quiz questions that I plan to use before making that decision.  But either way I will let you know ASAP, before the quizzes start up, so that it's not a question for you.

I've thought a lot about how to manage academic integrity issues in our new course setting.  Talking about it solely in terms of rules and punishments avoids having to confront the underlying causes of academic dishonesty, so let me briefly turn to that.  Those who make college academic integrity a topic of their research have compiled list of common reasons for why students cheat.  Pressure to get high grades is one of them, and we have a lot of that here but we also have this semester's unique S/U policy, which is about diminishing that pressure. Another is parental pressures, which I also discussed in my earlier note.  Another is pressure to get a job, and I've also already discussed the neutral position of this semester's S/U grades on job search.  Another is a desire to excel, which is an admirable trait that you should maintain, but with an understanding that doing so through dishonesty isn't actually excelling it's cheating.  The other reasons they have identified for cheating?  Laziness, lack of responsibility, lack of character, poor self-image, a lack of pride in a job well done, and lack of personal integrity.  None of which I believe you will want to see when you later look into the mirror.

We are in a time of stress.  How we behave under stress reveals our character. This is both a statement about each of us individually - what we would want to see in the mirror when we look back at this time - and about our society and what values we believe it embodies.  It's also a statement of putting your trust in others, that they will similarly exhibit the best of behaviors.  If you find yourself in a situation where you are tempted to violate Cornell's academic community standards, don't.  Contact me about what in your life has made it difficult to keep up with the course within the behavioral expectations of being a Cornell student and let's see what we can do about it.  Notice that I didn't say come see me and tell me why you want to cheat, because what I'm seeking isn't just something to do when you feel like cheating.  Please let me if there are forces in your life that are making progress in the course in our current circumstances difficult for you.""",
    """further information about CS 4700 quiz
The first quiz for CS 4700 will be executed on Canvas.  Here is further information about how that will work.

The quiz window will open on Canvas Thursday, Apr 9, at 12 noon EDT and will remain open for 24 hours.
You will have 20 minutes to take the quiz.  If you have documented for us a special accommodations need that involves the timing of exams it will be implemented for all quizzes without your needing to do anything about it.
Questions will be a combination of True/False, Multiple Choice, and Short Answer.  You will not need to do draw pictures or scan in images
The exam will be open book, notes, and Internet browser (especially since the book and my slides are situated online).  You might find it useful to have some scratch paper and a pen or pencil available if there is something that you'd like to work out.
You are not to consult with others during the quiz, and must not share information about its contents with others.
The topic of this quiz is uninformed search methods, which is the material that was covered in lectures 2-4 of the class.
The prelim preparation questions that I prepared last month (link) include examples of the type of questions that you might get.  Question 1 includes sample True/False questions of the sort that could be on the quiz, and questions 1a-c are on topics within the scope of the quiz.  Question 3 includes sample short answer questions of a similar nature, and 3a-c are on topics within the scope of the quiz.  These questions also give you a flavor of the style of the questions that you will get, asking questions that should be readily answerable if you understand the material without it being about factual information that you could easily look up in the book or notes.

(This is my current best guess for how to do quizzes.  I'll see how this first one goes, and may adjust details of future quizzes depending on the experience.)""",
    """solutions to prelim prep questions relevant to quiz 1
I'm attaching to this post the solutions to the questions among the prelim prep problems that are relevant to quiz 1.""",
    """HOW TO Ask Lecture Slide Questions
To help us provide you with high-quality answers on Piazza and to help us answer everyone's questions as quickly as possible, whenever you have a question about lecture slides please include...

1. The title of the lecture

2. The slide number

3. What you are confused about

Thank you!""",
    """IMPT FOR QUIZZES: Browser Information
Students have run into issues using Safari for quizzes. We recommend using Chrome on Mac.""",
    """send emails for me to FAI-L@Cornell.edu and put "4700" at the start of the subject
Just a reminder to everyone: If you're going to email me, do it via FAI-L@Cornell.edu and put "4700" at the start of the subject.  I'm getting massive amounts of email right now, and I'm finding that I'm missing some 4700-relevant emails that are sent directly to me.

If you've sent me a 4700-relevant message prior to today and I've missed it, please resend it as above.""",
    """Grade estimates posted in canvas
[Please see @341 for further context for this post]

Grade estimates calculated by Prof. Hirsh have been posted on Canvas. It's important to emphasize these are just estimates and estimates typically come with error bounds. The general idea here is that if a student does comparably the rest of the semester to where they are now their final grade would be within a half grade of what is listed.

Here is how the grade estimates were calculated:

For the "Grades Thus Far" grade for each student:

Q1 and Q3 were used to compute the Thursday quiz score (37.5%)

Q2 and Q4 were used to compute the Tuesday quiz score (37.5%)

HW1-3 were used to compute the homework score (25%)

It includes all updated grades for items where the regrade window has ended.

It includes the +/-5% adjustment of highest/lowest score across the three categories.

It does not include consideration of Karma Points.

 

For the "Grades with Media" grade:

Grades were assigned for all the missing quizzes and homeworks for the rest of the semester.  For each category if the student’s score in that category was above the median for the class for that category, the student’s score was used for the missing entries.  If the score was below median, the median was used for the missing entries.

Otherwise everything was identical.

If you do not have grades for these assignments, please email fai-l@cornell.edu and we can resolve that issue via email.""",
    """status check
As everyone no doubt has seen, Canvas now has "mock grades" for you based on your work this semester, together with what you might get if you perform at median for the rest of the semester if you're currently below that.  It's intended to help you understand how you're doing and what the S/U question might mean for you.

More generally, please use this as a chance to pause and reflect on how your semester is going.  Some students are facing relatively modest difficulties coping with what COVID-19 has thrown their way and others are facing massive challenges.  If elements of your life right now are intruding in your ability to perform as you'd have liked in CS 4700, if you haven't been in touch with me about it already please don't hesitate to do so.  You would not be the only person facing challenging times, and we can see what might make sense for 4700 given your situation.""",
    """checking in one last time
Dear students,

I'm writing one last time to check in on how things are going for you concerning CS 4700, and particularly to check in on students who are facing the most difficult of struggles in being a student as this semester draws to a close.

You received my earlier "mock grade".  Just about everyone in the class was in range of an S grade.  If your work since then continued at your prior level you should still be on track for an S.  Some of you were sufficiently strong that even with a decline in subsequent coursework you'll continue to get an S.

I'm writing specifically for students whose circumstances are sufficiently difficult that they are struggling to keep afloat for this last part of the semester.  You know how you've done in your coursework since the mock grades (Quiz 8 grades should be out later today).  At this point there are two quizzes and one homework left to the semester (or just one quiz if you've already taken Quiz 9).

I'm checking in asking for you to take a moment to introspect and be honest about how things are going for you.  I don't mean like whether you wanted an A and are on track for a B.  I'm asking you if you are struggling to get the barest of work done.  Is it difficult to even get around to taking quizzes or are you taking quizzes despite knowing that you haven't kept up with the class?  Does it look impossible to get through HW 5 because of what's going on in your life?  Some of you have been faring ok since classes were suspended.  Others are facing some challenges but are muddling through.  What I'm writing about are students who have been facing circumstances that are undermining their ability to be a student at the most basic of levels.

This isn't something that I can tell.  I need you to pause and assess whether this describes your situation.  If it does and you have not reached out to me please absolutely do, and do so now.  While whatever challenges that you're struggling with will undoubtedly be uniquely your own, you are not alone if you are facing severe difficulties in getting through 4700 this semester.  I've made sure everyone thinks seriously about S/U grading, but it's not the only option available if things are severe enough for you.  Unfortunately, some of those options go away if you approach me after classes end, so I'm asking you to let me know over the next few days if what I've described above applies to you.

I'm sending my best wishes to you all, but a little bit more of them to those that need it the most.  If I can be of help please let me know.

Haym Hirsh""",
    """Quiz 8 Grades Posted
Quiz 8 grades have been released on Canvas. Regrades will be accepted until 1:00pm EDT on Friday 5/15.

The quiz was out of 10 points; the mean was a 92% with a standard deviation of 2.2.

Solutions are on the course website.""",
    """last lecture: societal implications of AI
One last lecture, one last quiz, one last homework submission, then CS 4700 is over for you.

During the first lecture I noted that is the most exciting time for AI in its entire history because of the dramatic and widespread success that it's seeing.  It's going to change our world, in many positive ways and likely negative ways too.  It's important that you understand the societal implications of AI, both for your own benefit but also so that you can be a resource to others who may not have an AI course under their belt.

Nothing from this last lecture will be on a quiz.  However, it's a mandatory lecture, either live or via video.  This is my own way of playing a role in public discourse about AI and the future of our world, by exposing the students in 4700 to our best understanding of what may be ahead.  I hope it gives you some ideas about how to think about AI on more than just a technical dimension as you move ahead in your lives.""",
    """topic of last quiz: k-means clustering
Quiz 10 normally would cover material from the three CS 4700 lectures that took place last week.  I'm really pleased with the guest lectures given on Wed and Fri about Natural Language Processing and Computer Vision.  However, while they did a create job of depicting the landscape of work in those two areas, they were at a sufficiently high level that there really wasn't enough meat to ask anything but the most superficial of quiz questions about them.  I'm posting this note so that you'll be aware that the last quiz will only be about k-means clustering, the topic of the Monday lecture.  I'll be posting prep questions later today, once I complete the solutions.

That said, NLP and Computer Vision are two areas where AI is having the greatest impact.  We don't cover it in much depth because we have entire courses on each of them.  So, whether or not I'm testing you on the material, it's rare that you get self-contained 50-minute lectures on these topics just for you, designed with knowledge of what we've covered in 4700.  Whether or not you watch the lectures will have no impact on your course grade.  But from a practical standpoint if you're, say, interviewing for a job and someone sees AI on your transcript it would be nice to have superficial understanding of the topic, and intellectual scaffolding for going into it in greater depth should circumstances warrant.  So watch the Monday lecture (if you haven't already) most directly because of the quiz, and the Wednesday and Friday lectures because it's good for you.""",
    """Reporting Karma Lectures
How should we report the karma lectures we've viewed this semester. Should we email the FAI-L email account?""",
    """grading basis/course withdrawal deadlines reminder
Some reminders for everyone:

Today:
Today is the last day you can change classes to S/U.
Today is the last day you can drop classes without it appearing on your transcript with a W.
May 23:
You have until May 23 to drop a course with it appearing with a W on your transcript.  I am aiming to get CS 4700 grades completed by then to help those who want to make this decision in light of their final grade.  I will post something on Piazza when grades are available.
The special rules that Cornell set for this semester also stipulate that you can petition to change the grading basis to S/U until May 23.  This is not a decision that it is my hands, it is up to the specific college that you're in.  I do not know the criteria that they will use for this, or even if the colleges will be consistent in how they handle this.  However, in my unofficial experience the colleges are reluctant to grant petitions like this unless there is something truly significant that happened after the normal deadline, and I'm guessing that's especially so given that in this case they are only 11 days apart.  If you have any questions about this facet of the special COVID-19 registration policy please reach out to your college advising staff as early as you can - I am sure they have an exceptional number of students reaching out to them as the semester draws to a close.""",
    """Quiz 9 Grades Posted
Quiz 9 grades have been released on Canvas. Solutions are posted on the course website. 

The quiz was out of 20 points; the mean score was a 61% with a standard deviation of 5.7.

Regrades will be accepted until 1:30pm EDT on Tuesday 5/19.""",
    """Quiz 10 Grades Posted
Quiz 10 grades have been released on Canvas and solutions posted on the course website. This was the final quiz of the semester (you did it!).

The quiz was out of 15 points; the mean score was a 82% with a standard deviation of 4.4. 

Regrades will be accepted until 1:30pm EDT on Tuesday 5/19 (note this is a 6 day window not a 7 day window to allow us to finalize grades in a timely manner).""",
    """Course Evaluations
It's a weird semester, but course evaluations are still useful.  Just a reminder that you have until Friday to fill out course evals.

[ADDED]: Please also fill out TA evaluation forms as well if you had significant interactions with a TA (typically in office hours). Just like for the main course evaluations, these are useful for our staff.""",
    """HW5 Grades Posted
HW5 grades have been released on gradescope and solutions posted on the course website. As always, the grade does not reflect the 50% late penalty, which we calculate offline.

Statistics are below.

The regrade period is short for HW5 in order for us to be able to calculate your final grades well before the 5/23 deadline. Regrades are only accepted until 1:30pm on Tuesday 5/19 through gradescope.  This means please review and submit any regrade requests ASAP!""",
    """Remaining Due Times
This is a reminder that you have until tomorrow to do the following tasks. No further extension will be given in an effort to have your final grades calculated in a timely manner.

11:59am EDT tomorrow (extension)

Karma survey on Canvas
1:30pm EDT tomorrow

HW5 regrade requests
Quiz 9 regrade requests
Quiz 10 regrade requests""",
    """academic integrity violations with Karma Lectures
I am very pleased with how many of you saw value in watching various karma lectures this semester.

I had planned to use students' self-reported data on which they watched.  However, because all videos were restricted to Cornell NetID authentication it was simple enough for me to download the data on who watched which videos to check on this self-reported data.  I am sad to report that for some students the data from the logs reflects far fewer viewings than their self-reported data.  This is a violation of academic integrity.

I have not yet done the full collation of the data.  I understand that this was an unusual and difficult semester that might have led some to exhibit poor judgment about this, so what I've just done is reopen the quiz that was used to gather data on Karma Lecture viewing to give those of you who provided false information a chance to correct your misstep.  It will remain open until 10am EDT tomorrow morning, May 22.  This is a chance to take ownership of and remedy a bad decision that you might have made.  If you do so I will treat this solely as negative karma points.  Recall that karma points only impact you if you are just below a grade threshold, so negative karma would mean that I wouldn't choose to bump you up to the next grade (and if you're going S/U would only impact you if you're just missing a C- grade).  Any significant discrepancies that remain after the quiz closes tomorrow will be treated as academic integrity violations.

(If you are worried that maybe you misremembered which lecture you watched and/or clicked on the wrong item don't worry, this isn't about you.  I anticipate such small errors when considering karma lecture data.  This is about the students who fabricated much larger numbers of viewings than actually occurred.)"""
]
