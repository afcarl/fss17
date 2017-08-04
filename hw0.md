

---
title: Homework0: Num, Sym
published: true
---

Creaate a public github repo (not in the NCSU repo, but in public).

Add your team and `timm` to that team.

Create a directory called `hw/0`.

Answer the following questions in hw/0/README.md.
All scripts you write should also be in hw/0.

__________________________

In any language you like, build a `Num`  and `Sym` class based on  the following.
Note that you will need only a small fraction of the funationality 
of those files.

- https://lualure.github.io/info/sym.html
- https://lualure.github.io/info/num.html

Using the weather data below, read that data from disk and run into through
a `Num` or `Sym` held for each column. Note that you will need to know
what type is each column. What I do
is add a `$` to the nueric column names.

    outlook,	 $temp,	$humid, windy,play
    sunny,	   85,	  85,	  FALSE, 	 no
    sunny,	   80,	  90,	  TRUE, 	 no
    overcast,	 83,  	86,	  FALSE,	yes
    rainy,	   70,	  96,	  FALSE,	yes
    rainy,	   68,  	80,	  FALSE,	yes
    rainy,	   65,	  70,	  TRUE,	   no
    overcast,  64,	  65,	  TRUE,	  yes
    sunny,	   72,	  95,	  FALSE,	 no
    sunny,	   69,	  70,	  FALSE,	yes
    rainy,	   75,	  80,	  FALSE,	yes
    sunny,	   75,	  70,	  TRUE,	  yes
    overcast,	 72,	  90,	  TRUE,	  yes
    overcast,	 81,	  75,	  FALSE,	yes
    rainy,	   71,	  91,	  TRUE,	   no

Report the entropy and  standard deviation of columns 1 and 2.

