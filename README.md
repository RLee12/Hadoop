# Hadoop Streaming in Python - Name Count

This repo stores codes and scripts that run Hadoop streaming. Hadoop Streaming is used to process Wikipedia articles dump, which is in data folder. 

The name_count_script runs the streaming application. A name in the dataset satisfies following properties:
1. The first character is not a digit
2. The first letter is uppercase, and all the other letters are lowercase
3. When this word appears in the dataset regardless of its case (i.e. the first letter is not necessarily upper case) and condition (2) is not met, the occurrence of such case is less than 0.5%

Top 20 names in the dataset:

1. american	17215
2. english	7794
3. british	6668
4. john	5762
5. french	5742
6. german	4622
7. york	4457
8. roman	3805
9. europe	3586
10. european	3528
11. greek	3499
12. london	3299
13. america	3156
14. december	3139
15. christian	3135
16. david	3115
17. january	3079
18. england	3073
19. april	3023
20. june	2941 

It is recommended to use Docker to set up the environment. 
