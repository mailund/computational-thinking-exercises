# Searching and Sorting

## Selection sort

**Exercise:** Give an example input where selection sort is not stable.

## Insertion sort

**Exercise:** Describe what the input list should look like to achieve best-case and worst-case time performance, respectively.

## Bubble sort

**Exercise:** Since O₁ and O₂ tells us that the last j elements are already the largest numbers and are already sorted, we do not need to have the inner loop iterate through these last j elements. How would you exploit this to improve the running time of bubble sort? The worst-case behaviour will not improve, but you can change the running time to about half of the one we have above. Show that this is the case.

**Exercise:** With cocktail sort, after running the outer loop j times, both the first j and the last j elements are in their final positions. Show that this is the case.

**Exercise:** Knowing that both the first and last j elements are already in their right position can be used to iterate over fewer elements in the inner loops. Modify the algorithm to exploit this. The worst case complexity will still be O(n²), but you will make fewer comparisons. How much do you reduce the number of comparisons by?

## Comparison sort comparison

**Exercise:** Insertion sort runs in O(n²) when the input is sorted in the reverse order, but can process sorted sequences in O(n). If we can recognise that the input is ordered in reverse, we could first reverse the sequence and then run the insertion sort. Show that we can reverse a sequence, in place, in O(n). Try to adapt insertion sort, so you first recognise consecutive runs of non-increasing elements, then reverse these before you run insertion sort on the result. Show that the worst-case running time is still O(n²), but try to compare the modified algorithm with the traditional insertion sort to see if it works better in practice.

## Bucket sort 

**Exercise:** Argue why the inner loop when we collect results only executes n times.

**Exercise:** Argue why the bucket sort actually sorts the input.

## Two-complement representation of negative numbers

**Exercise:** Show that with this representation, if you take the numbers -n,-n+1,…,-1,0 and sort them as binary numbers, you get a reversed sort of the negative numbers. This is why, if we do radix sort of signed integers by extracting $k$-bit sub-keys and sort this as unsigned integers, the negative numbers get sorted in reverse order. Because negative numbers will have the most significant bit set to one, while positive numbers will have it set to zero, the negative numbers will end up at the end of such a sorted list.
