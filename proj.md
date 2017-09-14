
---
title: Project Possibilities
published: true
---

Explanation

- Take soemthing opaque (neural nets, NB) and summarize the training data with some English-like generator (PRISM+,  Decision trees, fast and frugal trees)
- Report the cost of explanation 
    - compare performance of the opaque "it" vs the explained "it"

Scale up with sub-sampling

- When all the data won't fit into RAM
    - Random Forests: N times: select X% or rows and (say) log(C) of the columns at random. Look for conclusions stable cross all N
    - Incremental clustering and only keep C examples per cluster (centroid, N picked at random, M most distant)
- Report the cost of sub-sampling
    - compare performance of the sub-sampled "it" vs the full "it"
 
# Explanation

Using some sumamrization method (*)

(*) Only use the Nth most interesting columns

## Inspiration

What is learned at university? Is it techniques (that  age and
whither in 2-5 years), tools (that become out-dated tomorrow)?  Or
is it _inspiration_? Fuel for a lifetime of thought and accomplishment?
Ways to thing differently, to stand out in the crowd. To boldly go
where no one has gone before (ok, that last one was probably a
metaphor too far...).

Now I know that 10 years out from university, you will only retain
10% of all those ideas you sampled at university. But if you start
with nothing, you'll end up with 10% of nothing, which is still
nothing. So while at university, collect as many crazy ideas as you
can. Hence this subject.

"Education is not the filling of a pail, but the lighting of a fire"    
-- William Yates

"If the world merely lived up to our wildest dreams, what a dull place it would be. Happily..."
-- Tim Menzies

"The best thing for being sad," replied Merlin, beginning to puff
and blow, "is to learn something. That's the only thing that never
fails. You may grow old and trembling in your anatomies, you may
lie awake at night listening to the disorder of your veins, you may
miss your only love, you may see the world about you devastated by
evil lunatics, or know your honor trampled in the sewers of baser
minds. There is only one thing for it then — to learn. Learn why
the world wags and what wags it. That is the only thing which the
mind can never exhaust, never alienate, never be tortured by, never
fear or distrust, and never dream of regretting. Learning is the
only thing for you. Look what a lot of things there are to learn."    
-― T.H. White, The Once and Future King

## Maturity

I ran my first decision tree learner in 1980s. It was amazing: I saw structure dribbling out
from samples of data. That was (and still is) thrilling to watch. Just imagine, with these data mining tools we can see  something no one has **ever** seen before.

Decades later, that thrill remains. BUT. Now that that thrill is routine, that anyone can do that, you have to ask, what else is there?   Given all that experience with induction, what might we say about the nature of learning **now** that we did not know before?

My answer to this question is that we have to move from data mining _worship_ to data mining _caution_. If everyone can use these tools to quickly build models, they everyone can quickly build crappy models. We need to way to _critique_ these models, to push back, to demand better models.

So here's a little story on how to make a grown man cry:

- Him: "Hey Timm, I've got this great new on-line machine learning platform where researchers can log on and do
really fast queries over complex SE data."
- Me: "Cool. But does it support XYZ..." (long list of "operators" follow)
- Him: "er.. no..."
- Me: "It really should. I've been doing data mining for years and I'm pretty sure that XYZ are the things
we really need."
- Him: "But my tool is a base system on top of which the services you describe could be built."
- Me: "Sure, whatever. Everyone says that. But no one does it. Its like everyone succeeds at primary school
data mining and then stops maturing their ideas and expectations about data miners. You need to START with XYZ."
- Him: "I don't think so. I'll just go talk to that person over there now..."


## Why Exactly should anyone ever Listen to me?

Been doing this for a while now (UNSW AI).

Seen a lot of software (NASA).

Been helping a lot of people do data mining for a long time (PROMISE).

Get cited, a lot (citations = Facebook likes; we all complain about them; we all like it when it is us).



## Need to be more ambitious

## Fear

Newbies think data mining is running simple queries like `age > 21`.

But the more you work it, the more intricate it becomes:

