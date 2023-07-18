<img src= ../../galyleo-logo.png width=200>

# BigQuery Example
This example shows how to load data from Google BigQuery into a Galyleo Table, via a Pandas Dataframe.  Pandas is a ubiquitous data science framework for tabular data, which we use here.  In particular, Google's BigQuery Python library supports download into a Pandas dataframe, and the GalyleoTable supports input from a dataframe.  Note that further conditioning of the data is often required (we don't show that here); replacing missing values with NaNs in numeric columns, ensuring that timestamps and datatimes are in the right format, etc.

The Google BigQuery library requires a Google Cloud account and  authentication, which this example doesn't cover.  See the tutorial at https://codelabs.developers.google.com/codelabs/cloud-bigquery-python, 

To run this tutorial, a service account must be created and the key stored in /home/jovyan/key.json.  If it is stored elsewhere, make the appropriate changes to the Notebook.