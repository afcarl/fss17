---
title: Welcome
---


NCSU CSC 591-023 (10722)  
CSC 791-023 (11162)  
Tues/Thurs 4:30 to 5:45  
Mid-session exam week 10 (on terminology)    
No final exam.

<img align=right src="https://github.com/txt/fss16/raw/master/img/science.png">


# Why this subject?


"Science" is the process of communities sharing and reviewing and improving each other's ideas. Sadly, most "data science" is not about "science". Rather its about vendors selling you stuff that does not work properly and does not
ring an alarm when it starts failing.

So a million million people can run data miners. But how many  now when those data miners start going wrong? And how to fix faulty models?

Do this subject, learn answers to those questions, become the data scientist everyone needs to consult with  when things start going wrong.


 

# Project

Apply SE principles to a data science problem. 

- Implement add any of the operators listed on slide 9 of [this tutorial](http://tiny.cc/timm) (and listed below) to any 
  data science problem 
- Ideally one from SE but i can be flexible on that. e.g. if you are doing X in your thesis, then we can apply all this to X.


  
Operator | Notes
------|--------
Comprehensible | Something we can read, argue with
Fast | Not a CPU hog
Light |Small memory footprint 
Goal-aware |Different goals means different models. ANd multiple goals = no problem!
Humble | Can publish succinct certification envelope (so we know when not to trust)
Context-aware | Knows that local parts of data ⇒ different models. Knows how to find different contexts
Privacy-aware | Can hide an individual's data
Anomaly-aware | Can detect when new inputs differ from old training data
Shareable | Knows how to transfer models, data, between contexts
Self-tuning | And can do it quickly
Incremental | Can update old models with new data


FYI: I have a basline tool for all of those. But most parts of it remain untested. And might want to use
         the tool for inspiration rather then execution.
 

# Student Goals

The goal of this work is to destroy, or at least
find limits with my prior work. As inputs for that task
I offer FLASH, a tool kit that ofers a baseline0 implementation
of many of the tools that I think are important. 
Your job is to 

- research alternate ways to implement any part of that  kit
- implemenent on of them
- compare them to FLASH
- show where FLASH falls down
- make a recommendation about 
   - when not to use FLASH and use something else
   - how to improve FLASH to make it let your better thing.
   - how to improve the better thing to make it more like FLASH

Now, of course, you should expect to do better than FLASH. FLASH
is a one-size-fits all tool designed with a "near enough is good
enough" attitude. Specific tools often do better
on specific data sets.  So consider yourself a success if
you prove FLASH a failure!
