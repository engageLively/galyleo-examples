<img src= ../../galyleo-logo.png width=200>

# Senate Elections
This example is similar to Presidential Elections.  It uses the [MIT Senate Elections dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/PEJ5QU), using columns 'year', 'state', 'special', 'candidate', 'party_simplified', 'candidatevotes', 'totalvotes', to which it adds a 'percentage' computation.  Candidates with < 1% of the vote were stripped out for clarity; all cleansing and preparation is done in Notebook.ipynb.  The original MIT dataset  is in 1976-2020-senate.csv.  The Senate Control dataset was compiled by hand, and is in senate-control.csv.

## Use of Pandas
The Presidential Elections Notebook used only raw Python; this Notebook uses Pandas to illustrate the power of this library/analytics environment.  The net is that this Notebook is only 35 lines of code, largely because Pandas abstracted away most of the complex operations.

## Special Elections
One interesting feature of this dashboard is the toggle Special Elections widget.  A Special US Senate Election is held on a vacancy to the Senate, and is often (e.g., 1992 in California, 2020 in Georgia, 2018 in Mississippi) held at the same time as the regular election.  When the Special toggle is false, regular elections are shown; when the special toggle is true, only special elections are shown.