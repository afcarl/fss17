---
title: Lecture1 (6 times)
published: true
---

# Why This Subject? 

Six introductions, the last one actually has engineering principles.

The rest are "just" poetry, things I need to get out of my system.

## Inspiration

What is learned at university? Is it techniques (that  age and whither in 2-5 years), tools (that become out-dated tomorrow)?
Or is it _inspiration_? Fuel for a lifetime of thought and accomplishment? Ways to thing differently, to stand out
in the crowd. To boldly go where no one has gone before (ok, that last one was probably a metaphor too far...).

Now I know that 10 years out from university, you will only retain 10% of all those ideas you sampled
at univesity. But if you start with nothing, you'll end up with 10% of nothing, which is still nothing. So while
at university, collect as many crazy ideas as you can. Hence this subject.

XXX need to be more cautios )(verification)

XXXX need to be more adverntous. maybe ive been doing tjhis too long but the more i do "
data mining" the more i realize its core algorithms can be used for other tasks. stop calling to "data mining" sart dalled int "idea engineering" I dunno

## Slogans


Limits to test = limits to build ([My PhD](http://menzies.us/pdf/95thesis.pdf)

- No guessing without checking; no induction without verification.
- Testing is something that succumbs to engineering... better engineering, easier testing.

This subject: a set of engineering principles for testing the results from data mining.

Software has bugs.    
Data mining tools are software.    
Therefore....    

Worse, data miners have "bugs", aka biases, [built into them](https://goo.gl/9ssteS). Without those biases, they cannot decide what to keep and what to ignore.
If they cant prune much of their search space then they will never terminate.  So, by necessity, data miners are
  skwed tools, possibly mis-directed.

"But this is not correct", I think you might say, "how can a data query like the following bee biased?"
  
    SELECT * FROM Customers
    WHERE Country='Mexico';`selct 

Just consider: where does the data come from? How was it pre-processed? And there are 119,530,753
people linving in Mexico (as of 2015). WHen this query returns millions of results, how will you sort and summarize
the results? When you show these results to anyone that needs to take action on this data, what
aspects of those results will you stress or gloss over?

More generally,  data ming gets **much** more complicated that the above. Hyperparameter optimization,
discretization, spectral learning, visualizations, etc etc. Most folks don't realize the vast range of options
within data mining. Why? Cause they use these tools "black box" with no poking around. Which means they are
inhereting all the biases of the specific case studies used to set up their tools. And are those biases appropriate
for your problem? You won't know unless you look around.

## Why Listen to me?

Been doing this for a while now (UNSW AI).

Seen a lot of software (NASA).

Been helping a lot of people do data mining for a long time (PROMISE).

Get cited, a lot (citations = Facebook likes; we all complain about them; we all like it when it is us).

## Seeking Insights

So if biases cannot be avoid, and those biases get very complex and arcane, what does it mean to "vertify" a data miner?
The best we can do is to explore two sets of biases

- The biases of the learner;
- The biases of the people who need the model.

So data mining is the process of icnrementally discovering and reducing the distances between these two biases.
And that means:

- re-running the learners again and again and again
- storing and revisiting lots of old data and results
- _showing the users_ the results of the data mining then asking them "what do you think?"

This is this path to insight (Bird example).

## Fear

Newbies think data mining is running simple queries like `age > 21`.

## Beyond Magic

I ran my first decision tree learner in 1980s. It was amazing: I saw structure dribbling out
from samples of data. That was (and still is) thrilling to watch. Just imagine, with these data mining tools we can see  something no one has **ever** seen before.

Decades later, that thrill remains. BUT. Now that that thrill is routine, that anyone can do that, you have to ask, what else is there?   Given all that experience with induction, what might we say about the nature of learning **now** that we did not know before?

My answer to this question is that we have to move from data mining _worship_ to data mining _nervousness_. If everyone can use these tools to quickly build models, they everyone can quickly build crappy models. We need to way to _critique_ these models, to push back, to demand better models.

## Fear

Newbies think data mining is running simple queries like `age > 21`.

But the more you work it, the more intricate it becomes:

- Choice of data, choice of goals, interaction with users, feedback from business uers, choice of learners, data pre-processing, trying different learners, choice of statistical methods
- [All these effect what gets learned](https://github.com/txt/ase15/blob/master/models/icse14-v5-min.py).

I've watched 100s of newbie graduate students botch up data miners. I know how badly they can screw up.

 
I've also watched dozens of supposedly skilled data mining people screw it up (yours truly included), [discover supposedly important conclusions that, in fact, were just trite](https://pdfs.semanticscholar.org/ae7d/96ee5c7838343a7cf176d008cf3eaaeba1ef.pdf). We jsut need to accept it, humans are brilliant, but flawed. Human cognition is usually biased/blinded by a variety of factors (see below). Hence, I say: 

- all those decisions we make during data mining can actually contain numerous errors 
- Even skilled users of these tools need someone(s) leaning over their shoulder, checking their results.

![](http://images.mentalfloss.com/sites/default/files/styles/insert_main_wide_image/public/cognitive_biases.png)

(For a much longer list of human cognitive biases, see [Wikipedia](https://en.wikipedia.org/wiki/List_of_cognitive_biases).

## Worried about Continuous Deloymemt



## Engineering Details

Here's  my standard toolkit for exploring data. Note the commitmnet to various
data structures and algorithms. You can, and you should, critize those choices
(and run experiments on different choices). 

Regardless of the _how_, I hope you reflect much on the _why_ of the following;
i.e.

- _no data mining without verification _ and  
- _before anything else, design for verification_.

### Discretization, feature selection

When explaining things to business users, 

### Instance selection

Find groups of data where conclusions are different

From clustered data, we only need share  exemplars (e.g. N random items per centroid).

- **Bad idea if** inference from exemplars worse than inference from all data. FYI, current evidence = not wrong:
     - [Vasil's data carving thesis {username=password=guest}](http://unbox.org/things/var/vasil/thesis/thesis-v3.pdf (username=password=guest)
     - [Vivek's configuration sampling work](https://arxiv.org/pdf/1701.08106.pdf)
     
### Mutate (a little) prior to sharing

(Fayola's approach](http://menzies.us/pdf/15lace2.pdf). To hide individuals:

- Find everyone's nearest unlike neighbor
- Mutate by a random amount up to, but not more than, halfway to that neighbor

### Who are these people:

- Vas

