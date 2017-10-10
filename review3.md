

# Review3:  (09/25 - 10/09)

- What are the differences between unsupervised and supervised discretizer.
- Which one should we run first? Why?
- What't the advantages of using supervised discretizer? 
- What should we do when the supervised discretizer have multiple dependent variables?
- Is mean or median a better metric to compare two learners? Why?
- What can you tell me about these two data samples?

```
 one         * --|            , 0.28,  0.29,  0.32,  0.41,  0.48
 two             |    -- * -- , 0.71,  0.79,  0.80,  0.90,  0.98

```

How would you rank the following five results from five treatments. Show all working.

```
 x1  0.34  0.49  0.51  0.6
 x2  0.6   0.7   0.8   0.9
 x3  0.15  0.25  0.4   0.35 
 x4  0.6   0.7   0.8   0.9 
 x5  0.1   0.2   0.3   0.4
```

----

Consider the following table. 

|                  |parametric     | non-parametric|
|------------------|---------------|---------------|
|effect size       | hedges, cohen | cliffsDelta   |
|significance test | ttest         | bootstrap     |

- How are effect size tests different to significance tests?
- How are parametric tests different to non-parametric tests?
- Explain: parametric tests are faster than non-parametric tests since they make limiting assumptions.
- Define the cohen test.
- Explain, with a diagram, ttests how much normal curves overlap. In your explanationd draw (a)two normal
  curves which tests would say are **not** significantly different and (b) two more normal curves that
  ttests would say **are** signfificantly different.
- Write down the pseudocode of cliffsDelta.
- In bootstrapping, what is a bootstrap sample? How does bootstrapping using 100s of such samples to
determine if two lists are significantly different.

----

When examining data from multiple sources, chant this mantra:


- Visualize the data, somehow.
- Check if the central tendency of one distribution is better than the other; e.g. compare their median values.
- Check the different between the central tendencies is not some small effect.
-  Check if the distributions are significantly different;

For each of the above four points,

- List two ways to achieve all those goals (hint, some of your answers come from the above).