- Choice of data, choice of goals, interaction with users, feedback from business users, choice of learners, data pre-processing, trying different learners, choice of statistical methods
- [All these effect what gets learned](https://github.com/txt/ase15/blob/master/models/icse14-v5-min.py).

I've watched 100s of newbie graduate students botch up data miners. I know how badly they can screw up.

Now I'm watching continuous deployment people rush data miners into production, and when I check those data miners I can usually find **stuff** I think needs changing.
 
Also I've also watched dozens of supposedly skilled data mining people screw it up (yours truly included), [discover supposedly important conclusions that, in fact, were just trite](https://pdfs.semanticscholar.org/ae7d/96ee5c7838343a7cf176d008cf3eaaeba1ef.pdf). We just need to accept it, humans are brilliant, but flawed. Human cognition is usually biased/blinded by a variety of factors (see below). Hence, I say: 

- all those decisions we make during data mining can actually contain numerous errors 
- Even skilled users of these tools need someone(s) leaning over their shoulder, checking their results.

![](http://images.mentalfloss.com/sites/default/files/styles/insert_main_wide_image/public/cognitive_biases.png)

(For a much longer list of human cognitive biases, see [Wikipedia](https://en.wikipedia.org/wiki/List_of_cognitive_biases).



## Need to be more Cautious

Limits to test = limits to build ([My PhD](http://menzies.us/pdf/95thesis.pdf)

- No guessing without checking; no induction without verification.
- Testing is something that succumbs to engineering... better engineering, easier testing.

This subject: a set of engineering principles for testing the results from data mining.

Software has bugs.    
Data mining tools are software.    
Therefore....    

Worse, data miners have "bugs", aka biases, [built into them](https://goo.gl/9ssteS). Without those biases, they cannot decide what to keep and what to ignore.
If they cant prune much of their search space then they will never terminate.  So, by necessity, data miners are
  skewed tools, possibly mis-directed.

"But this is not correct", I think you might say, "how can a data query like the following bee biased?"
  
    SELECT * FROM Customers
    WHERE Country='Mexico';`selct 

Just consider: where does the data come from? How was it pre-processed? And there are 119,530,753
people living in Mexico (as of 2015). When this query returns millions of results, how will you sort and summarize
the results? When you show these results to anyone that needs to take action on this data, what
aspects of those results will you stress or gloss over?

More generally,  data mining gets **much** more complicated that the above. 

- See
the [source code](https://github.com/txt/ase15/blob/master/models/icse14-v5-min.py) used to get the results for [this paper](https://arxiv.org/pdf/1609.05563.pdf).
- Consider the effects of  
Hyper-parameter optimization,
discretization, spectral learning, visualizations, etc etc. 

Most folks don't realize the vast range of options
within data mining. Why? Cause they use these tools "black box" with no poking around. Which means they are
inhereting all the biases of the specific case studies used to set up their tools. And are those biases appropriate
for your problem? You won't know unless you look around.



## Not Data Mining, But "Idea Engineering"

(Note to those who know data mining: in the following "bit" == "cluster" and "delta"=="contrast set".)

Much commonality within a learner

By the time you build a table reader and sort out your column tracking 
then (e.g.) knn and NB are very small variations of each other.

So as software engineerings, we need to study the design patterns of data miners


The thing  we call "data mining", isn't that at all.

+ Its a way to explore the world, to divide into bits your like and bits you don't then to
    - Then you can learn thing specific to each bit
    + Also, if you have some really slow processing, you can speed things up by just applying them to the leaves
+ It turns out that the contrasts between things can be a very short list
    - So you can learn _minimal descriptions_ about the differences between bits
+ If you know how to score the bits, you can describe a _landscape_ of _slopes_ between bits you like and otherwise:
     + The delta towards the bits you like is a   _plan_  (of what you could do next).
     + And the delta towards the bits you don't is a _monitor_  (of what to watch out for).
+ Another important landscape are _slopes_ between past and present bits
     - If you were happy before and you are sad now then a _diagnosis_ is delta between
       the bits from before and the bits now.
    - The bits between what you saw before and what you see now are _anomalies_. 
    - Anomalies are triggers that tell us its time to change our ideas.
    -  If the bits are divided hierarchically, you usually  ever need to _revise_ the sub-bits with anomalies.
of that hierarchy.
+ Further, you can _compress_ the data by just keeping a few items in each bit.
+ Then you can _share_ the data by sharing the mutants, after a little _mutation_ (where you move
  items no more than half way to the nearest other items in compressed space).

It turns out the above is not just about data mining, but also about the internals of an optimizer.
So you can use the above for something called _hyper-parameter optimization_ where you learn how to
twiddle different bits.

For more on this see, see [Idea Engineering](http://menzies.us/pdf/13promise.pdf).

## Need more "science" in "data science"

<img class="pure-img displayed"  src="https://github.com/txt/fss16/raw/master/img/science.png">



An important part of knowledge  is "no"; i.e. the ability to critically assess something, and to recognize when one idea  is better, smarter, than another.

"Science" is the process of communities sharing and reviewing and improving each other's ideas. Sadly, most "data science" is not about "science". Rather its about vendors selling you stuff that does not work properly and does not
ring an alarm when it starts failing.
This
is strange since an important part of knowledge is "no"; i.e. the
ability to critically assess something, and to recognize when one idea
is better, smarter, than another.

So a million million people can run data miners. But how many  now when those data miners start going wrong? And how to fix faulty models?

So here are some operators that I demand a modern data minign toolkit supports. Note: minority view alert!




_Comprehension_:

- Something we can read, argue with
- Essential for communities critiquing ideas. If the only person reading a model is a carburetor, then we can expect little push back. But if your models are about policies that humans have to implement, then I take it as axiomatic that humans will want to read and critique the models.

_Fast_:

-   Not a CPU hog
-  Reproducing  and improving an old ideas means that you can reproduce that old result. Also, certifying that new ideas often means multiple runs over many sub-samples of the data. Such  reproducibility and certification is impractical when such reproduction is impractically slow

_Light_:

-  Small memory footprint
- Again, reproducing an old data mining experiment or certifying a new result means that the resources required for reproduction are not exorbitant.

_Goal-aware_:

-  Different goals means different models. AND multiple goals = no problem!
- This is important since most data miners build models that optimizer for a single goal (e.g. minimize error or least-square error) yet business users often want their data miners to achieve many goals.

_Humble_ :

-   Can publish succinct certification envelope (so we know when not to trust)
-  Delivered data mined models should be able to recognize when new data is out-of-scope of anything they've seen before. This means, at runtime, having access to the data used to build that model. Note that phrase _succinct_ here: certification envelopes cannot include all the data relating to a model, otherwise every hard drive in the world will soon fill up.

_Privacy-aware_:

-   Can hide an individual's data
- This is essential when sharing a certification envelope

_Shareable_:

-   Knows how to transfer models, data, between contexts.
-  Such transfer usually requires some transformation of the source data to the target data.

_Context-aware_:

-   Knows that local parts of data generate different models.
-  While general principles are good, so too is how to handle particular contexts. For example, in general, exercise is good for maintaining healthy. However, in the particular context of  patients who have just had cardiac surgery, then that general principle has to be carefully tailored to particular patients.
  ideas need to be updated.

_Self-tuning_:

-   And can do it quickly
-  Many experiments show that we can't just use data miners off-the-shelf.  Rather, if their control parameters are tuned, then we can get much better data mining results.

_Anomaly-aware_:

-   Can detect when new inputs differ from old training data
-  This is the trigger for when old


_Incremental_:

-   Can update old models with new data
-  Anomaly detectors tell us something has to change.  Incremental learners tell us what to change.



## But What About "Big Data"?

(Mostly) missing in this subject will be talk of Hadoop, MapReduce, ElasticSearch,
Spark, TensorFlow, DeepLearning, MapReduce, AWS, Zeppelin, Kafka,
and all the other system-level staples of the standard Big Data
tool stack. These are all great tools  which you should,
of course, learn and understand.  There are many fantastic on-line,
freely-available, resources which can offer detailed tutorials on
all the above (and if you want to prioritize, start with
Zeppelin+TensorFlow+Spark).

But here's the thing. I've been doing data mining for far too long to use these tools uncritically.
Data mining tools as heuristics for taking wild leaps across a huge space of possible models.
And having supervised dozens of graduate students building and using those tools,
I assert that many of those leaps can be too far-fetched.

Now many other people and much more trusting than me.
They
view data miners as perfect oracles that will deliver the "right" answer, which we will
never need to question.

- So, if you prefer (spurious) certainty, just study
Hadoop, MapReduce, ElasticSearch,
Spark, TensorFlow, DeepLearning, MapReduce, AWS, Zeppelin, Kafka, etc.
- But if, like me, you have doubts, then you want to know how to engineer environments that support the exploration and reduction of doubts.
  In which case, this subject is for you.

### Aside

(Of course, the above could be criticized as a trite dichotomy, that
it  may be  possible to use the Big Data tools to implement the operators
described above. That would be a good project for this subject.)


## Student Goals

The goal of this work is to destroy, or at least
find limits with my prior work. As inputs for that task
I offer LURE, a tool kit that offers a baseline0 implementation
of many of the tools that I think are important.

For everything I show you, your response should be:

- I've been reading some on that topic...
- ... and I see that there are several other ways to do that thing ...
- ... and I'm going to code them up and see if they work better than LURE.

Your job is to

- research alternate ways to implement any part of that  kit
- implement on of them
- compare them to LURE
- show where LURE falls down
- make a recommendation about
   - when not to use LURE and use something else
   - how to improve LURE to make it let your better thing.
   - how to improve the better thing to make it more like LURE

Now, of course, you should expect to do better than LURE. LURE
is a one-size-fits all tool designed with a "near enough is good
enough" attitude. Specific tools often do better
on specific data sets.  So consider yourself a success if
you prove LURE a failure!
