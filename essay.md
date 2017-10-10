---
title: Essay
published: true
---


## Your Task

By Oct23, plan your Oct/Nov project work. To that end, write an essay.

## Setting up

Person1 has not done this subject and uses the most popular, complex, slowest, most thorough state
of the art tool.

Person2 has done this subject and is willing to make compromises in order support:

- model readabilty
- actionable conclusions
- learnability and repeatability of the results
    - i.e. using ess CPU and less disk/RAM
- mutli-goal reasoning
- anomaly detection (a little bell that goes "ping!" when new questions not in old data)
- incremental (knows how to forget old knowledge and learn new stuff, when required)
   - many use an anomaly detector
- sharable 
    - can succinctly describe the training data (somehow)
    - and/or that data can be mutated to lower the odds of detecting idividuals within the data
    - and/or that summarized/mutated data still works well for learning a model
- context aware: generates different conclusions for different regions of the data
- self-tuning (knows how to tune its own parameters)

How much does Person2's approach "cost", compared to Person1, in terms of reduced fucntionality
measured on some criteria?

## Sections

Your essay should have the sections:

- **CRITERIA**: 
    - Briefly expand on the above criteria. Explain why each is useful/ useless or easy/hard.
- **KEY CRITERIA**: 
    - Expand in details on  (or more) of the above that you most care about (explaining why)?  Hint: the fewer you care about, the
  less you will have todo in this project.
- **CRITIQUE**: 
    - For any domain (see below), what is the most popular, complex, slowest, most thorough state-of-the-art SOA tool?
    - On which of the above criteria does that SOA fail?
- **REVIEW**:
    - What are   simple engineering approach that enables that criteria?
- **PLANNING**: which of the REVIEWed technologies do you plan to implement and assess?
    - What is a plan for building it and **comparing** the performance of your simpler tools with
      the SOA in  order to determine what is won and lost between the simpler and the most complex.
    - For that comparison, consider use the stats.py tool 

## (x) Domains:

- preferrably from software engineerings;   see the recent proceedings of 
    - ICSE confererence https://goo.gl/GdWULY
    - TSE journal https://goo.gl/qretcJ
    - IST journal https://goo.gl/XDQbKu
    - MSR conference https://goo.gl/By9nU1
    - EMSE journal https://goo.gl/UM8Bxd
    - ICMSE conference https://goo.gl/xtJa6g
- preferbly using data from [seacraft](tiny.cc/seacraft)
    - Hint: find a paper doing something you like, then see if you can access their data

## What to hand in

- An essay, 4 to 6 pages, 10pt, 2 column.
    - For format templates, see 
      http://www.acm.org/publications/proceedings-template
         - For an examle, see [here](img/sample-essay.pdf)
         - Note that if your submission look very different to this sample, you have to redo it.
    - For an on-line editor of those files (in tex), see https://www.overleaf.com/gallery/tagged/acm-official#.WdJkchNSzdu
    - For an MS word version look for "ACM_SigPlan.docx" inside "ACM Sample Files" of the
      "word" links at http://www.acm.org/publications/proceedings-template
- All the citations mentioned in the text are in the references
- All the references in the back are discussed in the text
- All the figures/tables are mentioned in the text.

--------

## Hints

Note that you **cannot** read all the the following.  Best to focus in on one or two areas.

### Methods for  model readabilty

- Fast Frugal Trees
    - Good overview: https://goo.gl/5Kkary
    - Background motivation: https://goo.gl/kHrb9s
    - R package: https://cran.r-project.org/web/packages/FFTrees/vignettes/guide.html
- Bayes nets
    - Note that WEKA has a Bayes nets tookbox
    - IEEE TSE article: https://goo.gl/JQ6mYw
    - IEEE TSE article2: https://goo.gl/yEyZae

Measures of success here are (e.g.) size vs performance of model. Perhaps bigger models are better but
by how much? And is it really worth it?

### Methods for Actionable Conclusions

- PLanners
    - Don't report the classifications, but the deltas between
      nodes in the tree
    - As done in your homework.
    - As done in CrossTrees https://arxiv.org/pdf/1609.03614

### Methods for learnability and repeatability of the results

i.e. using less CPU and less disk/RAM

