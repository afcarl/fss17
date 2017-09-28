---
title: Privacy with Lace2
published: true
---

Lesson: Everything is data mining

Fayola Peters, Tim Menzies, and Lucas Layman. 2015. LACE2: better privacy-preserving data sharing for cross project defect prediction. In Proceedings of the 37th International Conference on Software Engineering - Volume 1 (ICSE '15), Vol. 1. IEEE Press, Piscataway, NJ, USA, 801-811.

http://menzies.us/pdf/15lace2.pdf

## Lace2


Before a community can learn general principles, it
must share individual experiences. Data sharing is the fundamental
step of cross project defect prediction, i.e. the process of
using data from one project to predict for defects in another.
Prior work on secure data sharing allowed data owners to share
their data on a single-party basis for defect prediction via data
minimization and obfuscation. However the studied method did
not consider that bigger data required the data owner to share
more of their data.

In this paper, we extend previous work with LACE2 which
reduces the amount of data shared by using multi-party data
sharing. Here:

- data owners incrementally add data to a cache
passed among them and contribute â€œinteresting€ data that are
not similar to the current content of the cache. 
-  before data
owner i passes the cache to data owner j, privacy is preserved
by applying obfuscation algorithms to hide project details. 

The
experiments of this paper show that (a) LACE2 is comparatively
less expensive than the single-party approach and (b) the multi party
approach of LACE2 yields higher privacy than the prior
approach without damaging predictive efficacy (indeed, in some
cases, LACE2 leads to better defect predictors).


## Privacy concerns:

- At a keynote address
at ESEMâ€™11, Elaine Weyuker doubted that she will ever
be able to release the AT&T data she used to build defect
predictors 
- Due to similar privacy concerns, we were
only able to add seven records from two years of work to
our NASA-wide software cost metrics repository.
- In a
personal communication, Barry Boehm stated that he was able
to publish less than 200 cost estimation records even after 30
years of COCOMO effort.

## The LACE Approach


- Private data remains with data owner inside firewalls.
- All the algorithms are run behind firewalls by data owners.
Hence, in LACE, there is no need for a central server or
some third party privatization service.
- Most data are never shared. LACE prunes away most of
the data while retaining â€œinteresting€ data points.
- The shared data are obfuscated such that queries to that
data return different values than in the raw data.
- Obfuscation of the data does not change the classifications
of the training data. That is, LACE privatizes data without
damaging data mining efficacy.

## The Privacy problem:

Privacy
threats are classified as

1. identity disclosure or re-identification,
2. membership disclosure, 
3. sensitive attribute disclosure

Lace2 directly addresses 3; indirectly addresses 1,2


###  Re-identification occurs

An attacker uses  external information such as a voters
list, can re-identify an individual from data that has been
stripped of personally identifiable information such as a social
security number. Prominent examples of this are the
re-identification of Governor William Weld from released health-care
data and Thelma Arnold from the AOL search data.

### Membership disclosure

Focuses
on protecting a personâ€™s micro data. 

- If an
attacker is able to confirm that the target€™s data is contained
in a particular data set.

For example, if the data set contains
information only on HIV patients, then the attacker can infer
that the target is HIV-positive.

### Sensitive attribute disclosure 

When a target is associated
with information about their sensitive attributes, such
as software code complexity. 
For example:

- In the case of
defect data, one attribute that might want to be kept hidden
are the lines of code (loc) associated with the shared data.
It is well documented that loc is highly correlated to development
effort  and development effort is something most
organizations wish to keep private (since it effects how many
billable hours they can charge their clients).

## Inside Lace

### Assumptions

LACE2 assumes data is _not extreme_ i.e. For example, consider a case where Microsoft
Windows and several small â€œstartupsâ€ contribute to a private
cache. Even with the random perturbation in MORPH (described
in Â§III-D3), it will be obvious which defect data came Msoft

### Homogeneous Transfer

All attributes same in all data sets. For Heterogeneous Transfer Learning, see 
Jaechang Nam and Sunghun Kim. 2015. Heterogeneous defect prediction. In Proceedings of the 2015 10th Joint Meeting on Foundations of Software Engineering (ESEC/FSE 2015). ACM, New York, NY, USA, 508-519. DOI: https://doi.org/10.1145/2786805.2786814

## Leaf + CLiff + Morph

Leaf = leader follower algorithm for collecting data

- Run a cache over n data sources do
- Add to the cache anything anomalous in data source i

### Steps

1. The initiator (data owner) is chosen at random.
2, Data owner applies CLIFF to identify the subset of data
that best represents the target classes. Only the data selected
by CLIFF are used in LACE.
3. If the data owners decided to use LACE1 then go to
the next step, otherwise, with LACE2, LeaF is applied to
further prune the CLIFFed data and facilitate collaboration
among data owners.
4. The results are then obfuscated with MORPH
and privacy is measured.
5. Steps 2-4 are repeated until a user defined privacy criterion
is met. Once this is achieved, the MORPHed data is added
to the private cache.
6. The private cache is sent to the next randomly chosen site
(data owner), where they execute Step 2. As in Step 3, if
LACE1 is used then move on to Step 4, otherwise, with
LACE2 test each instance of their CLIFFed data using
LeaF with the private cache. The test involves each instance
finding its nearest exemplar in the private cache. If the
instance and exemplar are a certain distance away, then
the new instance is MORPHed and added to the cache.
7. The private cache moves on to the next random data owner
and Steps 2-6 are repeated.
8. The protocol is complete when all data owners involved
have had a chance to contribute to the private cache. This
final private cache can be added to a public data repository


### Cliff= Data Reduction 

Discretize all numerics (supervised)

Rank ranges by their _power_ often them appear in one class more than others

- L(H,E) = like(H|E) = P(E|H) * P(H)
- e.g. if "loc=hi" appears 100 times in the 1000 defective rows and there are 10000 rows then
     - 100/1000 * 1000/11,000
- a good range appears a lot in one class, and more often than note
     - prob*support
     - L(H,E)**2 / (L(H,E) + L(notH,E))

Sort columns by their average power. Keep the most powerful rows of each class.

Sort rows by the sum of the _power_ of their ranges. Delete lower half

### Leaf= Follow the leader:

- Given a distance measure between rows.
- Cluster data, find centroids
      - Using k_NN
- New data arrives
     - Find its distance to nearest centroid 
     - If D small, ignore data
     - If D large, add to that cluster

To compute _large D_, find median distance to centroid of 100 random items in a cluster

### Morph= Mutate

Within each cluster. Find nearest row of another class. Mutate this row by a distance between
0.15 and 0.35 towards that other guy.

### Measure privacy

A=X%: Find out how much of data is not added to cache 

B= (100-X%)*IPR
- Pick an attribute range
- Find all rows in raw data with that range
- Find all rows in privatizes data with that range
- Increased piracy ratio = division of those two numbers.

Report A*B

- Typical numbers> 99%
- Mostly in how much data is removed (usually, 84%)

## Results,

see slides 47..56 of https://www.slideshare.net/timmenzies/icse15-techbriefing-data-science

see fig 3 of http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7972992

