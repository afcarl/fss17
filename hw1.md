

---
title: Homework1
published: true
---

Using the weather data from class, built a Naive Bayes classifier
that 

- reads data one row at a time
- incrementally updates the frequency counts
- classifies the new row BEFORE   updating the frequencies
  (so new examples are classified on old data)
- Increments a counter of correct classifications as it goes
- Prints out  that counter as it goes.

You may assume all columns are symbolic.

Stress test your code as follows:

- Google for soybean.arff
- Covert that file into your input format
- Run soybean through your classifier.
