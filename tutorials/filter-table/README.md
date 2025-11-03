<img src=../../galyleo-logo.png width=200>

# Tutorial 3: Techniques for Filtering Data

This tutorial demonstrates  building a filter to filter rows from one or more tables in response to user inputs
# What You'll Learn

1. Creating a Filter
2. The difference between range and select filters, and what each type is used for.
3. The different filter widgets (to date) in Galyleo
# Prerequisites

1. Create Table
2. Publish Table
# Uses

1. Galyleo Dashboards

# Instructions
Launch a new dashboard.  You should see this.
![Table Tab on screen](images/initial_table.png)

These tables are identical to the tables you see by clicking "View Tables" on the Galyleo Service.

![Galyleo Tables](images/galyleo-tables.png)

Click on "Filters" to bring up the filters tab, then click on "Add Filter".  The Filter builder/editor will pop up, inviting you to build a filter.  Type in the name, select the kind of widget to use (more below), the table containing the column and the column to filter.  Then click Create.

![Filter Dialog](images/filter-dialog-new.png)

When you click Create, the widget appears in the top-left and the filter name appears in the filter list.  A gear button next to the filter lets you edit it.

![Filter UI](images/filter-ui.png)

Let's create another filter.  A slider is an example of a select filter; it chooses a single value, and (when applied to a Table) selects only rows whose column value for the selected column is equal to the filter value.  Click on Add Filter, and this time, choose column = Month and widget type = doubleSlider from the popup. Give it a name MonthSlider.  You'll see a slider with two knobs appear.  This slider selects a range of values, inclusing.  Setting the lower value to 6 and the upper to 9 chooses months 6-9 (June-September) inclusive, and it will select all rows where the month column is 6, 7, 8, 9.

![Double Slider](images/two-sliders.png)

Finally, clicking on the selection/edit button on the top right will let you edit the set of filters, so you can click on that and delete filters by clicking on the delete button to the left of the filter name.  Let's go ahead and delete MonthSlider.

![Delete Filter](images/delete-filter.png)
