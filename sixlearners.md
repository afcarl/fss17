---
title: 6 Learners (and which is "best")
published: true
---

## Caveat emptor

The following remarks are very subjective. In fact each of the following "sentences" is really just one of my current
heuristics, each of which really needs experimental verification.

## Eval Criteria

Note that in the following it is important to distnguish between performing and explainable systems.
All learners produce an output (usually a prediction). Its ust that some do that by first building a succinct model,
tthen use that model to generate the prediction. When learners produce an outout that is short enough to read, we call that comprehensible.
When that comprehension includes a clear effect of "change this " to "achieve that", we see the system is also plannable.

```
+----------------------------------------+-                  
|                                        |                   
|    All learners perform e.g. NB        |                   
|                                        |                   
| +-----------------------+              |                   
| | Some                  |              |                   
| | learners   +----------|-----------+  |                   
| | explain    | e.g      | Some      |  |                   
| | (e.g.      | XTREE    | learners  |  |                   
| | decision   |          | plann     |  |                   
| | trees)     +----------|-----------+  |                   
| |                       |              |                   
| +-----------------------+              |                   
|                                        |                   
+----------------------------------------+                   
```


But also, is a learner:

- Readable (users can understand the output, with a glance)?
    - Who cares?
    - Anyone who has ever had to explain an output to a business user, or defend a conclusion against a critical audience.
- Can I learn what to _change_, just by reading the output?
    - Who cares?
    - Prediction is one thing, but when the users say "what can I do to change/fix that?", then you care about planning
- Simple to code?
    - Who cares? Just use an existing package!
    - I care. Complexity counts for maintainance, adding bugs, being able to experiment with the algorithm; being able to mash up this
      algorithm with another?
- Incrementally update-able?
    - Who cares?
    - Anyone mining over infinite streams
    - Anyone doing anomaly detection
    - Anyone checking if old models still hold under new conditions
- Fast to train/test
    - Who cares? Just buy some cloud compute time.
    - See below

