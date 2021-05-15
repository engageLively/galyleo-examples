<img src=../galyleo-logo.png width=200>

# Guide to the Tutorials

There are (at this writing) seven tutorials in this directory.  They are:

1. create-table: learn how to create a Galyleo Table from a CSV file or PANDAS frame
2. load-table: learn how to send the created table to a Dashboard
3. filter-table: learn how to filter the columns of a table by value or range
4. create-view: use filters, column selection and ordering to prepare the data for a dynamic chart
5. create-chart: create a chart that takes as its inputs a view
6. use-chart-as-filter: Every chart is also a filter; use this to do data drill-downs
7. add-images-text-and-shapes: Add images, text, and shapes, and style them

These tutorials are in roughly the order that a person would go through in order to create a dashboard; of course, there is a great deal of iteration involved here, too.  Each tutorial is designed to teach a specific set of techniques and familiarize the reader with those techniques.  They aren't a substitute for the [User Guide](https://galyleo-user-docs.readthedocs.io/en/latest/), nor do they intend to show complete examples (the demos directory does that).

Most of the tutorials use a dataset of UFO sightings from 1949 to the present, by the National UFO Reporting Center (NUFORC).  We obtained the dataset from [Kaggle](https://www.kaggle.com/NUFORC/ufo-sightings), which credits Sigmond Axel for the data, and we thank them.  The dataset is in the file ufos.csv, in this directory.  The columns are:
1. Date: date in days since Mar 1, 1948 (day 0)
2. Month: Month of the year (1 = January, 12 = December)
3. Year
4. timeofday: morning, afternoon, or night
5. country: two-letter country code
6. state: two-letter state code (only meaningful for US and Canada)
7. type: type of sighting.  One of ['delta', 'formation', 'fireball', 'triangle', 'egg', 'cross', 'cone', 'dome', 'diamond', 'rectangle', 'changed', 'round', 'other', 'teardrop', 'light', 'cigar', 'cylinder', 'hexagon', 'pyramid', 'oval', 'crescent', 'chevron', 'circle', 'disk', 'flash', 'flare', 'changing', 'sphere', 'unknown']
8. Duration: duration in seconds of the sighting

We have cleaned and simplified the dataset somewhat for the purposes of these tutorials.  Those interested in doing any serious work on this question should use the original dataset from Kaggle.

Comments are welcome!  Please use the bug reporting form or send email to galyleo-support@engagelively.com
