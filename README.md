# Hadoop Streaming - Name Count

This repo stores codes and scripts that run Hadoop streaming. Hadoop Streaming is used to process Wikipedia articles dump, which is in data folder. 

The name_count_script runs the streaming application. A name in the dataset satisfies following properties:
1. The first character is not a digit
2. The first letter is uppercase, and all the other letters are lowercase
3. When this word appears in the dataset regardless of its case (i.e. the first letter is not necessarily upper case) and condition (2) is not met, the occurrence of such case is less than 0.5%

# Hadoop Streaming - Word Group

Calculate statistics for groups of words that are equal up to permutations of letters. For example, ‘emit’, ‘item’ and ‘time’ are the same words up to a permutation of letters. Determine such groups of words and sum all their counts. Apply stop words filter. Filter out groups that consist of only one word.

Output: count of occurrences for the group of words, number of unique words in the group, comma-separated list of the words in the group in lexicographical order:

sum \<tab\> group size \<tab\> word1,word2,...

Example: assume ‘emit’ occurred 3 times, 'item' -- 2 times, 'time' -- 5 times; 3 + 2 + 5 = 10, group contains 3 words, so for this group result is:

10 3 emit,item,time

It is recommended to use Docker to set up the environment. 
