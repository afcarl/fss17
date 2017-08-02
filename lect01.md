---
title: Lecture1 (6 times)
published: true
---


# Why This Subject? 

Six introductions, the last one actually has engineering principles.

The rest are "just" poetry, things I need to get out of my system.

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