(For references to the following, see [this file](https://arxiv.org/pdf/1703.00133.pdf).)
   
The more complex the method, the harder it is to apply the
analysis. Fisher et al. [20] characterizes software analytics as a
work flow that distills large quantities of low-value data down to
smaller sets of higher value data. Due to the complexities and
computational cost of SE analytics, "the luxuries of interactivity,
direct manipulation, and fast system response are gone” [20]. They
characterize modern cloud-based analytics as a throwback to the
1960s-batch processing mainframes where jobs are submitted and
then analysts wait, wait, and wait for results with "little insight into
what is really going on behind the scenes, how long it will take, or
how much it is going to cost” [20]. Fisher et al. [20] document the
issues seen by 16 industrial data scientists, one of whom remarks

- <em>Fast iteration is key, but incompatible with the
jobs are submitted and processed in the cloud. It
is frustrating to wait for hours, only to realize you
need a slight tweak to your feature set.</em>

Methods for improving the quality of modern software analytics
have made this issue even more serious. There has been continuous
development of new feature selection [25] and feature discovering
[28] techniques for software analytics, with the most recent
ones focused on deep learning methods. These are all exciting innovations
with the potential to dramatically improve the quality of
our software analytics tools. Yet these are all CPU/GPU-intensive
methods. For instance:

- Learning control settings for learners can take days to weeks to
years of CPU time [22, 64, 69].
- Lam et al. needed weeks of CPU time to combine deep learning
and text mining to localize buggy files from bug reports [39].
- Gu et al. spent 240 hours of GPU time to train a deep learning
based method to generate API usage sequences for given natural
language query [24].

Note that the above problem is not solvable by waiting for faster
CPUs/GPUs. We can no longer rely on Moore’s Law [51] to double
our computational power every 18 months. Power consumption and
heat dissipation issues effect block further exponential increases to
CPU clock frequencies [38]. Cloud computing environments are
extensively monetized so the total financial cost of training models
can be prohibitive, particularly for long running tasks. For example,
it would take 15 years of CPU time to learn the tuning parameters
of software clone detectors proposed in [69]. Much of that CPU
time can be saved if there is a faster way

## KNN (kth nearest neighbor)

Train: add new examples to a box of old examples.

Test: find k near examples, guess details of the new thing from the k old things

[Demo](http://scott.fortmann-roe.com/docs/BiasVariance.html)

Readable? No way. There is no model, just a big box of thousands and thousands of exmaples.

Planable? Nope. But you can cluster then learn details between clusters to infer plans. I [tried that once](http://menzies.us/pdf/12change.pdf) but it does not work as well as 
[planning via deltas between decision tree branches](https://arxiv.org/pdf/1708.05442.pdf).

Simple to code? Sure. Unless you want to optimize it. Then, things get tricky.

Incrementally update-able? Sure! Just add more examples to the box?

Fast? Nope. Every new test case has to peek at every old training case. But there are some standard optimizations:

- Mega-scale: Use [KD-trees](http://code.activestate.com/recipes/577497-kd-tree-for-nearest-neighbor-search-in-a-k-dimensi/) or some other tree clustering methods to quickly group the examples, 
- Web-scale: Use Mini-batch k-means to reduce the training data to just a few centroids. Then just reason over the centroids (note: this is a very low memory approach)
     - Aside: [Mini-batch k-means](https://www.eecs.tufts.edu/~dsculley/papers/fastkmeans.pdf) is incremental
- Peta-scale: many techniques. e.g. [canopy clustering](https://en.wikipedia.org/wiki/Canopy_clustering_algorithm) and many more besides

## NB (Naive Bayes)

A Naive Bayes classifier collects frequency counts of old events,
grouped into "classes". Then, if a new event arrives without a
classification, it checks through the old list of classes looking for
the one with the highest frequency counts for this new event.
This assumption allows us to collect
frequency counts just on each attribute value (and not pairs, or
triples, or quads of values) so such classifiers hav a very small memory footprint.

Because of its assumption, this  method is called "naive". 
BTW, turns out that NB is not so "naive". See 

- Webb, G. I.; Boughton, J.; Wang, Z. (2005). [Not So Naive Bayes: Aggregating One-Dependence Estimators](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.3.7847). Machine Learning. Springer. 58 (1): 5–24. doi:10.1007/s10994-005-4258-6.
- Rennie, Jason D., et al. [Tackling the poor assumptions of naive bayes text classifiers](http://www.aaai.org/Papers/ICML/2003/ICML03-081.pdf) 
  Proceedings of the 20th International Conference on Machine Learning (ICML-03). 2003.
    - And all its [citations](https://goo.gl/Um1SAs)
- Domingos, Pedro; Pazzani, Michael (1997). 
  [On the optimality of the simple Bayesian classifier under zero-one loss](http://engr.case.edu/ray_soumya/mlrg/optimality_of_nb.pdf). Machine Learning. 29: 103–137. 

The following table comes from the last reference. Note that NB performs as well as other methods that explore rich connections between attributes (e.g. the C4.5 decision tree
learner):

<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/nb.png">


Readable? No way! Just a big list of distributions (see below)

- There is the nomogram trick:  Mozina, M.; Demsar, J.; Kattan, M.; Zupan, B. [Nomograms for Visualization of Naive Bayesian Classifier](https://goo.gl/uTT33G). Proc. PKDD-2004. pp. 337–348.
- Whuch looks great... till you starting going pairs or triples of effects. Anyone care to fix that?

```
                 Class
Attribute          yes      no
                (0.63)  (0.38)
===============================
outlook
  sunny             3.0     4.0
  overcast          5.0     1.0
  rainy             4.0     3.0
  [total]          12.0     8.0

temperature
  mean          72.9697 74.8364
  std. dev.      5.2304   7.384
  weight sum          9       5
  precision      1.9091  1.9091

humidity
  mean          78.8395 86.1111
  std. dev.      9.8023  9.2424
  weight sum          9       5
  precision      3.4444  3.4444

windy
  TRUE              4.0     4.0
  FALSE             7.0     3.0
  [total]          11.0     7.0
```
Plannable? Nope. But see Bayes nets update algrithms for tools that, given a goal, [will find changes to the distributions that acheive that goals](http://www.cs.waikato.ac.nz/~remco/weka.bn.pdf):

- Fine in theory. But still need guidance regarding minimality and what to twiddle etc etc

Simple to code? [Sure!](nbc) Maybe you want to avoid using Guassians with an initial discretizer but these can be 
[very simple to implement](http://robotics.stanford.edu/users/sahami/papers-dir/disc.pdf).

- There are problems with low frequency classes, but that can be patched [see the Lagrange `b` and `m`  tricks](https://github.com/timm/lawker/blob/master/block/timm/evil/write/lib/app/nb/nb.awk), lines 120 and 125;
- And there are even NB fixes for ultra-low frequency e.g. [text mining applications](http://www.aaai.org/Papers/ICML/2003/ICML03-081.pdf) 

Incrementally update-able? [Absolutely!](nbc) 

Fast to train/test [Yes!](nbc)

## , svm,  rf, lr, dt

TBD
