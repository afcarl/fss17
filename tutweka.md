---
title: Time to LEARN something
published: true
---


U yearn to learn? Me to!

Log into public github (no account? create one!).

Got co c9.io. Click on the github icon top right


<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/c9.png">

Create new workspace, enter in the following github repo name:  _https://github.com/dotninjas/dotninjas.github.io_.

Then press the big green button (don't worry about the templates, they will work themselves out).

<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/ninja.png">

When you are in,

     cd ninja
     sh ninja

Now you should see something like this:

<img class="pure-img displayed"  src="https://github.com/txt/fss17/raw/master/img/ninjash.png">

Type "`eg0`" to show (a) some data and (b)  a decision tree learned from that data.
    
    @attribute outlook {sunny, overcast, rainy}
    @attribute temperature real
    @attribute humidity real
    @attribute windy {TRUE, FALSE}
    @attribute play {yes, no}
    
    overcast  64  65  TRUE   yes
    overcast  72  90  TRUE   yes
    overcast  81  75  FALSE  yes
    overcast  83  86  FALSE  yes
    rainy     65  70  TRUE   no
    rainy     68  80  FALSE  yes
    rainy     70  96  FALSE  yes
    rainy     71  91  TRUE   no
    rainy     75  80  FALSE  yes
    sunny     69  70  FALSE  yes
    sunny     72  95  FALSE  no
    sunny     75  70  TRUE   yes
    sunny     80  90  TRUE   no
    sunny     85  85  FALSE  no
    
    outlook = sunny
    |   humidity <= 75: yes (2.0)
    |   humidity > 75: no (3.0)
    outlook = overcast: yes (4.0)
    outlook = rainy
    |   windy = TRUE: no (2.0)
    |   windy = FALSE: yes (3.0)

If you want to know more, then

- This is the command line WEKA tool run by (e.g.)

        Weka="java -Xmx2048M -cp weka.jar "
        learner=weka.classifiers.trees.J48
        $Weka $learner -p 0 -C 0.25 -M 2 -t train.arff1 -T test.arff

This grows a decision tree downwards until there are more than `-M 2` examples in the leaves.

Then in prunes sub-trees. Sub-trees die if, after pruning, the overall test error does not get worse by more
than `-C 0.25`.

Why those magic numbers? Engineering judgement. I.e. the generated model is a result of decisions made by the analyst.
We'll get back to that.

For more examples, see

- [here](https://github.com/dotninjas/dotninjas.github.io/blob/master/ninja/ninja.rc#L1105,L1183)
- [and here](https://github.com/dotninjas/dotninjas.github.io/blob/master/ninja/ninja.rc.md)

For the theory behind decision tree learning, see [here](dt101)
