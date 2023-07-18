<img src= ../../galyleo-logo.png width=200>

# Google Sheets
This demo shows how to load data into a Galyleo Table using Google Sheets.  This is actually straightforward; once a Google Sheet is shared, it's quite easy to download to a Pandas dataframe.  Simply change the suffix of the Google Sheet URL  from  "edit?usp=sharing" to "export?format=csv" in the code, and then it reads directly into a Pandas dataframe with `pandas.read_csv(url)`.  At that point, the pandas dataframe can be loaded directly into a GalyleoTable.
