Source: author-supplied PDF (IEEE Access, 2015, doi 10.1109/ACCESS.2015.2424703; sole author; English; journal-copyedited)

Received March 21, 2015, accepted April 15, 2015, date of publication April 20, 2015, date of current version April 30, 2015.
Digital Object Identifier 10.1109/ACCESS.2015.2424703




Computerized Argument Delphi Technique
SADI EVREN SEKER, (Member, IEEE)
Department of Business, Istanbul Medeniyet University, Istanbul 34000, Turkey (academic@sadievrenseker.com)




  ABSTRACT The aim of this study is the computerization of the argument Delphi method. The Delphi
  method is mainly designed for qualitative prediction within a group of experts, where the experts make
  predictions and a facilitator controls these predictions until the experts end up with a level of consensus.
  Argument Delphi, as opposed to the classical Delphi model, is built on the contradictions of the ideas of the
  experts. Argument Delphi mainly focuses on a discussion topic and asks experts to create new arguments
  and criticize other arguments from other experts. After a certain level of contradiction, the method yields an
  amount of contradictory, criticized arguments and builds a decision over these antitheses, as in the Hegelian
  approach. This is the first time the argument Delphi method has been modeled in a graph of arguments
  and the problem of qualitative decision has been transferred into a graph problem using Delphi method. This
  paper is also the first time that argument aggregation and evaluation methods have been proposed. Moreover,
  the computerized version of argument Delphi is applied to real-world problems using crowd involvement
  through Facebook. The problem is defined as the prediction of petroleum prices for the end of year and more
  than 100 contributors from all around the world argued and criticized each other. This paper also discusses
  the findings of this case study.


  INDEX TERMS Delphi technique, decision support systems, qualitative methods, graph theory, social
  network, crowd opinion.

I. INTRODUCTION
The Delphi method is a qualitative prediction of forecasting
method, where experts share their expertise on the prediction
in a turn-based system [1].
   The Delphi method has three major phases as demonstrated
in Figure 1. In the first phase, the experts make predictions
about the question posed by the facilitator. In the second
phase, the facilitator collects and aggregates the predictions.
Finally, in the third phase the facilitator announces the
aggregated prediction back to the experts and all the experts
update their predictions and make new ones. The method runs                                      FIGURE 1. Three rounds of Delphi Method.

until a satisfactory level of prediction is reached by repeating
all three steps [2].                                                                             third stage as taking place between late 1960s to mid 1970s
   The Delphi method was first introduced into the literature                                    with 389 articles, papers and reports, while Rieger [9]
in 1944 during the World War II to create reports about future                                   indicates 61 dissertations between 1970 and 1974. According
military technological capabilities by the US Air Corps [3].                                     to the divisions proposed by Yousuf [8], in the fifth stage, the
   Following its introduction, the Delphi method had a great                                     number of dissertations on the Delphi technique between
long-term impact on the literature and it is still very active                                   1980 and 1984 was 441. The increasing impact of technique
for many applications all around the world. Most manage-                                         since it was first introduced into the literature can be
ment textbooks and popular management books even cover                                           understood from these statistics.
the method [4]–[7]. Because of its importance and impact                                            During the period of this study, according to the Google
on the fields of management and administration for many                                          Scholar statistics, the number of articles reports or dis-
years, many varieties of the method have been developed and                                      sertations related to the Delphi method just between
successfully utilized by researchers worldwide. In his study,                                    2010 and 2014 was more than 22,000.
Yousuf [8] divides the development of the Delphi method                                             There is also some recent work by the IS/IT researchers.
into 5 stages. In his division, he has underlined the                                            In one of these researches, researchers examined the impact

                                             2169-3536 ⌦ 2015 IEEE. Translations and content mining are permitted for academic research only.
368                                                Personal use is also permitted, but republication/redistribution requires IEEE permission.       VOLUME 3, 2015
                                            See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.
S. E. Seker: Computerized Argument Delphi Technique




of the Delphi method from 2502 articles and showed how the        media analysis, computerized argument Delphi is proposed
Delphi method is useful in different situations [10]. Another     as an alternative to gather structured data in order to
recent study involves the forecasting of financial markets by     understand the opinion of the crowd. The major impact of
the Delphi method, where the method has been applied in           the computerized argument Delphi method is being able to
two phases. The first phase corrects the belief perseverance      conduct all the operations in a web environment. For example,
bias, while the second phase tests a conditional forecast         the collection of arguments from the experts can be collected
process, which unexpectedly proves unsuccessful [11].             by interviews, in written form, in discussion groups or by
   Because of the limitations of the traditional Delphi method,   brainstorming [20], [21]. As a computerized version of the
there are several varieties which have been introduced into the   argument Delphi method, data collection via the Internet is
literature. One famous application—which is conceptually          proposed. Because of its various alternatives, this computer-
not far from argument Delphi—is policy Delphi [12].               ized version of argument Delphi lets the contributors write
Policy Delphi focuses on generating the strongest possible        their opinions, arguments or assumptions freely on the topic.
opposing viewpoints about any policy. Different than the          This version of Delphi has major advantages—for example,
consensus of traditional Delphi, policy Delphi is built on the    all the discussions on social networks or web pages are a
debates [13]. The beauty of the Delphi method can also be         form of written debate on the topic, such as the cases on
connected to its Hegelian nature [14]. After the first round of   Facebook, where one of the users shares an info-graphic
the Delphi method, the experts are divided into two camps.        and then hundreds of comments are made in the
For example, consider the weather forecast scenario. Experts      discussion [22]–[24]. In the computerized argument Delphi
are asked for the weather forecast for the next season. After     method, the first (basis) step is as easy as putting up an
the first round of predictions, the experts are divided into      argument for the discussion. After the first argument about
two groups, where the first group has an expectation lower        any opinion, anyone in the same environment (like social
than the average forecast and second group has an expecta-        media, such as Facebook, Twitter, LinkedIn or other web
tion higher than the average forecast. At any point, Delphi       environments like forums, blogs or portals [25], [26]) can get
produces two contrary groups, which can also be treated as        involved in the discussion within the rules of computerized
the thesis and anti-thesis for the discussion. The weakness       argument Delphi.
of the classical Delphi method is its lack of arguments and          Computerized argument Delphi is not a discrete approach,
only the numbers or the moderator collects the predictions.       where each step can only take action after the previous step
At any phase the reasons are out of discussion and each expert    is completed. Instead, the method has a continuous arguing
tries only to check their predictions with common sense.          behavior and all steps can take action after the first step. Also,
On the other hand, information exchange between experts           results can be collected at any time and the most important
can convince some of the experts about the prediction of          output of the method, called an argument graph, can be
the opposing camp, but unfortunately the classical Delphi         collected at any time after the method is started.
method lacks such an alternative.                                    According to its continuous behavior, the computerized
   In addition, another major impact on the Delphi method is      argument Delphi method allows any contributor to add new
