---
title: Homeworks
published: true
---

## Goal

To learn enough about data miners so that you can mash up your own, in creative ways.

There are two paths to this.

- For a _few_ number of students, I invite you to learn LUA and help me retire the open issues for
  my LUA LURE system. This will be an open ended set of very different tasks. 
- For _most_ students, you will NOT be coding in LUA
    - Rather, you will treat the LUA code as a specification
    - That you will recode in Python, Ruby, JAVA (not recommended) etc.

###  Path1: Pure LUA (for a few of you)


Aug29: 

- Port https://gist.github.com/jasonkeene/2140276 to LUA
- Add command line arguments to control size of display
- Add a command line argument to randomly set each cell to be alive on pop0 at probability `p`.
- Add a subdirectory contain a set of some patterns (so at the command line you can
  "start with this pattern file"
- See if you can duplicate the behavior of 
     - http://conwaylife.appspot.com/pattern/cap
     - http://conwaylife.appspot.com/pattern/cheptomino
     - http://conwaylife.appspot.com/pattern/achimsp8

Sept12, Sept19, Sept26, Oct5

- Fork the Lualure github repo
- Discuss the [open issues](https://github.com/lualure/src/issues) with the lecturer
  adn get some assigned to you.
- Each week, close some issues.
- Repeat, four times.

There exist numerous open task needed for my group size	code 1: Aug29	code 2: sept12	code 3: Sept19	code 4: Sept 26	code 5: Oct5

### Path2: Un-LUA-ed (for most of you)

Your task is to generate the  (e) the contrast sets between (d) the regression  trees learned
from (c) discretized data (supervised, of course) taken from (b) a table of data read from
(a) comma-separated
data.

Note that such contrast sets satisfy many of the demands of this subject. They  are
succinct (human readable) and  context-aware. The results are highly actionable (since
they tell you how much or little you need to do to achieve some goal). So by coding this,
you are building something that very few other people on the planet can access.
Go WolfPack!


In any case, your task is to deliver (abcde) on 
(a) Aug29, (b) Sept12, (c) Sept19, (d) Sept26 and (e) Oct5.
Notes on those tasks are given below. Note that I mention LUA code below- but don't presume that
you will write in LUA. Just treat the LUA code as something to read and review.

#### (a) Reading CSV files

[Example LUA code](https://lualure.github.io/info/csv.html)

Given a disk file like  this:

    outlook, $temp, ?humidity, windy,>wins,<play
    sunny,85,85,FALSE,10,20
    sunny,80,90,TRUE, 12,40
    overcast,83,86,FALSE,40,40
    rainy,70,96,FALSE,40,50
    rainy,68,80,FALSE,
           50,30
    rainy,65,70,TRUE,4,10
    overcast,64,65,TRUE,30,60
    sunny,72,95,FALSE,7,20 #adsas
    sunny,69,70,FALSE,70,70
    rainy,75,80,FALSE,80,40
    sunny,75,70,TRUE,30,50
    overcast,72,90,TRUE,60,50
    overcast,81,75,FALSE,30,60
    rainy,71, 91, TRUE ,50,40

Read each line, kill whitepsace and anything after comment characters (`#`), break each line on comma,
 read rows into a list of lists (one list per row), converting strings to numbers where appropriate.
 Note that some column headers contain `?`: all such columns should be ignored. For now you can
 ignore the other magic characters in row1.

Your code should contain checks for bad lines (and bad lines should be skipped over); i.e.
symbols where numbers should be and wrong number of cells (we will
say that row1 has the "right" length).

Tests:

- Report runtimes loading in https://github.com/lualure/src/blob/master/data/POM3A.csv.
- For https://github.com/lualure/src/blob/master/data/POM3A.csv, add in many bad rows and have 
  the code print out error messages from those lines

### (b) Reading tables of data

[Example LUA code](https://lualure.github.io/info/tbl.html)

- Note that, for now, you can ignore copy, discretize, goalN,  discretizeHeaders.

Read lines from CSV files one a time incrementally updating column headers for each line.

Headers are either `Num`s or `Sym`s as determined by the magic characters in row1.

- see [Tbl](https://lualure.github.io/info/tbl.html) for details

`Num` and `Sym`s incremental  maintain knowledge about mean, standard deviation,
and symbol counts in a column. For details, see the `update` function in

- [Num](https://lualure.github.io/info/num.html)
- [Sym](https://lualure.github.io/info/sym.html)

So when the table reads row1, it builds the headers of `Num`s and `Sym`s. 
And when the other rows are read, the headers get updated.

Code up the domination counter (the `dom` function in `Tbl` which also
uses `dominate` and `dominate1` in 
[Row](https://lualure.github.io/info/Row.html)

Test: Find and print the top and bottom ten rows of
https://github.com/lualure/src/blob/master/data/auto.csv, as sorted
by their `dom` score. with the top 5 and the bottom 5 domination
scores.  That print out will look something like this (you dont'
need to emulate this, just get the same info):

    {"cylinders", "$displacement", "$horsepower", "<weight", ">acceleration", "$model", "origin", ">mpg"}
    {cells= {4, 97, 52, 2130, 24.6, 82, 2, 40}, id= 2189}
    {cells= {4, 90, 48, 2335, 23.7, 80, 2, 40}, id= 2188}
    {cells= {4, 86, 65, 2110, 17.9, 80, 3, 50}, id= 2192}
    {cells= {4, 90, 48, 1985, 21.5, 78, 2, 40}, id= 2187}
    {cells= {4, 90, 48, 2085, 21.7, 80, 2, 40}, id= 2190}
    
    {cells= {8, 454, 220, 4354, 9, 70, 1, 10}, id= 1828}
    {cells= {8, 440, 215, 4312, 8.5, 70, 1, 10}, id= 1829}
    {cells= {8, 429, 198, 4952, 11.5, 73, 1, 10}, id= 1804}
    {cells= {8, 383, 180, 4955, 11.5, 71, 1, 10}, id= 1802}
    {cells= {8, 400, 175, 5140, 12, 71, 1, 10}, id= 1809}
    {cells= {8, 455, 225, 4951, 11, 73, 1, 10}, id= 1805}

Note in the above that the first thing printed is the first row of `auto.csv`. This tells us that we want to minimize column4
and maximize columns 5,6. Note also that the above print shows that our sort worked: we see smaller _displacements_ and large _horsepower_
and _mpg_ in the
first 5.


### (c) Discretization

Example LUA code:

- unsupervised Discretization: https://lualure.github.io/info/range
- supervised Discretization: https://lualure.github.io/info/superrange

_Unsupervised Discretization_
Write code that takes a table column of `N` numbers, sorts in, and breaks into bins of size approximately `sqrt(N)`. Note that these
breaks have to satisfy the following sanity rules:

- no range contains too few numbers (`sqrt(N)`);
- each range is different to the next one by some _epsilon_  value (0.2 * standard deviation of that column);
-  the span of the range (hi - lo) is greater than that _epsilon_;
- the lo value of one range is greater than than the hi value of the previous range

_Supervised Discretization_
Write code that reflects over the ranges found by the unsupervised
discretizer. Combine ranges where some dependent variable is not
changed across that combination of ranges. Specifically, sort the ranges
and do a recursive descent of the ranges. At each level of the recursion,
break the ranges at the point that most minimizes the expected value of the standard deviation
of the dependent variable. 

Tests: see [this
code](https://github.com/lualure/src/blob/master/lib/superrangeok.lua).
Note the function _klass_ that generates numbers around 50 `x`
numbers and 50 associated `y` numbers around 0.2, 0.6, and .9. Print
the unsupervised and supervised ranges, as follows.
My results for that test are shown below (and note
your results 
results may be very different, depending on your random number
generator). But the key thing is that there are far fewer supervised than unsupervised ranges.

    We have many unsupervised ranges.
    x	1	{span= 0.19205901315066, lo= 0.0076981862111474, n= 8, hi= 0.19975719936181}
    x	2	{span= 0.081475240216346, lo= 0.23777443367884, n= 8, hi= 0.31924967389519}
    x	3	{span= 0.13579630252709, lo= 0.32823422613006, n= 8, hi= 0.46403052865715}
    x	4	{span= 0.23776082379639, lo= 0.46444582495114, n= 8, hi= 0.70220664874753}
    x	5	{span= 0.12320988398195, lo= 0.75335583498392, n= 8, hi= 0.87656571896587}
    x	6	{span= 0.11380950785885, lo= 0.88564837113286, n= 10, hi= 0.99945787899171}
    
    We have fewer supervised ranges.
    super	1	{label= 1, most= 0.19975719936181}
    super	2	{label= 2, most= 0.46403052865715}
    super	3	{label= 3, most= 0.70220664874753}
    super	4	{label= 4, most= 0.99945787899171}

### (d) Regression Trees

Example LUA code: https://lualure.github.io/info/sdtree.html

To  build a regression tree learner:
  
- Apply supervised Discretization
- At each level of the tree, break the data on the ranges and find the column whose
 breaks most reduces the variability of the target variable (we will use `dom`).
- For each break, apply the regression tree learner recursively.
- Recursion stops when the breaks do not improve the supervised target score,
  when there are `tooFew`  examples to break, or when the tree depth is too much.


Write a list printer that recurses down the tree and prints details about each node, indented
by its level in tree. 

Test: run your decision tree learner on `auto.csv`. Using `dom` and `tooFew`  is 10, the auto.csv divides into
something like this:

     in=398 mu=198.50 sd=115.04
     horsepower = 1      		:	n=21 mu=373.71 sd=17.79
     horsepower = 2      		:
     | displacement = 1  		:
     | | origin = 3      		:	n=14 mu=368.43 sd=26.26
     | displacement = 2  		:
     | | model = 7       		:	n=13 mu=342.38 sd=30.69
     horsepower = 3      		:
     | displacement = 2  		:	n=20 mu=292.60 sd=37.36
     horsepower = 4      		:
     | displacement = 3  		:	n=11 mu=264.91 sd=43.22
     | displacement = 4  		:	n=10 mu=249.10 sd=35.57
     horsepower = 5      		:
     | displacement = 2  		:	n=10 mu=270.10 sd=40.14
     | displacement = 4  		:	n=15 mu=241.53 sd=32.19
     horsepower = 6      		:
     | displacement = 3  		:
     | | origin = 3      		:	n=12 mu=210.08 sd=33.27
     | displacement = 7  		:	n=13 mu=147.62 sd=27.41
     horsepower = 7      		:
     | displacement = 6  		:	n=11 mu=137.91 sd=25.26
     horsepower = 8      		:	n=22 mu=119.50 sd=49.68
     horsepower = 9      		:
     | model = 6         		:	n=11 mu=87.36 sd=11.76
     horsepower = 10     		:	n=29 mu=52.00 sd=23.11
     horsepower = 11     		:
     | model = 3         		:	n=10 mu=18.50 sd=14.29
    
#### (e) Contrast sets

Example code: https://lualure.github.io/info/contrasts.html

Our contrast learner will examine each pair of nodes in the decision tree and report
the `delta` and `effect` between each node in a pair

- The `delta` is the difference in the branch path between each node
- The `effect` is the mean difference in the performance score those nodes

Note that if the delta is:

- positive then the contrast is a plan (something to do).
- negative then the contrast is a monitor (something to watch for).

Note also that is statistically there is no difference between the population of instances in each node,
then there is no point printing that contrast. For code to conduct those statistical tests, see `same`
  in [num](https://lualure.github.io/info/num.html).

Test:
Using auto.csv, print the plans and monitors separately. Note that for the leaves with
best scores, there should  be no plans generated. Similarly, for the leaves with worst
scores, there should be monitors generated.

