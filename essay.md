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

## Hints

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

### Methods for learnability and repeatability of the results

i.e. using less CPU and less disk/RAM

- Naive Bayes is prety fast, low memory
    - See also NB variants that handle low frequency data sets (see ithe TWCNB psuedcode in section 4.4 of fig https://goo.gl/bM6b87)
- Cluster the data e.g. with mini-batch k-means or some of its more recent variants (https://goo.gl/uTBFu7)
   - Keep only small N examples per clustera (see reservoir sampling: https://goo.gl/cppkuI)
   - Learn one model per cluster
- Work on very small models
   - OneR (probably, too small): 
   - Fast Frugal trees (perhaps a little better)

## Methods for mutli-goal reasoning
## Methods  anomaly detection 

(A little bell that goes "ping!" when new questions not in old data.)

If learner performance plateaus faster that data generator changes states, then just use any learner and report anomalies when 
performance drops

# Methods for Incremental

(Knows how to forget old knowledge and learn new stuff, when required. )
   - many use an anomaly detector

- Mining over infinite streams

If learning over infinite N examples, how soon before the learning stops improving? 

## Methods for Sharable 

- can succinctly describe the training data (somehow)
- and/or that data can be mutated to lower the odds of detecting idividuals within the data
- and/or that summarized/mutated data still works well for learning a model

## Methods for context aware: 

- generates different conclusions for different regions of the data

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