the computerized versions [15]. These versions mainly give        arguments about the discussion as the second step and rate the
the advantage of computer technology, such as communica-          previous arguments as the third step. These three steps keep
tion capabilities, automatic selection or elimination, logging    running and contributors can access the system at any time or
and trace back and so on.                                         any number of times without limitations.
   One version of the policy Delphi method, named                    Computerized argument Delphi method has an output
Argument Delphi, also concentrates on the interchange of          phase, which can be executed simultaneously to the three
arguments between experts. The Argument Delphi method is          phases of the contributor involvement step. All these steps
more specifically used for stating the arguments and hosting      are demonstrated in figure 2.
discussions about the arguments [16]. For example, in an             The traditional argument aggregation is the weakest part of
application of the Argument Delphi method on engineering          the argument Delphi method and the strength of arguments
education for Finland 2015, the method starts by interviewing     is missed during the aggregation. The facilitator is forced to
the experts in the first round. Interviewing each expert takes    make an aggregation in order to end up with a single or only a
about 1.5 to 3 hours and in the application they have selected    few arguments for the next step. The aggregation step either
only 21 experts. In the following rounds, the experts are         completely loses the majority of the arguments or weakens
asked to give their opinions about the education system via       the effect of a majority of the arguments on the next step,
questionnaire [17].                                               because the arguments from the first step are aggregated and
                                                                  reduced into a single argument.
II. COMPUTERIZING ARGUMENT DELPHI METHOD                             The argument aggregation of the traditional argument
In this study, a computerized version of Argument Delphi          Delphi method can be explained by set theory. Let
is proposed which is also suitable for web, social media          A and E be the sets of arguments and experts, such as
or mobile applications. Besides the text mining [18]              A = {arg1, arg2, arg3 . . . argn} and E = {exp1, exp2,
or streaming data mining [19] approaches to social                exp3 . . . expn}. The aggregation function f is a surjective

VOLUME 3, 2015                                                                                                                  369
                                                                                               S. E. Seker: Computerized Argument Delphi Technique




                FIGURE 2. Continuous Behaviour of Computerized Argument Map and Three Simultaneous Steps.



function and can be demonstrated by set theory as in                       relation R can be demonstrated as in equation (3).
equation (1).
                                                                                   R:A!A
                                          n
      8a 2 A,     9aaggregated 2 A,     fi=1 (ai ) = aaggregated .   (1)           a,r1 , r2 , r3 2 A   and    R     (a,r1 , r2 , r3 ) 2 Rt   (3)

   In other words, the function f is a one-way function where                 I have limited the number of the rating to 3 because the
