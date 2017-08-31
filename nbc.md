---
title: NBC,  a not-so-naive Bayes Classifier
published: true
---

## Historical Note

Update: this code was wrtitten in 2004 and since then much has changed. Support Vector Machines, Tensor Flow, Hadoop, Spark, massive
text mining, etc etc.
But some conclusions stay. Even though the following conclusions seem olde worlde, Naive Bayes continues to have a niche. See

- Rennie, Jason D., et al. [Tackling the poor assumptions of naive bayes text classifiers](http://www.aaai.org/Papers/ICML/2003/ICML03-081.pdf) 
  Proceedings of the 20th International Conference on Machine Learning (ICML-03). 2003.
- And all its [citations](https://goo.gl/Um1SAs)

## Synopsis

     ./nbc -[hlx] train test

## Description

Is less more? Can a few lines of gawk developed in a day or two stand in
for a sophisticated state-of-the-art JAVA package? In the general case
there may be software engineering advantages to working with rich
languages like JAVA. However, in the specific case of a Naive Bayes
classifier for discrete data, it is interesting to test if less is
indeed more.

A Naive Bayes classifier collects frequency counts of old events,
grouped into "classes". Then, if a new event arrives without a
classification, it checks through the old list of classes looking for
the one with the highest frequency counts for this new event.

The method is called "naive" This assumption allows us to collect
frequency counts just on each attribute value (and not pairs, or
triples, or quads of values).

In practice, this "naive" strategy works remarkably well- often performs
as well as other schemes that try to model interactions between
frequencies.

Hence, we call this system a not-so-naive Bayes Classifier.

### Summary of Results

In summary, the performance on this simple gawk-based Naive Bayes
classifier is quite remarkable.

-   Not surprisingly, nbc.awk's accuracy are very similar to a standard
    bayes classifier (from the WEKA system). That is, this
    implementation is *adequate*.
-   Quite surprisingly, the awk version does not run much slower than
    java. In fact, for under 1000 instances, this implementation is
    comparatively *fast or faster* than a much more mature JAVA-based
    tool.


### Details: Accuracy

The following table compares classification accuracies between nbc.awk
and WEKA's weka.classifiers.NaiveBayes.

All the data sets were discrete so no kernel estimation was used.

Results come from a 10-way cross-val (but no initial randomization of
data set order).

The table is sorted by increase mean difference. Nbc.awk does better
than WEKA Bayes on the datasets shown at the bottom of the table.

                    mean                significant 
                    difference   std.   difference? 
          data      in accuracy  dev.   (alpha=0.01)
     -----------------------------------------------
            soybean | -3.02 |   2.02 |  y
               iris | -2.14 |   4.51 |  n
                zoo | -0.38 |   6.54 |  n
      primary-tumor | -0.30 |   3.28 |  n
          audiology | -0.27 |   2.67 |  n
           mushroom | -0.25 |   0.23 |  n
             splice |  0.00 |   0.00 |  n
           kr-vs-kp |  0.00 |   0.00 |  n
      breast-cancer |  0.00 |   0.00 |  n
     contact-lenses |  0.00 |   0.00 |  n
               vote |  0.27 |   1.47 |  n
              lymph |  0.73 |   5.01 |  n
           breast-w |  1.63 |   1.32 |  y
           credit-a |  7.40 |   5.60 |  y
             letter |  9.44 |   1.40 |  y

On the whole, nbc.awk works as well as WEKA Bayes.

### Details: Runtimes

The following table compares the runtimes of nbc.awk (awk) vs WEKA BAYES
(java) measured in seconds.

Each lines show total times for ten training+test runs (one for each
item in the cross val). E.g. letter actually ran in time 4.92 seconds
(on average) and this was called 10 times.

Note: the time for dividing files for the x-val is not shown.

The table is sorted on the ratio of awk vs java runtimes. Ratios less
than one mean awk ran faster than java. Sampler.awk does better than
Weka Bayes on the datasets shown at the bottom of the table (below the
middle line).

                     runtimes (secs) | 
                    -----------------|---------------------
               data  awk   java ratio| insts  attrs classes
     --------------------------------|---------------------
             letter  49.2  17.6  2.8  20,000   17      27
           mushroom  10.1   5.9  1.7   8,124   23       3
           kr-vs-kp   8.1   5.1  1.6   3,916   37       3
             splice  11.3   7.8  1.4   3,190   62       4
            soybean   4.2   3.4  1.2     683   36      20
     ------------------------------------------------------
          audiology   2.9   3.4  0.9     226   70      25
      primary-tumor   1.3   2.8  0.5     339   18      23
               vote   1.0   2.4  0.4     435   17       3
     contact-lenses   0.6   2.0  0.3      24    5       4
      breast-cancer   0.7   2.4  0.3     286   10       3
           credit-a   1.1   3.3  0.3     690   16       3
           breast-w   1.0   3.5  0.3     699   10       3
              lymph   0.6   2.4  0.2     148   19       5
               iris   0.5   2.5  0.2     150    5       4
                zoo   0.6   2.4  0.2     101   18       8
     ------------------------------------------------------
              total  93.1  66.8  1.4

All up, the awk-based learner was 40% slower than the JAVA. For larger
data sets, JAVA was always faster. However, for smaller datasets (under
1000 instances) the awk version was nearly as fast or faster. []{#7}

### Details: Memory

We have run this small Awk script on 100s of megabytes of data, without
crashes or core dumps. The code is very memory effecient- unlike the
WEKA which loads all the data into RAM. []{#8}

### Discussion

It is hardly surprising that a state-of-the-art tool kit built and
optimized by JAVA gurus can out-perform awk code on large examples.
However, what is surprising is that an 32 line AWK script built and
debugged in a weekend often works nearly as well, or better.

Perhaps "nbc" is not-so-naive after all. []{#9}

Options
-------

 -x
:   run an example

 -h
:   print help text

 -l
:   print legal notice


Installation
------------

To check the download, unzip the contents.zip then

     chmod +x nbc
     ./nbc nbceg.train nbceg.test  | 
     gawk -F, '{print $0  "\t " ($1 !=$2 ? " <== bad" : "")}' 

This should print:

     malign_lymph,  malign_lymph        
     metastases,    metastases    
     malign_lymph,  malign_lymph        
     metastases,    metastases    
     malign_lymph,  metastases   <== bad
     malign_lymph,  malign_lymph        
     malign_lymph,  malign_lymph        
     metastases,    metastases    
     metastases,    metastases    
     metastases,    metastases    
     malign_lymph,  malign_lymph        
     metastases,    metastases    
     malign_lymph,  malign_lymph        

The accuracy of the above outputis correct/total = 11/12 = 92%

## Awk code


Here is the nbc.awk code called by the Bash script (shown below).

     BEGIN {
      #Internal globals:
         Total=0    # count of all instances
       # Classes    # table of class names/frequencies
       # Freg       # table of counters for values in attributes in classes
       # Seen       # table of counters for values in attributes
       # Attributes # table of number of values per attribute
       }

     Pass==1 {train()}
     Pass==2 {print $NF "," classify()}

     ## note this code be fully incremental, as follows
     ## 1) wait for at least 20 instances before classifying
     ## 2) meanwhile, train on all incoming data
     ## 3) always update training data AFTER classification
     
     # NR > 20  {print $NF "," classify()}
     #          {train()}

     function train(    i,c) { 
       Total++;
       c=$NF;
       Classes[c]++;
       for(i=1;i<=NF;i++) {
         if ($i=="?") continue;
         Freq[c,i,$i]++
         if (++Seen[i,$i]==1) Attributes[i]++}
     }

     function classify(         i,temp,what,like,c) {  
       like = -100000; # smaller than any log
       for(c in Classes) {  
         temp=log(Classes[c]/Total); #uses logs to stop numeric errors
         for(i=1;i<NF;i++) {  
           if ( $i=="?" ) continue;
           temp += log((Freq[c,i,$i]+1)/(Classes[c]+Attributes[i]));
         };
         if ( temp >= like ) {like = temp; what=c}
       };
       return what;
     }

In the above, there are some `magic numbers` added in to handle low frequency cases 

- `1` used in `temp +=` 
- Added `Classes[c]` in the denominator

For more nuances magic numbers, see lines 120 and 125 of [this code](https://github.com/timm/lawker/blob/master/block/timm/evil/write/lib/app/nb/nb.awk)

## Bash Code



### Copyright

    copyleft() { cat<<EOF 
    nbc: a naive bayes classifier
    Copyright (C) 2004 Tim Menzies

    This program is free software; you can redistribute it and/or
    modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation, version 2.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
    EOF
    }


### Usage

     usage() { cat<<-EOF
        Usage: nbc  [FLAGs] TRAIN TEST
        Naive bayes classifier.

        TRAIN and TEST are comma-separated data files with the same
        number of columns. The last column of each is the class
        symbol. This classifier learns from TRAIN and then tries
        to classify the examples in TEST.

        Flags: 
          -h        print this help text
          -l        copyright notice
          -x        run an example
        EOF
        exit
     } 


### Demo code

     nbcDemo() { 
        main nbceg.train nbceg.test
     } 


## Main


     main() {
        gawk -F, -f nbc.awk Pass=1 $1 Pass=2 $2
     }

### Command-line Processing

     demo=""
     while getopts "hlx" flag
     do case "$flag" in
            l)  copyleft; exit;;
            h)  usage; exit ;;
            x)  demo="nbcDemo";;
        esac
     done
     shift $(($OPTIND - 1))
     if [ -n "$demo" ]
     then $demo
          exit
     else  main $1 $2
     fi

## Author

Tim Menzies

