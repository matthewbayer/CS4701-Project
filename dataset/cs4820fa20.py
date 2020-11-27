data = [
    """Zoom link?
Considering class starts in 15 minutes, if anyone could tell me where to find the zoom link for todays lecture that would be fantastic.""",
    """Zoom sign in problem
When I used cornell email to enter the zoom, it told me "This meeting is for authorized participants only". How can I deal with that?""",
    """Website
Does anyone have a link to the website? I can't seems to find it.""",
    """Grading
I saw in the syllabus that we are headed based on class participation. how does that work?""",
    """HW1 location
Where can we find a link to Homework 1?
Thanks!""",
    """C++ for HW assignments.
If I recall correctly there are a number of languages allowed for the programming questions, to include C++. Which compiler/C++ version will this be, and will there be any extra flags such as -Werror that we need to worry about?

I just want to ensure that any headaches are avoided early on, since I plan on using C++. Thanks!""",
    """Lecture Recording
around what time can we expect the recordings to be uploaded each day? the website said as soon as possible, but just wondering since we'll have to keep checking the course website

thank you!""",
    """Is LaTeX required for homework submissions?
Will handwritten assignments be accepted/pictures for diagrams?""",
    """Office Hours Notes
Would it be possible to have the notes from office hours today also posted on the course website (when you get the chance)?""",
    """[HW1] Crossover games.
"In addition, each team will play crossover games with two teams from the other division, one at home and one away."

I'm unfamiliar with what a crossover game is. I realize the directions talk about ambiguity; should I make my best guess, or is there a simple definition for this?""",
    """Lectures on HW 1
What lectures are HW 1 based on? Thank you""",
    """HW Formatting
In the LaTeX template for HW, there are spots for the questions as well as the subparts. Should we copy-paste the question again in our solutions, or would it be fine to just write the solutions and leave the headers as "First problem", "First subproblem", etc?""",
    """Switch the page order of the second scanning class notes
Hi guys,

When I review my class notes with the class notes published by the professor, I found out that the page order of the second scanning notes is a bit wrong. The order of Page 2 and Page 3 should be switched. Just a kind reminder for someone who feels confused if they did not attend the class today.""",
    """Confused with partial order and preference
A total order must be a partial order, and a partial order must be reflexive (every x has a relation to itself), but we can't prefer one thing over itself, so I'm confused why preference (< in lecture note) is a total order.""",
    """Office Hour Recording
I was trying to read through the notes for last oh and couldn't understand it. So I was wondering if it is possible to also have recorded videos for office hour right after class since some of the students might not be able to attend office hour right after because they have classes to go to?""",
    """Captioned video delays
It may be a while before we can post a captioned version of the lecture videos due to technical issues with the video captioning site.""",
    """Please do not email me about enrollment
Students: If you are already on the waitlist and already enrolled in CMS, please do not email me about enrollment or overlaps with other courses.

For instructions about overlap, please see

For waitlist information, please see

If you are not on CMS, please email me with your netId and I will enroll you.""",
    """HW 1 Supplement Example
For the example word problem presented in the HW supplement, I was wondering if it's also acceptable to minimize the sum of the least squared error, i.e., rather than minimizing the maximum difference of the number of problems each staff member grades, as in the solution.""",
    """Partner-finding social
Message from WICC:

Dear Professor Kozen,


Hi, my name is Anna and I’m the social co-director of Women in Computing at Cornell! This semester, we are holding a CIS Partner Finding Event for students to meet other people in their CIS classes to find friends or potential partners. Would it be possible for us to advertise our event in your class(es)?


The event will be held on 09/08 from 7:30-10:30PM EDT using the Glimpse platform. It will be split into class levels: 7:30-9:00PM for 1000 & 2000 level classes, and 9:00-10:30PM for 3000+ level classes. Students will need to RSVP to this form in order to receive the event link: . Below we have attached the event cover containing the necessary information. Please let us know if you have any questions or policies that we should take into account.


Thank you for your time!


Best,

Anna Nguyen""",
    """Can we specify presence or absence of cycles (of specific length) in our answers to problem 1?
see above""",
    """Problem 1
In class, we defined a matching between two sets X and Y to be a subset such that every element of X and every element of Y shows up at most one time in a pair in S. Perhaps a more flexible definition would be to allow every element of X to be matched up at most one element of Y and to allow every element of Y to be matched up with at most k elements in X for some fixed k. This would model the company-employee situation better. Problem 1 says to formulate certain problems as "matching problems on graphs". Could I formulate it as a problem with the more flexible definition that I gave?""",
    """1a More than 2 divisions?
Since the HW 1 intro says to not restrict to the problem sizes as given here, should our formal specification consider if there were more than 2 divisions, for example 4 divisions North, South, East, and West where teams play two teams from all other divisions?""",
    """1b Sudoku 3x3 boxes
Can we describe a helper function that outputs the 3x3 box number of a square? e.g. outputs these red numbers:

I remember we had a similar Sudoku question in CS 2800 where we were allowed to do this so I just wanted to check if we can do that here as well. Thanks!""",
    """3 network shows
I am not sure whether I understand problem 3 of HW1 correctly. " We’ll say that the pair of schedules (S, T) is stable if neither network can unilaterally change its own schedule and win more time slots. " Can we assume one network's show is fixed when the other changed theirs? And they take turn to change their scheduler?""",
    """2 - assume weakly connected
For problem 2, can we assume that each employer provides a graph (or equivalent list of preferences) such that the graph is weakly connected?""",
    """Q2 define equivalence relation
Hi,

For question 2 if we define a equivalence relation based on directed paths/cycles (as in the hint), do we need to prove this is an equivalence relation?

Thanks!""",
    """Functions created from formulating a problem
Is it ok if we use a partial function instead of a total function to formulate a problem?""",
    """Homework thoughts
A couple thoughts about the homework:

Please refrain from posting ideas or constructions that could be part of a solution publicly to Piazza. This is officially a violation of the course academic integrity policy (see the website). If you wish to post part of a solution, please post privately.

In general, the answer to the question, "Do I have to prove..." is: Yes, give a short argument. The reason for this is twofold: 1. It is good practice. 2. Even though it may be obvious to you, it is often not obvious to us that it is obvious to you. Don't make us guess!

In general, the answer to the question, "Can I assume..." is: Yes, make whatever assumptions you need to make to solve the problem and do a nice job under those assumptions. You may lose some points if your solution is not sufficiently general, but do what you need to do. We would rather see a nice solution to a restricted version of the problem than an incorrect solution to the more general problem.""",
    """Proof that every GS execution provides a the "best" matching for men.
In OH this morning, Prof. Kozen explained the following proof of why the GS algorithm always provides a "best" matching for every man. I thought others might be interested in the proof in case you missed the explanation. Also, you can refer to the textbook for the full details (page 11). If anyone has any comments or suggestions for the proof, feel free to say.

Defn "best": for an arbitrary man m, let best(m) be the highest-ranked women, (in m's ranking) for which there exists a stable matching, M, with (m, best(m)) exists in M.

Claim: best is 1-1

Proof: Suppose there is an execution of GS, e, in which a man, m, is the first man who is rejected by his best valid partner. Then, m would have been rejected by a woman w (his best valid partner) in favor of another man, m1.

However, given that w and m are valid partners, there must be another stable matching S1 in which (m,w) exists. Now we ask, who would m1 be matched with in S1? Assume, for the sake of contradiction, that m1 is matched with a woman w1 ≠ w. We know that w prefers m1 to m, because in our initial execution, e, m is rejected by w in favor of m1. We also know that in e, m was the first man to be rejected by a valid partner. Therefore, in e, m1 had not been rejected by any valid parter at the time at which (m1 , w) was formed. Therefore, m1 must prefer w to w1. Therefore, in S1, there exists an instability in that w prefers m1 , and m1 prefers w, however (m1 , w) does not exist in S1. Because of this instability, we must reject our inital assumption that "there is an execution of GS, e, in which a man, m, is the first man who is rejected by his best valid partner."

Finally, every man must be paired with best(man) at the end of GS, and best is 1-1.""",
    """Q3- networks have different shows
Can we assume that the n TV shows of network A are distinct from the n TV shows of network B?""",
    """Auditing
We had a question about auditing in class and I said I would post something. I believe auditing in-person or hybrid classes is disallowed by the registrar, but since we are fully online it does not apply to us. So to the best of my knowledge, there is no restriction on audits in 4820.""",
    """Q3
The question asks to provide an algorithm to reach the given defn of stability for "any set of TV shows and associated ratings" with no mention of networks - does this mean that, for example, we would assume some arbitrary list of shows/ratings and in our algorithm/answer dictate how we divide them up among two networks?""",
    """Q1: Matching problems vs finding functions
Since the question tells us to formalize the word problems into matching problems with graphs, does that mean we should not be defining the problems using functions? I wasn't quite sure and was a bit confused on the difference between the homework question and the formalization example in the supplement.""",
    """Will any homeworks be dropped?""",
    """Q2 orders and preferences
I'm having a lot of trouble understanding orders and wanted to check if I'm understanding this right--sorry if this is supposed to be really basic material :(

Partial order: if  and , then x=y in terms of preference lists would mean that if a man prefers w over w' and w' over w, then w = w', (and same for women's preferences), so basically there can't be any ties in preferences?

Total order: for all x,y, either  or  means that for a man, every w and w' can be compared and one is more preferable (and same for women's preferences), so basically everyone is comparable?

Preorder: Since we don't have antisymmetry, we could have x≤y and y≤x without x=y, so a man m could rank w and w' equally on his preference list?""",
    """HW1 Supplement Example a Matching Problem?
I know that we introduced matching problems in the context of problems like those faced by colleges and students or employers and employees, in which the vertices of one set can belong to multiple edges. I was wondering if the HW 1 supplement example about graders and problems is considered a matching problem. Also, should we know what algorithm solves this minimization problem?""",
    """The question in the supplement regarding graders and homework problems is a form of matching problem. However, it's not one that is naturally solvable by Gale-Shaply. Gale-Shapley is used for matching people in group A to people in group B, where all members of group A and group B rank the members of the other group.

There is no concept of ranking in this problem. We just need to assign graders to problems in a way that satisfies those constraints. This problem is known as a network flow problem. No need to worry about this now, you'll learn all about them in about a month or so into this course. The basic idea, if you are curious now, is you encode the constraints into a graphical network and push "flow" along paths in the network from source to sink (see Ford-Fulkerson algorithm).

So you do not need to know the algorithm that solves this minimization problem yet. We gave you this example as an introduction to what a reduction is (see @46), where you take a word problem and translate it to a new problem solvable by a known algorithm. We are just asking you to understand the idea of creating this construction -- not applying any algorithm just yet.""",
    """Q2 algorithm in English/pseudocode or math/graphs
Just to clarify, for question 2 would we provide the algorithm in English pseudocode style like this from the book, or using math notation like in terms of nodes, edges, and for preferences?""",
    """Q1
Since we do not have to solve a problem but simply formalize it mathematically, is it enough to say that the goal is to find a perfect match? As in, we do not need to say how the perfect match is found, but simply stating where a perfect match should be found in pairing the teams together.""",
    """What will the quizzes be like?
Are they synchronous online during the lectures or separate? Thanks!

What topics would they cover/how many questions?""",
    """HW1 1a Can only schedule games on weekends?
I'm unfamiliar with how rugby works (and sports in general) - This problem seems to imply that games only occur on the weekends. Is it true that we can't schedule on weekdays?""",
    """Q3 how to approach questions like this
Any tips for how to approach questions like this where you either give an algorithm or find an example that proves it isn't possible? Like should we start by just trying out some examples based on intuition to see if we find one that proves it isn't possible, or try to come up with an algorithm and find a contradiction in its proof?""",
    """Consulting Hours
Will all consulting/office hours will be in group settings or will 4820 implement some sort of queue system eventually so people are able to receive 1-on-1 assistance with questions they may have? """,
    """Q1 "interesting versions of unbounded size"
For Q1 it says "You should not restrict to the problem sizes as given here, but try to formulate interesting versions of unbounded size." so which factors in the rugby and sudoku problems should we make changeable, or is this up to our interpretation?

For the rugby game, I feel like we could change a lot of factors:

number of teams
number of divisions (asked earlier and was told that we can stick with 2)
number of games allowed per weekend
number of within-division games needed
number of crossover games needed
but for Sudoku, I feel like a lot would need to change together at once if we change any factors:

possible digits (hexadecimal Sudoku???)
box size (3x3 -> ?x? boxes)
column/row size
Is there a specific list of parameters we should be able to change, or is it up to our interpretation?""",
    """HW 1a
Just to double check what I heard in OH, we don't have to use math notation for 1a and can instead just use plain words to describe it?""",
    """HW1 Q1
Just to make sure, does our answer for 1) have to be in the form of a matching problem (i.e. you have a set A and set B, and a solution counts as a set of edges E that maps nodes from A to nodes of B), or is our answer valid as long as we formulate the question as a graph problem and make connections to what the edges/nodes would be? """,
    """General: how to know if you're on the right track
When I read explanations like the cornell class grading example in the supplement or the instructor response in @46, it makes sense to me and I understand how that solution satisfies the problem. But I'm having a hard time writing my own solutions from scratch. How do I know if I'm on the right track, and how do I get myself to think like that? Any tips? """,
    """Zoom Participation
Is participation during class (on Zoom) considered too, or is it just Piazza?""",
    """Comparing A to O for Interval Scheduling
At the very end of class it was explained that in our proof by induction we would want to show that for every r>1, the end time Someone asked in the chat if this comparison should be greater than or equals to, but the answer was no; however, in the textbook it does say which makes sense because we only have to prove our algorithm provides a solution that is at least as good as an optimal solution.

I just wanted to confirm what the correct comparison is for the proof. Thanks!""",
    """Citing Homework Supplements?
For homeworks, I understand we don't have to cite the text if we use it, but should we cite the Homework Supplement if we use it?

Thanks!""",
    """Ambiguity in formalizing problems
If there is an ambiguity in the questions (such as the followup discussion @18_f1), can we go with our best judgment? Or will points be taken off if our interpretation isn't the "correct" one?""",
    """Question 1 (a) the number of game
Question 1 (a) state that "In addition, each team will play crossover games with two teams from the other division, one at home and one away."

I just want to clarify Is the number of crossover games each team engages is 2 or 4?

I think it will be 4 because having games once at home and once away with each team is more likable in real world (due to fairness issue). But sports is not my area, so I am unsure about it.

P.S. It is on debating in followup question on post [HW1] Crossover game, but I think the instructor's clarification is needed.""",
    """1a
Should there be one game per weekend or multiple games per weekend as long as the same team isn't playing twice?""",
    """Office Hour Change to 3:30 PM - 4:40 PM
Due to a change in my schedule, I'll have to end my original office hour time (5 PM) earlier by 20 minutes. To compensate for this I'll start 30 minutes earlier today (3:30 PM). Apologize in advance for the inconvenience.""",
    """Q2 proof of correctness
I've asked about this in office hours but got different answers so I wanted to ask on here as well.

For 2, it says "Given the graphs specifying the preorders for the employers and candidates, do a precomputation that reduces the problem to the original version discussed in class." so basically we perform a precomputation and then use Gale-Shapley.

To me it seems like precomputation is kind of already explained in the homework help document, and we've already proven Gale-Shapley in class, so what should we include in our proof of correctness? Are we supposed to prove that our precomputation is valid, like the result of our precomputation maintains the original preferences from the pre-order graphs?""",
    """2: Cycles in graph
I thought cycles were allowed to be part of a preorder graph, but the sentence, "We write x < y if x < y but not y < x" in the homework question implies that the given graphs in question 2 are acyclic. Does this mean the group rankings are not allowed to have cycles, or could cycles exist?""",
    """why is "if v = best(u) then u = worst(v)" true?
I'm a little bit confused with this claim: if v = best(u) then u = worst (v). What if u' prefers v' to v, v' prefers u' to u and we match u' with v'. Then best(u') = v' and best(v') = u', but worst(v') = u which is not u'.

Thanks!""",
    """q1 number of teams
Can we assume the number of teams is an even number?""",
    """P2
In the file HW1-help, it says that we can solve P2 by 'extending the pre-order represented as G to a total order G'. I am curious as to whether our extension will cause the proof to be less significant than the original form.

For example, during the last step of extension, we use topological sort to add new edges to make the graph a total order, does that mean we are 'adding' information that is not present in the original problem? If the initial pre-order has no edge between two strong components, why can we order them and prove stable matching with the total matching (G')? """,
    """"Invoking an algorithm" for Q1
Is this essentially what we need in our solution for Q1?

   - what nodes and edges mean in terms of the context of the problem

   - the properties that a graph solution would entail and how the constraints given were translated into such properties

Do I need to cite an algorithm that's capable of creating the actual graph solution?""",
    """What is Q2 Asking For
I'm a little confused about what Q2 is asking for.

Is it asking for us to develop and prove an algorithm that will reduce the problem to something solvable by Gale-Shipley? Or are we simply asked to state the algorithms mentioned/implied by the problem note how they are used for the pre-computation to reduce it to something solvable by Gale-Shipley and then proving that it is in fact a stable matching on the original form of the preferences?""",
    """Directed/Undirected Edge Matching
Hi,

Does direction matter in the definition of matching? For instance, if there exist three vertices in a directed graph: u, v, w do edges (u, v), (w, u) form a matching in this graph?

My understanding is that by lecture 2's definition of matching which is:

A matching is a subset M in E such that:

1) For all u in U, for all v, v' in V if (u,v), (u, v') in M => v = v'

2) For all v in V, for all u, u' in U if (u,v), (u', v) in M => u = u'

then it is a matching as the condition of (u, v) and (v', u) is not specified.""",
    """Q1 reduction
Is it okay for us to formulate Q1 questions as linear programming problem? i.e. to have linear constraints and an objective function for the formulation

Or do we have to formulate them as matching problems on graphs?

Thanks in advance""",
    """Q2 - Multiple Constructions from Preorders
If we are modifying the preorder in some way to create say a different type of order, then we will have to do this for every node correct? That is, transform all preorders in the graph to our desired order type?

I'm asking this for the part about runtime analysis because then we have to consider that each of these transformations is done for every node in the graph, correct?

Thanks!""",
    """Q1A
Games only occur on the weekends right and not weekdays? Not sure how amateur leagues work.""",
    """Assume size of Soduk
Are we allowed to assume a 9x9 sudoko grid?""",
    """Q2 - Topological Sorting
Do we have to explain exactly how topological sorting works, or how we can create a total ordering from it?""",
    """Clarification on Matchings
Just to clarify, if I am creating a matching between two sets, say A and B, does every element of A need to be matched to an element of B for this to be a valid matching, or can there be elements in these sets that are not matched?""",
    """Q2 Questions about binary relations of preorders.
I read in the Wikipedia entry of preorders that:

"If a preorder is also antisymmetric, that is, a < b and b < a implies a = b, then it is a partial order".

Are there any cases where if, a < b and b < a, then a != b in a preorder? I can't wrap my head around it.""",
    """Proofs for Q1
Other than mathematical formalization of the problem, do we need to include any proof (e.g. correctness or run-time) for Q1?""",
    """Q2 Visualizing preference list
I just can't wrap my head around the explanation "an arbitrary finite directed graph G = (V, E) determines a
preorder < on its nodes in which x < y if there is a directed E-path of length 0 or greater from x to y".

Can someone provide an example - say if I have a preorder preference list A <= B = C <= D, what would that look like in a directed graph? """,
    """Office Hours 1-2 pm
Hi, are there office hours today from 1-2 pm? Zoom keeps displaying, "waiting for the host to start this meeting." Thank you!""",
    """Can a bipartite graph have multiple edges for a single node?
When I google "Bipartite graphs", I only see that it just means that no edges between vertices are within the same set. In that case, is it possible that with nodes {A,B,C} and nodes {1,2,3, ..6} that there are edges (A,1), (A,2), (A,3), (A,6), etc.? What about the other way around from numbers to letters? Or is the requirement for a matching that there can only be one edge that we talked about for Gale-Shapley a general rule for all graphs?""",
    """hw 1 q2
Can we assume every candidate or employer has a preorder or no preference, or always some preorder?""",
    """Question 2 preorder format
Can we assume that we are given a graph which represents the preorder, or can we say given a list of pairs representing the preorder, we can build a graph that represents it without explaining how exactly we would construct the graph? In other words, can we just say that we have a graph G which represents the preorder?""",
    """quotient graphs q2
can someone clarify why it's necessary to have a quotient graph? would it not be possible to do topological sort directly on the directed graph of the preorders?""",
    """Interval Partitioning Problem
During today's lecture (9/9), the professor mentioned that k = lower bound on # of processors needed for the interval partitioning problem. Why is that the case? Why is it not an upper bound considering it's the highest depth with the maximum number of "conflicts"?""",
    """More TAs in office hours?
Would it be possible to have at least 2 TAs in office hours? Then one could be handling specific questions in breakout rooms while the other answers general questions in the main room. Otherwise, we have to wait for the TA to come back from answering all specific questions, and that can take a long time. Or we end up asking our specific questions with everyone else, and that isn't a great use of everyone else's time.""",
    """TA Office Hours: Attendance Cap and Sign up form
Can there be a sign up sheet for office hours and can there be an attendance limit for every session? With 30 students for hour-long OH, office hours are rarely useful and the TAs don't end up speaking to all students 9 out of 10 times.  """,
    """Proving Q2
I have two questions regarding proofs for question 2:

Do we need to prove that collapsing a graph into a quotient graph always makes it acyclic?

I'm still a little confused about how to prove the overall algorithm for question 2. Would it mainly just be proving that the graph we get after reducing the problem to the original G-S algorithm format is equivalent to the original graph?""",
    """Q2 Clarification
Do we need to prove correctness and find running time in question 2?  I think we don't need to since we use Gale-Shapley instead of designing a new algorithm, but the homework 1 supplement for question 2 keeps mentioning the run times.""",
    """PDF is too big for CMS
My pdf of answers is too large for cms. Is it possible to allow an option to upload a zip file? Thank you.""",
    """Q2 algorithm
The hint for Q2 says to come up with a precomputation that will reduce the problem to the original problem solved by GS. Can we make small modifications to GS in our solution?""",
    """Additional Office Hour
Hi, I'm going to host an additional one hour office hour starting right now. If you have questions, fell free to join in.""",
    """Q2 topological sort
Do we have to give the algorithm for topological sort? or just say that we're going to use it? And if we do have to write out the algorithm, do we have to prove its accuracy?""",
    """Textbook Ch. 4.2
In chapter 4.2 on minimizing maximum lateness, the textbook mentions


"Instead of a start time and finish time, the request i has a deadline di, and it requires a contiguous time interval of length ti, but it is willing to be scheduled at any time before the deadline"

Does this mean that if the current interval has passed the deadline of a certain task i, i can never be scheduled? How would the lateness of i be calculated in that instance? How does this extension account for cases where not all tasks can be scheduled in a given time interval? Or is the time interval unbounded until all tasks have been completed?""",
    """runtime for obtaining quotient graph optimally?
^^^
i'm not sure what the optimal algorithm for obtaining the quotient graph is / how to analyze its runtime. what's the best way to figure this out?


i'm aware that we can find strongly connected components in linear time, but do we process the data further after identifying those components? """,
    """Confused about Q2
I've been reading through previous Piazza posts, and I'm confused on what needs to be done for Q2. Is it sufficient enough to modify GS to work for the precomputation and prove its runtime and correctness or do I have to do something extra? I saw a couple of posts talking about the quotient graph and developing an algorithm for the precomputation and proving that as well. Thank you!""",
    """Can preorder graphs have unconnected nodes?
Going by the answer to @33 it seems like yes, but an unconnected node isn't in a cycle, so I'm not sure how we could collapse it into a quotient graph  that works as the total order preference graph. Am I thinking about this all wrong?""",
    """Q1 Constraints on matching
Are we allowed to define constraints on the matching process or would that be considered part of a solution and not stating the problem?""",
    """Sudoku as Matching Problem
The textbook says "A matching S is a set of ordered pairs, each from M × W, with the property that each member of M and each member of W appears in at most one pair in S." Extending this definition to a non-bipartite graph. Should the definition be "each member of Node N appears at most once with another node in a pair in S"?

If so, how can I convert a sudoku question to a matching one?""",
    """Adding edges to get a new graph?

Is this statement asking us to add arbitrary edges between the strongly connected components or between the nodes in each strongly connected component to produce a new graph?""",
    """Q1b
I know for question 1 we do not need to use bipartite graphs. However, are we allowed to do sets of nodes that contain subsets of other nodes? For example, in terms of the sudoku problem, could I make a set of nodes be each individual cell and then within that have subsets for the rows, columns, and boxes?""",
    """Question 2 HW1
This might be a stupid question to ask, but in Problem 2 for HW1, how exactly does having a preorder instead of a total-order prevent us from applying Gale-Shapley? If we are given a linear order of preferences (preorder or total order) can't we just use the list from top to bottom and apply Gale-Shapley? How does a preorder list instead of a total order list create a problem in applying GS?""",
    """Q2 Runtime
Are we calculating best, average, or worst case run time?""",
    """Office Hour Today 11:00 am - 12:00 pm EST
I decide to change my office hour from 11:30-12:30 to 11:00-12:00 so that you can go to the next office hour (12:00-13:00) if you have more questions. """,
    """Q2 Proving Correctness
Beyond proving that the gale shapley algorithm can apply to our problem, do we have to prove that the Gale-Shapley algorithm itself is correct?""",
    """Q2 Does Preorder include all elem in other group?
1) For instance for a given u', a preorder might not necessarily include all v in the other group.

In this case, what do we do to construct a linear ordering when some v are absent?

Can we assume it includes some relation for all of the other group?

2) Can we assume same #employers and #candidates

Thanks""",
    """Q1 How exactly do you define a constraint of a matching problem?
For example, would it be correct to say that, if sets A and B are relevant to the problem, one constraint of the solution is that the bipartite graph (A, B, E) must have a perfect matching? Additionally, is it possible to define a problem in terms of multiple graphs? It seems like that would be necessary for 1a and 1b, as they seem too complex for a single graph.""",
    """duplicated nodes
Are duplicated nodes allowed in a graph? What's the proper way to represent, for example {1, 1, 1, 2, 2, 2}, in a bipartite graph?""",
    """Q2 Strong Components
Is it possible for two nodes that are equal to be in different equivalence classes if we make equivalence classes based on strong connectivity? If that is the case, does it affect how we topologically sort the quotient graph?""",
    """Q3 clarification
I understand this may be a bit of a silly question. But is it possible that we are talking about (S', T') instead of (S',T) or (S,T')? Because wouldn't it be more like a real competition if both networks could shift their strategies? If one cannot change their strategy, and the other cannot, it would very difficult for the other network.""",
    """About participation
Do Piazza messages to only instructors (say, if I have a question that could be part of a solution) count towards the participation grade?""",
    """Office hours
Are there no office hours for tomorrow?""",
    """Max number of edges
I'm having trouble thinking about the worst case number of edges in the preorder graph of preferences. Theoretically there could be a directed edge to and from each node, correct? If that is the case, then I believe there could be n*(n-1) edges where n is the number of nodes, which would mean O(n+m) is really an O(n^2) operation for each preference list worst case. That doesn't seem right to me because the book says that constructing the quotient graph is linear, which is why I'm confused. Is my analysis incorrect for the max number of edges?""",
    """2. Time Compexity clarification
Finding strongly connected components takes O( |V| + |E|)

if V is {1,...n}, and E can be a maximum of n^2 - n for any complete graph,

must we assume a worst case O(n^2) for this?

The reason I ask is because the hints make a claim that finding Sccs is linear (which I don't believe it is as a function of n only)""",
    """Nontotality of Preorder
The definition states that a total order is a partial order with x,y, either x <= y or y <= x. This seems to imply that in a pre-order, there can exist pair x,y such that neither are ≤ the either. This is mostly a clarification, but would that mean that there can be disconnected groups of nodes, right?""",
    """Q1 Minimum Number of Weekends
HW1 Q1a states that the "The schedule should take no more weekends than necessary." I'm a bit confused about how to state that formally. For the HW1 example, they did:

to formalize "The allocation is as equitable as possible, in the sense that all staff members grade roughly the same number of problems."

I was wondering if it was necessary to write something like this or would it be sufficient to state that the algorithm should provide a solution that minimizes the number of weekends by maximizing the number of games played per weekend.""",
    """Q2 proving acyclic
HW 1 help says "One can show that is an equivalence relation (reflexive, symmetric, and transitive), therefore partitions V into a set of nonempty disjoint equivalence classes whose union is V ."

When using and proving number 2 do we need to prove that it is an equivalence relation since it says "one can show"? """,
    """Office Hours Today
Since the PSET is due tonight and there are no scheduled office hours today, I'll be holding extra office hours starting now until 1 PM EST!""",
    """Office Hour Now
Another office hour from now till 12:00pm. """,
    """Q3 Time Slots
Q3 mentions n prime-time programming slots. However, since there are a total of 2n TV shows, does that mean that there are an additional n non-prime-time slots or that n TV shows will not be matched?""",
    """Q1 Number of weekends needed
I have some math worked out on my solution that concludes that, if you maximized the number of games played each weekend, that the season could be completed in n weekends. However, that assumes that n games can be scheduled every weekend without violating any other conditions. I've tested this on small sample sizes, and I believe that it is always possible to schedule it in n weekends, but I'm not sure how to prove it without just fully solving the problem. Should I just remove my work and leave my question asking that the weekends be minimized, or does it make more sense to demand the exact number of weekends that the schedule needs to fit into, with only a dubious proof to justify its possibility?""",
    """Super Confused about Running Time Analysis
Hi, I'm not pretty sure how could I provide a big O thing for question 1 a and 1 b. What I have for 1a) is a matching of my graph would give a valid schedule of a certain weekend, so there exists a valid schedule of a weekend according to a matching on my graph, but I don't know how many matchings I need or how many times I need to find matchings on my graph to give a complete schedule. For 1b), my solution enforces the constraints for a certain number, which means by finding a matching on my graph this would give valid coordinates for the given number. Still, I don't know how many times I need to run the algorithm to fill a sudoku. I'm super confused rn could someone explain this?""",
    """Hw1 Office Hours
Given hw1 is due tonight and there are no scheduled office hours, I'll be holding extra office hours from 6:30pm to 8:30pm tonight.""",
    """Q1a clarification
I'm kind of confused about how to interpret the question. Does the phrase "arrange the schedule" mean that we're given the list of team pairings (for example, for team 1 in the East division, we're already told which teams from the West division they're going to play), and it's the job of the algorithm to decide which weekends the matches are scheduled on, or whether we also need to create a schedule (i.e decide which two teams from the West division will play Team 1 from the East division). The question asks us to resolve ambiguities ourselves, so is that decision up to us?""",
    """Extra Office Hours Today
I will be holding office hours from 2-3:30pm today for help with HW1""",
    """Q2 disconnected graphs
If V = {1, 2, 3}, and E = {(1,2)}, would topological sort just make sure 1 is before 2? For example,

3,1,2

1,3,2

1,2,3

are all valid sortings? But 3 would still be a disconnected node?""",
    """Q2 SCCs
Do we have to show how to find all strongly connected components in linear time?""",
    """Q2 Requirements
Is there a rubric or the like for what is required in our response for question 2? I'm confused as to what components I need to be sure to include in my answer.""",
    """HW1Q1(a)
The question says that "play crossover games with two teams from the other division, one at home and one away".

Does this mean that a team will play crossover games with team1 from the other division, once at home and once away, team2 from the other division, once at home and once away, so a total of 4 games?)

(or team1 from the other division at home, team2 from the other division away, a total of 2 games?)""",
    """Any more extra OHs?
Share us some more bread crumbs""",
    """Q2 how to deal with special case in a pre-order graph
If there are two relationship x <= y and x <= z, how to deal with the order of y and z in this case? Can I order them arbitrarily since they have no explicit relationship in the original data?""",
    """Safe to assume GS always produces a stable matching?
I took down some notes from a TA saying that when proving correctness of your precomputation + GS in #2, you need to show that an unstable matching produced by GS is also an unstable matching in the preorder graph. However, this confused me because I thought that GS always produced stable matchings? And reading other piazza posts like @77, people are only mentioning proving that stable GS results are stable.""",
    """Confused about 1b
I have been thinking about how to formulate problem 1b for a long time. I know we should formulate as a bipartite graph and one set of nodes should be the nine digits. After that, I can't figure out how one graph can elegantly combine all constraints(row, column and subgrid). Can anyone give me some hint?""",
    """Q1a
Is it okay to put conditions in words? For example, can I simply state that there should be a matching of {some specific case}??

HW1 help file puts properties in mathematical statements but I'm not sure how to put things mathematically...""",
    """Question 3 Clarification
The question says "for any set of TV shows and associated ratings" - are these TV shows already split into which network they are associated with, or is it a group of 2n shows that the networks get to pick their group of n from?

That is, if there are four shows W,X,Y,Z,  can network A have any 2 shows or is it specified which 2 they get?""",
    """Q3b multiple decisions
In Q3b, if one network unilaterally switches its schedule to win more slots, and after seeing that, the other network decides to unilaterally switch to win back the slots, is that still stable? More generally, if that intermediate first step (S', T) is unstable but then it returns back to the original score (score meaning the number of slots won) in step (S', T''), then is (S', T) still a valid solution?""",
    """Proving theorem relating nodes to edges and connected components
In Friday's lecture, we said that for an undirected graph G with n nodes, m edges, and c connected components, n ≤ m + c and n = m + c iff there are no cycles in G. How would you begin the inductive proof to show that this theorem is true?""",
    """Starting 12 PM Office Hours Early
I will be starting my office hours a little earlier today.""",
    """HW logistics
Is there an estimated timeline for when grades will be out and when the next homework will be released?""",
    """Moving office hours to 7pm - 8pm
Moving my OH to 7 pm - 8 pm today!""",
    """Not able to watch lecture1
update:

Hi Priya, yes, I can watch other lectures. The link provided by another student works for me!

Thank you the anonymous poet.

-----

I just enrolled in this course, and I tried to watch lecture1 on 9/2 for so many times.

It seems like something goes wrong, and it pops up an error message. Like this.

The other videos are fine. But I need to watch this one.

Does anyone know what going on?""",
    """Cool Matching Algorithm
If you loved matching and want to know another cool matching algorithm, check out Hopcroft-Karp Algorithm (yes it's our Hopcorft). Unlike stable matching, it is an algorithm to find the maximum cardinality matching. In other words, you have a bipartite graph (that's not necessarily complete or fully connected), and you need to match as many pairs as possible. What's exciting about this algorithm, is that its runtime is O(EV)! Yes there's square root in the runtime! You can read the Wikipedia page to learn more about it (or you could take CS 6820 and learn about it next fall)""",
    """HW1 P2 Extend the graph G
Why do we only have to add edges between (xi,xi+1)? Don't we have to add edges xi,1 <= j <= i−1,(xj,xi) to make sure it's a total order?""",
    """Problem 2 Continuous Night Shifts
In Problem 2, by shifts throughout the day, does it mean like a normal workday, where there are definitive start and end times, and no one works between the end time of one day and the start time of another day? Or is it possible to have say Employee A work from 3 am to 11 am, Employee B work from 10 am to 9 pm, and Employee C work from 8 pm to 4 am (Notice that Employee A and Employee C have overlapping shifts from 3 am to 4 am)?""",
    """[HW2] Q1
Can you go into more depth about the list? Is it sorted from smallest to greatest or vice versa, is it partitioned i.e. {A1, …, AN | B1, … , BN }, etc.? Or are these assumptions we should make on our own, and then explain our assumptions as we did in HW1?""",
    """Moving Office Hours tomorrow, on Wednesday 9/15
Only for tomorrow, I (Giannis Fikioris) will not conducting my OH.

I will do them some other day this week, probably Friday, when I also suspect there will be more questions about hw2.

Will post another announcement for the exact time.""",
    """Problem 2 Clarification
The question states that the manager needs to make sure that whenever there is someone on duty, at least one employee on duty has a key to the main office, does that mean that there are situations where no one is on duty, or can we assume that the office is occupied 24/7?""",
    """Question about Ackermann's function in class(9/16/2020)

In the class today, we defined Ackermann's function and its inverse.

Ackermann function is a function A: N^2 -> N where,

A(0,n) = n +1

A(m+1,0) = A(m,1)

A(m+1,n+1) = A(m, A(m+1,n))

But then we go over to some function Am(n), which is a fucntion from N -> N.

We define Am(n) as:

A0(n) = n+1

An+1(n) = do An n times to n

and we define the inverse of ackermann's function as the inverse of Am(n).

How does Ackermann's function A relate to Am(n)?""",
    """Moving Office Hours
I'll be moving my 3pm OH today to 6pm today. Sorry for the last minute change. Hope to see you there!""",
    """Web Interface for Testing Question 3
In the Q3 description, it says there will be a web interface where we can test out solution for problem 3. Can we get a link to this interface?""",
    """Fri 11:00 pm OH -> Thu 12:30 pm
I am moving my Friday office hour to Thursday 12:30 pm (only for this week). Sorry for any inconvenience, and I will hold extra office hours before the deadline if necessary. """,
    """"Give an efficient algorithm"
In problem 1 of HW2 the question says to give an efficient algorithm. Does this mean that, unlike HW1, we are now expected to maximize the efficiency of our algorithm?""",
    """HW2 and Greedy algorithms
Are the algorithms we come up with (at least for 1 and 2) supposed to be of the greedy variety? Or can we try anything as a solution?""",
    """What if our algorithm is wrong
How much will we be penalized if our algorithm isn't the most efficient or is just incorrect, but we made good attempts at trying to give the algorithm, prove efficiency and correctness, and analyze the runtime?""",
    """Q3 Proofs
Since the question is just asking us to implement an algorithm, do we have to prove that it is correct? (If so, I'm not even sure what a "correct" algorithm would be.) I'm also asking because the directions at the top of the homework pdf says to just submit the source code when uploading to CMS, so I'm guessing that doesn't mean we have to include a proof? It also says the written submission should be the write-ups for 1 and 2, but doesn't say 3 should have a write-up.

I'm also assuming we don't have to analyze running time because the question already states that it is in linear time. Just wanted to clarify!""",
    """Q1 Clarification
Q1 says that we are given a schedule for network B's programs, but doesn't specify how we receive this information. Q1 does specify that we get a list of all programs, but nothing about B's schedule.

I know in general it's safe to make assumptions as long as we write them out, but I'm asking about this because it seems like a big thing to assume how you get B's schedule, or how much time it takes to get some information out of that data structure, esp since it impacts your runtime complexity and we're aiming for max efficiency here.""",
    """Pseudocode or actual code?
For 1 and 2, should we type out the actual source code for the algorithm, or is just pseudocode ok?""",
    """Q3 Preorder and Postorder
I'm having trouble understanding preorder and postorder numbering for DFS on a graph.

I'll try numbering the preorders and postorders on a few graphs, but I think I may be doing it wrong.

image.png

Preorder: 0, 1, 4, 2, 3

Postorder: 0, 2, 4, 1, 3

And for this graph I made:

8 6

2 3
3 4
2 4
5 4
5 6
6 7

Preorder: 0, 1, 2, 3, 4, 5, 6, 7

Postorder: 0, 1, 4, 3, 2, 7, 6, 5

If these preorderings and postorderings are correct, I'm also having trouble understanding how this should inform if an edge is a forward, back, or cross edge.

For instance in this graph, how do we know from the preorder that (2, 4) has a forward edge? It looks like node 4 occurs 3 times in our algorithm. The first time it is reached by a tree edge (3, 4), then it is reached by a forward edge (2, 4), and then it is reached by a cross edge (5, 4). I see that (3, 4) a tree edge because preorder of 4 has not yet been assigned, and but I'm not sure how to determine that (2, 4) is a forward edge and (5, 4) is a cross edge from the orderings. If someone could explain this bit especially, that'd be great!

Thanks!""",
    """Running Time of Dijkstra
I was trying to understand why Dijkstra has a running time of O(mlogn) instead of O(nlgn) or something at least containing a linear n. So the most outer loop, though it seems like it's operating on nodes, is actually a loop about edges. (I don't know whether I'm right about this. If I am, I think this statement can help me solve my question below) We maintain a priority queue of nodes and the only reason that priority queue gets updated is that some edges are visited. So for each edge, we either query the distance but not update it O(1) or update it O(logn). That is and we get an O(mlogn)
Then it comes the confusing part for me. It seems the set of currently visiting nodes (grey nodes) can have at most n elements and each extractMin operation takes logn time so it should be O(nlogn)?

Or does it have nothing to do with n in the first place, even though when we write the code, we would write while(!q.empty()){ ... }? We are simply extracting elements from the priority queue already updated by the previous O(mlogn) step and a simple query should only take O(logn) time?""",
    """Moving OH from Thurs 6-7pm to Friday 4-5pm
Sorry, I have a family emergency.""",
    """Q1
Does "assume the 2n programs are given in a list labeled by network and sorted by rating" mean two lists, one for each network or one combined list?""",
    """Q3 Stack Size
I have a recursive DFS implemented for Q3 but it crashes because of the size of the later test cases on the course website - otherwise, the algorithm is correct, runs quickly and passes all of the test cases. Is implementing runnable and just starting a new thread on the JVM with a larger stack size an acceptable way around this (it works on the web test interface)?""",
    """exchange proof question
I had a question about the exchange proof in the textbook. In the textbook, it says "Statement (4.9) proves that an optimal schedule with no inversions exists. Now by (4.8) all schedules with no inversions have the same maximum lateness, and so the schedule obtained by the greedy algorithm is optimal."

This implies that the greedy algorithm has no inversions, but how is it that we know that?""",
    """Sorting in our solutions
If we decide we want to sort something in our algorithm, can we simply say sort(<thing we want to sort>) in our psuedo code and say what attribute we want to sort by, or must we provide the psuedo code for a particular sorting algorithm?""",
    """Problem 2 hw2 clarification
'The start and end times of the shifts vary' is from problem 2 of hw2.

Does this mean that: for any two employees, they can not have the same start time. Also for any two employees, they cannot have the same end time?""",
    """Q3 DFS
In the Wikipedia article on DFS linked in the handout, there are 2 versions of iterative DFS. Is the order of the nodes our DFS is expected to print out the same as the order of the nodes printed by recursive DFS, or the order provided by visiting all neighbors of a node in reverse of the recursive DFS?""",
    """Office Hours Today - Giannis Fikioris
Because I didn't do my OH on Wednesday, I will be doing them today, 12:30-13:30.

Please see and complete the googledoc in the course's website, as you probably have done with other OHs.""",
    """Q3
Are there any instructions for how to work with ASCII charater stream? (for instance, how to covert stdin to common data structures, and how to convert output to ASCII charater stream stdout?) I'm very confused about this.""",
    """Can we use array notation?
On Q1, explaining my own algorithm would be much easier in terms of arrays (as they function in java) rather than ordered pairs. I'm asking because arrays have the property that an element of an array is undefined until it is set to some value. Making ordered pairs fit this property would do a bit more explanation.""",
    """Question 3
How long do we have in the portal (as specified in @225) before the code times out? I'm wondering because it is mentioned that we need to have our DFS run in O(m+n) time, but I have input code in my file that would not make this runtime possible. Should my function to process inputs be commented out when I submit into the portal?""",
    """HW 2 Q2
Is there any rule for when a key can be given to/taken away from an employee? And what does "employees do not share keys" mean? Or are the answers to both assumptions we need to make?""",
    """Q3 Python std-in processing
Just wondering how should we process stdin using Python, can I use sys.stdin and then read line by line?""",
    """Q3, algorithm correct for up to size n = 10000 m = 200000, but wrong for larger ones.
Hello, I've been struggling all night to try to debug my algorithm, because I have no idea what kind of problem would only arise when the input gets up above 10000 nodes. I can't find any sort of problem with smaller tests, and I really don't know how to approach figuring out why none of the six large tests will pass, while all the smaller ones pass fine. Any tips would be much appreciated.""",
    """Autotrader Error Message
What error message does the autograder give if memory limit exceeded? Does it give a WA?""",
    """Induction Review @ 12pm Reminder!
Hey everyone!!

Just a reminder that we're having an induction review session starting in ~10 minutes! We'll be covering various induction methods and applications including some dynamic programming examples which will be very relevant to upcoming PSETS!

Link to session:
The session will also be recorded if anyone can't make it!

Thanks!""",
    """Q3 DFS example
How is the example a DFS if it goes on the edge 1 2 before 4 2? I thought that the DFS order would be like:

1 4

then check edges from 4, so 4 2

then check edges from 2, so 2 4

back to 4, so remaining edge 4 1

back to 1, so remaining edge 1 2""",
    """Sequence alignment both unmatched case
When Prof. Kozen was explaining the cases for the sequence alignment problem in lecture, he mentioned that the case where a and b are both unmatched is handled in the other cases (37:21 in the 9/18 recording). How does this work? """,
    """hw2 q2
is that possible for two employees to have the exact same shift (same start time and same end time)? """,
    """Q2 Implementation of Array
In class, we simply stated "Sort all start and end times in a big array. In case of ties, put start times before finish times". I would assume in the actual implementation you would maybe store a tuple at each index containing whether the value is a start/end time as well as the actual time value. Since we didn't elaborate on how the array should be implemented in class, would it be safe to leave this kind of information out of our solution for #2? """,
    """Indenting latex for pseudocode
Does anyone know how to indent individual lines in the latex template that we were given? I've tried \indent and \hspace{\parindent} but neither are working.""",
    """Q3 Java stackoverflow
Is there actually a way to do Q3 recursively in Java without a stackoverflow error? I can't figure out how to not overflow using recursion, but I can't figure out an iterative solution either and am kind of stuck...any tips would be greatly appreciated, thank you""",
    """Additional Q3 Tests
I am attaching a .rar file with multiple (maybe too many) small inputs and their outputs for Q3.

The .rar also contains a python script that compares 2 output files (possibly not useful for small inputs).

Do not worry, no changes will be made to the autograder, so you don't have to re-upload your codes.

Edited 9/21 18:30

A python script that checks if your code matches all the test cases in the folder. It is meant to be run from inside the tests folder, where all the .in and .out files are:""",
    """Increased stack size in Java
The maximum stack size in Java has been increased considerably. All your LATEST submissions are now being re-graded, so check that everything is at least as good as they were when you last saw your submissions.""",
    """Q3 traversal order
I have questions on the traversal order of Q3.

In the handout, it's being said the search should be started from node 0, and "you must explore the edges (u, v) with source node u in
the order that they are given in the input".

So for example if the graph is

2->1->0

With input given as

3 2

2 1

1 0

The output should be 2 1 0 as the first line if we explore the edge by input. But doesn't this order counteract with the rule "the search should be started from node 0"? Vice versa.

Also if with the same graph, the input given is

3 2

1 0

2 1

How will the first line output be? because if traversing by the order of lines in input, the order will no longer be 2 1 0 although the same graph persists.

Any help will be appreciated!""",
    """Q3 Timeout
I'm passing the test cases at the beginning, but for the later, larger test cases, I'm timing out. However I'm pretty sure I have an O(m+n) implementation (iterative). The error I'm getting is "Killed". Is there any way to figure out how I can make the time limit?""",
    """Q3 Input
How do you manually input an ASCII character stream? I want to test some simple trees manually before actually testing it, how would I input that so that it exactly matches what is used in the actual tests? Do I need to use a converter? For example what would the following tree look like.""",
    """Loading time for testing
Whenever I try to test my code, the webpage is always stuck showing the purple loading bar. It was like this for a good few minutes before I refreshed and it showed that the larger test cases were all wrong (which I need to fix because I realized what was wrong with my algorithm after I uploaded it) and a few had timed out. Am I just too impatient or should the results of the test cases show up immediately? The timed out cases have the “Killed” error, and I’m not sure if this is because I refreshed the page or because my algorithm takes too long.

Edit for more info: the cases that time out are in the middle and are smaller than the larger cases at the end that are not timed out but are marked wrong.""",
    """hw2Q1_Assume map?
Since we are given a list of [B1, B2, ..., Bn] ordered by Bi's rating,

Can we assume that we are given a map of (Bi, time_slot_of_Bi)? In other words, for a Bi, can we assume the time we get its corresponding time slot in B's schedule is O(1)?""",
    """Hw2q2
Hi, I'm not sure if this is a dumb question, but for this question, can we assume that we are using a 24 hour clock to denote the start and finish time of each employee time interval? For example, for employee i, we have s(i)=0,and f(i)=3, and this means the employee i has a starting time of 0:00 and end time of 3:00 AM; we could also have employee j that s(j)=13 and f(j) = 14, which corresponds to 1:00PM and 2:00PM? Also, can we assume that we have 0 to represent 0:00 AM but not 24 to represent 0:00 AM? """,
    """Question 1
In question 1, the problem says "given a schedule for network B's programs". Does this imply that we know the order in which network B is going to play its programs and that this order will not change?""",
    """Q2
Would like to clarify this statement: "The manager needs to make sure that whenever there is someone on duty, at least one employee on duty has a key to the main office, but for the sake of security would like to have as few keys floating around as possible."

Can we assume that in the case where none of the shifts overlap, the minimum number of keys needed would be the total number of shifts? And should we not make any assumptions about times where there are no employees on duty?

E.g. Would we have a case where all shifts were the same length and started/ended same time? In this case, the minimum number of keys would be 1.""",
    """Web Interface Score
What does the score column mean on the web interface? Is that how many test cases passed? If so, what is the score needed to get full credit?""",
    """Maintaining Output Order
The autograder doesn’t mark outputs in a different order as incorrect. Will we lose points if the edges aren’t outputted in the same order as the input?""",
    """Q3 Input Size
Do the test cases shown in the autograder test the max input size? So, if our code passes all of the tests on the autograder, can we assume that our algorithm is efficient enough?""",
    """Q2 24 Hour Clock
@271 brought up the point that we could consider Q2 in the context of a 24-hour workday.

I was wondering if shifts that cross over the 12AM mark would be in the scope of this question (e.g. a shift that starts at 11pm and ends at 1am the next day). Can we assume that this is out of scope given that the question states "each employee works just one shift each day and the same shift each day." I would think that "one shift each day" implies that a "crossover shift" would technically count as two separate shifts a day.

If this assumption doesn't hold true, then would it mean we'd have to pick an arbitrary "overall start time" to run the algorithm? Different start times may theoretically result in a different number of minimum keys required (e.g. say if you ran the algorithm multiple times starting from the finish time of the last shift).""",
    """WRONG box for the same output as the expected
I uploaded my code to the autograder and it failed because of wrong output. But when I checked test case 1 which is given as an example in the handout, my output is the same as that in the handout. So I'm wondering where it could be wrong?""",
    """Reading the input for q3
I'm a little confused about handling the newline characters in the ascii file. Do I need to worry about those, or will I just need to process a string of integer charaters and spaces?""",
    """Quizzes
There haven't been any quizzes so far, so I was wondering what/when we should expect them throughout the semester. The website said "There will also be occasional quizzes. The quizzes will be available on CMS and can be done offline." Not sure if I missed any information during lecture about this.""",
    """Clearing Space on Laptop
I'm trying to download Xcode for C++, but it says I don't have enough space. Does anyone know if I can remove the Visual Studio Installer without affecting VSCode itself?""",
    """Is creating an adjacency matrix too time complex?
I am using python and am creating an adjacency matrix for size n, where n is the number of the nodes to keep track of the edges. This operation, as far as I can tell cannot be done in faster time than O(n^2).  I saw earlier a TA suggest creating an adjacency matrix, but won't this just make my program too time complex?""",
    """HW 3 Q3 global variables
Can we use global variables? Or create a class? (would creating a class be too much memory?)""",
    """Homework Extension Policy
If I requested a 24 hour extension for homework 2 but ended up submitting it on time, would it still count as part of the 72 hour free extension? Thank you!""",
    """Recursion limit / segmentation Fault

I did a rather straightforward python recursive implementation for problem3. I got the recursive limit error multiple times, so I set my recursive error to something higher. Then, I was able to pass one another test case. I do think my implementation is correct. I don't know how to fix these recursive limit errors, as the input data really defines how much recursion I need to call. Could I please get some help? Thank you in advance""",
    """Q3 output
I passed the first seven test cases but got wrong answer for the last seven cases. I'm wondering what might cause this situation to happen? I did not get timeout, so I'm thinking whether there are ways for me to figure out what causes those larger cases to fail.""",
    """Assigning edge type based on order
I am confused on how edge type is determine using the preorder and postorder. Is this done during or after the DFS traversal?

Additionally, I'm not sure how to compare the pre/postorder numbers. What exactly does it mean to have a "higher preorder number"?""",
    """forward edges q3
im a little confused by what is meant by a forward edge. in the example in the homework, why is (1,2) a forward edge and not a tree edge?""",
    """Algorithm Design
Sorry if this has already been asked, but I'm getting confused by some of the questions about interval representation (points on the unit interval, numbers, etc) for #2 on the homework. Do we have to define a representation, or can our algorithm just be written for vague start times and end times s and f as seen in class?

In general, how specific are these algorithms supposed to be? I know we might have to mention a specific data structure once or twice to explicate operations/runtime, but do we need to be defining everything in this much detail for a "give an algorithm" question?""",
    """Postorder number for iterative Python
I have no idea how to compute a node's postorder number in Python. Does anyone have any guidance towards this? I implemented a recursive solution but, as mentioned in many other Piazza posts, Python recursion doesn't exactly work for large test cases.""",
    """Q2 input
can i assume that the given start and end times are sorted? or do i have to sort in my algorithm?""",
    """Exchange vs greedy stays ahead
Is there a way to tell whether exchange or greedy stays ahead would be the easier one to use to prove something?""",
    """starting q3
this is probably a really silly question but im a little confused by q3 in general. should the approach to this be 1) taking the input and constructing a directed graph, and 2) performing dfs and labeling the edges 3) output?""",
    """Same Time Shifts Q2
On question 2, I understand that shifts can overlap, but can start/end times be identical or are all of them unique?""",
    """Q2
can a person have a 24 hour shift?""",
    """9/18 lecture
At around 37 minutes into the 9/18 recording, I keep getting this error:



anyone else run into this? """,
    """Q3 Efficiency
My java code passes all the autograder testcase for 0 <= n <== 105, but it times out on the test cases where n = 106. As long as my algorithm is O(|V|+|E|), will I get points taken off further? Additionally, after how many seconds does each test case time out? I have my n = 105,m = 2 ∗ 102 at 2.6 seconds runtime, so I'm wondering whether my code is causing a memory overflow.

Edit: I'm using stack of iterators, each for a specific node's edges""",
    """Tree edges in Java
After failing to implement an iterative solution in Python, I am now trying a recursive solution in Java but still failing. I'm just not sure how to differentiate between tree edges and forward edges. I know the difference between the two, but I have no idea how to find and label an edge as a tree edge when a node is visited for the first time. Any suggestions?""",
    """Description of algo
In problem 1 and 2, do we need to write pseudocode or we just need to describe in English? Do we need to analyze the running time and prove correctness for these two questions?""",
    """preorder and postorder
i feel like my interpretation of preorder and postorder is off. these numbers are numbers assigned to the edges, correct? does this mean that they do not have a relation to the numbering of the vertices and are independent? from the description this seems like something different from 'preorder traversal' or 'postorder traversal'""",
    """Q3
Would it be necessary (for efficiencies sake) to classify edges on the fly? Or could we store the post order and preorder nodes in a list somewhere and then classify the edges after all post order and pre order numbers have been calculated.""",
    """Autograder stdout
In the stdout section, does the autograder give us our output or the expected output?""",
    """Sequence Alignment Unmatched Case
Say ua is matched with v and b is unmatched in this case. How are ua and v matched with each other? Doesn't the fact that u and v are already matched prevent ua and v from being matched together?""",
    """Q2 algorithm
Are we allowed to use a dynamic programming algorithm for Q2?""",
    """Daniel Galarraga - Office Hours (09/22/20)
I am cancelling my office hours tomorrow (09/22/20). I will try to reschedule them later on in the week. Sorry for any inconvenience.""",
    """Q3 Preorders and Postorders with Stacks
I initiallly implemented my DFS recursively with Python, but that has the stack overflow issue and segmetation fault problem if you increase the stack size too much.

I've gone back and tried to do it iteratively with stacks, but after several hours or so working on it and some time in office hours, I still haven't been able to figure out how to keep track of preorders and postorders nicely.

Could I get any tips here?

Thanks!""",
    """HW2 Question 1
Hi! I would like to clarify that I'm stating the given list appropriately in my response.

I would like to state my assumptions as follows:

Assume we are given a list of length 2n where indices 1..n are network B's ratings where the index corresponds to its time slot and where indices n+1..2n are network A's ratings where the ratings are sorted such that index n+1 contains the smallest rating and 2n contains the largest rating.

Would it be similar to state the same thing but network B's ratings are also in order from smallest rating to largest? (Because the index actually doesn't matter that much?)

Would this assumption be alright? If not, how can I reword to make it align with the prompt? Thank you!""",
    """-pthread compiler flag
For my DFS i've been setting the gcc flag -pthread on linux, but this isn't set on the server so i get a build error. Is there anything I can do about this? or should i just ditch concurrency.""",
    """preorder of example q3
in the example we are given for problem 3, why is 2 numbered before 4 in the preorder (they are both neighbors of 1)?""",
    """Question about Preorder and Postorder
I'm confused by what the instructions mean by that the post order and pre order can be done "on the fly". wouldn't we have to go through the DFS forest twice in order to get both?""",
    """Failing Q3 large test cases
Can someone post the expected output for one of the autograde test cases where n=10^6? My algorithm is failing those test cases, and I want to compare my output to a correct one to see where my problem is.

Edit: I found my problem, but the expected output may be useful for some other students.""",
    """Question about deadline extensions?
Hi. When requesting an extension, is there a specific date the extension has to be requested by? For instance, at least 24 hours before the official due date of the assignment?

Also the website says "contact the instructor by email". Who is meant by the instructor? Is that anyone in the course staff or just Professor Kozen?

Thanks!""",
    """Efficiently finding the next starting node
I am at a loss of how to find the starting node for the next DFS in time proportional to the number of nodes visited by the current DFS, as opposed to the total number of nodes (so that when we carry out multiple DFS runs, the runtime is linear to total number of nodes rather than quadratic). I am fairly confident that this is the cause of my timeouts, since it is the only part of my code that I believe in running in quadratic time. I have been spending over 4 hours on this sub-problem alone, and I can't seem to find such a method/data structure. Does anyone have any hints? Am I taking a wrong direction? Would appreciate any input.

I am using iterative DFS on Python.""",
    """postorder assignment for cycles
i read the important points in the hw sheet, but i am still confused about assigning postorder. i understand that postorder can be assigned to a node once all of the subtrees have been visited, but if there are cycles how would this work? for example, originally i was thinking if a node does not have children, you can assign a postorder number, and then you can assign postorder numbers to nodes where all their children have postorder numbers, but this logic doesn't seem to work if there are cycles. could someone clarify how this should be done?""",
    """When will Homework 1 grades be released?
I read that grades for the first homework would be released by the end of last week, but I don't think they're out yet. Will they be released before Homework 2 is due? It'd really be helpful to see comments and things from last homework that I could improve on. Thank you!""",
    """File Name question 3
Do we need to rename the file to a specific name when submitting our source code for question 3 on this week's pset?""",
    """Reading from stdin in C
Any advice on how to process the stdin input using C? I'm not sure which function to use to read the input""",
    """PostOrder numbers and cross edges in iterative solution
Hi! I'm able to get the pre order and post order numbers for the nodes in an iterative solution.  However, since my postorder numbers are not absolute compared to the preorder numbers (the preorder and postorder numbers are each 1 through n, I can't do the necessary comparisons to compare the postorder of one node with the preorder of another.  Does anyone have any insight on this?  Thanks!""",
    """Q3 Sense of Inefficiency
So I think there are two sources of inefficiency in my code: The reading or DFS

I logged some of the time (NS) it took to read, run dfs, and write for test 1 and test 6:

Test1:

Read:24990521
DFS: 121576
Write:75952

Test6:
Read: 181722666
DFS:  20847178
Write:1711335

Not sure what the test size difference between test1 and test6 (so if a staff member could help that'd be great), but would this seem like O(n^2) complexity or O(n)? And what might be some better methods of reading input as currently it is sucking up the vast majority of the time (Currently using Scanner but i'm unsure how to use BufferedReader)""",
    """Web interface wrong score
I passed all the tests on the autograder but my score on it is still 6. Is it expected? Thank you!""",
    """Gap in output for Q3

My algorithm works on 8 test cases, but not on the largest graphs. I think it may be because of gaps such as this one in the output for the node order. I'm using the command print(*line1) in Python to print the path output. Is there a reason that it's messing up like this? """,
    """expected output for programs
would it be okay to use System.out.print for our output if we are using java?

i tried 'test' which is just doubling the input (which i used InputStreamReader and BufferedReader for) but i got 'build error'""",
    """Returning edges in same order
I'm unsure as how to return the edges in the exact order as the input without creating a n^2 matrix for the edge types. Does anyone have any suggestions for an efficient way of doing this?""",
    """Faster Python Print?
rn I have a nested loop for printing out the results according to the input's order. What's the better way to do this? This seems to be slow.""",
    """Moving OH to 4:30-5:30 today
Hello!

I am moving my OH to be from 4:30-5:30 PM today instead of 11:30AM-12:30 PM. I’ll be using the same zoom link as my original OH. I’m really sorry for any inconvenience this may cause! """,
    """Q3 - faster Python IO
Looking for a faster way to take in the input - currently the longest test takes me two seconds just to run through the input lines and get ready to run DFS.  Anyone have suggestions?""",
    """Did runtime for Java get increased?
I think the Professor said earlier they might increase it? Has it been increased or should we not use Java?""",
    """Example Input Q3
The output on the handout lists 0 1 4 2 3 as the order traversed;  0 1 2 4 3 also work? 4 and 2 are both outgoing edges, and since I'm using LIFO and 1 2 is input later, I traverse that edge first.""",
    """Tuesday 2-3pm Office Hours Meeting Link
Noah and I will be co-hosting the Tuesday 2-3pm OH today.""",
    """Q3: Is this considered as a good linearity?
Hi,

After I passed the autograder, I generated random graphs with sizes from 10^2 to 10^5 and tested my code and this is the scaling I got.

Is this a good linearity? Since I can see more uptilt at the end of the curve, technically I can also fit a slow quadratic function to it.""",
    """General Approaches for Q2
I understand all of the greedy algorithms and proofs we've done in class, but I'm still stuck on finding a general approach to Q2 that isn't violated by counterexamples. Any hints or general approaches the TAs would be willing to dispense?""",
    """Hw 2 q2 discrete or continuous shifts
can the shift start times be at any minute like 8:05 am or would we be allowed to assume the start of every hour as a valid start/end time?""",
    """Segmentation fault for python implementation
Does segmentation fault in the autograder for large inputs for a python implementation mean recursion limit is reached?

I am quite lost as to how I can debug segmentation fault for large inputs. Does anyone have any hints/tips to go about this?""",
    """Having trouble finding "start point" on problem 2
On problem 2, I think I have an algorithm, which goes in chronological order given a start point in time. However, I'm having a really hard time picking a "start point" for this algorithm, because the first timeslot you encounter will automatically be included in the schedule, even if it is not optimal. I have tried many heuristics to determine an optimal start point, but they are all wrong in some case, which makes me think that this is not something you can easily determine. Am I completely off about this? And if I'm correct that you can't easily figure out a "start point", what are you supposed to start the algorithm off of?""",
    """Does the input always end with a newline?
I know each line is separated by a '\\n' but does that also mean that the entire file ends in a newline character?""",
    """5:30 pm office hour is not started?
hi,

the zoom seems to be not started for the 5:30pm office hour.

thanks!"""
    """Q3
So as I understand an adjacency matrix is wasteful as not all other edges are being used for each edge, which means it makes sense to use an adjacency list. However, the reason adjacency matrices seemed appealing is because the edge values act as indices so you can store a value such as the edge type in it and have easy access to it if you just know the vertices. When switching to an adjacency list, you no longer have the waste issue but can no longer use vertices as indexes unless you use use something like a dictionary (I'm working in Python) which is recommended against as it's complex and slow. I'm just wondering how could we utilize an adjacency list while at the same time not making our structure inefficient?""",
    """Maximum input file size
Is there a maximum file size that we can reasonably expect the input to be? I noticed the largest input in the autograder seems to be about 3MB, but I wasn't sure if there might be a larger file possible.

For instance, if I'm reading in a chunk of memory for the input, can I bound that to 8 MB?""",
    """Proving Algorithms
Does it matter which proof method we use for #1 and #2? For example, would it be acceptable to do greedy stays ahead for both problems?""",
    """Q3: Indexing Newline Python
I am having trouble parsing through the input for Q3 because anytime I try to find the index of the newline character I get the following error.

ValueError: substring not found""",
    """"Efficient"
What will graders will be looking for when determining whether an algorithm is "efficient"?""",
    """Q2 questions
Say there is an interval (6, 6), meaning 6 am to 6 am. Does this interval represent a 0 hour shift, or a 24 hour shift?""",
    """Writing Out Question 3
Do we need to write anything (i.e. proof of correctness or runtime analysis) for our submission of Question 3. I'm assuming we don't but just double checking if anyone knows for sure.""",
    """Tips for proving correctness
So I have my algorithms for questions 1 and 2, but I'm struggling a little when trying to prove their correctness. I'm just not sure where to start with the proofs, and I'm also struggling a bit with what it even means to prove an algorithm's correctness. Does anyone have any tips on how to go about thinking about the proofs or where to start them? Any help is appreciated!""",
    """The two main things you want to look at are the exchange argument and the greedy stays ahead proof. Those are the two proofs we learned for greedy algorithms, so they will likely apply to these greedy problems. There are examples in the textbook as well as from lecture about these two proof methods.""",
    """Group Problem Sets
These problem sets are really interesting, but intensely time consuming. Would it be possible, in the future, to submit them as a member of a 2-3 person group? I know a lot of my classmates have the same concerns about the intensity of the problem sets, so I figured I should ask on their behalf, as well as my own.

Thanks so much.""",
    """Moving OH In-Person
Exciting news! I'm moving my office hours in person. They will be on Wednesdays 3-4pm at Gates 310. The way it's gonna work, we will have 15-minutes slots for at most three students at a time. You can sign up on Google Calendar here  (since Google calendar doesn't allow more than one person to sign up for the same split, I've split each 15-minutes slots into three 5 minutes intervals so we can have three students to sign up).

If you have any questions about the class, questions that have nothing to do with the class, or just want to chat with someone in-person, then sign up for my office hours!

Exciting stuff!""",
    """segmentation fault for C++
I got an error of segmentation fault for my code in C++ for Q3. I saw some other people met segmentation fault as well, and previous post said that it was because of the maximum stack size. I saw the instructor reset the JAVA stack size for the autograder and I'm wondering how we can solve this problem for C++.""",
    """labeling edges
im having some trouble labeling edges between nodes that have already been visited (ie 1-2, since 2 is already visited from the edge 4-2) does anyone have any suggestions? (basically i can label tree edges but that's it)

ex) how are you supposed to label other edges if dfs doesn't travel through every edge, just meets every node?""",
    """Queued Autograder Status
What does it mean if the status of my submission with the autograder is "queued"? Is the system just overloaded right now or was there an issue with my submission?""",
    """Java vs. Python Error
For HW2 Q3, I'm using Java and getting "java.lang.OutOfMemoryError: Java heap space." A friend using Python is getting "Recursion Error: maximum recursion depth exceeded." Are these two essentially equivalent errors that are caused by incorrect recursion during dfs?""",
    """Q3 Labeling Edges
So I have the pre-order and post-order correctly computed for the DFS, but I am confused about how to label the edges. Do we label the edges while we work through the DFS algorithm, or can we label edges using the pre and postorders of nodes after DFS is complete?""",
    """Q3 Grading
Will TA's be manually going through all of our code to ensure that we implemented it in linear time? If so, is there a penalty if part of our code is found to not adhere to this boundary?""",
    """print edge labels in correct order
i am able to print out the edges and their corresponding labels correctly, however i am having difficulty figuring out how to make it appear in the same order as the input.

for example, my (1,2) edge is appearing last but it should be printed out after the (1,4) edge in the hw example since everything is added to the output string in the order they are met along the DFS tree

any suggestions?""",
    """q3 python recursive issues
So I did a recursive python implementation for q3, and am trying to follow @290 to get it to not segfault. Does anyone know about how high I should set the RLIMIT? I'm scared to crash the autograder or something.

Also, if this doesn't work....... is the only other solution to redo q3 iteratively? Really trying to avoid this outcome. Did anyone here get their recursive python thing to work?""",
    """timeout - multiple array variables
Could keeping track of multiple array variables (ex. postorder, preorder, stack, visited, nodes, etc.) be a cause of timeout? Though I think array/list the fastest and simplest data structure, I'm not sure if I should reduce the number of them or use another data structure to combine them like a list of pairs to improve timeout errors. """,
    """Q3 Autograder Runtime Discrepencies
I noticed that submitting the same code to the autograder gave me slightly different run times for some tasks like <0.05s difference for the largest tasks. Why does this happen and can I assume that the runtime of final grader will be consistent with what I see currently?""",
    """build error java

can anyone provide clarification to what this error means?""",
    """Out of Order Case
What should the behavior of the DFS be in this case:

3 2

1 0

2 0

The algorithm will initially visit 0 and then find no edges coming from it. Then it will later visit 0 when it is looking at adjacent edges from 1. So what will the outputted order visited be? """,
    """will we be penalized for using recursive python?
if to make it work we have to increase stack size and recursion limit, will we be penalized for implementing our solution in python recursively?

will we run into any issues with timeouts?""",
    """Ideas on how to associate an edge to its letter type in Java?
Would it be inefficient to have a 2D Array since it's initialized just to store a subset of edges? Another possibility is using a hash map, but since Java doesn't support tuples, creating that class Tuple comes with its own set of problems? Map.contains requires a key, which we won't have unless we create a new object of class Tuple, which wouldn't have the same pointer regardless of what's in map.

I'm not sure how to correlate edges with letter type otherwise?""",
    """Better way to loop edges?
Currently I loop through all the edges everytime I do dfs for node i to look for edges starting from node i. However, this seems to cause a problem of "RecursionError: maximum recursion depth exceeded in comparison". How can I improve to solve this problem?""",
    """Java version for Q3
This might be a dumb question but the assignment says the compatible java version for Q3 is 1.8.0_265.

However when I run "java -version" on my terminal, it appears that my openjdk version is 11.0.4.

Will this be an issue when I am trying to submit? Should try to convert to an older version of java, or should anything above Java 8 work?""",
    """resource.setrlimit error
hello! i'm working in python trying to set my rlimit so i can implement a recursive solution.

However, I keep getting this error: ValueError: current limit exceeds maximum limit no matter what i set as my hard and soft values. Please help!

Saw some forums about how it doesn't work well on MacOS..which I'm on""",
    """Quick start for q2?
Can anyone give some ideas of how to start Q2?""",
    """It may be useful to try to tackle an easier, special case of the problem. Solving the special case might give you an idea of how to solve the general case.

If you're stuck, try writing out what you're trying to solve in English. List out in bullet points or short sentences what you want to find and why. Once you get that, think about what you learned (DP, greedy, stable matching), and see what this problem is most similar to. Is this more of an interval scheduling (ie more greedy), or is this more of a weighted interval scheduling (DP). Essentially, in this course, many problems can be reduced to a base problem you learned. So can you say "this is an interval scheduling with x twist" or "this is weighted interval scheduling with y twist". Additionally, you can try drawing out example schedules, and see if you can draw out examples of edge cases or cases where you would not want to give someone a key. Once you figure out those, then think about what data structure would be best with the data you have? A beauty about problems like this is you can choose if you want to organize the data given (the schedule) into whatever you want. Maybe list out some data structures you remember from 2110, and think about the unique properties of each data structure. Do you want a list? A map? a linked list? A tree? Try different structures and see which one best suits the relationships you need to highlight. Also consider if you need to sort. Finally, use the data structure/sorting plan, and determine how to account for the edge cases you thought about above. """,
    """Q3 input
I'm a bit unfamiliar with what exactly an ASCII character stream in stdin looks like exactly, is there any chance we could be provided with an example input? Would it look something like

35 38 0A 30 31 0A 31 32 0A to represent

5 8

0 1

1 2

And if so, what would numbers larger than 9 look like, would it then be like 3233 3130 0A

to represent 23 10?

Thank you, i tried figuring it out via googling things but i just want to be sure. i know there was some other posts asking a similar question but i didn't see a straight answer to it.""",
    """Office Hours
I've permanently moved my OH to Wednesdays from 5pm-6pm. The changes aren't reflected on the course site yet but they will be soon. The only inaccuracy currently on the site is the time(i.e. the zoom link and the google doc link are still correct). Sorry for any confusion. Hope to see you at 5pm today! """,
    """OH Waiting Queue
Hi, here is a link to my OH waiting queue""",
    """Multiple files for autograder and submission
I am wondering if our code can comprise of multiple files (multiple classes in Java). It seems that the autograder only accepts one file. Is this the same for submitting on cms? Thanks""",
    """Extending OH
I'm extending my OH until 6:30pm.""",
    """Tester Acting Strange
The tester says my code is giving the wrong output but I'm comparing the output to an earlier version of my code that passed that same test case and they're the same """,
    """Homework 2 Q1
For question 1, are we allowed to assume that network B's programs in the list are already sorted by rating, or would we need to include a step for such sorting in our algorithm?""",
    """Try not making unnecessary submissions.
Title.

The deadline is near and everybody is anxious to submit their code. However try not to make unnecessary submissions where you changed a tiny detail of a wrong submission, but rather take some more time to find other mistakes that might have contributed to WAs or TIMEOUTs. The grader right now has queued submissions of over 10 minutes ago, which means that you are slowing down the other students.

Also if you have 2 submissions queued, you are doing something wrong.

Hope you understand.""",
    """Q2 Cyclic schedule
I think I understand how to do a 0 - 24 hr algorithm. But since you can have a cyclic schedule, I failed to see how to pick a starting point. Any suggestions? Thanks!""",
    """q2 proof of correctness
Any tips on how to prove correctness for the second problem? I'm trying to prove that the size of my returned set equals the size of an optimal solution but depending on the input the actual shifts that make up that set may be different so I don't think I can prove that the sets are equal. Thanks!""",
    """timeout java recursion/checking for non-visited dfs trees
i'm getting timeouts on the last six cases for my java recursive implementation of q3. i have switched to using stringbuilder for my output as suggested, but now i'm wondering if i should be converting the input to stringbuilder as well?

in addition, the one place where i think there might be o(n^2) time is how i call dfs inside a loop since i am checking each node to see if it has been visited so that i may perform dfs on a new tree in the dfs forest after the previous one has been iterated through. if this implementation is faulty, are there any suggestions on how to reduce it?""",
    """main function naming
On the DFS_labeling page i see it says to name the function main if using Java. What should it be called otherwise? or what should i do otherwise to make sure it processes the file correctly? i wrote mine using Python.""",
    """Q3 first test case in the automatic grader
Is there a reason why I'm passing all of the test cases in the automatic grader but not the first? I get EXCN.""",
    """If the autograder passes, do we get full points or are there more test cases during actual grading?""",
    """Does anyone know what a preorder number is?
I thought that when you run a preorder traversal, you get a sequence of nodes. What does the preorder number represent then?""",
    """Only fails test case 7
I implemented an iterative DFS in Java, and I pass all the test cases except for number 7 which I Time Out. I noticed that, compared to other test cases, this isn't necessarily the most computationally expensive one. Does anyone have an idea for why this might be happening?""",
    """Q1 Proof Setup
I am lost as to how to use exchange argument for Question 1. I know I should switch things around in the optimal solution to get to my own, but I have no idea how that would work. Can I get some hints?""",
    """study groups
Would anyone be interested in having an online study group where maybe we could meet and discuss a couple times a week?""",
    """Using bufferedreader for input
Sorry if this is an obvious question, but I don't have much experience working with stdin. In Java, how would you use bufferedreader to read the stdin? Since it stops reading when it sees a newline character, wouldn't it only read the first line of the input? Really confused!""",
    """Only passing the first 8 cases
I'm not getting time outs from the larger cases. Instead I'm simply getting errors. How is this possible? Please help...

Edit: Figured it out. It was a careless mistake. Thanks for all the help anyways!""",
    """c++ implementation
I wonder if anyone uses C++ and recursion to do HW2. I used class and it keeps giving me "Segmentation fault" when the input is too large. It works correctly for small inputs.

It forces me to implement it with iterations. It works, even with large inputs, but I wonder how to make it work with recursion. I wonder if it's due to the large stack size with recursion. Just speculating......""",
    """Clarification on Shamos-Hoey Algorithm
I was reviewing my notes from today's lecture and am very confused. Some questions:

1) I don't understand how we return the closest point within each subproblem. How is y-distance taken into account? We keep splitting each subproblem in half by x-distance, so when we reach a base case with two elements, they are the closest in x-distance. But I don't understand how we are taking into consideration any of the other possibilities (i.e. points within a subproblem that are closer overall despite not being the closest in x-distance). Sorry if I am missing something super obvious.

2) If we compare the leftmost point of Qr and the rightmost point of Ql after performing the computations for the subproblems, and their distance is > delta, there is no need to do the post computation, right? We only do that if their distance is < delta? What if it is = to delta?

Thanks in advance :-)""",
    """Union-Find Data Structure | Complexity
Time for find is O(log n) and time for merge is O(1). Can someone explain why the time complexity for the whole algorithm is O(n log n)? """,
    """Is HW2 Q3 graded on code quality?
If our code passes all the test cases in the autograder can we be sure that it will be given all 10 points or can points be deducted on readability/code quality etc?""",
    """Runtime for Java
I used the exact the same method that using fast I/O and StringBuilder to buffer output but still can pass testcase 7, for other 13 testcases that can pass, the runtime is very close to the limit. So would professor increase a little bit of runtime strict for JAVA?""",
    """11:30 AM OH Right Now?
Are the OH right now still happening? I'm not being let into the zoom room""",
    """Fast Python Input
I currently use input and it takes a long time to just take in the inputs. Is there a way to take the inputs faster in python? I read someone saying something about buffering but Im unsure what that means and how to implement it. Thanks!

Also, is it even possible to do this in python without getting a timeout? Or should I not waste my time and just move to java?""",
    """StringBuilder
I've seen some people talk about using StringBuilder with Java to make printing the outputs faster, but I'm not familiar with StringBuilder so I'm not sure how to do this. I looked at the documentation online and I'm still kinda confused. Can someone give an example of how to use StringBuilder for fast printing?""",
    """HW1 has been graded
HW1 has been graded and comments are on CMS. You have a week to submit any regrade requests you may have. """,
    """[hw2] different behavior when running p3 on local and cms
When I run my code on local machine, it works well but when I run it on cms, something weird happens. Below are the two results: the first one is the result on cms and the second one is on my local machine. This thing happened after I use OrderedDict in python. I don't know whether the problem is because of that.""",
    """Pseudocode standards and readings?
(This might be similar to @52)

I realized I don't know how to write pseudocode while doing the HW, is there a standard for this course? Do ppl have any recommended readings on the style?

Thank you!""",
    """Does postorder as an order actually matter?
Is there a difference in correctness if I use the postorder value as a boolean (i.e, exists or doesn't exist) instead of an actual ordering from 0 -> n - 1? I don't see any place where postorder values are compared, only where their existence is checked.""",
    """Are 5PM OH still happening?
Are the 5PM OH still happening today?""",
    """HW3 Q2 Assumption
The problem asks us to divide a set of n precincts into two districts, each containing n/2 precincts. Does this mean we can assume n is even?""",
    """Can an additional extension be requested after an initial extension?
I asked for a 24 hour extension yesterday which was granted, but I am having trouble that I believe warrants an additional 24 hours. Is it permitted to request more time for an extension after already receiving one? """,
    """Dynamic Programming in a nutshell""",
    """How to proof correctness using DP
I am a bit confused as to how to prove the correctness of a DP, shouldn't its validness be proved already when we construct our recursive case? """,
    """Small Question about Bellman-Ford algorithm
At the end of the lecture on the Bellman-Ford shortest path algorithm, it was mentioned that outdegree(v)=m. Are we assuming that the graph is directed then for the algorithm? For undirected graphs, the notion of there being an outdegree would not be useful.

Plus, I can think of the simple counterexample where an undirected graph has only two nodes with one edge between them, in which case each node has outdegree 1, and so the sums of outdegrees are 2, even if there is only one edge.

If the graph is undirected, does anything change at all for the algorithm? I do not see any immediate reason myself why it should change.""",
    """finding non-overlpped interval in weighted scheduling problem
During the lecture, we said there is a way to find p(i), the interval with latest end time that doesn't overlap with i, within O(n lgn) time. How are we supposed to do that?""",
    """K&T 6.3
What does it mean by "if and only if the minimum is obtained using index i"?""",
    """Lemma in Bellman-Ford
Just want to make sure I actually understand this proof of "there is a shortest path with no more than n-1 edges". So we proved this lemma by taking an arbitrary shortest path P.

If P doesn't contain a cycle, this is a trivial case because every node along this path must be distinct so it cannot have more than n-1 edges.
If P does have a cycle and we call it C, we proved that C has weight 0. Therefore, we can construct a path P' from P but deleting C. P' and P has the same length, so P' will be our shortest path with no more than n-1 edges.""",
    """OH 11:00am -> 4:00pm Today
I am moving my oh from 11:00pm to 4:00pm just for today. Sorry about any inconvenience. """,
    """Helpful Short Videos on Bellman-Ford
I came across these videos on Bellman-Ford which I found extremely helpful and wanted to share them with the class:""",
    """These unfortunately give you absolutely no clue why Bellman-Ford is correct, or any complexity analysis, or any indication that there is a connection with the general technique of dynamic programming. Please do not consider these a substitute for the presentation in the textbook or lectures. We are trying to teach general techniques of algorithm construction and analysis, not simply specific algorithms.""",
    """A post on reddit called me a "dick" for the "massacre" of Poet in this post. I want to apologize if it sounded that way. It wasn't directed at Poet at all, it was only about the videos. I only wanted to point out that cutesy animations may be fun to watch, but they are superficial and do not touch on the deeper scientific content that we are trying to get across.

Anyway, very sorry to have offended. I would never do that purposefully.""",
    """11am OH Today
Are there 11:00 am OH today occurring? I've been waiting for the host to start the meeting? """,
    """Google Docs for Homework 3
I submitted my last two homeworks by "typesetting" them in Google Docs. There is a way to add an equation which formats things similar to LaTeX so that anything which needs special formatting is able to show up nicely. I also like having the ability to add digital drawings which I used for the second homework. Is this acceptable for future homeworks? I know on the pdf it specifically says to use LaTeX, but in lecture it sounded like this was to avoid the issue of handwritten homeworks.

If we have to use LaTeX, that's okay, I just thought I would check since I would prefer to use Google Docs since it's much faster for me!""",
    """3 PM OH -> Saturday 11 AM
Moving my office hours from 3 PM today to 11 AM tomorrow! However, I can make them a little longer if needed tomorrow! Sorry and thanks!""",
    """Textbook question 16 pic?
The online textbook I am using has a blank page where question 16 of chapter six should be. I reached out to the owners, but who knows if they will respond to me. If someone could email me a pic of the question, that would be awesome!!""",
    """Q1 problem setup
"Each ROTC person on campus except the ranking officer reports to a unique superior officer."

Does this mean each superior officer only has one direct subordinate, or that each subordinate only has one superior officer (and multiple subordinates can have the same superior officer)?""",
    """HW3 Q2 Time complexity
I have some ideas on how to construct the problem using DP, but I had some hard time figuring out the time complexity. Suppose each step in DP is constant time, how am I suppose to find out the "size" of the problem? I know that in class we visualize this kind of problem using a matrix and edges pointing between them, how should we do a similar thing for this kind of problem that is must larger/complex? Thanks!""",
    """Proving correctness of dynamic programming algorithms
I was looking at the textbook for proofs of correctness for algorithms developed with dynamic programming, and most of them seem to just say that the correctness follows from the recurrence relation. How exactly do we go about proving that the recurrence relation is correct, other than describing how we came to that equation (which is what the book seems to do)?""",
    """Okay to use HashMap for memoization?
Hi,

I was wondering if I could use hashmap for the memoization of Q1 from HW3, because I want to store the nodes mapped to their optimum values.  Because I want to do a post order traversal of the tree, is it also okay to have a recursive algorithm instead of the iterative examples in the book?  I do not know how to encode starting from the leaf nodes iteratively because the nodes are not easily stored in a "post order array" that I can then loop through in order.  would forming this post order array first recursively and then doing the actual solution algorithm iterativley be a better approach?

Thank you!""",
    """HW3 #2 Formulating As Dynamic Programming Problem
Hi, for #2 on HW3 I am trying to formulate the problem in a similar way as other dynamic programming problems we've done and I'm having some trouble. This is because, from what I see, there is no obvious "base case" or way to split up the solution into smaller parts. I tried thinking of it as "for any two precincts, we know they are either in the same or different districts" but didn't really get anywhere with this as it seems like there are so many pairs of precincts that this might be very inefficient. And, brute forcing this problem (checking every possible way to split the n precincts up into 2 groups) would be exponential, if I did the math correctly.

So, I was wondering if you had any ideas of example problems that I can reference that might help with formulating this problem as a dynamic programming problem, or any clues / ideas of how to think about this in order to make it into fit into this category. Thank you!""",
    """Q1 sudocode
Can I define a data structure to represent the ROTC tree for my sudocode representation of my algorithm?""",
    """Q1 Output the sequence of calls
Hi,

I am not sure how we want to output the list of phone calls because multiple calls happen in one round.  should I output the order that the root calls all of its children, and then the order of the children calling their children or should I output a preorder of the root down to its leaf?

Thank you!""",
    """HW3 Q2
Am I correct in thinking a set of precincts is susceptible to gerrymandering in favor of a given party A if and only if the precincts can be divided such that A wins the both of the districts and A has the overall minority of votes? Or is the second condition not necessary there?

Thanks!""",
    """Moving my OH this week from Sunday to Wednesday
Hi guys,

I'm moving my OH just for this week from Sunday 4-5 to Wednesday 7-8 PM. Sorry for the inconvenience and thank you for understanding!""",
    """Cycles in Q1?
Is it possible to have a cycle in terms of who reports to who (e.g A reports to B reports to C reports to A)? I understand that this makes no sense from the perspective of rank, but it doesn't seem to be explicitly ruled out.""",
    """Moving 12 PM Office Hours
Sorry for the late change but I will not be holding my regular 12-1 PM office hours today. Stay tuned for when the make-up date will be. Will be posted here.""",
    """Sorting Q1
For out pseudo code representation, I am trying to sort a list and was wondering if I can just put .sort() or I should actually sort it?""",
    """parallelism and runtime
When we provide a runtime calculation, are we allowed to exploit parallelism for this? I don't think anyone has single threaded computers anymore, and while I'm not asking for unlimited threads as then we could pull off some fun NP stuff, but having two is sometimes nice to do multiple unrelated calculations at once.""",
    """HW3 Q3 Solution = algorithm?
The handout for Q3 states "Give an efficient dynamic programming solution". By "solution", is this the same as giving an algorithm (and thus we'd need to analyze runtime and prove correctness)? Or is there something different we're supposed to be doing here?""",
    """POLL: programming language of choice for hw2
I've always wondered how Piazza polls work""",
    """Office hours 4:00
Hi I'm currently waiting at the 4:00 office hours with Yiduo and the host has yet to start the meeting. Have the office hours been moved? Let me know!""",
    """Shamos Hoey Algorithm Runtime
In the Shamos Hoey algorithm claim where p and q are within 16 elements on the list of each other in the sorted list of S, we say that finding the closest pair in S has a runtime of O(n). For each node in list S, don't we need to check all other n nodes in S? And if there are n nodes, wouldn't that be O(n^2)? Please clarify or let me know if I'm misunderstanding - thank you!""",
    """HW3 Document Preparation System
Would using Google Docs/Word be an acceptable replacement for Latex?

(I apologize I just realized this has already been asked).""",
    """Running time about HW3 Q2
If our runtime is n^4 * m^2, is it a valid result?""",
    """Feedback on HWs?
Is it possible for us to get feedback on hws, for example, for which part did we lose point? Thanks for any info!""",
    """Moving Tuesday 10am office hour to 1pm
I will be moving my Tuesday(tomorrow) 10am-11am office hour this week to the same day 1pm-2pm due to a conflict.

My OH next week will still happen at the regular time(10am Tuesday).""",
    """Q2 Number of Precincts
For #2, should we assume that the number of precincts, n, is always even?""",
    """HW3 Q1 Binary Tree?
Can we assume the input is a binary tree? Or can one superior officer have more than 2 direct subordinates?""",
    """Format of solution
Is pseudocode necessary or is a description of the algorithm in paragraph form ok?""",
    """PSET 3 Question 1
For question one on this week pset can we use graph traversal algorithm or do we have to use dynamic programming?""",
    """Office Hours moved today?
I noticed Yuwei moved his office hours but I don't see any such message from Shrey Baid. So, I was wondering whether Shrey was still having office hours today?""",
    """Julia and Wanxing OH Cancelled Today
Sorry for the late notice but our office hours are cancelled today from 11:30-12:30. Note that there is another OH going on at this time anyways, so please attend that session if you have questions!""",
    """Q3 Set of symbols the same at each state?
For question3, is the set of symbols that a state can output necessarily the same at each state?""",
    """HW3 Q2 gerrymandering
What if a particular political party actually has more supports than the other, so it has no choice but to win in both districts with any partition? In this case, it is not unfair, right?
This problem is not described in the problem (maybe because it is not required), but I just wonder whether we should deal with this exceptional situation in our algorithm. Or do I think in the wrong way?""",
    """HW3 #1
Do we know beforehand what the organization of the people looks like, or does the algorithm we provide need to determine how many subordinates each person has?""",
    """hw3Q1
Hi, for this problem, I'm currently using a method that is similar to dfs, and this gives me the list of nodes visited in the order. However, I'm not sure if this is the valid approach; also I'm very confused about how to calculate how many rounds is needed to complete the task. Could someone explain this? Thanks in advance""",
    """hw3Q1
When we're outputting the sequence, is it ok if the output isn't ordered by round? For example, is it ok if I output tuples in this order:  (1, A->B), (2, B->C), (3,C->D), (2, B-> E) where the round associated with an edge is correct but the round is out of order? """,
    """type hw3 solution in word document
Can I type my solution in a word document instead of using latex?""",
    """proof of correctness q1
any tips on how to do this? I was stuck on how to construct the recursive case for a proof by induction, so just wondering if there were other ways to do it.""",
    """HW 3 Q2
Can we assume that m is even as well, in addition to n?""",
    """Have you used LaTeX before this course?
I enjoy LaTeX, but understand some of my classmates may be unfamiliar with it... Polling out of curiosity.""",
    """HW3 Q1
As a follow up to another question regarding what we should assume we're given, can we assume we're using a data structure where we can access all officers at once (we don't necessarily need to traverse down the tree)?? """,
    """HW3 Q1 Tree Specification
May we assume that there are at most three levels of depth in the tree: the node, superior officers, and the leaves?""",
    """POLL: In the thick of the job application process?
Are you, or are you not (for after the 2020-2021 school year)?""",
    """Knapsack Problem, Time Complexity
Why does the knapsack problem have time complexity O(nw)? I also think I'm misunderstanding what the w here means because I thought it was a constant representing the upper bound of the total weight held by the knapsack. Thanks!""",
    """Giannis's office hours today?
Is Giannis having his 11am OH today?""",
    """Giannis OH Today
Sorry to everybody who tried to join my OH today. I had no Internet connection and no data for the last 2 hours (never happened before), so I could neither host the OH nor inform you about it. I will host it tomorrow instead. Keep an eye out for a follow-up to this post.""",
    """hw3q1 runtime
how would i reason about the runtime for this question? i use a data structure to organize my subordinates, but how do i (if i should) reason about the time it takes to call every officer in the tree?""",
    """hw3 q1 runtime complexity
For each node in the tree, (except for leaf nodes) I perform an ordering on all the subordinate nodes of the node. While I know this is O(klogk) if there are k subordinates, what is the overall complexity of this for all the nodes?""",
    """Proving algorithms discussed in lecture
If, for example, I decided to use the Knapsack problem or subset sum algorithm described in lecture today in this problem set, are they necessary to prove? I.e. can I assume their correctness, optimality, and runtime complexity and focus on the other parts of my algorithm?""",
    """HW3 Q2
When figuring out whether a list of precincts is susceptible - is it only susceptible if there could've been another outcome (so if someone actually has a majority in all possible combinations of precincts and districts then it wouldn't be considered susceptible right)?""",
    """HW3Q1
Can we assume we know from the input how many children a given node has, or would we have to figure that information out with a "helper" function? I'm just sort of confused in general on which information we're given""",
    """Moving Wednesday 5pm OH to Friday 5pm
I've been feeling under the weather. Will be moving by OH to friday at 5pm. Sorry for the inconvenience. Hope to see you then! Look out for a follow up post.""",
    """What are we allowed to assume?
Can I assume that at for a child c of a node, I know the rounds needed to traverse the subtree c""",
    """HW3 Q3
Can I get some hints on the best way to find the next state? I was thinking of finding the next state that outputs the next letter with the greatest probability but this might lead to a dead end in the middle of the process. But if I find all paths that work first then optimize that would be exponential n^n.""",
    """Assuming size of A for HW3 Q3
Should we assume that the alphabet A is small for question 3? Similar to how we assumed the maximum weight was small in the subset weight problem""",
    """Subset Sum algorithm
How did we get the runtime for the Subset Sum problem discussed in class?""",
    """Q2 Approach
I’ve been trying to think of this question as a knapsack problem but I’m struggling with generalizing the approach and fitting it to this question to get a recurrence. How can I think of the technique in a way that will help solve this question?""",
    """Pseudocode?
Is it necessary that we provide pseudocode/data structures explaining our algorithm? Is it sufficient to explain clearly in English, without pseudocode or data structures, what our algorithm is?""",
    """A typical night spent with my algo pset""",
    """Question on HMMs
Does an HMM first output a character when it enters the starting state, or only when it moves into a new state from the starting state?""",
    """Q2 Doesn't the winning party need to have a majority in the general population?
I read a piazza post @504 and I got confused because the student response said that the winning party doesn't need to hold a majority in the general population to hold both districts.

From what I gathered by the textbook and the example, it seems like the winning party must hold a majority in the general population. In order for a party to win one of the districts, it must have a majority of voters in that district. If it want's to have both districts, it must have a majority of voters in both districts. Since there are only two districts and the two districts hold all the precincts, doesn't that means there is a contradiction if the winning party held both districts but doesn't hold a majority in the general population?""",
    """Q3 tips for storing the path?
I'm having trouble thinking of a good way to store the path. My ideas included just lists of states, or a grid graph thing like for sequence alignment, but I can't figure out how it works with recursion and potential repeated states. Any tips? """,
    """induction proofs for 2-D arrays
Any tips for doing a proof by induction for questions involving an opt(i,j) that's essentially like a 2-D array? I'm having trouble figuring out what to induct on. If I induct on j, then I can assume opt(i,j−1), but am I supposed to do something with i?""",
    """HW3 space complexity
Are we supposed to give space complexity analysis for this problem set as we did before? It only asked for runtime analysis from the instruction. Just want to make sure.""",
    """HW 3 Q1 Sequence of Calls
In @502, the instructor said that "any representation that uniquely determines which calls occur in each round is ok". I just want to clarify: given the example in the textbook, does it suffice to output: A -> [B, D] and B ->[C], or do I need to process the output above to get round 1 = (A -> B) and round 2 = (A -> D), (B -> C)?""",
    """proof of correctness by induction q2
any tips please? unsure what would be the inductive hypothesis, or even the base case, if we think of this as something similar to the subset sum problem""",
    """Most Likely Path in Q3
In Q3, when it asks us to find the most likely path in M that could have output the string, does this mean we are looking for the path that, if taken, would have the highest probability of printing the string, or the path that is most likely to have been taken given that the string was printed?""",
    """hw3q1
can we assume we are using linked list to represent the tree?""",
    """Does Q3 require pseudocode/algorithm & proof?
Since it just asks for a DP solution, should we still do the usual algorithm, runtime, proof, etc. or just recurrence relation""",
    """Proof
I'm having some difficulty proving question 1. It seems like we want to do proof by induction but I'm not sure how to attempt the induction step/prove that my equation i''m using to calculate minimum rounds works.

I was told by a TA to focus on how I list the rounds of the children of that node (so it made me think about a greedy stays ahead approach but I'm unsure if this can actually help prove that my equation works.""",
    """Pseudocode
If, in one of my algorithms, I want to trace back through an array can I just say "trace back through the matrix and..." or do I need to define the trace in more detail""",
    """HMM clarification
I was just a little confused by the definition of NEXT(s, ) does this mean that for every s,s' in S there is a NEXT(s,s') probablity? As in every edge has a probability of connecting to every other edge.""",
    """Resursive runtime
I am super confused about how to find the runtime of a recursive algorithm. If I have a recursive call to a function I am defining, but there are non-constant time operations within this function apart from the recursive call, how do we account for those?

For instance, if I have n recursive calls and after that there is a sorting line, is the overall algorithm O(n) + O(n log n) = O(n log n)? Or is it O(n^2 log n) because that sort was technically run in every recursive call?""",
    """Q3 induction
should we be inducting on states, the string, or both? Not sure if you can answer this question on here.""",
    """Recurrence relation
I’m not sure how recurrence relations fit into the solution, is it something we are supposed to define and base our algorithm off of? Or do we define it from the algorithm to help proof the algorithm is correct?""",
    """Q2 union
I want to do something similar to the subset sum algorithm which was explained in @571. Within the answer there was the union of two sets. Do I have to go into detail about how to find the union as well as explain why the runtime is O(W) where W is the maximum total votes or whatever it may be.""",
    """How to relate Subset Sum to Q2
I understand how the "redistributing weight" idea factors into gerrymandering, but I'm confused on how to apply this to the subset sum problem. What sets are we exactly taking the union of?""",
    """HW2 grades/solution
I was just wondering in the future if it would be possible to get the previous hw's grades/solutions/feedback before the due date of the following hw? It would be helpful to see where I am going wrong and where I could improve before submitting.""",
    """Ideally that would be great, and I wish we could, but I'm afraid it is an unrealistic expectation. Your graders are students just like you, who have classes and other activities. We give them a week to do their grading and ask them to get it done on time, but there are 42 of them and there are always stragglers who get started late with their grading, just like a good percentage of you don't get started on the homework until the day it is due. We cannot release the grades and comments until they all finish. Another contributing factor is that we used to have in-person grading parties where we would all get together in a big room and eat pizza or Thai food and grade all evening till we got it done, and that is no longer possible. I really miss the grading parties and I think the rest of the staff do too. It was really a fun part of being on the course staff, and now that is gone. You don't see it, but we have a very active Slack channel where all communication among the course staff takes place, but it is a poor substitute.

Please understand that circumstances are difficult right now for everybody. It is an imperfect situation and we are trying to keep it running as smoothly as we can. We have had some attrition in the course staff too. Since the start we have lost 3 graders who were not able to keep up. I have asked for more grading support, and a call went out, but there are no more graders available. We did get an extra part-time senior TA (Spencer) who just joined the staff.""",
    """HW3 Q2
Can we assume that if the given set of precincts is susceptible to gerrymandering, then party A would be the one that holds the majority in both districts?

Edit: It seems like a valid assumption given @559 but I wanted to make sure!""",
    """3D Array for Q2
I don't think this will be too specific because a TA straight up said it in OH, but I guess if this gets privated I'll know.

So a TA said that it's easier to use a 3D array for the memoization on q2. They said that one of the dimensions was the number of voters? I think I get that the second dimension is the number of precincts. But I'm super stuck on what the third dimension should be, can anyone give me a hint?""",
    """HW3Q2 Best possible complexity
Probably an odd question, but what's the best possible runtime complexity we can have for our algorithm for Q2? I currently have O(n^3m) algorithm and I was wondering if I can improve on that""",
    """Q2 breaking ties
What would happen if a district had the same amount of Party A voters and Party B voters? Do we just arbitrarily break the tie and give the win to the party that won the other district?""",
    """Q2 Induction Proof
For question 2, I am using a 3D array to store the precomputed values of my algorithm, so my recurrence relation depends on 3 indices. Can I induct on all three indices at once, with an inductive hypothesis that assumes all A[i'][j'][k'] are correct where i', j', k' < i, j, k respectively?""",
    """Q3 String length
Hello! I was wondering what our algorithm for Q3 should do in the case of an empty string? Can we assume that the length of the given string is >0? If not, then would the probability of outputting an empty string be 1 (since we wouldn't enter any state), 0 (since the probability of a state outputting an empty string is 0), or something else (if "" is considered a part of the alphabet A)?""",
    """Proof by induction for multiple variables
If my recursive function involves more than one variable, say f(x, y, z), then to prove its correctness by induction, do I need to prove that f(x+1, y, z), f(x, y+1, z), f(x, y, z+1), f(x+1, y+1, z), f(x+1, y, z+1), f(x, y+1, z+1), and f(x+1, y+1, z+1) are all correct assuming f(x, y, z) is correct? Thank you!""",
    """Returning sequence of calls
Hi, so on Q1 i have a working algorithm, however I am having trouble finding the sequence of calls. A TA said that you had to "backtrack", and I have read the book section on this, but I'm still kind of confused because the book's example is very linear (weighted scheduling problem) so it's easy to backtrack, whereas here it doesn't feel that way. How can I "backtrack" on a tree structure?""",
    """proof of correctness longer than algorithm?
Is it odd for the proof of correctness to be longer than the algorithm itself? Throughout the last homework and this one, I've noticed the fact that my algorithms (including the thought process that goes into designing them) is consistently about a page long, while the proof of correctness is 1.5 pages long. On Every. Single. Question. Which strikes me as odd because I wouldn't expect this to happen. Is it stylistically bad to have long proofs of correctness?""",
    """Runtime of start, output, and next
Can we assume that the given functions to retrieve the start, output, and next probabilities take constant time?""",
    """Q2 time complexity
I've constructed my algorithm and as a final step, I need to go through an array of all possible combinations of "n choose n/2" to figure out if it is susceptible to gerrymandering. I'm not sure how to express the size of this array""",
    """HMM quick question
Can the outputted states for the most likely path repeat states, as in could the path return to a state multiple times throughout the path?""",
    """q3 output hint?
Hi, I've been super stuck on how to get the most likely path of Q3. I have an algorithm that gets the most likely probability, but I don't know how to trace its path because as the algorithm is going we don't know which path will end up being the maximum probability path and it's not like we can trace them all. Am I thinking about this wrong? I'm also having trouble figuring out how our memoized info helps us, but I'm pretty sure I'm memoizing the wrong thing too""",
    """DP Subset Sum/KnapSack weights
Just wondering, to make this DP algorithm work with the time complexity mentioned in class, the weights must be integers, right? otherwise, there will be infinite possibilities of weight in the induction process.""",
    """hw3 3
For this question, if we first start on a node s1 and then we discover that this node cannot produce a1, then we need to look at other nodes; however, do we just pick the next node randomly? Do we need to multiply some probability, say NEXT(s1, s3), for starting again at another state? I think if we just randomly pick another state in the set S we dont have to multiply any prob, but I'm not exactly sure.""",
    """hw3 q1
I'm having a really hard time figuring out how to start this problem. I have a general idea in my head for how the algorithm might work, but I can't seem to figure out how to translate that idea into an actual algorithm. Does anyone have any tips about how to get started? Thanks!""",
    """HW3 Q3
For the example given in question 3, how did you compute that there are "3^3 = 27 paths that could output the string aab" and "2 * 3^2 = 18 have nonzero probability, since start(t) = 0." I'm really confused thanks""",
    """HW3 Q3
Is it possible for two or more path to have the same probability and for both of them to be the likely path?""",
    """hw3 q1
I figured out the algorithm for finding the minimum number of rounds needed, but I'm having a hard time figuring out how to output the actual calls for each round. I thought I could keep a global list to keep track of the calls for each round, but I'm not sure how to figure out which round each call goes into since I'm using recursion. Any hints are appreciated.""",
    """Test Cases for Q3 - HW4
I am uploading a zip file with some test-cases to test your programs, before and after the autograder goes live. It contains every graph with 5 nodes, meaning that if you have a logical error you will probably find it with these test-cases. Errors that these test-cases will not find: out of bounds errors, memory overflows, timeouts, etc.

The zip also contains a script to run your program and compare the output with the correct one.


(it will probably take a while to run though)

[EDIT 10/05] Fixed the inputs in the zip (the lines ended with both \\n and \\r instead of simply with \\n). For those of you using standard reading functions (cin, scanf, Scanner, input, etc.) you should notice no difference.""",
    """Handouts Page Helpful for HW4 Q3
The HW4 release mentions that there may be some information on the handouts page that will be helpful with problem 3, is this released yet or is it one of the handouts already listed there?""",
    """Moving OH to Wednesday 3 PM to 4 PM
Hi, I will be moving my OH from tomorrow to Wednesday 3 PM to 4 PM due to a conflict. Sorry for the inconvenience. """,
    """HW 4 Q1
For question 1, I created a graph of nodes and edges representing supply and demand. Since there are a set number of blood types, for the running time of our algorithm, should we generalize it to any number of blood types? Otherwise, wouldn't it just be constant time because there cannot be more than a certain number of nodes and edges due to the restrictions on blood types and the fact that there are only 8 blood types?

I wasn't sure if this gave too much away so I made the post private. Thanks!""",
    """HW 4 topics
Is HW 4 more related to network flow rather than divide and conquer? Will we be learning anything later in the week we need to know to complete it?""",
    """Announcement from ACSU
ACSU's annual Research Night is back on Oct. 8th from 5:30 - 7:30 PM ET! Come join us to learn about the amazing research being conducted at Cornell CS and the current projects of our grad students spanning a variety of areas. If you are interested in undergrad research, there will be opportunities to discuss and join new projects! If you are already involved in undergrad research or are considering grad school, this is an excellent opportunity to learn more! Facebook Link: https://fb.me/e/1vdZqmJXe

Thanks and all the best,
Victor and Judy""",
    """HW4 Q1: using Ford-Fulkerson
For the first problem, I'm planning on using the Ford-Fulkerson algorithm that was demonstrated in lecture today for my algorithm. When writing the pseudocode/explanation for my solution, would I need to include all the steps for the Ford-Fulkerson algorithm in my solution or can I just say "use the Ford-Fulkerson on the graph to find the max flow" and then use that value in my algorithm?""",
    """Q2: Graph Assumption
For question 2, can we assume that the graph consists of one connected component that contains both S and T? Or, should we consider a forest in which you might not be able to reach T from S?""",
    """path in residual graph versus patn in our actual graph

Please correct me if I'm wrong describing the flow in both graphs. In this residual graph, when we push 10 from s to v, we back track 10 units from u to v and then use the 10 units residual capacity from u to t.

I don' think such a path means much as for how the real path in our original graph will look like? Because we will eventually have 10 units from s to v, causing 10 units from u to v backtracked. However, those backtracked units are the ones actually got pushed from u to t. The units we pushed from s to v took place of those flows got backtracked and eventually took the path v-t.

Now it seems like thinking about this process on the original graph only makes it more confusing. I guess I should simply focus on the residual graph when looking at a maximum flow problem?""",
    """Formulation and proof
If we somehow managed to mathematically formulate (like in HW1) a homework problem into a known problem whose solution was shown and proven in class, do we still have to prove correctness? I feel like a proof that our problem is in line with the mathematical formulation is redundant to the explanation of the formulation itself.""",
    """HW2 has been graded
HW2 has been graded and comments are on CMS. You have a week to submit any regrade requests you may have.""",
    """After we submit a regrade request, will we get any confirmation email? I didn't get one.""",
    """Sophie OH Cancelled Tuesday
Sorry for the late notice, but I have a prelim today during my OH so I have to cancel my OH at 3-4 pm. There are some other OH at the same time, so please attend these accordingly. Sorry for the inconvenience.""",
    """Interpretation of demand in hw4 q1
For homework 4 question 1, the textbook prompt states that we are given the projected demand amounts dO,dA,dB,dAB. Does each demand variable represent the demand for that specific blood type or for blood types compatible with that blood type? For example, for dAB+, can we fulfill that demand with any blood type (because AB+ patients can receive any type of blood), or with only sAB+?""",
    """Q1 and Q2 regrade
Can I ask regrade for HW2 Q1 and Q2 since I submitted the instruction PDF instead of my solution. Can I resumit?""",
    """Cancelling my OH for 7-8PM Tuesday
Hi all,

For medical reasons I can't hold my office hours this week. (Mine are 7-8PM on Tuesday). Hoping to be back in the saddle by next week.""",
    """HW4 Q3 has been released at the auto-grader
HW4 Q3 has been released at the auto-grader, code named Villages.

Some things mentioned in the problem definition in the auto-grader worth repeating:

1≤n≤10^5
0≤m≤10^5
The time limit is 2 seconds.
[EDIT 10/6] Terminate your output with a single new line.
For full credit you should use O(n) storage. This is not tested by the autograder, as you will see correct answers even if you use O(m) storage. We will check this later while grading.
Make sure you submit your code both to the auto-grader and to CMS. The code in CMS should match the last submission in the auto-grader (even the comments as it is easier for us to check if the two files are identical). Do not submit code to the autograder after your deadline (due to extensions each student has a separate deadline).
Things not mentioned in the problem definition:

Check @275 for tips and tricks. I try to update it when a bunch of students have the same problem.
In this problem you have to output a single integer. This means that the output will definitely not be a bottleneck (buffering the output etc. as done in the previous exercise will not reduce time).""",
    """Using existing algorithms
Are we allowed to use algorithms that we haven't yet proven in class but we know exist and have already been proven true to help solve the questions?""",
    """Runtime of Ford Fulkerson
What is the runtime for Ford-Fulkerson algorithm we learned in class (with a simple explanation if possible)?""",
    """grading optimality in the homework 2.
I am a little bit confused about the grading guideline in general. I made a "small" polynomial run-time algorithm, which was O(n^2logn) for hw2 question 2. However, I got penalized for not having optimal run-time of O(n), even though my reasoning about the run-time was correct. Piazza post @219 does say that "To clarify:  you do not need to provide the most efficient algorithm.  You need to provide any efficient algorithm.  Here "efficient" is defined as polynomial with respect to the input size".

The question does not state any upper-bound for this problem. So, what is an algorithm that is very unreasonable in run-time? I personally thought O(n^2logn) was reasonable, but two graders thought that it was unreasonable. How should we know about this upper-bound in a problem in general? I would like to know about this, as I would love to get full credit next time

Thanks""",
    """I was also penalized for efficiency, but I think I understand why. The grader pointed out a very easy way to modify my algorithm to run faster. I think that we are supposed to make our algorithms as efficient as reasonably possible, and if we miss an easy way to speed things up we are penalized. Is this correct? If so, I think that's a fair grading scheme but I also think it should be clarified going forward. Thanks Professor Kozen + TAs!""",
    """When we say small polynomial time is good, we are giving you something to aim for, but we will never set limits on you by saying exactly what you need to do for full credit, especially if it is suboptimal. We do not want to limit your thinking. Small polynomial time is certainly good and will be worth most credit, but it is not absolute. If you miss some improvement that we think you should have seen, we will deduct.""",
    """I think that must be a miscommunication, either in the way the TAs expressed it to you or in the way you heard it. It is never our intention to limit you by saying that this is exactly what you need to do to earn full credit, because that is when you will stop thinking. In general a good solution with reasonably efficient runtime, a well-reasoned proof of correctness, and an accurate complexity analysis will be looked on with favor. However, if you miss obvious improvements that you should have seen, there will be a deduction. So you should always do your best and always think about ways to improve your solution.""",
    """Q3 O(n) space
Does this include storing the inputs? If my algorithm takes up O(n) space, but I store the edges from the input before executing the actual algorithm, does that mean I used O(m) space, or is only the space used by the actual algorithm logic counted?

To clarify, I read in all of the edges in main and store them before calling the function that executes the actual logic. This function and it's logic only take up O(n) space.""",
    """Q1 exactly k paths?
should our algorithm return where there are exactly k paths, or at least k paths? in the latter case if there are more than k paths, does it only need to return k?""",
    """HW4 Resubmission
I'm curious if other students are able to resubmit (re-upload) their .zip file for HW4 on CMS. I am currently not able to, but maybe its something on my end.""",
    """Autograder Question
If we pass the autograder before the deadline but then reupload shortly after the deadline (ex. due to the addition of comments), is that okay or will that result in us taking a slip day?""",
    """Hw4 Q2 assumption
For Q2, can we assume that all edges have the same capacity? Or should we consider both cases where edges have the same and different capacities?""",
    """Matthew Xu OH Cancelled Wednesday
Super sorry for the late notice, but I am currently taking a prelim, so I won't be able to make it to my OH today at 3-4 pm. There are some other OH at the same time, so please attend these accordingly. Sorry for the inconvenience.""",
    """hw4 q1 integer assumption
The language in K&T specifies "whole units" of blood supply - can we assume this is an integral flow problem?""",
    """Proving Correctness Q3
Do we have to prove correctness for Q3?
Thanks""",
    """HW 4 Q3: size 2n?
Is the space complexity strictly O(n) or are we allowed to create another data structure that take size less than or equal to n?""",
    """HW4 Q1
For question 1, do we have to only do 7.8(a) or do we have to do 7.8b as well (with the reformulated prompt)?""",
    """Q2 finding the paths
Any tips for how to find the paths? I guess my question is more like how do you guarantee that you choose the best paths so that you end up with at least k edge-disjoint paths if you already know they exist?""",
    """hw4 q1 8 supplies and demand?
This might be straight forward but I just want to confirm. For Q1, would we then have 8 supply variables and 8 demand variables now that there are 8 blood types (factoring in Rh)?""",
    """dfs on q3
if i can pass all the test cases using dfs or bfs on q3 does that mean I stayed within the O(n) storage limit?""",
    """HW4 Q2 definition of k edge-disjoint paths
"there exist k edge-disjoint paths from s to t" = exactly k edge-disjoint paths, or at least k? bc if there were more than k edge-disjoint paths, wouldn't there be k edge-disjoint paths too?""",
    """conservation of flow ford fulkerson q1
should we prove conservation of flow for our graph in q1 or can we assume that is true if we perform ford fulkerson""",
    """Moving THURS 6-7pm Office Hours to THURS 7:30-8:30pm
Go check out CS Research Night!""",
    """Problem 2
If I decide to apply Ford-Fulkerson Algorithm in some degree, should I need to include all the procedure of the algorithm in my pseudocode? Or can I just mention that I will use the algorithm (like I use a function) in the code block?""",
    """Q1
If I am referring to augmented paths x and y that have no common edges, are these augmented paths disjoint or independent?

edit: Also there are no common vertices in the augmented paths""",
    """Friday 11:00am OH Canceled
Hi, I have to cancel my office hour only for this week because of time conflict. Please go to other office hours starting from 12pm.""",
    """Q1 Runtime
Can we just say that the textbook has already proven Ford Fulkerson runtime? For Q1, does the creation of the graph also count towards runtime?""",
    """Hw4 Q3 runtime
Out of pure curiosity, how fast does the instructor solution run for the autograder tests?""",
    """HW 4 Question #2 proof of correctness
For #2 proof, do you have to use something like proof by contradiction or induction? Can we simply explain why the paths have to be edge-disjoint, or would that be not enough? I'm wondering how much details we need for this proof.""",
    """Q3: Max input size
I am wondering what the maximum input size is for question 3. Is it 10^5 for the number of edges? If anyone knows where I could go to get this info, that would be great, thanks!""",
    """Space complexity
If you use two separate arrays both of size n, is it still O(n) space?""",
    """External Libraries Q3
Are we allowed to use external libraries that already exist if there is a data structure I want to use, or are we expected to implement any data structures we may want to use?""",
    """Is the Ford-Fulkerson algorithm greedy?
The way that the textbook discusses the algorithm makes me believe it is not greedy. In particular, it says that greedy solutions to the maximum-flow problem "break down." However, on the Wikipedia page it states that it is a greedy algorithm. Is this right? And if so, what makes Ford-Fulkerson greedy?""",
    """moving friday 3-4pm office hours
Hi, sorry I didn't realize this post didn't go through, but I had to move my 3-4pm office hours today. I'll be holding them tomorrow at 11am-12pm instead. However, to make up for the logistical issues, depending on how many people come, I can make it longer if needed! Thanks and sorry!""",
    """q3
I'm pretty sure I'm hitting O(n) - is there any other reason i could be segfaulting.""",
    """Number of Autograder Submissions
I apologize in advance if this has already been asked, but do we get unlimited submissions for the programming question before it's due?""",
    """HW4, q2
Do we allow to just say "Apply Ford-Fulkerson Algorithm to find the maximum flow value in the graph" without explain how Ford-Fulkerson Algorithm goes?""",
    """q3 segfault
When I increase recursion limit I segfault but when I don't increase it then I fail with 'excn'""",
    """Unable to Run Test Cases for Q3 (from tests-fixed.zip)
I'm setting exe to be 'javac Main.java' and I'm running the script from the folder that contains all the inputs/outputs + Main.java. However, I kept on getting the following error - does anyone know what I'm doing wrong here?""",
    """Column limit
Should we format our code with a column limit of 80, 100, or 120?""",
    """Does the Ford-Fulkerson runtime depend on the graph being implemented as an adjacency matrix?
Or can it just as easily be implemented with an adjacency list? I'm considering this as I'm thinking about the space complexity of my algorithms, and I'm not sure if the graph needs to take up O(n^2) space or not.""",
    """Polynomial vs Pseudopolynomial Time Complexity
Hi,

If we use Ford-Fulkerson in a homework problem and use it's proven time complexity O(mC), and find that our C is polynomial in the numeric value of the input, but therefore only pseudopolyomial/exponential in the size (i.e. bits) of the input, would this be considered an efficient or polynomial algorithm in the eyes of this course? That is, would we be penalized for giving an inefficient algorithm if it was polynomial in terms of a numeric value input? Thanks for the clarification!""",
    """7.7 Survey Design
Why do we want an edge from t back to s in this algorithm?""",
    """HW#4 Q2 Question about Ford-Fulkerson
When the Ford-Fulkerson algorithm is run on a flow graph, the flow values for each individual edge are changed in order to yield the max integral flow value for the source and sink, correct? I'm trying to see that when I return to my graph G' after the ford Fulkerson algorithm returns, the flows on each edge are set according to what yields the max flow.

Also as short followup, is it possible for there to be cycles along the edges of the graph when there is max integral flow? When developing my algorithm for constructing the paths, I'm thinking about whether I need to account for cycles and keep track of nodes visited in a path. Is it okay if I include the same node twice in my path if it is visited again by a cycle?""",
    """Q3 correct on on tests but failed all on submission
I passed all offline tests with the "all correct" printed, but I did not pass any submission tests. I got 0 as output for the submission test 3, which contains 300 nodes and 299 edges, each linking two adjacent ones, I think 0 is the correct answer, but why was mine marked wrong? I also include a new line character after the desired int by doing "print(str(loop(g)) + '\n')" in python, is it something with this format? if so, why could I pass all off-line tests? Any help appreciated!""",
    """How many homeworks will we have?
Will help me determine whether I should use a slip day on this HW or try to save it.""",
    """Set of sets?
Python does not let me implement a set of sets, so I was confused as to what data structure to use to keep track of my connected nodes for q3? Thanks!""",
    """Proving one problem reduces to another
Since I've never done this before, how would I formally prove that one problem reduces to another, and that solving the second problem in a specific way gives me a correct solution to the first? Is there a procedure/template or is each such proof unique?""",
    """Offline test cases, "not allowed to raise maximum limit"
Hi! for the offline cases I got the error stating that I wasn't allowed to raise the maximum limit specifically referring to the line:

resource.setrlimit(resource.RLIMIT_STACK, (100000000, 100000000))
Earlier when I was having some issues someone told me to do this... is this now allowed (its the only thing that lets me pass the autograder)???""",
    """HW4 Q1 pseudocode?
Do we need to provide a Pseudocode for HW4 Q1?

If I say I want to use F-F algorithm, should I write Pseudocode for F-F algorithm, which is already in the textbook?

Thanks!""",
    """Moving Tuesday 3.30pm-4.30pm OH to 3pm-4pm
I'll be moving my office hours this coming Tuesday 3.30pm - 4.30pm to 30 minutes early, 3pm - 4pm, only for this week, due to a scheduling conflict that suddenly came up. The zoom link will be the same.""",
    """Moving Tuesday 11:30-12:30PM OH to Wednesday 3PM-4PM
I'm moving my 11:30-12:30PM OH on Tuesday to be Wednesday 3-4PM for this week only due to a required lab section that got moved to be from 11AM-12PM this Tuesday. Super sorry for the last minute shift. There should be other OH sections on Tuesday 11:30AM-12:30PM to help! """,
    """exception from stackoverflow
i am running into exceptions caused by recursion (from finding the root of a tree i think) are there any hints on how i can fix this? i pass some cases but fail with exception for most of them""",
    """recursion on q3?
How do we determine our space complexity if our solution uses recursion to determine the parent node? I want to ensure that I’m not exceeding O(n) space.""",
    """When will the video from today's lecture be posted?
Hi!  I didn't have a chance to make it to today's lecture live, and now I'm looking to watch the recording.  Will it be posted soon?""",
    """Proving Lack of Solution for Reductions
If Problem A is reduced to Problem B, we must show that solutions to Problem A correspond to solutions to Problem B, and that solutions to Problem B correspond to solutions to Problem A. Do we also need to show that an algorithm for Problem B failing to find a solution to Problem B corresponds to the non-existence of a solution to Problem A, for example?""",
    """Submitting
On the a4 handout it says to submit a text file of our source code. Does that mean you want us to submit our code with the .txt extension as opposed to .py if I used python?""",
    """Q2 multiple edges from a single pair of nodes
Is it possible to have more than one edge (u, v) for a given u and v?""",
    """Lecture videos not being posted to Cornell Video On Demand?
Seems like the last two lectures' videos haven't been posted to Video on Demand? Is it just because Prof. Kozen hasn't gotten to it yet or because Prof Kozen decided to stop posting them? I hope it's the former!""",
    """Iterations of FF and total flow
Is it guaranteed that every iteration of Ford Fulkerson increases the amount of flow reaching the sink node?""",
    """Clarification for HW4 Q2:
Does the algorithm need to find if there exist exactly k paths from s to t, or at least k paths?""",
    """Moving my Tuesday 10am OH to Friday 10 am
Due to some scheduling conflicts, I have to move my office hour from tomorrow 10am to 11am to Friday 10am - 11am. Super sorry for the last minute notice! There should be another TA hosting OH from 10am to 11am tomorrow.""",
    """Timeout Limit
Is the timeout limit on the autograder dependent on the language of the submitted file? If not, wouldn’t that create an advantage to using a specific language?""",
    """Result: Uncaught exception (or broken ruleset).
I wrote my program in c and the autograder is showing the correct number in stdout with no exception. What kind of rules could I be breaking. I'm fairly certain I have no memory leaks and I never allocate an array with length m.""",
    """Office Hours - 10/13/2020 (5:30 - 6:30pm)
I am cancelling my office hours tomorrow due to an interview. Sorry for any inconvenience.""",
    """Office Hours 10/13 10:00AM-11:00AM
My apologies for the short notice, but I need to cancel my office hours in the morning for health reasons.""",
    """Python Runtime for Hw 4 Q3
I had a couple of questions about timing which may have already been answered. Does the autograder allocate more time for python solutions than c++? Also in @704 it notes the runtime of the instructor's solutions on the autograder. Is this the total runtime for all of the test cases or just the longest one? I passed all the test cases but I'm not sure if my solution is fast enough if the times listed are for the total runtime.""",
    """Cancelled Office Hours 10/14 4pm
Hi guys, I'm cancelling my office hours tomorrow from 4-5pm due to wednesday being a day off for everyone!""",
    """Cancelling 7-8pm OH
I can't run my Tuesday 7-8pm OH this week again for medical reasons. Sorry! I should be feeling better soon.""",
    """Q2 Relationship between s, t and G
Can we assume that s and t also exist in V with their edges in E, or are they supposed to be separate nodes that should be manually added to V and their edges added to E?""",
    """Question regarding time complexity for FF
In Q1 and Q2, when we analyze the time complexity, can we just write O(mC) where C stands for the max flow value, or do we need to give an estimate value for C? For example, if we know C<=m, do we need to say the time complexity is O(m^2) or O(mC)?""",
    """Extra office hours today
Due to the large number of canceled office hours today (10/13), since we have a homework set due tonight, I will hold extra office hours from 6-7pm.""",
    """Moving Office Hours to 7:30-8:30pm
As there are a lot of questions regarding HW4, I will be moving my Office Hours from Friday to tonight 7:30-8:30pm for this week. """,
    """HW4 Q1 Demand Clarification
Just to clarify, say a person with blood type AB needs blood. Will he be incrementing the demand for all blood types by 1 or will he only be incrementing the demand of blood type AB?""",
    """Q1
For the runtime on q1 should we be putting it in terms of variables or constants because there are limited blood types/ limited types that every blood type can supply to?""",
    """regrade request?
Hello! I submitted a regrade request for one of the problems in hw2, but never got a response. I was wondering if I should wait longer or assume it was denied? Thank you in advance!""",
    """Paper that uses union find properties.
Just thought I'd share a paper that I read today that uses union-find to solve their problem in an efficient manner. They weren't the first ones to do this, but cool nonetheless to see its application in the wild.""",
    """Cancelling OH from 11:30 to 12:30 on Wednesday
Hi guys, I'm canceling my OH tomorrow from 11:30 to 12:30 due to a scheduling conflict. Good luck with the problem set! :)""",
    """HW4 Q3 correct when I run my own tests, but nothing prints on autograder
When I run my own tests, I am printing the correct answer for Q3. However, on the autograder, none of the test cases print/output anything. I am using python. I am not timing out, it is just nothing is printing to stdout. Has anyone had this issue or have any insight as to how I might solve it?""",
    """changing inputs into ints
my code for q3 is timing out and I think the bottleneck is the way I take in each input line and map them to ints. Currently if I just delete the rest of the code and straight up just take in all inputs (Im not taking all inputs in my actual code; only working with one line at a time and then deleting) it takes ~0.6s for the largest test case (idk if that is par or too slow). Does anyone know an effective way of converting each input line from string to int? currently this is what I do:

list(map(int, data.split()))
where data is the input().

Sorry for the long post.

TLDR: efficient way of transforming input line to int tuple/whatever?""",
    """10/14 Office Hours
Should we assume usual office hours are still going on tomorrow (excluding the cancelled ones on Piazza)?""",
    """Circulation problem where total demand exceeds total supply
This is a general question towards circulation problem. In the lecture & textbook, we used requirement d(v)=0 as a step in proving that circulation problem can be reduced to a a problem of finding max-flow. I think if total supply > total demand, our reduction still works and I am wondering if that's true.

In the event where total supply exceeds total demand and d(v)>0, we have a smaller d(vB) and larger c(A,B) then before, the theorem "for all cuts (A,B), d(vB)c(A,B)" still holds, thus in this flow chart, "max flow = min cut" still holds, and we can still use F-F to find a maximum flow and check if it is larger than the total demand (which may be less than total supply). Intuitively, this is when not all supplies were depleted, and in the flow chart not all edges coming out of S are saturated, but all edges going into T are saturated.

Is that correct?""",
    """Homework due dates
Hi, I noticed that Homework 5 is due on October 22 in the schedule on the course website but due on October 25 in CMS. Can we get that fixed on the course website? Also, are any of the other upcoming assignments going to have their due dates pushed back as well? If so, can you please also update those dates on the schedule? Thanks.""",
    """Semi-Final
Our semi-final isn’t on the exam list anymore (but it was before, even though it was a take-home). Did something change?""",
    """2-3 OH today
I will be about 10 minutes late to my 2-3 OH.  Sorry about that, see you soon?""",
    """Regrade
I felt I deserved some points back from a regrade in homework 2, however my grader did not respond until the last day to respond and at night so I could not respond for the regrade response. My regrade response did not make sense to me, and I was wondering what steps I can take to respond to this?""",
    """Polynomial Time Reductions
Hi,

I was reading Chapter 8 of the textbook and was kind of confused as to why we say Y<=pX refers to problem Y being polynomial time reducible to X when it also means that X is at least as "hard" as Y. It comes to me naturally that since X is at least as complex of a problem as Y is, X should be reduced to Y (problem Y needs to be passed through some blackbox to solve problem X) rather than the other way around that is said by the definition of reducibility. I'd really appreciate an explanation!

Thank you!""",
    """Moving Office Hours
Given that my OH this Wednesday were cancelled due to Fall break, I will be moving my OH to this Sunday(10/18) from 6pm to 7pm. Hope to see you then!""",
    """Handwritten HW no longer be accepted?
Hello, I just found that on the course website, it's said that handwritten HW is no longer accepted.

I'm sorry if I missed it, but was this being announced on Piazza or before any lecture?

I submitted my HW3 as handwritten, will this cause a problem?

Thanks!""",
    """Prof Kozen's pen
Hi Prof Kozen,

the pen you were using during lecture today was smooth with solid ink lines. What kind was it?""",
    """moving 3-4pm office hours
Hi, I'll be moving my 3-4pm office hours to Tuesday 10 AM to 12 PM. Sorry for any trouble!""",
    """HW 5 Q1
Are x and y disjoint sets? For example, can someone be dropped off at x1 and then another person gets picked up at x4? Is the set of locations in x only for being picked up and y only for being dropped off?""",
    """HW3 has been graded
HW3 has been graded and comments are on CMS. You have a week to submit any regrade requests you may have. """,
    """Will the lowest pset score be dropped?""",
    """NP-complete, NP-hard, NP Definition
From lecture and a bit of researching online, NP stands for "non-deterministic polynomial time", and NP-complete problems, to my understanding, is basically a set of problems that cannot be solved in polynomial time (at least not with anything we have right now), and we reduce problems to other such problems to show they take a lot of time to solve. And, if we were to ever solve one, we could solve the others as well.

What is the difference between NP, NP-complete, and NP-hard? Will we go over this in lecture? The next few weeks of lectures will cover NP-complete, but not sure how it relates to NP and NP-hard. Also, is there anything else to keep in mind about NP-completeness besides that we can reduce a given problem to an NP-complete problem?""",
    """HW5 Q3 clarification please
On my understanding, the Submatrix Domination problem is finding two one-to-one mapping, 1-m1 -> 1-m2 and 1-n1 -> 1-n2, so that A[i, j] ≤ B[r(i), c(j)]. But I think this is down to the comparison between the max element of matrix A and B.

If max(A) > max(B), then there should not be a valid mapping since anyway max(A) cannot ≤ any element of B;

Conversely, if max(A) < max(B), suppose max(B) has the indices u, v, then we could map all of 1-m1 to u and all of 1-m2 to v and those are still one-to-one mapping.

Considering m1 m2 pair, or n1 n2 pair might not be equal, I guess the problem does not require a perfect matching.

I wonder where I think wrongly above.

Thanks for any suggestion.""",
    """Cancelling Tuesday 2-3 Office Hours (10/20)
I'll be cancelling my office hours tomorrow due to a time conflict.""",
    """Moving OH to Wed 3-4:30 PM
Hi, I’ve become a bit ill over the weekend and will be moving my OH to Wednesday as a result. I apologize for the inconvenience and will hold my OH for an extra half an hour to answer extra questions that day! Hope to see you there.""",
    """Regrade Request for HW2
I submitted a regrade request on October 6th for HW2 Q3 and it hasn't been responded to (unless I'm missing something, which is certainly possible). I understand that there are many regrade requests to go through and thus it can take awhile, but I just wanted to check in to make sure it didn't fall through the cracks.""",
    """Proving NP-completeness
Since we need to come up with a reduction to a known NP-complete problem, does that mean we have to formally prove our reduction correct using an iff statement? Or can we just say what the reduction is.""",
    """Q1
For question 1, is it possible for D(i,j)+D(j,k)<D(i,k) for some i,j,k? That is, do we need to account for taking "shortcuts" between locations?""",
    """Grading feedback
Will it be okay if graders left a note on which problem they graded? I sometimes have to decipher which grading comment refers to which problem, and it'd be super helpful if the grader left the problem number in the comment.""",
    """Is a clique a near clique?
Is a k clique also a near clique of k or is a near clique exclusively when the addition of a single edge would take a non-clique and turn it into a clique?""",
    """Q1 shortest path?
Is the distance in the matrix provided the shortest known path between the points? i.e. is there a better way to get from i to j than D[i][j] that is known to the problem?""",
    """Running time of Dinic Algorithm
I think the difference between Edmonds-Karp and Dinic is that Dinic employs a memoization dfs to find the augmenting path. However, I'm still a bit confused about how we analyzed its running time.

It seems like Advance, Retreat, and Augmenting recursively calls each others, so why can we analyze each running time as if they were paralleled? Is it because we analyzed the maximum number of times they get called no matter how they call each other?

And how does this search improve running time as compared to an ordinary depth first search?""",
    """Cancelling Tuesday 4:30-5:30 Office Hours (10/20)
Hi all:

Unfortunately I have to cancel my office hours for 10/20 (4:30-5:30) due to a conflict at that time. I apologize for any inconvenience this may cause.

Thanks!

Ben""",
    """Q2: Logical Formula to CNF
For question 2, I managed to come up with some grotesque looking logical formula that captures what it means for a graph to be a near-clique. However, it is not in CNF form. I am considering using the distributive and DeMorgan's laws, but it is still very messy. I am therefore writing to ask if it is fine to just state the raw formula and argue that it can be transformed into a CNF without the full derivation. """,
    """dinic stack constructions
In lecture, the professor was saying we construct p as a stack for Dinic's algorithm, and talked about a node u as the last element of the stack. By the last element, does that mean the one we most recently added to the stack (last in) or the last out (first in) element?""",
    """Showing that a problem is in NP
"Show that B is in NP by giving a nondeterministic polynomial-time guess-and-verify algorithm for it"

For this part of showing NP completeness, there are no requirements for the overall runtime of the guess-and-verify algorithm, right? Since it's "nondeterministic", we just have to show that, by making optimal guesses (via magic), the algorithm would run in polynomial time? So an overall O(n!) guess and verify algorithm that takes O(n^2) to verify would fulfill this requirement?""",
    """Q1 starting position
Can we assume the cab can start at any location?""",
    """Office Hours Cancelled (Tuesday 7pm-8pm)
Sorry again, but I won't be able to do my office hours today for medical reasons and because of conflicting prelims.""",
    """Question on Reductions and NP-completeness Notes
I was reading through the notes on Reductions and NP-Completeness. In the section "The Class NP", it talks about one-place predicates and two-place predicates in determining if a decision problem is P or NP. I think predicates are logical formulas, but I am having trouble understanding the difference between one-place and two place. Thanks for any help.""",
    """NP definition
I don't have a good understanding of NP. These are some of the questions that I have: Is NP only defined for decision problems? what would be an example of w and xi(x,w)? How would we define the length of w, if we define such w. Could I please get some help in understanding what NP is? Thank you""",
    """A few questions about CNFSAT and cliques
Hi, I have a couple of questions regarding these two problems.

First, what is the runtime of each?  I'm a bit confused because we said CNFSAT was only solvable exponentially but then we were able to get around that by a reduction.  Second of all, can we assume that (based on the algorithm we gave for the clique problem) that the solution to finding whether there is a k-clique can be slightly adapted to count how many k-cliques there are?

Thank you!""",
    """Clarification on NP-Hard vs NP-Complete
I have read @859, but just to clarify, the difference between NP-Complete and NP-Hard is that an NP-Hard problem doesn't need to necessarily have a polynomial-time verification function, but the NP-Complete problem does? """,
    """Friday 11am OH to Thur 9am-10am
I am moving my office on Friday to tomorrow 9am just for this week. Sorry about any inconvenience. Here is the zoom link to my OH. """,
    """Typeset Lecture Notes
I noticed on the course website that the recent lectures had detailed typeset lecture notes that I thought were really helpful. I was wondering if a typeset version of the older lectures are also available?""",
    """P vs NP
I read @859 and the handout for section 4, but I'm still confused about P vs NP. My current understanding is that if something is P, then it would mean we can cover all possibilities and verify in polynomial time. NP would be covering all possibilities is at least nondeterministic polynomial, but if given a possible solution, we can verify this solution in polynomial time? Also, for proving NP do we have to show that searching for all solutions is at least nondeterministic polynomial? or just showing that given a witness, we can verify in polynomial time?""",
    """late oh
sorry I came a bit late to OH today, so I will go until 2:30pm instead of 2""",
    """Q2 Definition Clarification
Just to clarify what it means to have a size k near-clique as a subgraph: does a graph have a near-clique if you can take away nodes from the graph and then derive a size k near-clique, or must that near-clique already exist as-is within the graph? Thanks!""",
    """Paul's OH right now?
I'm waiting for Paul's office hours to start- are they cancelled?""",
    """Office Hours Moved to 8-9PM Today
I'm sorry for the late notice, something came up. My office hours will be held from 8-9PM today instead at the same link.""",
    """Running about 10 min late to OH
Sorry, I’m running 10 minutes late to my office hours. See you at 6:10! Will run to 7:10 to make up the time""",
    """Q1 formulating algorithm
I just started number 1 and I'm having some trouble deciding on a method to go about solving this problem.

My first idea that I think would work would be to use dynamic programming and adapt the weighted interval scheduling algorithm to fit this taxi scheduling problem. I think it would work as in both problems you try to maximize a profit (number of taxi rides) and you are given start times. The only difference that would be need be addressed is the fact that there are also start and end locations. For this, I was thinking of sorting the given list of requests into starting locations and then using an 'opt' function to recursively maximize the number of taxi rides for the given requests at the given location.

I think this algorithm would work well however I am wary to use it, because the homeworks have usually been related to recent topics and we seemed to have finished the dynamic programing portion of the class.

Because of that, my second idea would be to use network flow and adapt the project selection algorithm to it. To formulate the graph, all edges represent a request and the nodes represent locations. Then add a source with edges to all nodes and a sink with edges from all nodes. The issue here would be time which would be difficult to incorporate into the existing algorithm which would make this much more difficult than my first idea.

I understand if you can't tell me if I'm right or wrong, but I was just wondering if there are any glaring errors in my logic or things that I am overlooking that could be leading me astray?""",
    """Proving NP-complete Clarification
If we want to prove a problem X is NP-complete, is the only thing we need to do is reduce a known NP-complete problem to X (along with the proof and complexity analysis)?

We don't need to first show that it is NP, right? Though I guess that's a bit redundant, since if it's NP-complete, it has to be NP""",
    """Does restricting a problem generally preserve the complexity?
This is loosely related to Q3, but I am more curious about the general answer to this question.

As we have learned from the lecture, we prove that problem A is NP-hard by reducing a known NP-hard problem B to A with a polynomial-time mapping from inputs of A to those of B as well as a witness set of B that's polynomial in terms of the size of witness set of A(please correct me if I mixed some stuff up). However, in many cases, the inputs of A and B can have very different "structures". For example, in Q3 the inputs are two matrices(each of which probably has a composite number of entries), whereas in Q2 the input is a graph can have arbitrary number of nodes. I'm under the impression that some NP-complete problems can run in polynomial time for a subset of its input set(like relaxing the conditions of some P problems can make it NP, etc.).

Now my question is, when we map the inputs of A to B, how do we know that we are not "restricting" B to a subproblem with lower complexity? In other words, do we always know that the "input-map" is surjective? is it possible for the "image" of the "input-map" to guarantee polynomial run-time when fed into B?""",
    """q3 clarification
I feel like I am not understanding this problem correctly. The question straight up tells us that the submatrix domination problem is NP-complete. That means that it is NP-hard.

However, it seems like this problem just boils down to finding a mapping from elements in matrix A to elements in matrix B such that you are mapping to a number greater than or equal to what you are mapping from. In this case, for each element in A, can't we just create a mapping to the smallest element in B that is still greater than or equal to the element in A? In this case this would just be O(n^2) time which is polynomial. But that cannot be, because we are told that the submatrix domination problem is NP-hard. Could someone let me know where I am going wrong? Thanks.""",
    """assumptions q1
am I allowed to assume that the set of requests is sorted in some way or do I have to do the sorting in the algorithm ?""",
    """Use of DFS
If I use DFS as part of the algorithm do I have to prove that it works and explain how it works in the algorithm or can I just reference it because we used it on a past programming question?

Edit: I see that DFS is given in the textbook, so I am assuming I can just point to the text?""",
    """Moving office hours today from 2-3pm to 4-5pm
For this week only, I will be moving my office hours today from 2-3pm to 4-5pm.""",
    """Friday 12-1 OH Cancelled
Apologies, but I will have to cancel my office hours today from 12-1.""",
    """P2 undirected graph edges
For an undirected graph G = (V,E), we can assume (u,v) = (v,u) right? And does that mean both of those are in E, or just one?""",
    """moving friday 3-4pm office hours
Hi, I'll be moving my Friday 3-4pm office hours to Sunday 10:30am. Thanks and sorry!""",
    """Reductions
For a reduction from A to B, is it ok for a reduction algorithm to output only a certain subset of the possible input instances of B, given any input instance of A?""",
    """Giving a poly-time verifier
How specific should we be when giving the verifier?

Also, just to make sure, when we prove X is in NP, all we have to do is state what a witness for X would be and how to check that any witness is yes/no?""",
    """Q1 pickup time
Can the cab pickup the passenger before the desired pickup time ti if they arrive at the pickup location early? Or would they have to wait for ti before sending the passenger to their destination?""",
    """Reduce A to B and reduce B to A
I feel like most of the time, when we can reduce A to B, we can reduce B to A( true for clique and independent vertex, independent vertex and vertex cover)

And now I'm confused between this observation and the if and only if we have to show in proving a reduction. Could anyone give me an example where two way reduction isn't possible? I think that'll clear up this confusion.""",
    """Time Complexity for NP
Do we have to do time analysis for the NP reductions, or would we forego time analysis for these questions?""",
    """specifying witness in showing B is in NP
From the lecture handout, we have image.png

Do we also need to specify a suitable set of witnesses and prove that a witness can't be too big aside from giving a verifier?

If so, could I get more explanation on what that entails, possibly an example? Thank you. """,
    """Q1 Requests
If we want to find the maximum number of requests we can serve, does this mean we can exclude certain requests in order to get a maximum? For example, if we have n requests and a request i in the middle of them throws things out of balance, could we exclude it and have n-1 feasible requests? Or do we have to obey the order and only end up with i-1?""",
    """HW5 Q3 Reduction
Hi - I'm having trouble with where to start for number 3. Do you have any hints to give for how to reduce to get to a matrix? """,
    """Q1
For some x, y in X, s.t. x != y, is it possible that D(x, y) = 0? """,
    """Verification
I am a bit confused about NP. In the notes, when describing NP, there is this two-place predicate phi(x,y). I understand that x is like an instance of the problem, but what is y? When the handout describes CLIQUE, it seems to describe y as a subset of nodes K subset V, and phi checks if K has k nodes and is a clique. But why does phi(x,y) get to assume that y is a subgraph? And can it instead assume that y is a subgraph with k nodes so phi(x,y) only has to check if that subgraph is a clique, and doesn't have to check if it has k nodes?""",
    """hint for q1
Can anyone give me some hint for q1? I guess I should reconstruct this problem into network flow problem but I don't have a clear idea for how to do it.""",
    """Proof for DP
To prove a DP algorithm, do you compare the outputs with what you define to be the optimal solution? Or do you have to also reason that the optimal solution is really an optimal solution""",
    """Quizzes as a part of grading?
I'm not sure whether this has been brought up but on the course site under grading, it says that 5 percent of our grades will be based on quizzes? What exactly are they and are they still happening?""",
    """Semi-final details
It might be a little early for me to ask about semi-finals, but when will the semi-final for this class be? The website says it will be a take-home exam in the week of Nov 16 but is there a specific window it will be released and be due by?

I am asking because I am an international student and I am trying to figure out travel plans. Thank you!""",
    """Proof of simple graph algorithms
I know that there are some basic algorithms from 2110 that we are allowed to invoke without needing to explain them / prove them right / prove time complexity (@95). I just wanted to check if the professor / course staff assume these algorithms to be known from 2110 and whether time complexity and correctness for these algorithms would need to be proved if used in the HWs.

Topological Sort of DAG
Shortest paths in DAG
Longest paths in DAG""",
    """What's the complexity of airline scheduling using circulation?""",
    """HW3 solution Q1
I'm getting a little lost in notation while reading the solutions to HW3 Q1, specifically:

What do the subscripts i of xi mean? I'm confusing the difference between the sequences x1,x2,…,xk and xσ(1),…,xσ(k); do the indices in the former refer to the 1st successor, 2nd successor...kth successor, while the indices in the latter refer to the first member of the permutation sigma, the second member, ... the kth member?
(as a result of not understanding the above) What are we sorting in descending order? If xi is some number that is a member of {1,2,…,k} then wouldn't any sequence of xis, sorted in descending order, be k,k−1,…,1? I'm then unsure how this relates to the statement "...where sigma orders the successors t of s in descending order of opt(t)" (or really, what this statement means)
Alternatively (or additionally) an explanation of the solution to HW3 Q1 in plain English would be appreciated. Thanks so much!""",
    """Question 1
Can there be requests which take 0 units of time to complete?""",
    """Q2
If we reduce the problem to clique problem. We already proved the clique problem is NP-complete, can we just simply say since clique problem is NP-complete, then nearly clique problem is NP-complete. Or we need to prove the clique problem is NP-complete in Q2?""",
    """Q2
Can we assume that the given graph is not a multigraph?""",
    """hw5 q3
I am still struggling with which np-complete problem I should be reduced from for q3. Is there any more hint addressing this problem?""",
    """Moving 12-1 PM Sunday OH to 12-2 PM Friday
I will be moving my Sunday office hours today to Friday 12-1 PM this week. Sorry for any inconvenience. """,
    """Time complexity of σ dependent on graph representation
If we are arguing the time complexity of sigma for a reduction but this depends on how a graph is represented, what should we do?
Should we assume the representation that gives the best complexity for sigma? Or just assume whichever representation we like?""",
    """I could be understanding your question incorrectly, but I don't think sigma should depend on the representation of a graph since the number of vertices and edges would always be the same regardless of representation. For instance if I had G = (V, E) where V is a list of vertices and E is a list of edges, there are the same number of vertices and edges in G' where G' is a node object and has an adjacency list of pointers to other node objects. Since σ depends on the input, which is the graph in this case, the run time should probably in terms of |V|, |E|, or maybe k if σ has multiple parameters. Also, for reductions, σ just has to be polynomial, so if one representation is causing σ not be polynomial anymore then I would think something is probably wrong.

Although as a general rule of thumb:

- For runtime complexities, you should really be considering worst case complexities (or amortized complexities).

- For these homework assignments we have been able to assume our input representation as long as we specify our assumptions and don't lose the generality of the question.""",
    """DP proof by induction
When proving my algorithm using induction, am I allowed to assume OPT(j) for 1<=j<=i-1 when proving OPT(i) or am I only allowed to assume OPT(i-1)?""",
    """For 2, do we have to specify runtime or is it ok to just say it will definitely be polynomial""",
    """q3 one to one
Since functions r and c have to be one to one, does that mean that m1 = m2 and n1 = n2 if r and c exist? I would assume that this must be true by the definition of a one to one function but many of the questions on piazza refer to matrices of different sizes. Any clarification would be helpful""",
    """guess and verify for q3
hi - i'm really struggling with Q3 and was wondering if anyone had any advice for a good guess and verify algorithm for proving NP.""",
    """Q2 struggling
I know we have reduce clique to the problem but I am not sure how to create the sigma transformation, are there any hints?""",
    """Try not to constrain yourself to any specific reduction. Remember that we have a lot of NP-complete problems at our disposal, and all of them can be reduced to near-clique. It's just up to us to find one where we can spot a good reduction. And maybe also let go of trying to immediately create a function sigma for now, just think about what type of similarities/relationships you can spot between near-clique and known NP-complete problems. Which ones seem to be most obviously talking about the same type of thing, but in a different way? How can you make little changes to input instances in order to match the constraints of the near-clique problem? If you can latch onto an abstract idea of what you want your transformation to do, then you can move onto the specifics, put it to paper, and hammer out any issues.""",
    """question about NP hard and NP complete
Just to make sure I understand correctly.

The definition of NP-hard is : A is NP-hard iff every problem in NP reduces to A.

So can we understand it as, A is at least as hard as the hardest problem in NP?

The definition of NP-complete is: A is NP-complete iff A is NP-hard and A in NP.

So can we understand this as, A is one of the hardest problem in NP?""",
    """Is reduction the only way to prove NP-completeness?
Hi,

    For example I want to prove A is NP-Complete and I already know B is NP-Complete. If I show that I can solve A by solving B plus some additional steps and additional steps take polynomial time, can I say that I proofed A is NP-complete? I am not doing any mapping of inputs here, and output of B is not equal to output of A.

    I am not sure is this also a reduction or this is a wrong approach.

Best.""",
    """q3 reduction
hello! i have been trying to figure out this problem all day and i am incredibly stuck about what we are supposed to reduce from? i've looked through the examples from lecture but i still can't figure out what to reduce from.

also, if im interpreting this correctly, i just need to find a way to explain how this question is represented as another np-hard question, but don't need to explain how we would construct our r or c (so for the NP-hard problem we reduce from, can we assume that it already has a r and c defined somehow?)""",
    """Prove NP-Complete
Just to confirm that I'm not missing anything, but for proving np-complete, we want to explain the reduction, prove why the reduction is right, explain why the reduction happens in a polynomial time, and that the solution can be found in polynomial time? """,
    """Still stuck on Q1 and Q3
It's due today and I have no more extensions after this (took 24 hours for this homework), and I am hopelessly stuck. All the hints for Q3 keep asking which structure do we know that can be represented as a matrix, and obviously that's a graph (because graphs can be represented as adjacency matrices). But what after that? What do I do? How do I proceed? I recall there was some post where Prof. Kozen wrote something about permutations of rows and columns. Is that important?

Also for Q1, I considered a reduction to the Interval Scheduling Problem, and although I came up with a really nice polynomial time reduction that would, if n was the length of the input of the Taxi Problem, give an O(n^2) size input for the Interval Scheduling Problem (by defining a reachability relation somewhat similar to what we had in Airline Scheduling), I can't for the life of me figure out how to prove the fact that a solution to the Interval Scheduling Problem would imply a solution to Taxi, since I keep coming up with cases where we get a valid list of Intervals but it doesn't correspond to a feasible schedule. I'm at my wit's end. Please help.""",
    """DP Dough is dynamic programming dough
But what’s the optimal calzone though""",
    """Q3
When we prove that "Show that x is a “yes” instance of problem A if and only if sigma(x) is a “yes” instance of
problem B.", i understand we need to show "both ways" ie A iff B and B iff A, but would we need to show that "no" instances -> "no" instances? The handout gives conflicting detail as it says we must do this but neither of the  CNFSAT ≤p CLIQUE or CLIQUE ≤p CNFSAT reductions do the "no" step. """,
    """3D Matching Cleanup Widgets
Do we assign two different nodes to each uncovered tip? So if there are (n−1)k of them, we will add another 2(n−1)k nodes as cleanup gadgets?

I don't get why in lecture we say we want to connect "all" tips to these cleanup gadgets because I think the same point cannot appear twice in a matching?""",
    """Base Color in 3-Coloring Problem
Just want to make sure, the first Base Widget doesn't serve practical purposes in this proof and when we construct the variable widgets, it is alright to connect each variable to some other "base node" instead of a same node, right?""",
    """Moving OH to Wednesday 10:30AM -11:30AM
I'm super sorry for the late notice, but I will be moving my 11:30-12:30 OH to be Wednesday, October 28, from 10:30 AM -11:30 AM for this week only. There should be other OH around my usual time today if you need help! """,
    """Petition to move HW 6 due date
November 3 is Election Day and I suggest that the due date is moved back one or two days so people can get out and vote!""",
    """HW 6 Q1 Clarification
Would it be correct to assume that we should only be visiting each city once?""",
    """Tuesday 7-8 OH cancelled
I am cancelling my office hours today from 7-8pm. Sorry for any inconvenience.""",
    """Edmonds-Karp: Why do we have to do do multiple BFS?
During each phase, we find an augmenting path, augment along the path, and delete the saturated edges from the residual graph. After we can find no more augmenting paths, the phase ends and we start a new phase, doing BFS again. Is this the correct understanding? And if so, what is the point of each BFS if we're building the residual graphs in each phase anyway?""",
    """Regrade Requests
I've submitted regrade requests for the last released assignment and have not gotten any responses to them, and now the system is not allowing any more regrade requests/grade changes.""",
    """Question regarding CNFSAT --> 3DM
Where did the idea to create these particular widget constructions come from? As in, did the person or people who figured this out just happen to decide to use these constructions on a hunch and it worked, or is there some natural thought process that led to this that comes with more knowledge in the field?""",
    """Q1 Assuming TSP's decision version NP-complete proven?
Can we deduce from the fact that the decision version of normal TSP is NP-complete and start from there to show this changed version is also NP-complete?""",
    """Q2 length 0 paths
Is it ok to assume that every node in a graph has a path of length 0 to itself? In the context of the problem: if we have an isolated node in U (with no edges to any other node), which is also in V, can we say that it has a path of length <= l to a node in U, namely itself?""",
    """Q1 clarification
As mentioned in one of the older posts, the 'plan' we have may contain duplicated path/visits to a node, I am a bit confused as to how that will affect the time complexity of the verification of predicates. how should we approach the time complexity of the verification algorithm? If there can be repeated visits of edges, will there be a possibility of un-polynomially bounded verification if, for example, the 'answer' we are trying to verify is simply a cycle that repeats itself many times?

Any ideas appreciated!""",
    """if and only if in graph coloring
We proved both statements in the class, but we also said this is the proof of "a satisfying truth assignment gives a coloring." I think the second statement along says if there is a satisfying truth assignment, there is a coloring.

Can we conclude that if there is a coloring, then there is a satisfying truth assignment by taking the contrapositive of statement 1 and then just finish the proof of if and only if? Or that's exactly what we did?""",
    """HW 6 Q2
Can we assume that dominating set is NP-complete? More specifically, is it enough to show that question 2 reduces to dominating set, or must we show that it reduces to vertex cover (or some other NP-complete problem)?""",
    """Why we need widgets.""",
    """TSP reduction to Hamiltonian cycle
In the book, it mentions that the tour for TSP should start and end at a certain home city. How does solving the Hamiltonian Cycle Problem conserve this property? I know a Hamiltonian cycle should start and end at the same node, but how do we know if this node is exactly the specified home city?""",
    """Wednesday 5-6pm OH moved
Will be moving by OH to Sunday at 5pm due to a time conflict. Sorry for the inconvenience. Hope to see you then! Look out for a follow up post.""",
    """Cancelling this Sunday's 4-5 PM OH
Thank you for your understanding""",
    """runtime
do we need to analyze runtime when proving NP-complete?""",
    """Thursday (Oct 29) Canceled OH
Hello,

Unfortunately, I have to cancel my OH (7 - 8 pm) tomorrow, Oct 29. This change doesn't apply to my future office hours. I apologize for any inconvenience caused due to this.

-Tejas""",
    """When will the Alignments Test program be added to the Autograder?
As above; thank you!""",
    """hw6, q3 - what is the max input string length?
title""",
    """Research Night Form
@1009 I tried to submit my form 3 times and got an error all 3 times. Is there another way I can RSVP?""",
    """Q1 TSP with revisits?
I checked the book and search on the internet for quite a while, but found little material on how to approach a TSP with the possibility of duplicates. It is quite hard for me to understand why TSP with the possibility of revisit is in NP, as the verification of witness may take some unbounded time. Can someone point me to the right direction? Thanks""",
    """Q3 autograder
I am not sure if this is an issue, but it looks like when running code on the autograder, the first two test cases have "\\r" characters embedded in them as part of the input, thus violating the fact that the alphabet is only between a-z. It looks like trimming the input strings will allow get the correct result on the autograder.""",
    """Q3 autograder weird newline in output
I am using python, when testing on my local machine, the output has the correct format, but when running on the autograder, I got this weird newline between two output words. Any idea what is causing them? It is showing up on all the cases. I am not sure whether there is something wrong with my code or with the input/output themselves""",
    """3-colorability for planar graphs
In lecture 10/26, to reduce from 3-colorability to planar 3-colorability, we need to replace crossing edges with the crossing widget. And is it mentioned that the crossing widget would allow for North-South and East-West flow (same colors for N-S and E-W nodes) but I wasn't sure why that needs to be fulfilled? I thought edges (North, South) and (East, West) in the original 3-colorability graph mean that the North node should have a different color from the South node, and similarly for East and West as well?""",
    """Thursday 5-6PM Office Hours Cancelled
Paul's Office Hours from 5-6 will be cancelled today""",
    """Make Q3 faster Python
I followed the hints and used a list of lists to store both value and alignments, but still failed the larger test cases. My run time is ~10 s vs the 2s boundary on the largest ones. Any suggestions on how to make the code faster? Thanks!""",
    """Office Hours
I drafted a post about moving my Office Hours this week but it seems it did not post, sorry for anyone who tried to join. I will hold OH on Sunday 6-7 pm instead (for this week only). Sorry for any inconvenience, and hope y'all can make it.""",
    """Eugene's OH?
Is it still being held today at 6-7pm? There hasn't been a TA for a while""",
    """HW4 has been graded
HW4 has been graded and comments are on CMS. You have a week to submit any regrade requests you may have.""",
    """HW6 Q1
Can we assume that there exists a non-negative solution for the TSP, since if the maximum profit is negative then it is better to simply not travel with a profit of 0?""",
    """HW6 autograder question
The strings that we output may not be the exact same as what is shown in the example but still be correct if the edit distance is optimal? Is there any reason why this test might be failing?""",
    """So what language is everyone using for your code?
I was really curious, especially to see if people are using C or OCaml at all. I'm personally using Java but seriously wondering if I should switch to C++ because its supposed to be faster and I don't have to worry as much about optimisation as I do with Java.""",
    """Can we make a weekly megathread for the TA Office Hours that have been canceled?
Can we please have a megathread every week for the TA OH's that're cancelled, instead of the TAs making individual posts which might get buried quickly, especially when it's just before a homework submissions and people are making a lot of posts? I've seen situations where a TA rescheduled but I was the only one who turned up at those rescheduled OHs because no one remembered, which feels like a waste of a very useful resource (I'm literally surviving this course simply because of the amazing TAs we have and I'm sure many others feel the same). @Professor Kozen and all the senior staff, I believe this would be a really useful resource for the students. Thanks""",
    """Q3 Space Complexity
Will we be graded on our space complexity in Q3?""",
    """HW6 q1 Clarification on which to prove (given versus decision variant)
Says to "state a decision problem version of this optimization problem and prove that it is NP complete". Are we proving NP complete for the given problem, or our decision variant?""",
    """Debugging hw6 q3
I am passing half of the test cases on the autograder for Q3. When I look at the inputs for the ones I am failing, it is nearly impossible to figure out why they are failing because the inputs are so long and complicated. I am not encountering timeout errors and when I manually test various inputs, I am getting the correct outputs. Any advice on how to debug?""",
    """list index out of range
When running the test cases, I keep getting list index out of range for the line ans[0] = int(ans[0]). I can't figure out why this is happening and my code runs fine when I test it manually""",
    """Office Hours Changes/Cancellations Megathread
Hi, I see that there's 2 other TA's scheduled for Friday 3-4pm office hours so I'll move my office hours to slightly later in the evening at 6:30. I'll make my office hours longer than usual if needed as well! Also, moving forward, I'll move my office hours in the future (will have the time changed on the website) since it's probably not ideal to have 3 TA's in the same office hours slot anyways. Thanks!""",
    """TSP variant - target profit?
Since we're given a target max distance for TSP, are we also given a target min profit for the TSP variant, or are we just given the graph?""",
    """hw6 q3
This might be a really simple question. I was looking at the pseudocode in 6.6, and there is a line that says

"Array A[0...m,0...n]". Is this referring to an m+1 by n+1 matrix?""",
    """hw6 q3
The textbook mentions that we can trace back through the array A, using the second part of fact (6.16), to construct the alignment itself, where the second part refers to "Moreover, (i, j) is in an optimal alignment M for this subproblem if and only if the minimum is achieved by the first of these values." Could someone explain what this means?

I understand that the pseudocode constructs the matrix containing alignment costs but I am confused about how this should help us create the alignment.""",
    """Question of HW6Q1
Hi, I'm very confused about the "decision-problem version of this optimization problem". I'm not sure what does that actually change of the normal TSP problem? Since in class we are shown that we could  reduce HC to TSP, is that a reduction of the "decision-problem version" or not? What's the difference between "decision-problem version" and the normal version?""",
    """Sat 2-3 OH
I’ll be holding office hours in half an hour. see you there!""",
    """printing alignment
My code is properly computing the edit distance however I am having trouble figuring out how to actually print the optimal alignments using the dp table. Any tips?""",
    """Q 1 Assumptions
Can we assume that the cost of a ticket and the revenue of each city is nonnegative?""",
    """Q3 seg fault
For Q3, I am passing the first 11 tests, but getting a set fault on the rest of them. Any idea why this could be happening? Seems weird that it would happen only on the last problems like that.""",
    """HC <= TSP
In lecture we said that there is a TSP tour of size n, iff H has a HC; and we defined n=k.  Where did k come from?  Is H built using the same widgets as the vertex cover reduction, therefore k refers to the b1...bk nodes at the bottom?  Or is it an arbitrary number that will be the resulting minimum distance?""",
    """Optimal alignments
Im confused by when the specification of Q3 states that we need to output AN optimal alignment, obviously there can be multiple optimal alignments so how do we know what optimal alignment we output, for example how to we know to output 2 occurrence occura nce instead of 2 occurrence occur ance.""",
    """Bipartite graphs
Am I right in thinking that in a bipartite graph, nodes in the same set cannot have edges between them? If thats true, then Im kind of stumped on how to make the bipartite graphs for Q2, for a vertex cover if its simply a bipartite graph of set nodes and set edges.""",
    """Crossing widget
In 10/26 lecture, we learned how to reduce from 3-colorability to planar 3-colorability. I don't understand why the property of crossing widget (having same colors for N-S and E-W nodes) allows us to replace crossing edges to crossing widget.

I already saw the answer in question @1019 but still don't understand. Let's take the example in the post. For a simple crossing (just 2 edges: North-South and West-East), we need to choose different colors in North and South. How could you make the North (South) node be the North (South) end of the crossing widget? I am confused because North and South nodes in crossing edges graph must have different colors while the North and South ends of the crossing widget have the same color.

Thanks in advance!""",
    """Subset Sum Reduction Detail
For the subset sum reduction covered in class, I was wondering about the sigma function that transforms subsets into a binary number.

Why are we worried about carrying? If it carries, then wouldn't there be a repeat in the subsets, causing it not to be a valid solution for subset sum?

My thoughts were that this is to show that there is no other way to reach the ith digit through lower digits, thereby making the proof that a solution for subset sum exists iff it exists for exact cover more difficult, but I'm not sure if that is the case.""",
    """Q3 using code from another class
Can I use my own code written in another class for this programming question?""",
    """OH?
Are there still OH today from 4-5pm?

Thank you!""",
    """Reduction "yes" in A means "no" in B?
I know that in a usual reduction, you want to prove that a "yes" instance in A means a "yes" instance in B.

Can we also do a "yes" in A if and only if "no" in B?""",
    """HW6 Q3 Timeout when finished?
The autograder is currently killing my process for the last two test cases, 1499x1499 and 1500x1500, but the stdout shows that the whole output has been flushed. Also, I copied the 1500x1500 test locally and I was able to pass it locally in 1.576 sec. I then even added time blocks around all of my code, even after printing the final result, and it said it took 2.34 seconds to complete everything in the autograder.

I am using Python. I double checked my code and I'm fairly confident that it's O(m * n) so I'm starting to believe it could be an issue elsewhere, thanks""",
    """General understanding of optimization problem and np class of decision problem.
Hi all,

I am taking a mathematical programming course this semester, so I am trying to generally understand the relationship between optimization problems and what we learn (especially np) in this course. I think two subjects are highly related to each other, but have difficulties to gain a comprehensive understanding. I think someone who has knowledge also in the optimization area can answer.
In HW6 problem 1, there is an optimization problem and we restate it as a decision problem and prove it is np. This invokes me several questions.
If decision version problem of an optimization problem is P (NP), the original optimization problem is always P (NP)? I think the answer is YES because we can always try a binary search to map optimization problem to decision problem and it always adds O(log n). Do I have the right understanding? I think I am wondering whether the restatement process of converting an optimization problem to its decision version of problem is always linear mapping.
After I formulate optimization problem and classify which categories the problem falls into (convex/nonconvex, LP/QP , etc..), can I have clues whether the decision version of problem will be p/np-hard/np-complete ?
NP is a class of decision problem. Why is np only defined for decision problem in the first place? Is there any special reason we cannot discuss the hardness of the problem outside of decision problem?
Thanks in advance!""",
    """Hamilton Path to Travelling Sales Person
Say we have G=(V,E) in Hamilton Path problem, when we create our new graph G′ for Traveling Sales Person, why did we add an edge between nodes the were originally not connected in G? How does that help the proof?

Can the proof still proceeds if we simply let G′=G with all edges have a cost 1?""",
    """HW 5 Solution
Has HW 5 solution been posted (I can't seem to find it on CMSX)?""",
    """No class today?
Am I the only one who cannot enter the zoom link now?""",
    """Showing a problem is NP-Hard
When proving that a problem is NP-Hard do we need to show that the problem that we reduce from is only NP-Hard or does it also have to be NP-Complete? If it has to be NP-Complete, why do we need to know the extra information that the problem is in NP?""",
    """Integer valued assumption for Q1
Can we assume that costs and revenues for question 1 are integer valued or are at least to two decimal places, similar to an actual currency? ie. Costs and revenues are at least 0.01,""",
    """HW6 Q3 Solution passes all but one test case
My solution to Q3 passes all 1000 cases uploaded by Giannis, as well as 19/20 of the test cases from the autograder. It only fails on one case, and that too on a case that's so big (1000 x 1500, test no. 16) that I can't debug it by hand. What do I do? (In case it's important, I'm using Java)

image.png

EDIT: Fixed it, there was a small issue with my logic that somehow managed to slip under my radar lol""",
    """hw6 q2
If a node v is an isolated node in a graph G then is that true that there is a path from v to itself?""",
    """Does anyone know how to earn participation points?
On the syllabus there's 5 points for piazza participation. I am wondering how to get a full participation point""",
    """Q1 and the start city
Can the salesperson sell product in the start city s?
I know that this should probably not affect my reduction too much. It might just affect some small details. I am currently assuming that they can.

Thanks!""",
    """python with autograder
hi! so i’ve been using java for programming questions so far and for some reason i’ve decided to use python for homework 6. i’m unfamiliar with using the autograder with python code and was wondering if anyone had some tips/resources for taking in autograder inputs and feeding the autograder your outputs? thanks!! :)""",
    """Q2 defining l
For question 2, I'm trying to reduce a problem that has a graph and a number k as its input to our given problem. For the sigma function, can I arbitrarily define l as any positive number? For example, can I just say let l = 1 or let l = 2....?

Thanks!""",
    """general question about proving np-complete
Does it matter whether we show the problem is np-hard first or show the problem is np first?""",
    """Reducing for Decision Problems
I was wondering if I am correct all decision problems (of the set NP) are solved by the simplified reduction as shown in the handout? And will we have the opportunity to have reduction problems that require the longer reduction process in later homework?""",
    """Does "problem A is an instance of problem B" = NP hard proof?
The hint for Q2 says that the dominating set problem is a special instance of Q2. If we know that dominating set is NP-hard, does that mean we automatically know that Q2 is NP-hard, and don't need to provide too much explanation for it? @1114 makes me think so.

On the other hand, if we can prove that one specific instance of problem B is NP-hard, does that mean B is NP-hard? Sorry, still wrapping my head around it.

Edit: Is this what's going on with the proof that TSP is NP-Hard using Hamiltonian Circuit? We reduce Hamiltonian Circuit to an extremely specific instance of Travelling Salesman using 1s and 2s for all distances?""",
    """Can we assume there's no isolated vertex when doing problem 2?""",
    """Question regarding the clause widgets in 3DM
I am wondering whether there is any connection between how we pick +/- set in variable widgets and how we connect +/- sets with the two dummy nodes in clause widgets. e.g. in the example in class:

we pick - sets when x is true and + sets when x is false. Then we connect + sets with the dummy nodes when x appears in the clause and connect - sets with the dummy nodes when ¬x appears in the clause. Is there any connection between how to choose the +/- sets and how to connect +/- sets to dummy nodes? Like, can we pick + sets when x is true and - sets when x is false in variable widgets?""",
    """Edges for decision TSP
Hi, I just have a quick question-- for q1, since we have directed graph for tsp, does this mean we need to have edge both (i,j) or (j,i)? Or is it okay for us to have only one direction and just assuming the person cannot go in the other way?""",
    """Happy Election Day!
One of our problems on a previous homework was to detect if a set of precincts could be gerrymandered. Found an interesting (and relatively recent) article about using k-means clustering to generate non-gerrymandered district maps. Also, this definitely isn't the only article about "solving" gerrymandering and redistricting, but k-means clustering does seem to be a commonly used algorithm in fixing gerrymandering.""",
    """time complexity for reduction
When finding the time complexity for reduction, for example, if we are reducing a HC to a TSP and we are creating a new graph for TSP, will the time complexity be O(time for construct graph of HC)+O(time for construct graph of TSP)? """,
    """HW6 q1
If we specify the values for a specific TSP and sigma and prove a reduction to the variant is this enough to show NP-hardness. I am specifically asking about specifying the values D and d_ij for a particular TSP.""",
    """Grading question for #3
If we get say 16/20 test cases on the autograder, does that mean our actual grade for that problem would just be scaled down to an 8/10?""",
    """Proving TSP is in NP
Slightly confused here--as we have to prove that there is an efficient verifier for witnesses, don't we have to account for every potential witness? If there is an itinerary that is infinitely long, how can we verify efficiently that it is a witness?""",
    """For 1, we can't, say, remove edges or vertices without changing the variant right?""",
    """Turing machines question about tape alphabet
In lecture today it was discussed that the input alphabet is a subset of the tape alphabet. What does the tape alphabet consist of? From my understanding, it is simply the input alphabet + the left end-marker + the blank symbol. Is there more?""",
    """question
How come every time the TAs grade my homework they are so devastating in their percentage and power of deduction?""",
    """HW7?
never thought that I'd be asking for more homework, but does anyone know when hw7 is going to be released?""",
    """Q1 Writing left-ending-mark in TM?
I have some idea on how to construct a TM for Q1, just wondering can we write a left ending symbol in TM, since that would (probably) make my TM simpler and require no use of space character?""",
    """Tim's OH -> sometime this weekend
Since we just released the homework, I want to push back my office hour to this weekend. I will notify beforehand. Sorry for any inconvenience.""",
    """Turing Machines Handout Questions
Hi,

I'm confused in page 4 of the notes where the turing machine transition function is defined in the form of a table. How did we know there were 10 states, q1, ..., q10, and in general TM problems, how would we come up with this?

Thank you!""",
    """Proving correctness for Turing machine
For homework 7, do we have to prove that our Turing machine is correct? I'm not quite sure if this will be covered in lecture (or if proving correctness is even a thing for TMs?). Thanks!""",
    """Turing Machines Handout Error

Is there an error in this transitions table? I would think that more of the inputs for the s state would result in a reject response. For instance, shouldn't (s,c) be a reject response since if there is a c and no other characters before it, then it won't be a string the Turing machine should accept? I asked a TA about this in OH, and they seemed to think it might be an error too.

Thanks!""",
    """Empty string for Q1
Should we accept or reject the empty string?""",
    """Overwriting with left end marker
Can we overwrite a letter with a left end marker? Provided that the tape never moves left from the new end marker, of course.

Also, this might be a dumb question, but is our input guaranteed to only have letters from the input alphabet?""",
    """Distinct tape cells for Q2
I want to clarify what it means for M to visit 4820 tape cells. Does this mean that M visits 4820 distinct tape cells, so that M visiting the same tape cell 4820 times would not count as visiting 4820 tape cells?""",
    """What does n refer to in Q3?
Length of the input string?""",
    """Turing Machine Handouts Example 1
Why is the one to one correspondence between {0, 1}* and the natural numbers not just defined as x = #(x)? Why is it defined as x = #(1x) -1? I understand that we are effectively translating the binary number to the natural number equivalent to two times the binary number, but why not just define it as the equivalent natural number?""",
    """Turing machine storing symbol in the state

I am just confused how a Turing machine can store some character in its finite control.

How would this formally work? the set of characters are different from the set of states, so I am having a hard time understanding how we can use the states to store the characters.""",
    """problem 1 corner cases
I am exploring several corner cases for problem 1.

1. If there an instance is given by palindrome with empty (e.g. 'a b a'), do you accept the strings?

2. How can we deal with the situation where alphabets other than a, b come out (e.g. d,e,f...)? For example, I think the transition function In Handout page 4 cannot deal with an instance 'abcdef' because the symbols 'def' are not defined in the transition function. Do I understand correctly? If so, can I get a high-level instruction to deal with it?""",
    """Study tips for semi-final
Just wondering if there are any study tips for the semi-final. Problems can seem to be straightforward once you know the answer to them but also really tricky if you don't. Would studying exercise problems in the book be a good idea?""",
    """Q1 transition table using "don't care"
Can we use the "don't care" symbol for our q1, similar to the notes?""",
    """q1 do we need to analyze runtime?
Instructions don't mention analyzing runtime or proving correctness as in past homework, but @1156 seems to imply that we still need to prove correctness. Does this mean we should also analyze runtime?""",
    """hw 7 q1
does our machine have to have/lay down a right end-marker ?""",
    """The Table
I'm a bit confused on how we use the table for turning machines, in the example for a Turing Machine for checking if some number is a prime number there is no mention of the table instead it describes how the Turing machine would work on an input, is this fine for the homework?""",
    """Levels of Informality for Q2
How informal can we be regarding the turing machines in question 2?  Can we just say construct a total turing machine that does x?""",
    """HW7 Q2
Does visiting the left endmarker count as one of the 4820 tape cells being visited? Or should the Turing machine move 4820 tape cells away from the left endmarker?""",
    """Returning to start state in TM
Are we able to have the transition function move to the start state from a non-start state?""",
    """Proving a problem is decidable
Hello,

In lecture, Professor Kozen said that (i) A is decidable if and only if both A and its complement are accepted by TMs, and said that we have to prove both directions of this.

In the notes handout, it says that (ii) a problem is decidable if there exists a total TM with L(M)=A.

For 2 on the hw when proving one is decidable, it is sufficient to just do (ii) and describe a total TM that solves the problem?  Would we have to prove anything about the TM?  Or, do we have to do the two directions of (i)?

Thank you""",
    """Homework 7 q1 initial tape
For question 1, does our machine have to start out as a single tape TM strictly containing the original input string or can we initialize the tape to have two levels to start with. This was mentioned in class and I'm not sure if the input string by itself has to be initially on the tape or if we can substitute it for some variation in the beginning (i.e. make the tape multiple lines like in class) before traversing the tape.""",
    """Turing Machine keeping tracking of previous symbol
In the handout on TMs, on page 8, it says that the example TM "remembers that symbol in its finite control". What does that look like in a formal definition of a TM? Does it show up in the transition function table?""",
    """Writing the left endmarker symbol
Is there any rule against writing the left endmarker symbol to the tape in a turing machine?""",
    """HW7 Q2 Tape Cells vs. States
Can someone please explain the difference between tape cells and states? What does it mean for a program to visit tape cells? In office hours, we kept using state instead of tape cell so I was not sure how to proceed.""",
    """HW 7 Due Date
As outlined on the Cornell Fall 2020 Calendar and Exam Policies webpage, there can be no assignments due on the 14th, 15th, or 16th of November, and for classes with semi-finals, assignments also cannot be due from November 17th through November 24th. Would it be possible to extend the homework deadline?

The page I mention is here:""",
    """What does the diagonalization of Turing Machines say?
I understand we can build a Turing machine that behaves different from all the Turing machines we currently have, but how does that help with the argument that there are some problems undecidable?""",
    """Office Hours
Will there still be office hours during the study days?""",
    """HW7 Q2
So I think there has been some confusion about Q2 and what is meant by "does M visit more than 4820 tape cells on input x?"

Please check @1162 to clear these confusions.""",
    """Tables (again)
This is more of LATEX question really but if my table for the transition function in q1 has a lot of parts of the symbols in the input alphabet (the English alphabet) is there a way to make this into a big table? Using the TM Table template  leads to the table not looking right.""",
    """Is the exam intended to take 72 hours?
Is the intention for us to have to use that amount of time or is it for example, a 24 hr exam that we have 72 hours to do etc.""",
    """Sophia's Office Hours
Does anyone know if Sophia is doing her office hours today?  The zoom meeting hasn't begun yet.""",
    """Explaining how a machine halts?
When we say a universal machine N halts when the machine M it's simulating halts, do we have to explicitly define how? Like would we have to say we know that when M halts it enters the accept state so when we notice this we also enter our accept state or something more elaborate""",
    """Clocked diagonalization

There are few parts that I am confused about the setup of M in the handout.

M initially layes out f(n) tapecells, which is a superpolynomial function, and then simulate N on x.

Wouldn't M already take f(n) steps, just to layout f(n) tapecells?

So whatever the result is simulating N on x, wouldn't M already have ran over polynomial steps, just by laying out f(n) tapecells? Then we can immediately conclude that L(M) != L(N) as M ran over the polynomial time by just laying out f(n) tapecells.

Another confusion was how to obtain n_0. So in the handout, with my poor understanding, we know the value of n_0. How is the n_0 given? Do we have to run another turing Machine to find n_0 that satisfy condtions given in the handout?

Lastly, in hw7 q3, we have a single-tape turing machine. I understand that we can have multiple tracks on a single tape. Then, it would require multiple steps in this multi-track single-tape machine, just to simulate one step of N on x. How do we account for this when approaching this problem?

Sorry about all these questions, I was just really stuck on how to do hw7 q3.""",
    """Q2a
Just to clarify, can a tape cell be visited twice or 4820 unique tape cells?""",
    """office hours from November 17th to November 24th?
Will there be office hours from November 17th to November 24th (semi-final exam week)?""",
    """What does recursively enumerable mean in terms of sets in simple language?""",
    """Generating arbitrarily long string
When we talked about the proof of |L(M)|>4820, we said we could feed every possible inputs of M to it, but I cannot think of a way to generate all inputs without using infinite states, so how are we supposed to do that?""",
    """Non R.E. reducing to show undecidability
Can we show that a problem is undecidable by reducing from a non-recursively enumerable problem (like the non-halting problem) to our problem in question?

Thanks!""",
    """clocked diagonalization step 3
In the handout it says that we simulate N on N#0^m, does that mean we are giving using a universal TM with N on input N#0^m, or are we using the universal TM with N on input 0^m?""",
    """TM visiting cells
Is it correct to say that any TM never "skips" a cell? Like, if it was at tape cell x_i, then the next tape cell it visits must be x_(i-1) or x_(i+1)""",
    """HW5 has been graded
HW5 has been graded and comments are on CMS. You have a week to submit any regrade requests you may have.""",
    """Semifinal Note Policy
Is the semifinal open-note or completely closed-note?""",
    """Another Reduction Example
I don't think I'm understanding a Turing machine reduction correctly. For the example where we are trying to decide if the TM accepts an empty string, we construct a machine M' that accepts if M halts on x. But aren't we trying to reduce HP to the empty problem? So how do we know if M halts on x if that's what we're trying to figure out? I think my understanding might be incorrect.""",
    """Wrong Algorithm.
If my algorithm has a bigger complexity than the solution, then it's considered to be a wrong algorithm?""",
    """Q2b, visiting infinitely many distinct tape cells is different from looping?
In the handout, there is a problem that explains how we can detect looping over a finite number of tape cells by counting the number of steps and seeing if it exceeds the total number of possible configurations. So for 2b, when we are proving the decidability/undecidability of visiting an infinite number of tape cells, does this mean that if the TM was looping, it would not be visiting an infinite number of distinct tape cells because looping involves visiting a finite number of tape cells an infinite number of times?""",
    """Q2 - proof clarification
The hand out says that to prove undecidability you can use either a reduction or diagonalization.  But to prove decidability it shows many proofs which are a just a few sentences detailing total TMs.  For problem 2, is such a description of a total TM a valid proof of decidability? Is there a more formal way to do the proof of decidability (it seems easy to miscommunicate when just using a few sentences)?""",
    """What counts as enough detail?
Received my homework 5 back. I'm not really sure what counts as a sufficient level of detail, especially when we don't have solutions the problem set. How can I ensure that my proof contains a sufficient level of detail on the exam? I followed the same form for the proof on the reductions handout, so I'm a little lost on what to do next.""",
    """Answer keys for textbook practice problems
Will an answer key be provided for the suggested textbook problems? It can be difficult to know if we truly understand the problem and the material without knowing if our solution is correct or not""",
    """Formal Q1
Do we actually have to describe what each state represents in our table, or is it sufficient to give general intuition in our informal solution and just give the transition table (of course also defining the other parts of machine M)""",
    """3 one-tape TM
Does it matter that the TM has to be a one-tape TM if multiple tapes can just be condensed onto one tape by changing the alphabet to be tuples rather than single characters like we showed in class? """,
    """Checking understanding of clocked diagonalization
Is this correct for clocked diagonalization:

We want to build a machine M is total but takes longer than polynomial time, because then L(M) is the decidable problem we're looking for

Now we need to make sure that M differs from every polynomial time machine, so it either accepts if a polynomial time machine rejects or vice versa

M's input is N#x but we don't know the efficiency of N, so we set an upper bound longer than polynomial time, say 2^n. Then if N halts before our bound, we know it's polynomial and want to have M differ, so we accept when N rejects or vice versa 

But then to make sure M is total, we'll also need to make sure it halts for non-polynomial inputs, so we'll have it accept/reject if we reach the time bound, which means N isn't polynomial and we don't have to worry about being different than these, so we can just either accept or reject""",
    """Which one brings you more joy?""",
    """Multiple tracks on a single tape Q2b
If there are multiple tracks on a single tape, and only the head of one of the multiple tracks visits infinitely many cells, does that count as the TM in general visiting infinitely many tape cells?""",
    """TM Handout decidable examples
In section 5 of the TM handout, I understand why example d is decidable, but I don't understand the reasoning behind the answer to example c. Why can't we just state M will take more than 481 steps on any input longer than 481 characters?""",
    """Does N have to mirror M?
Sorry if this question is obvious, but when we say "simulate M on N" for a reduction, does that mean N does exactly the same thing as M? So if M moves to the right, does that mean that N also moves to the right? Or can we define N to do something else when M steps? Thanks! I'm just a little confused in general, so my understanding of this might be off.""",
    """Hw3Q1
Do we have to include the transitions for t and r in our table for Question 1? Wouldn't they just be all "-" anyways?""",
    """Start Symbol in Input Alphabet
Based on the reading, it seems like the left end marker isn't necessarily part of the input alphabet. However, it's also always the first "letter" the Turing machine reads. Just for clarification, the input alphabet need not (and usually won't) include the left end marker, right?""",
    """Does HW7 q1 needs a proof?""",
    """question about left end marker and right end maker
Do we have to include the left end marker or right end maker in the tape alphabet? I feel it's not necessary to use them for Q1 HW7.""",
    """Q3
For Q3, when the problem states "one-tape Turing Machine", does this mean we can only use one track and cannot have the seperate tracks we talked about in class? In addition, if we use a similar technique as the exponentation described in class to lay out our cells, would we have to describe the process again or can we just say 'for each a we double the size of separate track"?""",
    """Undecidability Proof
Is this a sufficient undecidability proof? If we also wrote something similar to this, would it be enough for an undecidable proof or should the proof be more complicated?""",
    """Question about fakesol7
Hi I have a quick question regarding this example question--in the reduction of this question, we are only considering the case that each roommate can only have a list of two friends to invite and the minimum required person to invite for every roommate is 1. I understand that if we can give a reduction for this specific example to a NP hard problem, we can prove the party invitation problem to be NP hard; however I'm not sure how can we know if our example is too specific/or we are assuming too many things for the reduction? In this practice question we are assuming len(Pi)=2 and mi=1 for every roommate, and we are also assuming we have a "magic number" q that is the max number of friends that can be invited. How can I know if I need a magic number q as the upper bond, and what are the reasonable things to assume for the reduction?""",
    """Piazza on Semifinal
I think it was said in lecture and the handout that we won't be allowed to use the internet for our semifinal. 

This includes Piazza?""",
    """practicefsol Q3
Does P=U and Q=V?""",
    """Ford-Fulkerson vs. Edmonds Karp
Can we use either to find max-flow in any networking problem? It seems to me that is may be advantageous to use Edmonds-Karp over Ford-Fulkerson if this is the case because the runtime isn't dependent on flow/capacity.""",
    """Can we use tuples as characters in the alphabet of a TM?
If we wanted to simulate two tracks, both with alphabets {a,b} could we use a tuples of (a,a), (a,b), (b,a), (b,b) rather than a,b,c,d to represent those pairs (and add those tuples to the alphabet)? Would be easier for me to reason about and understand.""",
    """How does a Turing machine lay down X cells?
If I wanted a Turing machine to lay down X cells (e.g. X = 1,000), would i need X different states (s_1, s_2, ..., s_{1000})? Can't imagine any other way to keep track of how many we have put down so far, but having 1000 states seems like a lot of states.""",
    """q2 build turing machine
For a proof of decidability, are we able to create new Turing Machine or are we only supposed to add tracks to our current tape? Or are both approaches valid.

for example, in the handout it says "Problem (a) is easily decidable, since the number of states of M can be read off from the encoding of M. We can build a Turing machine that, given the encoding of M written on its input tape, counts the number
of states of M and accepts or rejects depending on whether the number is at least 481." So I interpreted this as building a Turing Machine separate from M, rather than dividing the tape to act as a multi-tape machine.""",
    """makeup1sol complexity
For algorithm A in 3a and 3b, why are the time complexities different? They both solve two subproblems of size n/2, which is O(nlogn), then do extra operations, which are just added on to the time complexity and since O(n) and O(1) both < O(nlogn), I would think that the total complexity for both algorithms would be O(nlogn), unless I'm misunderstanding something. Thanks!""",
    """Q2, small clarification on distinct tape cell.
Let's say that the turning machine changes the character on a tape cell from a to b. Then it revisits that tape cell. Is that considered a different tape cell (since the tape cell is at the same position relative to beginning of the tape) or is it a different tape cell (since the character encoded is different)?""",
    """Handout Example 1 (AnBnCn)
How did we know how many states to include in this machine? I am having trouble figuring out why there are 12 states (s, q1...q10, t). When we go to build our own Turing machine, how do we know how many states to use?

My confusion comes from my assumption that we should know what each state represents. For example (nothing to do with handout example 1), state v means that we saw an a. But then in the case of handout 1, we would've then only had five states (s, q1, q2, q3, t), where q1,q1, and q3 would represent having seen an a, b, or c respectively. Is this an invalid assumption?""",
    """Question 3 Misleading
According to the handout and the equivalence principle of all of the different forms of effective computation we've been learning about, a multiple tape Turing Machine can be described as a single tape Turing Machine. Question 3 specifies a single tape Turing Machine. Is this just slightly misleading or is there something about the reduction from multiple tape Turing Machines to a single tape machine that I'm missing?

Can we simply state the assumption that any multiple tape TM is equivalent to some single tape TM and use either in our response?""",
    """PracticeP2 Question 1d:
PracticeP2 Question 1d:

With this graph of the max flow where the edge weights are the flow,
how do we get that this is the min-cut?

I looked up how to do a few examples of these and drawn out the final residual graph, but I can't seem to understand exactly where the choice of cut comes from based on the final residual graph.

Thanks!""",
    """Practice Exam 2 1c
Hi, could someone explain how the max flow graph was generated? Just to double check, in order to find an augmenting path, you create a residual graph and subtract the bottleneck capacities and increment backwards edges along any path that goes from s to t, correct? You then use that flow in on the original graph and decrement accordingly? And you continue doing this until there are no more augmenting paths in the residual graph?""",
    """practicefsol Q5
What's the difference between undecidability and recursive enumerability? Is undecidability literally just "not strictly decidable/recursive"? I'm just confused because it would seem to me that there should be three categories (decidable, semidecidable, and undecidable) but it looks like undecidable covers both semidecidable and "true" undecidable (languages not accepted by any TM).

Also, part c says that a problem pretty much equivalent to "M takes more than 4820 steps on all inputs" is decidable, how would we go about proving this? Shouldn't it have to check every possible input, therefore looping forever?""",
    """Coding Assignments Statistics
Since some students ask for it, I am posting how many submissions of each programming language each problem had:""",
    """Two track, many to one TMs
For a counter TM, where one track simulates the execution of some TM and the other counts how many steps the simulation takes, can the counting track take multiple steps based on what the simulation track is doing? For example, could the counting track increment each of its non-blank cells whenever the simulation track takes a step? If so, can it be variable (i.e, does the previous behavior unless the simulation encounters a blank, in which case it does nothing)?""",
    """Q1
In Question 1., when it says "reject all other strings", do we consider only strings containing the alphabets a and b? or do we also explicitly reject strings which contain alphabets other than a and b?""",
    """Q1
Can we assume that the input is followed by a blank?""",
    """Yes, there are infinite blanks following the input string on the tape.

Page 3 of the TM handout:

The input string is of finite length and is initially written on the tape in contiguous tape cells snug up against
the left endmarker. The infinitely many cells to the right of the input all contain a special blank symbol _.""",
    """Why do we lay off tape cells?
Why can't we just compute a value for f(n) and then check that the machine N can be simulated in f(n) steps or less?""",
    """PracticeP2 Question 2b
In this question, it claims that if P != NP, then there is no polynomial-time reduction from Max Flow to Subset Sum.

I see how this claim is definitely false in that all problems in P can be "reduced" to the harder problems in NP, regardless of if we have P=NP or not, but I wasn't super sure if I understand the reduction given from Max Flow to Subset Sum. Here's the reduction given:

"Let Y and N be arbitrary “yes” and “no” instances, respectively, of Subset Sum. Given an instance G of Maximum Flow, run your favorite polynomial-time max flow algorithm, e.g. Ford–Fulkerson, on G to determine a max flow. If the value of the max flow is at least k, output Y. If the value of the max flow is less than k, output N."

This reduction seems pretty trivial. Can all reductions from P to NP problems take this form? If we were to try using a reduction of this form to reduce an NP problem to another NP problem, where would it fall flat?

Thanks!""",
    """Intuition behind the "HP is undecidable" proof
During the 11/9 lecture we first proved HP is undecidable by assuming there is a machine K that decides HP, construct a machine N on top of K, and then getting a contradiction that "N accepts N iff N does not accept N". We then explained why it is called diagonalization by drawing a matrix and seeing that "HP is decidable"  will contradict the fact "there are finite number of TMs".

I understand that both processes prove the claim by contradiction, but have a hard time seeing how these two processes and their intuitions relate to each other since the two proofs give contradiction to different facts. Would appreciates some insights on their relation. Or are these two proofs simply different approaches and don't really relate?""",
    """format for asking questions about practice exams of semi-final
Can we post screenshots with questions and solutions publicly when asking questions about practice exams of semi-final?""",
    """practice prelim 3, q1b
how was 8 calculated as the threshold for whether an edge would be included in the minimum spanning graph?""",
    """TM Handout 5(e)
Hi, I'm a little confused about example (e) regarding decision problems with Turing Machines on the handout. We're trying to determine if M moves its head more than 481 tape cells away from the left endmarker on an empty input. We claim that if M doesn't move more than 481 tape cells away, then M either halts or loops in a manner we can detect (because there is an upper bound on the number of configurations we can have). 

But then we conclude that if we exceed 482km^481 steps, then M has looped. I'm a little confused by the logic / conclusion drawn here -- if we exceed the upper bound, why do we conclude that M didn't move more than 481 tape cells away (due to looping)? Why can't we conclude that we might've exceeded the upper bound because we travelled more than 481 tape cells away from the left endmark? Thanks! """,
    """Office Hours
I know that there was a post that office hours were cancelled but there were office hours earlier today so I'm not sure what's going on - are there some going on right now?""",
    """proof of (e) on page 19 of handout "Notes on Turing machines"
The handout says that "This can be detected by a machine that simulates M, counting the number of steps M takes on a separate track and declaring M to be in a loop if the bound of 482km^481 steps is ever exceeded."

Don't we need three trackers that we also need one to track whether M halts before visit 481 tape cells?""",
    """Dumb question but...
The timer only starts once the exam has been downloaded right? Because instead of clicking on the entry for the practice final in CMS, I accidentally clicked on the entry for the final, but haven't downloaded the final or anything else. My timer hasn't started right?""",
    """What is 0^m in Clocked Diagonalization?
I am understanding N#x as the encoded simulated Turing machine N with input x. But what is N#0^m? Does it mean an input string with all 0 of length m?""",
    """General clarification on TMs
If a TM halts, does that mean it must halt in finite time, i.e after a finite number of steps? Or does the definition of halting not cover this technicality? The definition of accept and reject under the reflexive transitive closure of the next configuration relation makes it seem like it must accept or reject in a finite number of steps, but I wanted to be sure.""",
    """Clocked Diagonalization English Intuition
I know that it was alluded to in class that clocked diagonalization (and maybe the corresponding homework problem?) should be fairly easy, but I don't know if all this TM stuff is getting to my head, but I'm having a hard time grasping clocked diagonalization on my own. Any additional intuitive insights anybody has ascertained which could help complement the handout would be greatly appreciated.""",
    """Reduction Example - (f) on page 19 of notes
I am confused about the step to design such a reduction. 

For example (f), it saids "erase its input y" then "write x on its tape"

but how do we know which input x to use here? Is input y of M' and input x of M related ? Do x any y have any 1-to-1 correspondence ?  How does M decide which input to run given different y ? 

I think I am missing something here.  Thanks in advance for help :)""",
    """Input to M in clocked diagonalization
I'm still pretty confused about the nature of the input given to TM M we are constructing in clocked diagonalization. I'm not really sure why it's some machine N with an (arbitrary?) number of zeroes following it, and why M is running N by passing N an input of N followed by the zeroes. I generally understand why M needs to create, say, a super-polynomial number of cells on a separate track to keep track of executing another TM to see if it runs in polynomial time, but I guess I'm just quite confused at exactly what M is executing and with which inputs.""",
    """Hw7 Q3
Hi, so if I understand the clocked diagonalization handout correctly, we need to lay off some number of tape cells where the number of tape cells we lay off is superpolynomial.

However, I can't find anything that's super.... 2 to the 2 to the 2 to n? I see that n! beats 2 to the n, but how can I know what beats our chained exponents?

Also, slight clarification: what exactly does "laying off" f(n) tape cells do for us? It seems like we're somehow using those f(n) cells to count f(n) steps, but how?

Sorry if these have already been explained but I read every piazza post on Q3 and diagonalization and still feel like I'm missing something""",
    """clocked diagonalization laying off tape cells
In the clocked diagonalization proof, am I correct to say that we lay down f(n) tape cells in step 2 solely to keep track of the f(n) simulated steps in step 3? And in that case, does it matter what the character contents of those f(n) tape cells are?""",
    """Q1
Do we need to prove the correctness of our Turing machine?""",
    """practicefsol 2c Dynamic Programming vs Flow
How can we tell which algorithm to use for 2c? Can I get some intuition behind why we would use flow for k=2 case but dynamic programming for monotone partition?""",
    """Proof on semifinal
Can we assume that we need to write the algorithm, prove its correctness, and analyze its runtime complexity for problems on semifinal like we did in the homework?""",
    """hw7 q2
for counting, can we just write just like "Simulate N on input x with a universal TM for up to f(n) (simulated) steps, counting on a separate track. " for hw 7 q2?

Or

we need to write specifically about how that track works? """,
    """General Clarification Question about Flow
I haven't started the test, I just have a general question about the definition of flow/value of flow. 

f(e) is the amount of flow running across a specific edge e, but v(f) is the sum of the f(e)'s for edges coming out of s.

Is my understanding correct?""",
    """Why is HP re?
I'm just little confused on why HP is re. 

Isn't HP just saying that we can't know whether machine M halts on input x..?""",
    """Question of time complexity of divide-and-conquer problems
Hi, I'm a little unsure about time complexity of divide-and-conquer problems; I'm thinking that if we recursively solve subproblems, then the time complexity would be O(nlogn)? Why the time complexity for the problem below (in a practice prelim) is O(n^2)?

Example. Algorithm A is a greedy algorithm that runs a single loop over i = 1,...,n, with a constant number of operations per loop iteration.

Algorithm B is a divide-and-conquer algorithm that recursively solves four subproblems of size n/2, then does O(n) extra operations to combine the four answers.

Solution. A is faster. (Algorithm A runs in O(n) steps, whereas Algorithm B runs in O(n2) steps. As noted earlier, you are not responsible for writing this information in your solution; merely writing “A is faster” in this case would earn a perfect score.)""",
    """Q7 2b
Can a Turing Machine that visits infinitely many tape cells on a given input ever halt on that input?

For example, suppose a Turing machine that halts when 1/(cell number that head is currently on) = 0, be said to halt after visiting infinitely many tape cells?""",
    """Practice Exams Reference
Are the provided practice exams considered course materials and thus fair game for reference for the semifinal, or are they off-limits once the exam has begun? Thanks.""",
    """Is handwritten accpeted for semifinal?""",
    """Phase one of Edmonds-Karp
Does the first phase refer to a single BFS path or multiple BFS paths that have the same level?""",
    """Does visiting infinitely many cells mean a machine doesn't halt?
If we know that a machine visits infinitely many cells, do we know that it halts? This is about 2b. """,
    """Clocked Diagonalization Nature of N
Hello, I'm the one who has spent many days trying to understand clocked diagonalization and still can't. I guess I'll try to ask a couple more questions, although I'm not sure if exact answers to them will fully resolve the issue for me.

The handout states "build a total TM M that differs from every machine with input alphabet that runs in polynomial time on at least one input". Does this mean, given every machine that runs in polynomial time, M should differ from it on at least one input? Or does it mean, given every machine which runs in polynomial time on at least one input, M should differ from it?

Later in the proof on the handout, it states "Since N halts within the time limit, M will do the opposite of what N does on input x". How do we know that N is going to run in polynomial time specifically on x=N#0^m? Are we assuming N runs in poly-time for all inputs x (such that |x|>n0), or only for at least one input?""",
    """Finite Control Simulation
Say we somehow encode a machine M and its input X into the finite control of another machine T. Can T simulate steps of M on input X just by moving through different states and not actually writing anything on its tape?""",
    """Penalty on late submission.
Hi! What is the penalty if we are late by 1 hour when submitting the exam ?""",
    """It's not about the points
Congratulations to everyone that finished their semi-final.  You're free! Now go enjoy your break."""
]

# from old to new
# stopped at https://piazza.com/class/kea8ntdsn097ev?cid=1505
