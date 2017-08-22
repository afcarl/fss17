---
title:  No microscope without mud
published: true
---


## Preamble

Before reading this, do this [quick tutorial exercise](https://txt.github.io/fss17/tutweka).

Note the end of that tut: the models we get are a function of the choices we make while running the learner.

Say what? Don't data miners find truth in data? 

Well.... not so much. 

If you are not faint of heart, read on. But be warned. You may be shocked at how... subjective.. are the results
of data mining. Kinda brings to mind the old adage:

- Laws, like sausages, cease to inspire respect in proportion as we know how they are made.     
  -- John Godfrey Saxe (1816 - 1887)

--------

## What do data miners do?

Data mining algorithms generate summaries of data. They are like microscopes we look through to reveal internal structure.

If a microscope has mud on the lens, what we see might be distorted. The point of this lecture is that, in data mining, all data miners have mud on them.
All the models we find are wrong, or irrelevant, or useless to some extent for some users.

Data miners are algorithms and algorithms have known best and worst cases.
Consider the quicksort algorithm:

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

More generally, there are various no free lunch (NFL) theorems saying that if an algorithm works well on _X_ then there
exist just as many cases _Y_ whre it will perform badly:

- <em>We have dubbed the associated results NFL theorems because they demonstrate that if an algorithm performs well on a certain class of problems then it necessarily pays for that with degraded performance on the set of all remaining problems.</em>    
   --  Wolpert, D.H., Macready, W.G. (1997), "No Free Lunch Theorems for Optimization", IEEE Transactions on Evolutionary Computation 1, 67.


From [Machine Learning Lesson of the Day, Jan 24, 2014](https://goo.gl/UWh2gK):

- A model is a simplified representation of reality, and the
simplifications are made to discard unnecessary detail and allow
us to focus on the aspect of reality that we want to understand.
    -  These simplifications are grounded on assumptions; these assumptions
may hold in some situations, but may not hold in other situations.
    - This implies that a model that explains a certain situation well
may fail in another situation.  
    - In both statistics and machine
learning, we need to check our assumptions before relying on a
model.  
- The "No Free Lunch" theorem states that there is no one
model that works best for every problem.  
    - The assumptions of a great
model for one problem may not hold for another problem, so it is
common in machine learning to try multiple models and find one that
works best for a particular problem.  
    - This is especially true in
supervised learning; validation or cross-validation is commonly
used to assess the predictive accuracies of multiple models of
varying complexity to find the best model.  
    - A model that works well
could also be trained by multiple algorithms – for example, linear
regression could be trained by the normal equations or by gradient
descent.  
- Depending on the problem, it is important to assess the
trade-offs between speed, accuracy, and complexity of different
models and algorithms and find a model that works best for that
particular problem.

From ME:

- It is also important to assess the goals of the learner. If the users care about goals ABC and your algoritm is trying to
  reduce XYZ then the learner could be building a model no one camg
res about.
- Also, how we assess a model critically effects what model we prefer; i.e. what lessons we learn.

----

## Case study

The conclusions we draw are a function of the decisions we make during data mining.

For example:

<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/aucRecall.png">

<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/precPf.png">

 
What are the parts of this figure?

- Figures: one figure for different evaluation critieria (false alarms, recall,
  AUC, precision)
- Boxes= data sets (velocity, synapse, art, ..)
- Rows= learners (knn, svm, nb, rf, lr, dt)
- Columns= data treatments (no, s1, s2) 
- Stats tests= gray scale

Now, take a deep breath and consider all the choices made to generate this data...


### Boxes= data sets

<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/ckMetrics.png">

For example: [velocity](https://zenodo.org/record/322455#.WZwmxJOGOfc).

### Learners

For all the learners knn, svm, nb, rf, lr, dt

- write 2 lines describe the algorithm
- write down some of the control parameters of that algorithm
- For those doing KNN (kth nearest neighbor), please see [here](http://menzies.us/pdf/11teak.pdf), section 2.5
- For those doing RF (random forests) and dt (decision trees) please:
    - see [here](dt101)
    - [and here](https://arxiv.org/pdf/1609.01759.pdf) table2.
- For naive bayes people, 
    - look [here](http://robotics.stanford.edu/users/sahami/papers-dir/disc.pdf_
    - look [here](http://i.giwebb.com/wp-content/papercite-data/pdf/YangWebb02a.pdf), secion 3
-  SVM people need to read about kernel functions
- Logistic regression people have it easy! Nothing to tune!

### Data Treatments

- No= do nothing
- S1= SMOTE= synthetic minority over-sampling
    - One way to handle class imbalance
    - Many other ways, see [here](http://ieeexplore.ieee.org/document/5128907/)
- S2= SMOTUNED. 
    - An NCSU special that automatically learns best control parameters for SMOTE. 
    - See [here](https://arxiv.org/pdf/1705.03697.pdf).

<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/smote.png">

### Evaluation criteria

Formally, defect prediction is a binary classification problem.
The performance of a defect predictor can be assessed
via a confusion matrix like Table I where a "positive" output
is the defective class under study and a "negative" output is
the non-defective one. Further, “false” means the learner got
it wrong and "true" means the learner correctly identified a
fault or non-fault module. Hence, this table has four quadrants
containing, e.g FP which denotes "false positive"

<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/abcd.png">

From this matrix, we can define performance measures like

- Recall is the fraction of relevant instances that are retrieved:
   - Recall = pd = TP/(TP+FN)
- Precision is the fraction of retrieved instances that are relevant:
   - Precision = prec = TP/(TP+FP)
- False Alarm is the ratio of false positive to total predicted negative:
   - False alarm = pf = FP/(FP+TN)

As shown below,  a typical predictor must "trade-off"
between false alarm and recall. This is because the more
sensitive the detector, the more often it triggers and the higher
its recall. On the other hand, if a detector triggers more often,
it can also raise more false alarms. Hence, when increasing
recall, we should expect the false alarm rate to increase
(ideally, not by very much).

<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/roccurve.png">

Which means we can offer another measure: the Area Under Curve (AUC), which is the area covered by an
ROC curve  in which;
   - the X-axis represents FPR = FP/(FP+TN)
   - and the Y-axis represents: TPR = TP/(TP+FN)

### Stats tests 

To check the effects of our treatments,

- Five times, we randomized the order of the data
- Each time, we divide the data into five bins
- So 25 experiments in all, each report recall, precision, false alarn, auc


Each box of data has triples of results for each learner (one for each treatment).

- If there are three colors (dark gray, light gray, white) then the numbers are different
- If there are two colors (dark gray, white) then the numbers fall into two groups
- If there is one colors (white) then the numbers fall into one group (i.e. no difference).

To find those colors,
we use a statistical significance test and an effect
size test. 

- Significance test are usefully for detecting if two
populations differ merely by random noise. 
   - i.e. is there any difference at all?
- Effect sizes
are useful for checking that two populations differ by more
than just a trivial amount.
   - i.e. is the difference interestingly large?

Here, our significance test was the Scott-Knott procedure:

- Sort the results (so this would be a list of 3 sets of numbers)
- Recursively bi-clusters to sorted set of numbers.
- If any two clusters are statistically indistinguishable, ScottKnott
reports them both as one "rank". 
- Scott-Knott first looks
for a break in the sequence that maximizes the expected values
in the difference in the means before and after the break. 
- More
specifically, it splits "L" values into sub-lists "M" and "N" in order
to maximize the expected value of differences in the observed
performances before and after divisions. 
- E.g. for lists L,M and
N of size LS,MS and NS where L = union(M,N)nx, Scott-Knott divides
the sequence at the break that maximizes:


<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/maxdiff.png">

Here's that test,  coded up, for those of you who [like code](https://lualure.github.io/info/sk.html) (and that's all of you, right?)

### Q: What do we see?

- A: None
-  No learner was consistently "best" across
     most of our experiments. 
-  RF (random
     forests) has the highest "best" scores, it was still defeated in
     (18−7)/18 = 61% experiments. 
- On the other hand, S2 (SMOTUNED)
     was consistently used by whatever learner was found to be
     "best" (in recall and AUC). Hence, we conclude from the
     that "better data" might be better than "better data miners".

### Oh But does all this really matter?

Darn tooting it does. Check out the improvements seen when using "S2" (auto-tuned SMOTE). In the following, _positive numbers_ mean that _larger_ scores were seen in Auto-tuned SMOTE than with 
standard SMOTE.

<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/autotune.png">

### In the Literature

In February 2017, we searched scholar.google.com for the
conjunction of "software" and "defect prediction" and "oo"
and "ck" published in the last decade. 
- This returned 231
results. 

From that list, we selected "highly-cited" papers, which
we defined as having more than 10 citations per year. 
- This
reduced our population of papers down to 107. 

After reading
the titles and abstracts of those papers, and skimming the
contents of the potentially interesting papers, we found 22
papers that either performed ranking studies (as
defined above) or studied the effects of class imbalance on
defect prediction. 

In the following, the column "evaluated using multiple
criteria", papers scored more than "1" if they used multiple
evaluation criteria:


<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/litreview.png">

Which can be summarised as follows:

<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/venn.png">

that is, most of the literature does not explroethe space of options shown above and do
does not find the improvements reported above.
