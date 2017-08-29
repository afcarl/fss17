
# Review1:  (08/21 - 08/25)

```
@relation weather

@attribute outlook {sunny, overcast, rainy}
@attribute temperature real
@attribute humidity real
@attribute windy {TRUE, FALSE}
@attribute play {yes, no}

@data
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,72,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no
```

Using the above example, answer the following:

Column types:

- What is symbolic variables? Please give 2 examples.
- What is numeric variables? Please give 2 examples.
- Name one operation that can be performed on both numeric and symbolic variables.
- Name one operation that can be performed on  numeric but not symbolic variables.
- How do you calculate the distance between symbolic variables? Please give 1 example.
- How do you calculate the distance between numeric variables? Please give 1 example.
- What is normalization? Why might it be useful?
- In the above data, normalize temperature=65, humidity=70

Independent variables:

- What is independent variable? Given an example
- What's the difference between decision tree and random forest?

Impurity

- What is the connection between variance and standard deviation?
- What is the same about variance and entropy?
- What is difference between variane and entropy? 
- How do we calculate entropy?  What is the entropy of `play?` Show your working.
- How do we calculate standard deviation? What is the standard deviation of `temperature`? Show your working.
- The Gini Index is used to compute the impurity of a data partition. It is computed as
  1 - (&sum; (p.i)^2). For example, assume the data partition D consisiting of 4 classes each with equal probability. Then the Gini Index (Gini Impurity) will be: Gini(D) = 1 - (0.25^2 + 0.25^2 + 0.25^2 + 0.25^2)
       - Is Gini defined for symbolic or number variables?

Dependent variables:

- Define a dependent variable. Given an example.
- What the difference between supervised and unsupervised learning? Please give 2 example tasks for each of them.
- In classification taskes, is the dependent variable numeric or symbolic? What about regressions?
- If there are more than one numeric class variable, what kind of problem do we have?

Decision Tree learning:

- Decision tree is often called "iterative dichomization". Why?
- In the following decision tree, `outlook` is the top split and `temperature` never appears in the tree.
  Do the following, showing all your working, and explain why:
    - calculate the entropy of the class variables in the golf data set
    - calculate the expected value of the entropy of the class symbol after splitting on `outlook`.
    - calculate the expected value of the entropy of the class symbol after splitting on `temperature`.
    - compare the three values. What can you say?

```
outlook = sunny
|   humidity = high: no (3.0)
|   humidity = normal: yes (2.0)
outlook = overcast: yes (4.0)
outlook = rainy
|   windy = TRUE: no (2.0)
|   windy = FALSE: yes (3.0)
Number of Leaves  :   5
Size of the tree :  8
```
