---
title: Maths
published: true
---

## Variability

### For Symbols

use Entropy or Gini

#### For Numerics

use Standard Deviation

## CDF

### Natural Range

## Expected Value

## Argmax

## Argmin

### Ranking

### Supervised Ranking

## Success metrics

### For Symbol

Accuracy, precision, recall, false alarm, AUC, Popt, etc

### For Numerics

RE, MRE, medMRE, MMRE, SA, etc

## Distance

Metrics space

    d(x,y) >= 0
    d(x,x) = 0
    d(x,y) = d(y,x)
    d(x,z) <= d(x,y) + d(y,z)

E.g. the discrete (symbolic) metric

    d(x,y) = 0 if x==y else 1

E.g. Euclidean metric

    d(x,y) = sqrt( sum( square( x[i] - y[i] )))

E.g. Minkowski metric (at n=1,2 this becomes Manhatten, Euclidean metric)

    d(x,y) = sum(  ( x[i] - y[i] )^n )^(1/n)

Max distance across a hypercube

Normalized distance

Projections, cosine rule
- note, now N dimensions are one.

## Better(s)

Boolean domination
- fine for low dimensions.
- not so good for higher (graphic from abdel's paper)

Indicator domination (also called continuous domination).

## Equality

For single values, easy!

But when comapring sets of numbers, must study set overlap (something studies extensively in statistics).

Bayesian

- Given M rows divided into C classes, a new row is "closest" to the class that "likes" it most.
- A row "_x_" is "likely" to belong to a class at probaility given by Bayes theorem
 
    new       = now    * past
    like(C|x) = P(x|C) * P(C)

(Those familar with Bayes theorem will note a missing term: P(x). If we only ever report
that ratios of `like` in different classes then this term always cancels out. So we can ignore it.)

e.g. in the following, we have two classes `yes` and `no`
where `P(yes) = 9/14` and `P(no) = 5/14`.

     outlook  temperature  humidity   windy   play
     -------  -----------  --------   -----   ----
     rainy    cool        normal    TRUE    no
     rainy    mild        high      TRUE    no
     sunny    hot         high      FALSE   no
     sunny    hot         high      TRUE    no
     sunny    mild        high      FALSE   no
     overcast cool        normal    TRUE    yes
     overcast hot         high      FALSE   yes
     overcast hot         normal    FALSE   yes
     overcast mild        high      TRUE    yes
     rainy    cool        normal    FALSE   yes
     rainy    mild        high      FALSE   yes
     rainy    mild        normal    FALSE   yes
     sunny    cool        normal    FALSE   yes
     sunny    mild        normal    TRUE    yes%%
 
This data can be summarized as follows:

               Outlook            Temperature           Humidity
    ====================   =================   =================
              Yes    No            Yes   No            Yes    No
    Sunny       2     3     Hot     2     2    High      3     4
    Overcast    4     0     Mild    4     2    Normal    6     1
    Rainy       3     2     Cool    3     1
              -----------         ---------            ----------
    Sunny     2/9   3/5     Hot   2/9   2/5    High    3/9   4/5
    Overcast  4/9   0/5     Mild  4/9   2/5    Normal  6/9   1/5
    Rainy     3/9   2/5     Cool  3/9   1/5
    
                Windy        Play
    =================    ========
          Yes     No     Yes   No
    False 6      2       9     5
    True  3      3
          ----------   ----------
    False  6/9    2/5   9/14  5/14
    True   3/9    3/5

So, what happens on a new day:

         Outlook       Temp.         Humidity    Windy         Play
         =======       =====        =========    =====         ====
    x =  Sunny         Cool          High        True          ?%%

First find the likelihood of the two classes

    like(yes|x) =  2/9 * 3/9 * 3/9 * 3/9 * 9/14 = 0.0053
    like(no |x) = 3/5 * 1/5 * 4/5 * 3/5 * 5/14 = 0.0206

Note that we `like` "yes" much more than we like "no".

