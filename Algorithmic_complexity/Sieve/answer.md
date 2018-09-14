# Sieve of Eratosthenes

Recall the Sieve of Eratosthenes from the previous chapter. 

**Exercise:** Derive an upper bound for its running time. 

**Answer:** For each i=1,…,n we potentially iterate through all larger numbers j=i+1,…n. On average this means that we iterate through n/2 numbers for each i, so an upper bound is O(n²).

**Exercise:** Is there a difference between its best-case and worst-case running time?

**Answer:** We do not *actually* iterate through all numbers larger than i. Only those that we have not eliminated as divisible by a number smaller than i. Getting the average number of elements left in the list when we look at prime p is not so straightforward; at least not to me. But we can give it the old college try.

When p=2, we run through n-1 elements—we have all but the first to run through. After that, there are n/2 left. Then, for three we run though those n/2, but we remove every third, so now there are no more than n/3 left. We do not remove a third of those that were left after removing the even numbers—it is not a third of those that are divisible by three—but there can’t be more than a third left of the original list when we have removed those divisible by three. The same argument then goes for p = 5; there can’t be more than a fifth of the original numbers left after that.

We can therefor bound the numbers of elements left after we have processed prime p by n/p. 

You can run the program [count.py](count.py) to see how n/p compares to the actual numbers.

So, an upper bound of the algorithm is O(n + n/2 + n/3 + n/5 + … ) or O(n + n × (sum of 1/p for primes less than n).

The sum here is called the "sum of reciprocals of primes", and this [can be proven](https://www.wikiwand.com/en/Divergence_of_the_sum_of_the_reciprocals_of_the_primes) to be in O(log(log(n)).

So, a tighter bound on the running time is O(n × log(log(n)) ).