the aggregated argument can be created from the set of                     computerized version is designed for massive involvement
arguments, but the set of arguments cannot be created back                 environments like social networks or web pages. For
from the aggregated arguments. Also, the set member oper-                  example, it is also possible to ask a contributor to rate all
ator in equation (1) is a conceptual approach and it can be                of the previous arguments, but in this case contributor would
considered as an exact set member operator only when one                   either spend an excessive amount of time doing so or would
member of set A is selected. The surjective function has only              prefer to rate the contributions without concentrating on the
one exceptional case for a two-way possibility, which is the               actual arguments. The number of arguments in further studies
set union on all members of argument set A as demonstrated                 can be parametric and the facilitator can decide on the relevant
in equation (2).                                                           number.
                                                                              The computerized version of the argument Delphi method
                                        n
                                        [                                  can be reviewed from the Hegelian point of view by dividing
                        aaggregated =         ai                     (2)
                                                                           the contributors into two camps of thesis and anti-thesis [27].
                                        i=1
                                                                              Figure 3 demonstrates the role of each group in the
   In the computerized version of the argument Delphi                      argument Delphi method. After the first prediction,
method, it is possible to ask for the opinion of experts about
the arguments produced by other experts. In my proposi-
tion, the argument generated by one expert is displayed
to another expert, and this expert’s opinion on the
argument is asked by a rating system. After entering their
opinion, each expert is asked to rate three random arguments
which have been previously entered into the system by other
experts.
   The proposed approach also can be modeled by set theory.
Let A and Rt be two sets of arguments and ratings,
respectively, such as A = {arg1, arg2, arg3 . . . argn} and
Rt = {r1, r2, r3 . . . r3n}, where the cardinality of rating
set R is three times the cardinality of the argument set A,
because for each argument, the contributor rates three
previous arguments. Any contribution is a relation between
set A and A itself, where the relation has an insertion to the set
of arguments A and a rating tuple on set Rt. The contribution              FIGURE 3. Hegelian Approach to Delphi Method.

370                                                                                                                                 VOLUME 3, 2015
S. E. Seker: Computerized Argument Delphi Technique




the experts divide into two camps, the thesis and antithesis        Step 4, Round 2: Contributors make another personal
camps. Each camp argues the prediction from their point          prediction after they receive back the aggregated prediction,
of view, considers the contrary arguments and updates their      but the previous aggregation divides the contributors into
prediction if they feel they have to. Also, the facilitator      two camps. The first camp has a lower prediction than the
keeps collecting predictions, aggregating and announcing         average, while the second camp has a higher prediction than
them back to the experts.                                        the average. In this case, both contributors in the lower and
   In the computerized argument Delphi method, a similar         higher camps may argue about the reasons for their predic-
approach to dialectics in the Hegelian approach is kept. The     tions, and why the aggregated prediction should be lower or
only difference—and the biggest impact—of the computer-          higher, respectively. So contributors update their predictions
ized version is adding multiple arguments into the discussion    by arguing and send them back to the facilitator.
and giving multiple paths for anybody to follow. Even the           Step 5, Round 3: Facilitator collects the updated
contributor can add a new path of dialect for himself.           predictions and arguments from the contributors. The facil-
   In figure 4, one of the many possible paths about arguments   itator then aggregates the predictions (e.g., average) and
is demonstrated. The power of the computerized argument          aggregates the arguments and announces them back to the
Delphi method comes from the possibility of keeping and          experts.
processing thousands of arguments. Any contributor can              Step 6, Round 3: Experts now have the information for
easily join the system by making decisions on previously         the aggregated prediction and arguments from the opposite
added arguments and can add his own argument to the graph        camp and the supporting camp. They can think about these
as well.                                                         arguments and, according to their judgment, they can make
                                                                 more sensitive and intelligent predictions. The scenario can
                                                                 also be demonstrated in figure 5.




                                                                 FIGURE 5. Running Scenario of Computerized Argument Delphi,
FIGURE 4. Personalized track of argument graph.                  Argument Aggregation.

                                                                    During the development of the computerized argument
III. SAMPLE SCENARIO FOR THE COMPUTERIZED
                                                                 Delphi method, one problem we faced was the aggregation of
ARGUMENT DELPHI METHOD
                                                                 arguments. As a solution, below a list of aggregation methods
The simplicity of the traditional Delphi method is one
                                                                 are proposed.
of its advantages. Everybody can easily understand the
                                                                    List of arguments: In this aggregation method, all the
Delphi method and can apply it simply to any problem such
                                                                 arguments are collected and listed together. For example, the
as prediction, decision support, forecasting, etc. Below is a
                                                                 facilitator says, people who believe the forecasting is low
scenario for the Computerized Argument Delphi Method to
                                                                 say ‘‘argue1, argue2, argue3 . . .’’ and people who believe the
help explain it in its most simple form. The scenario is built
                                                                 forecasting is high say ‘‘argue10, argue11, argue12, . . .’’ etc.
for a simple prediction of numbers and collects arguments
                                                                 This method requires less time for the facilitator but requires
about the prediction. Thus, contributors can argue about their
                                                                 a higher amount of time for the panelists in order to read all
predictions. In addition, after the first step of prediction,
                                                                 and evaluate all of the arguments. This can be represented in
contributors can be assumed to be divided into two camps
                                                                 set theory as in equation (4), similar to equation (2).
like in the Hegelian approach.
   Step 1, Round 1: Facilitator asks question; what is your                                            n
                                                                                                       [
prediction?                                                                            aaggregated =         ai                (4)
   Step 2, Round 1: Contributors write their predictions and                                           i=1
send to the facilitator in closed form.                             Drop similar: In this aggregation method, the facilitator
   Step 3, Round 2: Facilitator collects the predictions and     reads and eliminates arguments in the same way. For example,
aggregates them (e.g. average of all predictions until this      if contributor 1 and contributor 2 have similar arguments,
time) and announces back to the contributors.                    the facilitator simply drops one of them, using one of the

VOLUME 3, 2015                                                                                                                 371
                                                                                            S. E. Seker: Computerized Argument Delphi Technique




arguments only. This can be represented in set theory as in                The computerized argument Delphi method has 3 screens
equation (5).                                                           connected to each other and each screen plays a major role in
                      n
                                                                        the argument evaluation.
                      [                                                    The screen design shown in figure 6 has an algorithm flow
      aaggregated =         ai ,   if any Dnj=i+1 (ai ,aj ) > t   (5)
                                                                        chart, which is also demonstrated in figure 7.
                      i=1

   In equation (5), the aggregated arguments are prepared
from the set of arguments, where all the arguments are tested
through a distance function D and the argument is accepted
to the aggregated result only if the distance is above a certain
threshold value t, which is defined by the facilitator. The dis-
tance function can be based on a natural language processing
or a string distance function [28], [29].
   Tournament selection: In this aggregation method, one
expert, perhaps the facilitator, reads and decides the best argu-
ments as thesis and antithesis, depending on his knowledge
and expertise. The aggregation method can also be based on
the evolutionary computation [30].
   Use qualitative marginal: In this aggregation method, the            FIGURE 7. Screen Designs from a sample implementation of the
facilitator uses the arguments from the top n highest and               computerized argument Delphi method.

lowest forecasts from the experts. For example, if the n in this
method is 2, then the facilitator prepares a list of arguments
                                                                           The flow chart of the algorithm can also be written as
from the highest two and lowest two forecasting arguments.
                                                                        in Algorithm 1.
                               [
                 aaggregated =      max Rn0 =1 ai             (6)
                                         k                              Algorithm 1 Continuous Contribution Algorithm
  The aggregated argument is the set union of k maximum                   Input: Prediction value, as p,
arguments in the rating.                                                  Argument, as a,
  Algorithmic Approach to the Argument Delphi Method.                     Output: Argument a, Prediction p, Ratings set
                                                                          R={ <a1 , r1 > , <a2 , r2 > , <a3 , r3 > }
                                                                          Pre-calculation: n, the number of arguments in database
                                                                          1: p     Read prediction from user
                                                                          2: pavg      Calculate average ( p1 , . . . , pn )
                                                                          3: if p < pavg then
                                                                          4: a       Ask argument, why is your prediction low?
                                                                          5: else if p > pavg then
                                                                          6: a       Ask argument, why is your prediction high?
                                                                          7: end if
                                                                          8: for i := 1 to 3
                                                                          8: ai       rand(a1 , . . . an )
                                                                          9: ri       Ask rating for ai
                                                                          10: end for
                                                                          11: save record<a, p, {<a1 , r1 > , <a2 , r2 > , <a3 , r3 >}>

                                                                           The computerized argument Delphi method gives an
                                                                        opportunity to create a report with arguments. For example,
                                                                        during the prediction period, the average prediction value
                                                                        from the contributors can value the argument and a report can
                                                                        be generated based on the average predictions.

                                                                        IV. EVALUATION OF ARGUMENT GRAPH
                                                                        Questions about any argument graph include ‘‘Which
                                                                        argument is most valuable and most accepted?’’, ‘‘How can
                                                                        we evaluate all the arguments and summarize them into a
                                                                        single report?’’, and ‘‘What is the most efficient way of
FIGURE 6. Flowchart of a sample computerized argumnet Delphi method.    aggregating the graphs?’’.

372                                                                                                                              VOLUME 3, 2015
S. E. Seker: Computerized Argument Delphi Technique




   In the study, possible evaluation methods are researched
and listed below:
   1. Sort and Rate
   2. Propagated Path Sort
   3. Average Propagation Sort
   4. Leave Lowest Out
   5. Two Camps Approach
   The Sort and Rate approach sorts arguments by their aver-
age rating from the other contributors. The argument with
highest rating or highest-k ratings can be selected as a result
of the computerized argument Delphi method.
   Aside from some possible naïve analyses, the questions can
be answered via graph theory.
   During the evaluation of the computerized argument
                                                                      FIGURE 8. Visualization of Sample Argument Graph G1.
Delphi method, the arguments and ratings between argu-
ments creates a weighted directed acyclic graph, which is a           an element of the vector set of graph [31]. During this
weighted tree. The argument can be represented via graph              research, there is no interest in the calculation of out-degree.
theory as G = (V , E), where V is the set of vertices                 Moreover, the average in-degree is taken into account, and
(arguments) and E is the set of edges (ratings). The order            the below equation (8) is proposed for the calculation in the
of the graph can be defined as |V| and the size of the                ‘‘sort and rate’’ approach.
graph is |E|, where |V| is the number of vertices and |E| is                                           X w(u)
the number of edges. The degree of vertices is always three                                deg (u) =                               (8)
                                                                                                            |V |
                                                                                                        u2V
except for the root nodes, so the argument graph can be
considered as a 3-regular graph. Although the regularity of              The degree calculation is modified for the weighted graph
the graph is parametric and can be considered as k-regular            with weights on the edges and the average is calculated
for the number of arguments rated after each entrance, the            simply by dividing the element count of set V . The calculation
sample will be demonstrated over a 3-regular graph. Another           for each node is given below:
assumption about graph G is the weights of the edges. In the              deg(A1 ) = 5,      deg(A2 ) = 3.25,          deg(A3 ) = 3.66,
proposed graph, the weight of an edge is defined as between               deg(A4 ) = 4,      deg(A5 ) = 3.5,           deg(A6 ) = 4.5,
1 and 5 because the argument rating is from 1 to 5 and can be
represented with w 2 R and 1  w  5.                                     deg(A7 ) = 1,      deg(A8 ) = 0
   The evaluation of the argument graph will be explained             from the degree calculation, the highest three arguments in
through a sample argument graph G1 as represented below:              the graph are A6 , A4 , and A5 .
   G1 = (V1 , E1 )                                                       For the directed graph as an argument graph, it is possible
                                                                      to define a directed path, dipath [32] as a sequence of vertices
   V1 = {A1 , A2 , A3 , A4 , A5 , A6 , A7 , A8 }
                                                                      or edges. In this paper the notation of edges will be used to
   E1 = {< A4 , A1 , 5 >, < A4 , A2 , 3 >, < A4 , A3 , 5 >,           represent the dipaths. In addition, it is possible to define the
            < A5 , A4 , 3 >, < A5 , A2 , 2 >, < A5 , A3 , 5 >,        weight or length of a dipath as in equation (9).
            < A6 , A5 , 2 >, < A6 , A2 , 3 >, < A6 , A3 , 1 >,                                         k 1
                                                                                                       X
            < A7 , A4 , 5 >, < A7 , A2 , 5 >, < A7 , A5 , 5 >,                               w (P) =          w(ei )                      (9)
                                                                                                       ,i=0
            < A8 , A7 , 1 >, < A8 , A5 , 3.5 >, < A8 , A6 , 4.5 >}
                                                                      where P indicates any directed path on the argument graph
   Any tuple t in E1 can be defined as below:                         and w is the weight of any edge e 2 E. All nodes have a path
t =< e1 e2 w >, where (e1 , e2 ) 2 E ⇥ E              and 1  w  5   from root nodes on the G1, which can be calculated as below:
   The above graph representation can also be visually                 PA1 = {PA4 [ < A4 , A1 , 5 >}
demonstrated as in figure 8.                                           PA2 = {PA4 [ < A4 , A2 , 3 >, PA5 [ < A5 , A2 , 2 >,
   The sort and rate approach for graph G1 can be calculated                  PA7 [ < A7 , A2 , 5 >, PA6 [ < A6 , A2 , 3 >}
by simply calculating the average in-degree of each node in            PA3 = {PA6 [ < A6 , A3 , 1 >, PA5 [ < A5 , A3 , 5 >,
the graph. In-degree can be calculated as demonstrated in                     PA4 [ < A4 , A3 , 5 >}
equation (7):                                                          PA4 = {PA7 [ < A7 , A4 , 5 >}
                                X
                     deg (u) =      (u)                  (7)           PA5 = {< A8 , A5 , 3.5 >, < A6 , A5 , 2 >, < A7 , A5 , 5 >}
                                      u2V                              PA6 = {< A8 , A6 , 4.5 >}
  In the graph theory, ‘‘deg ’’ indicates the in-degree                PA7 = {< A8 , A7 , 1 >}
and ‘‘deg+’’ is the out-degree of any node, which is                   PA8 = {}

VOLUME 3, 2015                                                                                                                            373
                                                                                                S. E. Seker: Computerized Argument Delphi Technique




  Using the above set of paths, the weight of each path can                   From equation (12), the values of each path can be
be calculated as below:                                                     normalized as below:
      w(PA1 ) = 11,      w(PA2 ) = 35,              w(PA3 ) = 32,                     wa (PA1 ) = 0.4,          wa (PA2 ) = 3.86,
                                                                                      wa (PA3 ) = 0.2,          wa (PA4 ) = 1.06,
      w(PA4 ) = 6,       w(PA5 ) = 10.5,            w(PA6 ) = 4.5,
                                                                                      wa (PA5 ) = 0.1,          wa (PA6 ) = 0.96,
      w(PA7 ) = 1,       w(PA8 ) = 0
                                                                                      wa (PA7 ) = 2.53,         wa (PA8 ) = 0.
   From the above calculation, the highest path weight is                      The negative values of path weights can be considered
w(PA2 ) with 35. This approach is proposed as ‘‘propagated                  as ‘‘disliked’’ arguments by the society—for example, an
path sort’’ in this paper.                                                  argument against the collective opinion of the social network
   On the other hand, the above classical graph theory                      society, like Facebook, Twitter or LinkedIn. From the final
approach would be a mistake because the first argument in the               results of normalized path weight via average weight, the best
argument graph will be the leaf with the highest path weight                three paths can be considered as PA6 , PA1 , PA2 and PA3,
in most cases, which can also be observed in the sample                     and the rest are less than or equal to zero. This approach is
graph G1 , where the highest three weights are the leaf                     proposed with the name of ‘‘average propagation sort’’ in
nodes A1 , A2 and A3 .                                                      this study.
   As a solution to the above path length problem, an average                  Another solution proposed in this paper is called the
weight solution is proposed. For an argument graph, an aver-                ‘‘leave lowest out’’ technique. The motivation behind this
age weight can be applied in two ways. The first approach                   technique is the dirty data insertion in the social networks,
can be the mean calculation via equation (10) below:                        like empty fields, uncompleted forms or erroneous entrances
                                     k 1
                                     X                                      on purpose. Since the argument Delphi method was originally
                                         w(ei )
                      wavg (P) =                                     (10)   designed for the experts, application of the method over mas-
                                            k   1                           sive user environments like social media or web pages brings
                                     ,i=0

   If equation (10) is applied over the weights of all the paths,           such problems. The computerized version brings the solution
the values would be as follows:                                             from the problem itself and uses the contributors to evaluate
                                                                            and understand the dirty data in the system. One major reason
          wavg (PA1 ) = 3.66,          wavg (PA2 ) = 3.33,                  of rating an argument to a ‘‘1’’, which is the lowest rating
                                                                            possible, is because it is dirty data and contributors don’t like
          wavg (PA3 ) = 3.66,          wavg (PA4 ) = 3,
                                                                            dirty data rating.
          wavg (PA5 ) = 3.5,          wavg (PA6 ) = 4.5,                       The ‘‘leave lowest out’’ technique was originally devel-
                                                                            oped for understanding and removing dirty data from the
          wavg (PA7 ) = 1,            wavg (PA8 ) = 0.
                                                                            system, but later on the technique evolved to compute the
   The average calculation makes the weights normalized                     winning arguments by removing all the lowest arguments
between 1  wavg  5, which makes them comparable.                          until the winner is left.
   Another normalization method is based on the qualitative                    This technique simply starts from the argument with the
nature of the computerized argument Delphi method, where                    lowest rating and then deletes it from the system. One impor-
the weights between nodes are considered as positive and                    tant issue during the deletion of any argument is removing
negative. For example, a rating of 1 means the contributor                  all the ratings from the first argument to other arguments.
does not share the idea of the argument or else the contributor             This means that when an argument is removed, all connected
is against the argument. From this point of view, an average                arguments are affected and there is a possibility of changing
edge weight can be calculated and the path weights can be                   the second lowest argument.
normalized by the edge weight average. The edge weight                         The technique keeps running until the desired top k argu-
average can be calculated as in equation (11):                              ments are left in the system. Some possibilities during the
             n                                                              deletion of arguments from the system are demonstrated over
             X w (ei )
eavg (G) =               ,     where        n = |G| and ei 2 E       (11)   the graph visualization.
                     n                                                         The degree of each node is already calculated in the
             ,i=0
                                                                            ‘‘sort and rate’’ approach as below:
   During the calculation of eavg the approach is slightly
different than the calculation of wavg (P) and the average is                   deg(A1 ) = 5,     deg(A2 ) = 3.25,        deg(A3 ) = 3.66,
calculated via all the edges instead of the edges of the path                   deg(A4 ) = 4,     deg(A5 ) = 3.5,         deg(A6 ) = 4.5,
as in equation (11). After calculating the average weight in                    deg(A7 ) = 1
graph G, the path weights can be normalized as demonstrated                    From the list, the lowest degree is A7 with 1 and the second
below in formula (12):                                                      lowest is A2 with 3.25. The removal of the lowest node A7 is
                               k 1
                               X                                            demonstrated in figure 9:
                    wa (P) =         w (ei )    eavg                 (12)      The removal of node A7 triggers the removal of the edges
                               i=0                                          from this node and also the edges connecting to this node.

374                                                                                                                                  VOLUME 3, 2015
S. E. Seker: Computerized Argument Delphi Technique




FIGURE 9. Removal of an argument from argument graph.                   FIGURE 10. Prediction values together with the arguments.

After the removal, the averages are recalculated and the
degrees are as shown below:                                                The ratings between opposite camps are signed negatively
                                                                        and the rating values are calculated by the degree equation
        deg(A1 ) = 1,       deg(A2 ) = 3,        deg(A3 ) = 3,          given in the ‘‘sort and rate’’ approach. The updated graph with
        deg(A4 ) = 1,       deg(A5 ) = 2,        deg(A6 ) = 1           the signs is also demonstrated in figure 11:
   Previously the lowest second node was A2 with 3.25,
but after the removal of node A7 the lowest nodes are
A1 , A4 and A6 . After the removal of these three nodes, the
graph will end up with only the A2 , A3 and A5 arguments.
Using the ‘‘leave lowest out’’ technique, those three nodes
can be declared the winning arguments.
   The final technique proposed in this study is the
‘‘two camps approach’’. In this approach, the arguments are
divided into two camps according to their approach to the
prediction. One camp has arguments below the average and
the other camp has arguments above the average. The
‘‘two camps approach’’ divides these arguments into
two camps from this respect and assumes the opposite camps
                                                                        FIGURE 11. Updated weights by the predictions.
will rate these arguments negatively. On the other hand,
supporting arguments from the same camp would be expected                  Updated degree values are: deg(A1 ) = 5, deg(A2 ) = 3,
to be high.                                                             deg(A3 ) =          3, deg(A4 ) = 0, deg(A5 ) = 2.16,
   The application of the ‘‘two camps approach’’ to the sam-            deg(A6 ) = 4.5, deg(A7 ) = 1.
ple graph G1, requires the calculation of difference from the              From the above list, the highest three arguments are
prediction and the average of predictions. The calculation              A1 , A4 and A5, rather than arguments A4 , A5 and A6 as seen
of prediction differences for each argument is calculated by            in the classical ‘‘sort and rate’’ approach.
equation 13:
                      diff (A) = Pavg       PA                   (13)   V. CRITIQUE OF COMPUTERIZED ARGUMENT DELPHI
                                                                        This section prepares for criticism of the computerized
   In order to calculate the differences, the prediction values         argument Delphi method. Advantages, disadvantages, weak-
are given as below in sample graph G1 .                                 nesses and strengths of the method will be discussed along
   Values on the nodes of figure 10 indicate the prediction             with the problems and proposed solutions faced during the
values by the contributor of the same argument. The aver-               creation of the method. This section is organized as follows:
age prediction value of the argument graph in figure 10                    1. Properties, strengths and weaknesses of the computer-
is 66.25. The difference for each node can be listed as:                      ized argument Delphi method
diff(A1 ) = 16.25, diff(A2 ) = 3.75, diff(A3 ) = 13.75,                    2. First come gets higher attention
diff(A4 ) = 21.25, diff(A5 ) = 8.75, diff(A6 ) = 1.25,                     3. Dirty data
diff(A7 ) = 1.25, diff(A8 ) = 3.75.                                     Besides the above problems, it is possible to apply any
   From the list of differences, the arguments can be divided           graph analysis technique like Page Rank [33], modularity,
into 2 camps—positive and negative—and the camps can be                 HITS [34], Eigen Vector Centrality [35], etc. These
grouped as below:                                                       techniques are already included in the literature and details
   Positive camp: A2 , A3 , A5 , A8                                     will not be covered in this paper. However, their applications
   Negative camp: A1 , A4 , A6 , A7                                     will be covered in the real problem in section 5.

VOLUME 3, 2015                                                                                                                      375
                                                                                      S. E. Seker: Computerized Argument Delphi Technique




A. STRENGTHS AND WEAKNESSES OF THE                                       • Role of facilitator: In the traditional Delphi method,
COMPUTERIZED ARGUMENT DELPHI METHOD                                the facilitator has three basic roles, which are creation of the
The computerized version of argument Delphi can be                 initial question, aggregation of predictions/arguments, and
discussed based on the following aspects:                          deciding when to finish. All three roles also apply for the
      • Anonymity: In the traditional Delphi method, the           computerized version of argument Delphi. Furthermore, the
identity of the expert is not revealed. The method is use-         computerized version gives the possibility of automatizing
ful for environments where identities can be kept secret,          the jobs of the facilitator. For example, the aggregation of
like social media or web pages. During the development             arguments can be done automatically via one of the aggrega-
of the computerized argument Delphi method, because                tion methods proposed in section 2.2 of this paper. In addition,
of several problems faced, a few different variations are          the finishing condition is no longer required in computerized
studied. First, the computerized argument Delphi method            version, since the results can be collected at any time because
has two alternatives from the perspective of anonymity and         of its continuous behavior model.
authentication.
        Anonymized Identity                                        B. FIRST COME GETS HIGHER ATTENTION
        Authorized Identity                                        One major problem about the computerized argument Delphi
   In the anonymized version, the users are not required to        method is the aspect of ‘‘first come gets higher attention,’’
login into the system. Each user has only one opportunity          which means the first arguments in the system will be
to get involved in the system and they simply contribute           displayed more than the last-entered arguments if the
by adding a new argument about the system and rating the           arguments are truly displayed with a fair random gener-
three previous arguments already in the system. Users are          ator. The reason is because each time an expert rates an
not able to update their previous answers, but they can get        argument, he will rate the arguments that have previ-
involved in the system multiple times and affect the final         ously been entered. Obviously the first-entered argument
results of the system.                                             will have a chance to be displayed for all the ratings; on
   In the authorized identity version, users can access the        the other hand a fresh, newly-entered argument will never
system through an authorization such as a username/password        be rated.
or other credential like Facebook login, Twitter login, etc.          The directed acyclic feature of the argument graph is also
After they get into the system, they are able to contribute,       one of the major impacts of the computerized argument
similar to the anonymized version. They are free to rate any       Delphi method, so the solution proposed is using an unfair
number of arguments that have previously been entered into         random generator on the behalf of newly entered arguments.
the system. They can come back and update their opinions at        This solution both keeps the argument graph acyclic and at
any time.                                                          the same time gives a higher probability to the less-rated
      • Structured flow of information: The steps, involvement     arguments.
of moderation, role of experts and limitations are                    The random generator algorithm has been modified
well-defined. This also reduces the negative group effects of      as a weighted random generator, where the last-entered
face-to-face discussions. From this perspective, the method        arguments have a higher possibility to be picked up for
can be applied only if the information flow, roles and steps to    rating.
the final output are well defined. In the computerized version
of argument Delphi, the contributors can even be from all                                  Prob (Ai ) = i                           (14)
around the world and they can be far away from face-to-face
communication.                                                       In equation (14), i is the index of argument A and prob
      • Regular Feedback: Because the identities of the            function returns the probability of the argument to be picked
contributors are hidden, the arguments of contributors are         up for the next rating.
isolated from their identity. This isolation has the advan-
tage of allowing contributors to revise their opinions at any      C. DIRTY DATA
time. The Delphi method prevents this negative effect and          One major problem during the evaluation of the argument
allows contributors to revise their opinions at any time. This     graph is the effect of spam, errors, and unrelated argu-
option is also available in the computerized version of the        ments. Because the computerized argument Delphi is mainly
argument Delphi method through two possibilities. In the           designed for crowd sourcing, the possibility of abuse or
public version of the computerized Delphi method, where            unrelated entrance is always possible. During the study, the
there is no authentication required, users can contribute to the   problem has been solved by two approaches. Initially all
argument graph many times to affect the map multiple times         the arguments are moderated and if any unrelated argument
with multiple aspects. On the other hand, the private version      is entered into the system, it is removed by the moderation.
of the computerized argument Delphi method allows the              Unfortunately, the increased number of participants makes
moderator to assign authentication for the contributors and        this approach ineffective. Instead, another solution is applied
allow them to get involved in the system only a limited            by putting a report button next to the argument ratings.
number of times.                                                   In this way any participant can mark an argument as
376                                                                                                                        VOLUME 3, 2015
S. E. Seker: Computerized Argument Delphi Technique




unrelated and this argument is then directly reported for
moderation.
   The removal of unrelated arguments also brings other
problems. The first problem is arguments without weights
since each time an argument is added into the argument
graph, the last added argument has no chance to get a weight.
Also there is a chance of having other arguments not rated
yet, because the last added argument is selecting 3 random
arguments from the argument graph and during the selection
there is a possibility of not selecting the one most recently
added, which means this previously added argument also has
no rating.
   As a solution, the unrated arguments are accepted at an
average weight. Another solution might be getting them as
zero but in this case the removal would start from the most        FIGURE 12. First Page of the Web Application.
recently added node and all the nodes would be removed in
the reverse order of addition.                                        In the second step, the user is asked to argue about his
   Also, one problem during the removal of the arguments           position. He can either be in the negative or the positive camp,
with the lowest ratings is the possibility of an argument with     as in figure 13.
no rating in the middle of the graph. This can happen if all the
nodes connected to this argument are removed. Again, one
solution for this problem is to consider the average weight of
the argument.
   While removing the argument, the argument ratings from
the same participant should also be deleted. This problem          FIGURE 13. Screenshot of the Second Step.
was the motivation behind the ‘‘leave lowest out’’ method
explained above in section 3.                                         Finally, the contributor is asked to rate three randomly
                                                                   selected previous entries, as in figure 14. Finally all data is
                                                                   stored in the database, which can be reported from the admin
VI. REAL PROBLEM: PREDICTION OF
                                                                   interface, as shown in figure 15.
PETROLEUM PRICES
After the definition of the problem and first time solutions
to the computerization of the argument Delphi method, the
method is applied to a real-life prediction problem. For
the problem, a web page is coded and the link is shared
on social networks. Within a few minutes, more than
100 contributors reply with feedback. It takes about 1 minute
to 5 minutes for a contributor to get involved with the
prediction. After removing the dirty data like unfinished
                                                                   FIGURE 14. Final Rating Step of the Application.
attempts or null entries, only 63 of them are accepted as clean
data. The scenario generated for test purposes was arguing
about predicting petroleum prices. Computerized argument
Delphi has successfully transformed all 63 of these arguments
into an argument graph. After the transformation into a graph,
it is now possible to apply classical graph metrics to
this data.

A. WEB INTERFACE
The web interface of computerized argument Delphi is imple-
mented with PHP/MySQL technologies. The web page has
three phases as previously covered in section 2.3, and screen      FIGURE 15. Screenshot of the Administrator Interface.
shots are given in figure 12.
   Initially, the user is informed of the petroleum prices since   B. GRAPH DEMONSTRATION
2001 and asked for a prediction for the end of 2014. The user      The data collected from users are visualized in a graph as
can enter his prediction in the text box at the end of the page    shown in figure 16. The graph is weighted and the thickness
as shown in figure 12.                                             of the edges indicates the weight of the edge from 1 to 5.

VOLUME 3, 2015                                                                                                                 377
                                                                                 S. E. Seker: Computerized Argument Delphi Technique




      FIGURE 16. Graph Visualization for Petroleum Prediction.



In addition each node is randomly distributed on the graph       Two groups of approaches will be covered in this paper.
by the visualization software yED [36].                          The first group of approaches in this study is for under-
  After converting the arguments from the contributors into      standing the features of the graph and classical graph
a graph, it is possible to make a graph-based analysis.          analysis methods will be applied. The second group of

378                                                                                                                   VOLUME 3, 2015
S. E. Seker: Computerized Argument Delphi Technique




      FIGURE 17. Graph Metrics of Case Study.


graph analysis approaches includes the novel approaches            VII. CONCLUSION
proposed for the computerized argument Delphi method               This study is first time a computerized version of argument
in this paper.                                                     Delphi—a variant of policy Delphi—has been proposed.
                                                                   The technique is developed for several alternative cases
                                                                   and the problems faced during the application of the
C. GRAPH METRICS
                                                                   method to real life problems and solutions are proposed
After successfully converting all clean argument entries into      and applied. This novel version of the Delphi technique
a graph with the argument ratings, the graph metrics are           can be applied to many environments, including Web 3.0,
collected as shown in figure 17.                                   like social networks, web platforms, blogs, forums and
   Metrics of the graph are calculated using Gephi [37]            wikis [40].
software. Figure 17-(a) indicates the Hubs Distribution,              Besides the proposed processing techniques on the argu-
which is also known as hyper-link induced topic                    ment graph, introduced for the first time during the process of
search (HITS) [34]. Initially an algorithm is generated to         the computerized argument Delphi method, it is believed that
calculate the impact of journal articles or web pages by           the graph model of argument Delphi will be an acceleration
considering their incoming and outgoing links. For the HUBS        of current studies and it is open for further studies of graph
distribution, each node starts with a score value of 1 and         theory, statistics and social sciences.
the number of links are considered with the weights of their          One natural outcome of the real-life problems yielded
incoming links. The algorithm calculates the total score via       40 alternative implementations of the computerized argument
the outgoing links by considering the incoming links.              Delphi method as a variation of authorized/unauthorized
So the importance of the node is considered to be higher if the    versions or argument aggregation by ‘‘list of arguments’’,
score is increased [34]. Similar to the Hubs Distribution, page    ‘‘drop similar’’, ‘‘tournament selection’’ or ‘‘use qualitative
rank in figure 17-(c) is originally developed for calculating      marginal’’ or the evaluation of arguments by ‘‘sort and rate’’,
the impact of the web pages by using Google [33]. Again,           ‘‘propagated path sort’’, ‘‘average propagation sort’’, ‘‘leave
the higher page rank means a higher impact of a web page           lowest out’’ or ‘‘two camps approach’’. All these methods
or node value in the argument graph. After converting the          of computerized argument Delphi are here introduced into
Delphi arguments into an argument graph, now it is possible        the literature for the first time. In addition, the number of
to apply a citation impact or web impact algorithm over the        arguments in each step or the final step is left parametric for
algorithms. Arguments also can be queried via these impact         the facilitator.
algorithms.
   Besides the classical graph metrics like degree distribution,
degree of nodes [38] as shown in figure 17-(f), Eigen vector       REFERENCES
Centrality Distribution [35] as shown in figure 17-(d), and        [1] N. Dalkey and O. Helmer, ‘‘An experimental application of the DELPHI
                                                                       method to the use of experts,’’ Manage. Sci., vol. 9, no. 3, pp. 458–467,
eccentricity distribution [39] as shown in figure 17-(e) can           Apr. 1963.
easily be applied to the arguments gathered from                   [2] H. A. Linstone and M. Turoff, The Delphi Method: Techniques and
computerized argument Delphi.                                          Applications. Reading, MA, USA: Addison-Wesley, 1975.

VOLUME 3, 2015                                                                                                                              379
                                                                                                           S. E. Seker: Computerized Argument Delphi Technique




 [3] R. L. Custer, J. A. Scarcella, and B. R. Stewart, ‘‘The modified Delphi       [25] S. E. Seker and K. Al-Naami, ‘‘Sentimental analysis on Turkish blogs via
     technique—A rotational modification,’’ J. Vocational Tech. Edu., vol. 15,          ensemble classifier,’’ in Proc. Int. Conf. Data Mining, 2013, pp. 10–16.
     no. 2, pp. 50–58, 1999.                                                       [26] S. E. Seker, ‘‘Sentimental versus impact of blogs,’’ in Proc. Int. Conf.
 [4] G. D. Garson, The Delphi Method in Quantitative Research (Statistical              Internet Comput. Big Data (ICOMP), 2013, pp. 127–133.
     Associates ‘Blue Book’ Series Book), vol. 44. Asheboro, NC, USA:              [27] G. W. F. Hegel, F. H. Simon, and T. Rockmore, Hegel’s Lectures on the
     Statistical Associates Publishers, 2013.                                           History of Philosophy. Amherst, NY, USA: Prometheus Books, 1996.
 [5] S. Keeney, H. McKenna, and F. Hasson, The Delphi Technique in Nursing         [28] S. E. Seker, O. Altun, U. Ayan, and C. Mert, ‘‘A novel string distance
     and Health Research. New York, NY, USA: Wiley, 2011.                               function based on most frequent K characters,’’ Int. J. Mach. Learn.
 [6] R. J. Heuer, Jr., and R. H. Pherson, Structured Analytic Techniques for            Comput., vol. 4, no. 2, pp. 177–183, 2014.
     Intelligence Analysis. Washington, DC, USA: CQ Press, 2014.                   [29] S. E. Seker and C. Mert, ‘‘A novel feature hashing for text mining,’’ J. Tech.
 [7] B. K. Eakman, How to Counter Group Manipulation Tactics: The Tech-                 Sci. Technol., vol. 2, no. 1, pp. 37–40, Jun. 2013.
     niques of Unethical Consensus-Building Unmasked. Raleigh, NC, USA:            [30] B. L. Miller and D. E. Goldberg, ‘‘Genetic algorithms, tournament selec-
     CreateSpace Independent Publishing Platform, 2003.                                 tion, and the effects of noise,’’ Complex Syst., vol. 9, no. 3, pp. 193–212,
 [8] M. I. Yousuf, ‘‘The Delphi technique,’’ Essays Edu., vol. 20, pp. 80–89,           1995.
     2007.                                                                         [31] B. Satyanarayana and K. S. Prasad, Discrete Mathematics and Graph
 [9] W. G. Rieger, ‘‘Directions in Delphi developments: Dissertations and their         Theory. Cambridge, MA, USA: PHI Learning Pvt. Ltd., 2006.
     quality,’’ Technol. Forecasting Social Change, vol. 29, no. 2, pp. 195–204,   [32] W. McCuaig, ‘‘Intercyclic digraphs,’’ in Proc. AMS-IMS-SIAM Joint
     Apr. 1986.                                                                         Summer Res. Conf. Graph Minors Graph Struct. Theory, 1992, p. 205.
[10] D. Gallego and S. Bueno, ‘‘Exploring the application of the Delphi method          [Online]. Available: http://books.google.com/books?id=idigH5CTGWAC
     as a forecasting tool in information systems and technologies research,’’          &pg=PA205
     Technol. Anal. Strategic Manage., vol. 26, no. 9, pp. 987–999, Jul. 2014.     [33] S. Brin and L. Page, ‘‘The anatomy of a large-scale hypertextual
[11] K. Kauko and P. Palmroos, ‘‘The Delphi method in forecasting financial             Web search engine,’’ in Proc. 7th Int. Conf. World Wide Web, 1998,
     markets—An experimental study,’’ Int. J. Forecasting, vol. 30, no. 2,              pp. 107–117.
     pp. 313–327, Jun. 2014.                                                       [34] J. Kleinberg, ‘‘Authoritative sources in a hyperlinked environment,’’
[12] M. Adler and E. Ziglio, Eds., Gazing Into the Oracle: The Delphi Method            J. ACM, vol. 46, no. 5, pp. 604–632, Sep. 1999.
     and Its Application to Social Policy and Public Health. London, U.K.:         [35] K. Bryan and T. Leise, ‘‘The $25,000,000,000 eigenvector: The linear
     Jessica Kingsley Publishers, 1996.                                                 algebra behind Google,’’ SIAM Rev., vol. 48, no. 3, pp. 569–581, 2006.
[13] R. D. Needham and R. C. de Loë, ‘‘The policy Delphi: Purpose, structure,      [36] G. Ertek and A. Demiriz, ‘‘A framework for visualizing association mining
     and application,’’ Can. Geographer, vol. 34, no. 2, pp. 133–142, Jun. 1990.        results,’’ in Computer and Information Sciences—ISCIS (Lecture Notes in
[14] C. L. Paul, ‘‘A modified Delphi approach to a new card sorting methodol-           Computer Science), vol. 4263. Berlin, Germany: Springer-Verlag, 2006,
     ogy,’’ J. Usability Stud., vol. 4, no. 1, pp. 7–30, Nov. 2008.                     pp. 593–602.
[15] M. Turoff and S. R. Hiltz, ‘‘Computer based Delphi processes,’’ in            [37] M. Bastian, S. Heymann, and M. Jacomy, ‘‘Gephi: An open source soft-
     Gazing Into the Oracle: The Delphi Method and Its Application to Social            ware for exploring and manipulating networks,’’ in Proc. 3rd Int. AAAI
     Policy and Public Health, M. Adler and E. Ziglio, Eds. London, U.K.:               Conf. Weblogs Social Media AAAI Pub., 2009, pp. 361–362.
     Jessica Kingsley Publishers, 1996, pp. 56–88.                                 [38] R. Diestel, Graph Theory, 3rd ed. New York, NY, USA: Springer-Verlag,
[16] O. Kuusi, Expertise in the Future Use of Generic Technologies: Epistemic           2005.
     and Methodological Considerations Concerning Delphi Studies. Helsinki,        [39] F. W. Takes and W. A. Kosters, ‘‘Computing the eccentricity distribution
     Finland: Unigrafia Bookstore, 1999.                                                of large graphs,’’ Algorithms, vol. 6, no. 1, pp. 100–118, 2013.
[17] K. Korhonen-Yrjänheikki, ‘‘Using argument Delphi to anticipate                [40] M. L. Arslan, S. E. Seker, and C. Kızıl, ‘‘Innovation driven emerging
     the challenges of engineering education in a systematic way: Case                  technology from two contrary perspectives: A case study of Internet,’’
     Finland 2015,’’ in Proc. SEFI Annu. Conf. , Valencia, Spain, 2004,                 Emerg. Markets J., vol. 3, no. 3, pp. 87–97, Mar. 2014.
     pp. 221–227.
[18] S. E. Seker, C. Mert, K. Al-Naami, N. Ozalp, and U. Ayan, ‘‘Time series
     analysis on stock market for text mining correlation of economy news,’’
     Int. J. Soc. Sci. Humanity Stud., vol. 6, no. 1, pp. 66–91, 2013.
[19] S. E. Seker, K. Al-Naami, and L. Khan, ‘‘Author attribution on streaming
     data,’’ in Proc. IEEE 14th Int. Conf. Inf. Reuse Integr. (IRI), Aug. 2013,
     pp. 497–503.
[20] R. Loo, ‘‘The Delphi method: A powerful tool for strategic management,’’                                SADI EVREN SEKER (M’01) received the
     Policing, Int. J. Police Strategies Manage., vol. 25, no. 4, pp. 762–769,                               B.Sc., M.Sc., and Ph.D. degrees from the Com-
     2002.                                                                                                   puter Science and Engineering Department.
[21] A. R. McMurray, ‘‘Three decision-making aids: Brainstorming, nominal                                    He was a Post-Doctoral Researcher in streaming
     group, and Delphi technique,’’ J. Nursing Staff Develop., vol. 10, no. 2,
                                                                                                             data mining and social networks with the
     pp. 62–65, Mar./Apr. 1994.
[22] A. M. Kaplan and M. Haenlein, ‘‘Users of the world, unite! The chal-
                                                                                                             Computer Science Department, University of
     lenges and opportunities of social media,’’ Bus. Horizons, vol. 53, no. 1,                              Texas at Dallas. He has studied in natural language
     pp. 59–68, Jan./Feb. 2010.                                                                              processing and artificial intelligence subjects dur-
[23] S. Yardi and D. Boyd, ‘‘Dynamic debates: An analysis of group polar-                                    ing his education. He is currently an Academic
     ization over time on Twitter,’’ Bull. Sci. Technol. Soc., vol. 30, no. 5,                               Staff with the Management Information System
     pp. 316–327, Oct. 2010.                                                       Major Program, Business Department, Istanbul Medeniyet University. He
[24] D. A. Shamma, L. Kennedy, and E. F. Churchill, ‘‘Tweet the debates:           has authored numerous peer-reviewed papers, books, and patents. His active
     Understanding community annotation of uncollected sources,’’ in Proc. 1st     research topics are business intelligence, data mining, and social networks.
     SIGMM Workshop Social Media (WSM), Beijing, China, 2009, pp. 3–10.




380                                                                                                                                                   VOLUME 3, 2015
