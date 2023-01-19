<img src= ../galyleo-logo.png width=200>

# Galyleo Quickstart

Build a dashboard from scratch in under two minutes! In this exercise, we're going to build about half of the [Florence Nightingale Dashboard](https://galyleobeta.engagelively.com/public/galyleo/index.html?dashboard=https://raw.githubusercontent.com/engageLively/galyleo-examples/main/demos/nightingale/nightingale.gd.json).  To make this easy, we've set up the data and the Notebook to process it for the dashboard, so all you have to do is run it to populate the dashboard with data. 

1. Use the star icon on the launcher to launch a Galyleo Notebook.

<img src = images/launcher_shot.png width = 800>

You'll see an "untitled.gd.json" tab open up, and it will look like this:

<img src = images/blank_dashboard_shot.png width = 800>

2. Open the Notebook.ipynb file, and use shift-enter to execute its single cell

<img src = images/notebook_shot.png width = 800>

3. Click back to the `untitled.gd.json` tab, open the right sidebar with the knob

<img src = images/sidebar.png width = 800>

And click on the Tables tab to see this:

<img src = images/dashboard_with_tables.png width = 800>

4. Click on the Filter Tab and click the Create Button to bring up the Filter Dialog, choose "month" as the column, "doubleSlider" as the Filter type, and make the name "MonthFilter"

<img src = images/filter_dialog.png width = 800>

5. Click OK and the Filter appears in the top left.  Drag it to wherever you want on the dashboard

<img src = images/filter_shot.png width = 800>

6.  Click on the View Tab and Click on the Create Button.  A View Builder Dialog pops up.  Choose "Summary" as the Table, type in "SummaryMonth" as the View name, click OK

<img src = images/view_dialog_1.png width = 800>

7. A View Editor  pops up.  Click "Select All" in the top left to select all the columns, then click on the box next to MonthFilter, then   click OK

<img src = images/view_editor_1.png width = 800>

8. Click on the Chart Tab and Click on the Create Button.  A Chart Builder Dialog pops up. Select "SummaryMonth" from the dropdown as the data source for the chart, and type "SummaryMonth" as the name of the chart as well (you can pick any name that isn't the name of another Chart or a Filter, but picking the same name as the View helps you keep them straight).   Click OK.

<img src = images/chart_dialog.png width = 800>

9. The Chart appears (as a table) in the top-left corner, and a Chart Editor appears in the center of the screen.  Click on Column Chart and click OK

<img src = images/chart_editor_1.png width = 800>

10. The Chart Editor disappears, leaving the column chart in the top left.  Drag it to wherever you want on the dashboard.

11. Time to do a drill-down; we want to see the detail for a month when we click on the SummaryMonth chart.  Click on the Views Tab, click Create, and choose "Detail" as the source table and make the name of the View "MonthDetail"

<img src = images/view_dialog_2.png width = 800>

12. A View Editor pops up.  Click the boxes next to "cause" and "deaths" in the top (column selector) box, then click on the box next to SummaryMonth, in the bottom box then   click OK

<img src = images/view_editor_2.png width = 800>

13. Click on the Chart Tab and Click on the Create Button.  Select "MonthDetail" from the dropdown as the data source for the chart, and type "MonthDetail" as the name of the chart as well.   Click OK.

<img src = images/chart_dialog.png width = 800>

14. Click on Pie  Chart in the Chart Editor click OK. Drag the pie chart to wherever you want.

<img src = images/chart_editor_2.png width = 800>

15.  By default, the Dashboard is in Select Mode when you are in the Dashboard Studio and designing the Dashboard.  This means, when you click on a widget, the widget is selected.  For testing, though, you want to interact with the widget.  So click on the hand in the top bar to go into Interaction Mode (clicking on the arrow beside it will put you back into Select Mode)

<img src = images/interaction_select.png width = 800>

16.  Play with the dashboard!  Moving the knobs on the sliders will telescope the x-axis on the column chart; clicking on a bar will select that month for the detail chart.

<img src = images/final_dashboard.png width = 800>

17.  Save the dashboard file, and rename it to `florence.gd.json`.  Then copy it to any location where it gets an URL (the easy way to do this is to put it into a github repository) and then view it in any browser by entering 'https://galyleobeta.engagelively.com/public/galyleo/index.html?dashboard=<URL for your dashboard>`


