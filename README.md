# simple_stat

simplestats

Simple statistics mini-tool. Work with copy-paste text boxes in which tab-delimited data are pasted (partly in specific formats still to be decided. 

Mostly one input box for the data to be analysed, and one output box which provides the test results (always including some explanation of how to interpret the test results).



* 1. Descriptive statistics

One box on the left where user pastes numbers (one value per line, line breaks separate the different values). 
Then one button "Calculate"
And one box on the right where the following descriptive statistics are shown (one per line), always preceded like the text in the following so it is clear what is what:

Mean:
Median:
Minimum:
Maximum:
Standard deviation: 
Standard error:
Sum: 
Mean ± standard deviation (Minimum-Maximum): 





* 2. Test for normality
One box on the left where user pastes numbers (one value per line, line breaks separate the different values). 
Then one button "Calculate"
One box on the right where the results of the normality test is shown [it is important that the user can copy-paste the results, so they must be accessible in a box for marking and copying]




* 3. Binomial test


* 4. Fisher's exact test


* 5. Chi square test

* 6. Compare two independent samples (t-Test and U-test)

* 7. Bonferroni correction


# Run the GUI:

```
python stat_tool.py
```


