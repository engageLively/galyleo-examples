<img src= ../../galyleo-logo.png width=200>

# UFO Sightings
The [National UFO Reporting Center (NUFORC)](http://www.nuforc.org/) maintains a database of over 80,000 UFO sightings over the last century.  NUFORC, a volunteer organization, cautions its visitors that "We always caution visitors to our website to be discriminating with regard to what information posted there they accept as being true and accurate", and this dataset should be taken with that in mind.  This is particularly the case recently, since [Starlink satellites have been deployed across the night sky](https://en.wikipedia.org/wiki/Starlink), forming arresting images of lines of satellites in the night sky:
![Starlink train] (images/starlink_train.jpg)

## The Dataset

The dataset was put into CSV form by Sigmond Axel, and can be found as a [Kaggle dataset](https://www.kaggle.com/NUFORC/ufo-sightings), or at a [Github repo](https://github.com/planetsig/ufo-reports).  We based the dataset on the Kaggle dataset.  The dataset, after a little cleaning, is in the file ufos.csv in this directory.  The 
fields, their types, and semantics are:

| Field     | Type           | Semantics                                                                        |
|-----------|----------------|----------------------------------------------------------------------------------|
| date      | GALYLEO_NUMBER | Number of days since March 1, 1948                                               |
| month     | GALYLEO_NUMBER | Month, as a number, 1-12                                                         |
| year      | GALYLEO_NUMBER | Year of sighting, four digits                                                    |
| timeofday | GALYLEO_STRING | morning, afternoon, or night                                                     |
| country   | GALYLEO_STRING | two-letter country code                                                          |
| state     | GALYLEO_STRING | two-letter state code  -- only meaningful if the country is Canada or the USA    |
| type      | GALYLEO_STRING | type of the object -- sphere, light, triangle, disk, cylinder, other, or unknown |
| duration  | GALYLEO_NUMBER | Duration of the sighting, in seconds                                             |

## The Notebook
The Notebook  aggregates the data, counting the number of incidents by various dimensions.  The central goal is to aggregate by year, month and year, month and type, on both a worldwide and US basis.  The following tables are computed:

| Table | Fields | Description |
|-------|--------|-------------|
| aggregate_cy| country, year, count | Sightings by country and year |
| aggregate_cmy| country, month, year, count | Sightings by country, year and month |
| aggregate_cyt| country, year, type, count | Sightings by country, year and type |
| aggregate_sy| state, year, count | Sightings by state and year  (US only)|
| aggregate_sym| country, month, year, count | Sightings by state, year and month  (US only) |
| aggregate_cyt| country, year, type, count | Sightings by state, year and type  (US only) |

## The Dashboard

Here we describe the Filters, Views, and Charts in the dashboard.  The tables of the dashboard were already covered by the Notebook section, above

### Filters

There is only one _explicit_ filter on the dashboard, a slider which selects the year.  The maps are used as implicit filters, as described below.

#### Views

There are six views on the dashboard, one per chart.  They are:

| View | Table | Columns | Filters | Semantics |
|------|-------|---------|---------|-----------|
| CountryCount | aggregate_cy | country, count | YearFilter | Count of UFO sightings by country for selected year |
| StateYear | aggregate_sy | state, count | YearFilter | Count of UFO sightings by stated for selected year (US only) |
| CountryMonth | aggregate_cym | month, count | YearFilter, CountryCount (chart) | Count of UFO sightings by month for selected year and country |
| StateMonth | aggregate_sym | month, count | YearFilter, StateYear (chart) | Count of UFO sightings by month for selected year and state |
| CountryType | aggregate_cyt | type, count | YearFilter, CountryCount (chart) | Count of UFO sightings by type for selected year and country |
| StateType | aggregate_syt | type, count | YearFilter, StateYear (chart) | Count of UFO sightings by type for selected state and year |

### Charts

There are six charts on the dashboard, one per view.  They are:

| Chart | Type | View |
|-------|------|------|
| CountryCount | GeoChart | CountryCount |
| StateYear | GeoChart | StateYear |
| CountryMonth | Column Chart | CountryMonth |
| StateMonth | Column Chart | StateMonth |
| CountryType | Pie Chart | CountryType |
| StateType | Pie Chart | StateType |

## Credits

*Image Credit*: "Starlink 5 train - 21st April 2020 21:19 BST" by jabberwock is licensed with CC BY-SA 2.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/2.0/