# python-misc-Functions
In this project, we have 3 different python files for 3 functions and their unit tests using PyTest library described as follows:
1) find_firstRepNumber.py: A function that gives 2 vectors of integers and finds the first repeated number (Assignment1)
2) find_firstFile.py: A function that given a path of the file system and finds the first file that meets the following requirements [The file owner is admin, The file is executable and The file has a size lower than 14*2^20] (Assignment2)
3) find_minFlipChange.py: A function that gives a sequence of coin flips (0 is tails, 1 is heads) and finds the minimum quantity of permutations so that the sequence ends interspersed. (Assignment3)

test_data1, test_data2, test_data3 and test_data4: test data folders are necessary for the unit test of the find_firstFile.py file which contains different sample data to check this function

report.html: The auto-generated HTML report for unit test results

To execute the unit test and generate the report use the following cmd:
 pytest find_firstFile.py --html=report.html
