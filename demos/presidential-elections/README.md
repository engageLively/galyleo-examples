<img src= ../../galyleo-logo.png width=200>

# The Presidential Election Dashboard
The Cook Political Report maintains a database of US Presidential Elections, going from 1828-1920.  The election for every state
and year is in this database, with over 2000 individual state elections represented.  A graphic version of this is at
[elections](https://editor.engagelively.com/lively.freezer/frozenParts/rick/US_Presidential_Election/index.html).  In this tutorial, we'll
walk through the construction of that dashboard, which illustrates many of the components of Galyleo.

## Step 1, Preparation:

(This step can be skipped: to skip, use elections.csv in this directory).

Download the database from: [Cook Political Report Elections Database](https://docs.google.com/spreadsheets/d/1D-edaVHTnZNhVU840EPUhz3Cgd7m39Urx7HM8Pq6Pus/edit#gid=29622862).  Delete columns OJ-QG and B-HO, and rows 55-60.  After this, check column DD, Row 2.   This is the entry for Teddy Roosevelt in the 1904 election.  At this writing (4/26/2021) the Cook database has this (erroneously) as "Democratic".  Teddy Roosevelt was a Republican, so change this if the error is still there.  Further, the entry for Millard Fillmore in 1856 has two dashes, so delete " - "Know-Nothing" (in the South) / Whig (in the North)" (this is in ET, Row 2).  Save the result as a csv file.  The result  is elections.csv in this directory.

# Building the Dashboard

Detailed instructions for building the dashboard are in BuildingTheDashboard.md