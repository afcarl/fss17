

# Review2:  (08/24 - 09/25)

   


# Algorithms:

## Week 2:

- What's the differences between KNN and KMeans?
   - Could you explain KNN/KMeans within 2 sentences?
   - How K affects the output from KNN/KMeans? 
   - How do you choose K for KNN/KMeans?
- Random forests using a sub-sampling method to handle data too big to fit into RAM
    - Describe that method
    - Sub-sampling can miss some data. How does Random Forests reduce the odds of such misses?
    - How to make conclusions across the whole forest?
    - How to apply this heuristic to other learners?
- Naive Bayes classifiers divide their input rows according to the class variable, then collect different stats on each column for each class.
    - Let all _boys_ smell like sugar and be 1 meter tall and have long hair 
    - Let all _girls_ smell like spice and be 2 meters tall and have short hair
    - Let all _elephants_ smell like grass and be 3 meters tall and have very short hair
    - Given the above, describe the _likelihood_ calculation for classifying a new thing that is 1.8 meters tall with short hair.
- Comment on the merits of KNN or NB or RF for incremental anomaly detection.
- Comment on the merits of KNN or NB or RF for incremental model building
- Explain in your words what is dominance? Please give one compare function to be used for dominant.
- Are all the learners explainable for their output/predictions? Give 2 example learners that are explainable, and 2 that aren't.
- What are the common Evaluation Criteria for the learners? Why these criteria are important in the real world software engineering?

------
## Notes: Pareto Domination

The human condition is a constant balancing act between vaguely understood, often competing, goals. For example:

<img class="pure-img displayed"  src="https://camo.githubusercontent.com/51986c44f5eb582702e759f234fb9b411790c261/68747470733a2f2f696e666f736369656e63652e6570666c2e63682f7265636f72642f3135333637342f66696c65732f33345f323031305f53696d4275696c6425323047416f7074696d697a5f312e706e67">
<img class="pure-img displayed" src="https://github.com/txt/ase16/raw/master/img/planes.png">
<img class="pure-img displayed" src="https://camo.githubusercontent.com/eb13a3bf97a652a525b29da0c175caa541c630e6/687474703a2f2f696d6167652e736c696465736861726563646e2e636f6d2f6d756c74696f626a6563746976656f7074696d697a6174696f6e616e6474726164656f6666737573696e6770617265746f6f7074696d616c6974792d3131303331313230303135352d70687061707030322f39352f6d756c74696f626a6563746976652d6f7074696d697a6174696f6e2d616e642d74726164652d6f6666732d7573696e672d70617265746f2d6f7074696d616c6974792d322d3732382e6a70673f63623d31333739393833363937">

In such trade-off diagrams, point on the Pareto frontier


<img class="pure-img displayed" src="https://raw.githubusercontent.com/txt/ase16/master/img/pareto1.png">

Boolean domination says that I dominates J iff

- I is better on at least one objective, and worse on none.
- Cannot distinguishing between very near and very far dominance.
- Often gets confused by more than 3 objectives.

Indicator dominance sums the difference in the objective scores and shouts that out load (raises it to an exponential)

- Better for large number of objectives.

```lua
local function dominate1(i,j,t)
  local e,n = 2.71828,#t.goals
  local sum1,sum2=0,0
  for _,col in pairs(t.goals)  do
    local w= col.weight
    local x= NUM.norm(col, i.cells[col.pos])
    local y= NUM.norm(col, j.cells[col.pos])
    sum1 = sum1 - e^(w * (x-y)/n)
    sum2 = sum2 - e^(w * (y-x)/n) 
  end 
  return sum1/n < sum2/n end
```


------

###  Notes: K-means 

Pick K centroids at random; label all data with their nearest centroid; for all things with same centroid, compute means; move centroids to that mean position; repeat

<img class="pure-img displayed"  src="https://ds055uzetaobb.cloudfront.net/image_optimizer/ff1732816ba08239c0d3b200c3a9708070885705.jpg">

-----

### Notes: Mini-batch k-means

1. Data arrives in random order. Take the first "K" items, call them centroids (say, K-32);
2. Read next M items (say M=512)
     - Label each item with nearest centroid. 
     - Add +1 to a centroid whenever some new item decides it is its nearest
4. Nudge each centroid by a weighted towards each item in the batch. 
     - E.g. If centroid "weighs 250" then move it 1/250 th towards the item
5. Goto 2.     

------

### Decision Trees

See homework

----

### Fast Frugal Decision Trees

[referece](http://fastandfrugal.com/)

Extremely extremely simple decision trees. 

- Binary classes
- Restricted to just a few levels (e.g. L=4)

<img class="pure-img displayed"  src="https://snag.gy/9iOGeb.jpg">

2 nodes at each level. 

- Leaf node: One for the attribute range A=R that most strongly predicts for something
- Base of sub-tree: other node holds all rows that do not have A=R

More than 2 classes? No problem. For each class, repeat for C and not C.

So fast we can run it N times with different internal thresholds to get a ROC curve.

----

## PRISM:

Make a rule, throw away all the rows covered by the condition of that rule. Repeat on the remaining data.

- The result is a _decision list_ (aka nested _if then else_)  where rule[i] only applies if rules 1..i-1 are all false.

To make a rule of the form _LHS &rArr; C_ (short form)

- Set _LHS_ to empty.
- Find the attribute value _Ai=Vi_ that predicts for any class C with highest accuracy. Add to _LHS_.
- For all data with _Ai=Vi_, add to the _LHS_ add the range _Aj=Vj_ which most improves accuracy. 
       - If none found then  then print _LHS  &rArr; C_
       - and delete all rows with _LHS_
- Now go make another rule.

Full form:

```
For each class C
  Initialize E to the instance set
  While E contains instances in class C
    Create a rule R with an empty left-hand side that predicts class C
    Until R is perfect (or there are no more attributes to use) do
       For each attribute A not mentioned in R, and each value v,
          Consider adding the condition A = v to the left-hand side of R
          Select A and v to maximize the accuracy p/t
           (break ties by choosing the condition with the largest p)
       Add A = v to R
   Remove the instances covered by R from E
   Print R

t = total instances
p = positive instances
```

If applied to the weather data

<img class="pure-img displayed"  src="https://lh3.googleusercontent.com/ukEXoJRNKiJ1r4jHM5PEC4smvZKSY6fm9FeDy9B6OeYTzQQMUOrD6ZnsYcL9vLmIZT3xnDrFENO8-79N7fdT0ButCJwSbYhp41K3BnNwpOwumfKLN0z-LfwbBZn0Qc6ce4p6dH20eHqi8NJopA">

Comapre with decision tree:

<img class="pure-img displayed"  src="https://lh5.googleusercontent.com/M3EFzbiJrO81Yvpibpe8fUijSbw2w_GXbrQJ01MGzReUK_DNp4KvahP5YM2l4FCf-WCU_ii7izdWLBtkONdTZq1VEJ8Mw73Lfmm2x9RocktsDZT5eYb51Yb8ef2BUv0OJqXMncuXJvvpj0Hh_Q">

**IMPORTANT NOTE**: known to perform less-than-great _unless_ you restrict _Aj=Rj_ to "power ranges"; e.g. those with the above-median score from supervised discretization. 

For a startof the art incremental rule learning (in the PRISM mode), see 
  [Very fast decision rules for classification in data streams](https://goo.gl/EXGLHP), Petr Kosinai, João Gama, Data Mining and Knowledge Discovery January 2015, Volume 29, Issue 1, pp 168–202
