<img src= ../../galyleo-logo.png width=200>

# Senate Elections
This example shows Senate Elections in the years 1976-2020.   It uses the [MIT Senate Elections dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/PEJ5QU).  States are color-coded according to which party won, using the usual colors: red for Republican, Blue for Democratic, with the strength of the color measuring the strength of the victory.  The slider controls the year, and clicking on a state shows the detail for that state on the drill-down charts (state vote history, percentage of the vote in that election, and actual votes cast in that election).

## Special Elections
One interesting feature of this dashboard is the toggle Special Elections widget.  A Special US Senate Election is held on a vacancy to the Senate, and is often (e.g., 1992 in California, 2020 in Georgia, 2018 in Mississippi) held at the same time as the regular election.  When the Special toggle is false, regular elections are shown; when the special toggle is true, only special elections are shown.

# Implementation
The data set was downloaded from [MIT Senate Elections dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/PEJ5QU), and uses columns 'year', 'state', 'special', 'candidate', 'party_simplified', 'candidatevotes', 'totalvotes'.  The Notebook  adds a 'percentage' computation.  Candidates with < 1% of the vote were stripped out for clarity; all cleansing and preparation is done in Notebook.ipynb.  The original MIT dataset  is in 1976-2020-senate.csv.  The Senate Control dataset was compiled by hand, and is in senate-control.csv.

## Use of Pandas
The Presidential Elections Notebook used only raw Python; this Notebook uses Pandas to illustrate the power of this library/analytics environment.  The net is that this Notebook is only 35 lines of code, largely because Pandas abstracted away most of the complex operations.

## Seeing the Dashboard
The final  dashboard can be found at [Senate Elections](https://galyleobeta.engagelively.com/public/galyleo/index.html?dashboard=https://raw.githubusercontent.com/engageLively/galyleo-examples/main/demos/senate-elections/senate-elections.gd.json)

