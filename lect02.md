---
title:  No microscope without mud
published: true
---

Data mining algorithms generate summaries of data. They are like microscopes we look through to reveal internal structure.

If a microscope has mud on the lens, what we see might be distorted. The point of this lecture is that, in data mining, all data miners have mud on them.
All the models we find are wrong, or irrelevant, or useless to some extent for some users.


worst case in quick sort:

```
function quicksort(array)
    less, equal, greater := three empty arrays
    if length(array) > 1  
        pivot := select any element of array
        for each x in array
            if x < pivot then add x to less
            if x = pivot then add x to equal
            if x > pivot then add x to greater
        quicksort(less)
        quicksort(greater)
        array := concatenate(less, equal, greater)
```

Worst case:
- The pivot evlement is always the smallest or larger
  element in the arry
  	- i.e. all elements of array are same
- Uneven partitioning (one "half" always of size 1, the
  other "half" of n-1).

General lesson:

- If you know the algorithm...
- .. you know how to pick inputs that make it smile...
- ... or make it frown

NFL= no free lunch
  -<em>We have dubbed the associated results NFL theorems because they demonstrate that if an algorithm performs well on a certain class of problems then it necessarily pays for that with degraded performance on the set of all remaining problems.</em>
  -  Wolpert, D.H., Macready, W.G. (1997), "No Free Lunch Theorems for Optimization", IEEE Transactions on Evolutionary Computation 1, 67.


