# election_analysis

## Project Overview
The purpose of this project is to conduct an election audit for the Colorado Board of Elections. The outcome of the congressional election audit will determine, voter turnout of each county, percentage of votes from each county out of the total count, county name which has highest turnout.

A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local
congressional election.
1. Calculate the total number of votes cast.

2. Get a complete list of candidates who received votes.

3. Calculate the total number of votes each candidate received.

4. Calculate the percentage of votes each candidate won.

5. Determine the winner of the election based on popular vote.



## Resources

- Data Source: election results.csv

Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary

The analysis of the election show that:
There were "369,711" votes cast in the election.
The candidates were:

- Candidate 1 : Charles Casper Stockham

- Candidate 2 : Diana DeGette

- Candidate 3 : Raymon Anthony Doane


The candidate results were:

- Candidate 1 received "23.0%" of the vote and "85,213" number of votes.

- Candidate 2 received "73.8%" of the vote and "272,892" number of votes.

- Candidate 3 received "3.1%" of the vote and "11,606" number of votes.

The winner of the election was:

- Candidate 2, who received "73.8%" of the vote and "73.8" number of votes.

- Winner: Diana DeGette

- Winning Vote Count: 73.8

- Winning Percentage: 73.8%

## Overview

Election Audit requested additional data to complete the audit, such as 

1. Calculate voter turnout of each county.

2. Calculate  percentage of votes from each county out of the total count

3. Find out the county name which has highest turnout

## Results

Additional for loop helped to find out the following result.

The following results I got after the analysis

- Total Votes in the election - 369,711

- County name, % of total votes, total votes

- Jefferson: 10.5%  (38855)

- Denver: 82.8%  (306055)

- Arapahoe: 6.7%  (24801)

- Largest Country Turnout - Denver

## Summary

I could find out voter turnout of each county, percentage of votes from each county out of the total count, ounty name which has highest turnout by adding another for loop but we can have more detailed results if we use this script with additional for loop and Id statements to analyse the larger data set too.

Election commission can use this script to get election results. We can make some changes in the script and use this script to analyze larger data, such as,
1. If we are considering statewide or country wide election, we can add a for loop for city_names, another for loop for state_name and widen our analysis to find out election results.

2. We can find out how many people registered for the voting and how many people actually voted.