- Cluster the data e.g. with mini-batch k-means or some of its more recent variants (https://goo.gl/uTBFu7)
   - Keep only small N examples per clustera (see reservoir sampling: https://goo.gl/cppkuI)
   - Learn one model per cluster
- Naive Bayes is prety fast, low memory
    - See also NB variants that handle low frequency data sets (see xithe TWCNB psuedcode in section 4.4 of fig https://goo.gl/bM6b87)
    - Use some fast clutering method to divide the data, then build one NB classifier per leaf  (https://goo.gl/9PmLLB)
- Work on very small models
   - OneR (probably, too small): tutorial https://goo.gl/EkwAAx; paper: https://goo.gl/kPS7R6
   - Oneway (probably, too simple): https://goo.gl/PTdpEH
   - Fast Frugal trees: see above (perhaps a little better)
- Work on very small models, which are so small that it is cool to just blow them away everytime you get new data
   - e.g FLASH: https://goo.gl/DzsQyH
- Data carving:
   - Just generate a tiny table of data from the data, and let people look at that: https://goo.gl/nAdJcb (username=password=guest)

### Methods for mutli-goal reasoning

- Replace class with some aggregated number
   - e.g. the domination count in the assignment

Rule mutation algorithms: Each rule is a vector of size A\*R+1  (a ttributes, R ranges per attribute, 1 class var) that is mutated via DE or GAs

- Differential evolution (using our domination counter)
     - https://jvanderw.une.edu.au/DE_1.pdf
     - http://www1.icsi.berkeley.edu/~storn/code.html
     - Applied to SE: https://arxiv.org/pdf/1609.01759
- Genetic algorithms
     - Tutorial: https://www.tutorialspoint.com/genetic_algorithms/index.htm
     - Latest and greatest = NSGA-III and MOEA/D
     - Standard = NSGA-II and SPEA2
     - Java implementations: http://jmetal.sourceforge.net/- 
- Recursive spectral 
     - GALE: https://goo.gl/B7oC6w
     - SWAY (even simpler than GALE): https://arxiv.org/pdf/1701.07950.pdf

### Methods  anomaly detection 

(A little bell that goes "ping!" when new questions not in old data.)

Learner-based:

- If learner performance plateaus faster that data generator changes states, then just use any learner and report anomalies when 
  performance drops 
- e.g. SAWTOOTH http://menzies.us/pdf/05sawtooth.pdf 
- (caution: this paper was never accepted, sigh, even though it is cool++).

Cluster-based:

- e.g. non-parametric : cluster the data and find the 20 to 80th percentile of the distances of items to their cluster's centroid. and something
  is alien if, in its nearest cluster, it is outside 20-80
- e.g. parametric: http://ai-at-wvu.blogspot.com/search?q=elkan

# Methods for Incremental

(Knows how to forget old knowledge and learn new stuff, when required. )
Many use an anomaly detector.

Mining over infinite streams

- Incremental decision trees: 
    - Very dumb method: Learn one tree on all old prior data, learn a new
      tree on last 1000 examples. If New performs better than old,
      delete old and run forward with new.
    - Very fast decision trees (A classic): https://homes.cs.washington.edu/~pedrod/papers/kdd00.pdf.  This is in [weka](http://weka.sourceforge.net/doc.dev/weka/classifiers/trees/HoeffdingTree.html)
    - More recent work: [Accurate decision trees for mining high-speed data streams](https://pdfs.semanticscholar.org/87d0/523d9042e6482df0ae80b59c78f25252525f.pdf)
    - A nice way to do incremental decision trees that can handle uncertainty
      https://github.com/txt/fss17/files/1353358/MH_MSG_IDT2015.pdf
- incremental discretization and Naive Bayesa https://goo.gl/BU3aad:
- incremental clustering parametric: http://ai-at-wvu.blogspot.com/search?q=elkan
- incremental clustering mini-batch-k-means and  its recent  enhancements:

Active learning:

- Many tricks https://goo.gl/xgqeFJ

Naive Bayes is prety fast, low memory, incremental algorithm:

- See also NB variants that handle low frequency data sets (see xithe TWCNB psuedcode in section 4.4 of fig https://goo.gl/bM6b87)
- Use some fast clutering method to divide the data, then build one NB classifier per leaf  (https://goo.gl/9PmLLB)



If learning over infinite N examples, how soon before the learning stops improving? 

## Methods for Sharable 

Can succinctly describe the training data (somehow)

- Data carving (feature and instance selection, just share what is left):  https://goo.gl/nAdJcb (username=password=guest)

And/or that data can be mutated to lower the odds of detecting idividuals within the data

- LACE2: https://goo.gl/znErNY

And/or that summarized/mutated data still works well for learning a model

- LACE2: https://goo.gl/znErNY

## Methods for context aware: 

- Cluster the data e.g. with mini-batch k-means or some of its more recent variants (https://goo.gl/uTBFu7)
   - Keep only small N examples per clustera (see reservoir sampling: https://goo.gl/cppkuI)
   - Learn one model per cluster

## Methods for self-tuning

- Differential evolution
     - https://jvanderw.une.edu.au/DE_1.pdf
     - http://www1.icsi.berkeley.edu/~storn/code.html
     - Applied to SE: https://arxiv.org/pdf/1609.01759
- Genetic algorithms
     - Tutorial: https://www.tutorialspoint.com/genetic_algorithms/index.htm
     - Latest and greatest = NSGA-III and MOEA/D
     - Standard = NSGA-II and SPEA2
     - Java implementations: http://jmetal.sourceforge.net/
