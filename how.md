
---
title: How
published: true
---

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
