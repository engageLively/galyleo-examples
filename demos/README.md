<img src= ../galyleo-logo.png width=200>

# Demonstration Examples

There are three demonstrations in this directory.  Each comes with a description of the example, a Notebook, and a Dashboard file.  The three demos at this writing are:

1. presidential-elections.  The Notebook is in Elections.ipynb, and the dashboard file in elections.gd.json.  The dataset is originally from the [Cook Political Report](https://cookpolitical.com/) [database of Presidential elections](https://docs.google.com/spreadsheets/d/1D-edaVHTnZNhVU840EPUhz3Cgd7m39Urx7HM8Pq6Pus/edit#gid=29622862).  A cleaned version is in the file elections.csv.  Electoral college results are in the file electoral_college.csv

2. ufos.  The original dataset is taken from the  [National UFO Reporting Center (NUFORC)](http://www.nuforc.org/), cleansed by Sigmond Axel, and can be found as a [Kaggle dataset](https://www.kaggle.com/NUFORC/ufo-sightings), or at a [Github repo](https://github.com/planetsig/ufo-reports).  A slightly cleansed version is in the ufos.csv file in the directory.  The Notebook is in Notebook.ipynb and the dashboard in ufos.gd.json

3. ufos-pandas.  This is the same dataset and dashboard as in UFOs, but Notebook.ipynb has been adapted to using [Pandas](https://pandas.pydata.org/), and is an example of how to effectively construct a dashboard from Pandas dataframes.