<img src= ../../galyleo-logo.png width=200>

# Florence Nightingale's Dataset
Modern hospital care and nursing can be said to have begun with the English statistician and nurse [Florence Nightingale](https://en.wikipedia.org/wiki/Florence_Nightingale).  During the [Crimean War](https://en.wikipedia.org/wiki/Crimean_War), Ms. Nightingale tended to wounded troops, and invented modern hospital practices: primarily, sanitation and disinfection.  To show the efficacy of her techniques, she counted deaths due to disease, wounds, and undetermined causes, showing that disease was the primary killer in war.  She showed that after her reforms, deaths dropped dramatically, and deaths due to disease more so.

## Using the Dashboard
The dataset comprises 24 months' worth of disease, wound, and other death data.  Months 1-12 (April, 1854 - March, 1856) are pre- Ms. Nightingale's reforms.  Months 13-24 (April, 1855-March 1856) are post-reform.  As a result, the dashboard is in two halves, with double sliders controlling each half.  Move the sliders to adjust the x-axis bounds for the line charts; click on a bar on the line charts to see detail.  Comparing data from each period shows the efficacy of the reforms, and is one of the most influential visualizations ever made.

## Viewing the Dashboard
The final dashboard can be viewed at [Florence Nightingale Dashboard](https://galyleobeta.engagelively.com/public/galyleo/index.html?dashboard=https://raw.githubusercontent.com/engageLively/galyleo-examples/main/demos/nightingale/nightingale.gd.json)

## Original Dataset attribution
The original dataset is taken from [Nightingale's Rose](https://github.com/datasets-io/nightingales-rose/), and is copyright the [Compute.io](https://github.com/compute-io) authors.

## Dataset Augmentation
The original dataset is augmented by Pandas operations in Notebook.ipynb.  The resulting summary table is saved in nightingale.csv; the detail table in records.csv.
