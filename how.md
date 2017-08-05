
---
title: How
published: true
---

- _Errāre hūmānum est._  (To err is human.)   
  -- Anonomous Latin person.
- _If a little knowledge is dangerous, where is the man (sic) who has so much as to be out of danger_?  
  -- T.H. Huxley
- <em>We are all fallible, and prone to error; let us then
  pardon each other's folly. This is the first principle of natural right. </em> 
  -- Voltaire.

Consider an operating system that can schedule processes, but has
no editors, compilers, file system, network support, ports, memory
management, gui, etc. Would you use that operating?

Now consider a data repository used by scientists stored data and
code in order to repeat/ confirm/ improve or even refute old results.
I think such repositories should do more than just support setting
and getting data, with (perhaps) some limited search interface. I
want my data repositories to be forums within which communitie can
curate, critique and even improve the conclusions drawn from data.

What would that extra layer of tools look like? 

Science has escaped the lab 
and    roaming free in the world.


These days,
anyone can be a scientist (making generalizations from data)  by
just downloading a data mining toolkit, and running it over some data.

Now science is not just a way to build models, it is a way to evaluate
those models as well. Much of my work as a "sciencetist" is reviewing
papers, proposals, and the ideas of my colleagues.
So I say
it should be possible to audit the conclusions generated
in that way.
I 
want to  mistrust the conclusions of citizen scientists in
much the same way as I mustrust
ane explore , review, explore, evolve the conclusions of any other scientist. 



These days, anyone can act like a scientist- grab a data miner and build a model from data. But
should we trust the recommendations that come from such models? There are many examples of
people using data mining to arrive at misleading
conclusions or using models the wrong way (see Ekrem13](http://menzies.us/pdf/13distributed.pdf),  [Crateri13](https://ocw.mit.edu/courses/engineering-systems-division/esd-864-modeling-and-assessment-for-policy-spring-2013/projects/student-work/MITESD_864S13_NASA_Colbia.pdf)).

Standard scientific 
to generate bad models

Consider a table of data with rows and columns.
Let some rows be numeric and some symbolic 

- Numebrs are things we can add and sort. 
- Symbols are things we can only test for equal or not equal.

Some columns are independent variables and some are dependend

- Task: find combinations of the independent to predict values in the dependent.
- Prediction = there is onyl one dependent variable, and we have to guess what it might be:
   - Classification = one symbolic dependent variable. 
   - Regression = one numeric depedent variable
- Optimization =  N numeric dependents and we see ways to maximize, minize those values
   - Multi-objective optimization = N > 1
   - Many-objective optimization = N > 5


Somehow, cluster the rows into a dendogram (a tree of clusters and sub-clusters, etc).

For each leaf cluster, build a predictor (e.g. majority class or medium score in that leaf).

Feature selection

Instance selection
