<img src= ../../galyleo-logo.png width=200>

# Florence Nightingale's Dataset

Modern hospital care and nursing can be said to have begun with the English statistician and nurse [Florence Nightingale](https://en.wikipedia.org/wiki/Florence_Nightingale). During the [Crimean War](https://en.wikipedia.org/wiki/Crimean_War), Ms. Nightingale tended to wounded troops, and invented modern hospital practices: primarily, sanitation and disinfection. To show the efficacy of her techniques, she counted deaths due to disease, wounds, and undetermined causes, showing that disease was the primary killer in war. She showed that after her reforms, deaths dropped dramatically, and deaths due to disease more so.

## Running the Notebook

Run `Notebook.ipynb` to compute and publish the dataset. The notebook processes the original data and sends a POST request to publish a summary and detail dataset under names like `summary.gd.json` and `records.gd.json`.

Once published, these datasets become available to all dashboards that reference them.

## Viewing the Dashboard

The final dashboard can be viewed at:  
[Florence Nightingale Dashboard](https://galyleobeta.engagelively.com/public/galyleo/index.html?dashboard=https://raw.githubusercontent.com/engageLively/galyleo-examples/main/demos/nightingale/nightingale.gd.json)

The dashboard automatically loads the published datasets and displays their contents. No manual data transfer is required.

## Interacting with the Dashboard

The dataset comprises 24 months' worth of disease, wound, and other death data. Months 1–12 (April 1854 – March 1855) are pre-reform, and Months 13–24 (April 1855 – March 1856) are post-reform. The dashboard is organized in two halves, with double sliders controlling each time period. Use the sliders to adjust x-axis bounds, and click a bar on the line charts for detailed views. The stark contrast between the two periods illustrates the power of Ms. Nightingale’s reforms.

## Original Dataset Attribution

The original dataset is taken from [Nightingale's Rose](https://github.com/datasets-io/nightingales-rose/), and is copyright the [Compute.io](https://github.com/compute-io) authors.

## Dataset Augmentation

The original dataset is augmented using Pandas in the notebook.  
- The summary table is published as `summary.gd.json`  
- The detail table is published as `detail.gd.json`

Once the Notebook is run, the datasets can be viewed using the Galyleo Service.