From [Machine Learning Lesson of the Day, Jan 24, 2014](https://goo.gl/UWh2gK):

- A model is a simplified representation of reality, and the
simplifications are made to discard unnecessary detail and allow
us to focus on the aspect of reality that we want to understand.
These simplifications are grounded on assumptions; these assumptions
may hold in some situations, but may not hold in other situations.
This implies that a model that explains a certain situation well
may fail in another situation.  In both statistics and machine
learning, we need to check our assumptions before relying on a
model.  
- The "No Free Lunch" theorem states that there is no one
model that works best for every problem.  The assumptions of a great
model for one problem may not hold for another problem, so it is
common in machine learning to try multiple models and find one that
works best for a particular problem.  This is especially true in
supervised learning; validation or cross-validation is commonly
used to assess the predictive accuracies of multiple models of
varying complexity to find the best model.  A model that works well
could also be trained by multiple algorithms – for example, linear
regression could be trained by the normal equations or by gradient
descent.  
- Depending on the problem, it is important to assess the
trade-offs between speed, accuracy, and complexity of different
models and algorithms and find a model that works best for that
particular problem.

From ME:

- It is also important to assess the goals of the learner. If the users care about goals ABC and your algoritm is trying to
  reduce XYZ then the learner could be building a model no one cares about.
- Also, how we assess a model critically effects what model we prefer; i.e. what lessons we learn.

<img class="pure-img displayed"  src="https://github.com/txt/fss16/raw/master/img/aucRecall.png">

<img class="pure-img displayed"  src="https://github.com/txt/fss16/raw/master/img/precPf.png">

 
What are the parts of this figure?

- Boxes= data sets (velocity, synapse, art, ..)
- Rows= learners (knn, svm, nb, rf, lr, dt)
- Columns= data pre-processing treatments (no, s1, s2) 
- Stats tests= gray scale

Now, take a deep breath and consider all the choices made to generate this data...

Class exercise:

## Boxes= data ses

<img class="pure-img displayed"  src="https://github.com/txddPt/fss16/raw/master/img/ckMetrics.png">

## Data Pre-processors

- No= do nothing
- S1= SMOTE= synthetic minority over-sampling
     - One way to handle class imbalance
     - Many other ways, see [here](http://ieeexplore.ieee.org/document/5128907/)
- S2= SMOTUNED. An NCSU special that automatically learns best control parameters for SMOTE. See [here](https://arxiv.org/pdf/1705.03697.pdf).

<img class="pure-img displayed"  src="https://github.com/txddPt/fss16/raw/master/img/smote.png">

## Learners

- For all the learners knn, svm, nb, rf, lr, dt
      - write 2 lines describe the algorithm
      - write down some of the control parameters of that algorithm
      - For those doing KNN (kth nearest neighbor), please see [here](http://menzies.us/pdf/11teak.pdf), section 2.5
      - For those doing RF (random forests) and dt (decision trees) please see [here](https://arxiv.org/pdf/1609.01759.pdf) table2.
      - For naive bayes people, 
            - look [here](http://robotics.stanford.edu/users/sahami/papers-dir/disc.pdf_
            - look [here](http://i.giwebb.com/wp-content/papercite-data/pdf/YangWebb02a.pdf), secion 3
      - SVM people need to read about kernel functions
      - Logistic regression people have it easy! Nothing to tune!

Before lookin at those, your going to need to know:

- Decision trees are recursive _diversity reduction_ algorithms
- Find the split that most reduces diversity
- Recurse on each split.
- Stop when (e.g.) too few examples in each split.

RandomForests says "if one tree is good, why not build 100?"

- each time, grab (say) log(N) of the attributes and some percent of the rows
- build N trees
- make a conclusion by voting across the forest

### Example1

- let us measure diversity using _standard deviaton_ 
     - sqrt((&sum; square(x - &mu;))/(n-1))
- standard deviation &sigma; of 9,2,5,4,12,7 has &mu; = 6.5 and &sigma;=3.619.
- Learners like CART and M5prime and Random Forest Regressorts used standard deviation.
    - Why? Cause these learners predict for _numeric class variables_.

### Example2:

- let us measure diversity using _entropy_; i.e. _-1* &sum; p*log2(p)_
- e.g. 1 orange, 1 apple, 2 bananas, and 4 grapes 
      - occur at probability 1/8, 1/8, 1/4, and 1/2
      - 8 =2*2*2 so log2( 1/8 ) = -3
      - 4 =2*2 so log2( 1/4 ) = -2
      - 2 =2 so log2( 1/2 ) = -1
      - what is entropy of (o,a,b,b,g,g,g,g) 
      - -1 * (1/8*-3 + 1/8*-3 + 1/4*-2 + 1/2*-1)
      - = -1 * (1/8*-3 + 1/8*-3 + 2/8*-2 + 4/8*-1)
      - = -1/8 * (-6 + -4 + -4)  
      - = 14/8 
      - = 1.75 
- Learners like decision trees and random forests use entropy
     - Why? Cause these learners predict for _symbolic class variables.

### Example3: 


What is the best split for this data?

<img class="pure-img displayed"  src="https://github.com/txddPt/fss16/raw/master/img/golf.png">

Here are the options (note that this is four different splits):

<img class="pure-img displayed"  src="https://github.com/txddPt/fss16/raw/master/img/tree.png">

Consider the _outlook_ tree. We have three sub-branches so the _expected value_ of the diversity after the split is

- 5/14 * entropy of sunny split 
- 4/14 * entropy of overcast split 
- 5/14 * entropy of rainy split 

The overcast split is easy: 

- we only have _yes_ so _p(yes)_ = 1 and log2(p) = 0
- and 4/14 is zero

The sunny and rainy split are symmetric

- sunny: 2 yes and 3 no =     -1 * (2/5 * log2(2/5) + 3/5 * log2(3/5)) = 0.97
- raning: 3 yes and 2 no = same entropy as sunny

So the expected value after the outlook split is

-  (5/14 * 0.97) + (4/14 * 0) + (5/14 * 0.97) = 0.69

(BTW, this is an improvement since before the split we have 9 yes, 5 no; ie. entropy was 0.94; i.e. **more** diversity).

If we repeat this calc over all splits, we get

- outlook split: 0.69
- temperate split: 0.91 
= humidity split:  0.79
- windy split: 0.89

So we would split on outlook.

 


## Boxes= data sets (velocity, synapse, art, ..)
Boxes =

George Box

Wolpert.

Inductive bias

Sampling bias

Programming errors

Design choices: so many design choices. Let slook at some of those.

Tables. structure. what goals.

How to sumamrize the goals (bdom, cdom)

How to sumamrise the indepnent vairabels: non-parametric, parametric, random numbers.


     186


The SE literature is so large that most papers are cited very rarely and researchers and practitioners    routinely miss important related work.   Accordingly, much recent research has explored automatic active learning tools to help researchers find work that is relevant to their own. Those tools however, have two significant problems: (a) they offer no guidance on when a reader can stop reading; and (b) they 
they suffer from frequent ``runaway reading times'' where a large percentage of studies take far too long to find  relevant papers.

This paper addresses these problems, as follows. Firstly, at the start of the reading process, we explore methods to quicker find an initial set of relevant documents.  We find that a new initialization method based on the inverse document frequency can dramatically reduce the variance in   reading times. This new method has the additional benefit that it also reduces the total number of papers required for each reading study (by an average   of 10\% to 30\%).

Secondly, as reading progresses, we use a new mathematical estimation model to estimate the remaining  number of relevant studies. Users can use this estimate to better understand when can they safely stop reading.
When compared with the prior state of the art (an incremental SVM method), our new method
is far more accurate.
