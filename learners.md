---
title: 5 Classifiers
published: true
---

The following remarks are very subjective. In fact each of the following "sentences" is really just by current
heuristics, each of which really needs experimental verification.

Is a learner

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

-Learning control settings for learners can take days to weeks to
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

## knn, svm, nb, rf, lr, dt
