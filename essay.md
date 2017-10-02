---
title: Essay
published: true
---

## Your Task

Plan your Oct/Nov project work.

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

How much does Person2's approach "cost" in terms of reduced fucntionality
measured on some criteri?

## Sections

Your essay should have the sections:

- CRITERIA: 
    - Briefly expand on the above criteria. Explain why each is useful/ useless or easy/hard.
- KEY CRITERIA: 
    - Expand in details on  (or more) of the above that you most care about (explaining why)?  Hint: the fewer you care about, the
  less you will have todo in this project.
- CRITIQUE: 
    - For any domain (x), what is the most popular, complex, slowest, most thorough state-of-the-art SOA tool?
    - On which of the above criteria does that SOA fail?
- REVIEW:
    - What are   simple engineering approach that enables that criteria?
- PLANNING: which of the REVIEWed technologies do you plan to implement and assess?
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


