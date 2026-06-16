<img src= ../galyleo-logo.png width=200>

# Galyleo Quickstart

Build a dashboard from scratch in under two minutes! In this exercise, we're going to build about half of the [Florence Nightingale Dashboard](https://engagelively.github.io/galyleo-dashboard/?dashboard=https://raw.githubusercontent.com/engageLively/galyleo-examples/feature/static-gcs-deploy/demos/published/dashboards/nightingale.gd.json).  To make this easy, we've set up the data and the Notebook to process it for the dashboard, so all you have to do is run it to populate the dashboard with data. 

1. Use the star icon on the launcher to launch a Galyleo Dashboard.

<img src = images/launcher_shot.png width = 800>

You'll see an "untitled.gd.json" tab open up, and it will look like this:

<img src = images/blank_dashboard_shot.png width = 800>

2. Open the right sidebar with the knob.

<img src = images/sidebar.png width = 800>

And click on the Tables tab to see this:

<img src = images/dashboard_with_tables.png width = 800>

3. The Tables tab is pre-populated with all the tables that you have access to in the Galyleo Service.  You can leave them all (there is no downside to having too many tables available), but for convenience, clarity, and keeping your dashboard file minimal and neat, it's better to delete the tables you won't use.  Click on the edit button at the top right of the Tables tab

<img src = images/dashboard_with_tables_edit.png width = 800>

Red "delete" buttons will appear to the left of each table:

<img src = images/dashboard_editing_tables.png width = 800>

4. Click on the delete buttons for every table except "tables/rick.mcgeer@engagelively.com/nightingale.sdml" and "tables/rick.mcgeer@engagelively.com/records.sdml".  Click on the edit button again to get rid of the red circles.   You'll be left with two tables:

<img src = images/dashboard_tables_done.png width = 800>

5.  Click on the Filter Tab and click the Add Filter Button to bring up the Filter Dialog, choose "month" as the column, "doubleSlider" as the Filter type,  make the name "MonthFilter" and choose "rick.mcgeer@engagelively.com/nightingale.sdml" as the table.

<img src = images/filter_dialog.png width = 800>

6. Click "Create Filter" and the Filter appears in the top left.  Drag it to wherever you want on the dashboard

<img src = images/filter_shot.png width = 800>

7.  Click on the Views Tab and Click on the Add View Button.  A View Builder Dialog pops up.  Choose "rick.mcgeer@engagelively.com/nightingale.sdml" as the Table, type in "SummaryMonth" as the View name, click Create View.

<img src = images/view_dialog_1.png width = 800>

8. A View Editor  pops up.  Click  on the boxes "month", "Other rate", "Disease rate" and "Wounds rate"  to select those columns ("month" since it is first, will be the x-axis), then click on the box next to MonthFilter, so the slider picks the months, then click Update View.  The effect of this will be for the MonthFilter to zoom the x-axis  on a chart that uses Summary Month as its view.

<img src = images/view_editor_1.png width = 800>

9. Click on the Charts Tab and Click on the Add Chart Button.  A Chart Builder Dialog pops up. Select "SummaryMonth" from the dropdown as the data source for the chart, and type "SummaryMonth" as the name of the chart as well (you can pick any name that isn't the name of another Chart or a Filter, but picking the same name as the View helps you keep them straight).   Click Create.

<img src = images/chart_dialog.png width = 800>

10. The Chart appears (as a table) in the top-left corner, and a Chart Editor appears in the center of the screen.  This is the Google Chart Editor; it's exactly the same editor that's used to edit charts in Google Sheets. Click on Column Chart and click OK.

<img src = images/chart_editor_1.png width = 800>

11. The Chart Editor disappears, leaving the column chart in the top left.  Drag it to wherever you want on the dashboard.

12. Time to do a drill-down; we want to see the detail for a month when we click on the SummaryMonth chart.  *In Galyleo, every chart is a filter and can be used to select values in a view*.  The filter is always a *Select* filter.  It picks a single value for the column, and the value chosen is the value on the *x* or category axis.  The name of the filter is the name of the chart.  In this case, clicking on the SummaryMonth chart picks the month for the bar it was clicked on.   Click on the Views Tab, click Add View, and choose "rickmcgeer@engagelively.com/records.sdml" as the source table.  Make the name of the View "MonthDetail".

<img src = images/view_dialog_2.png width = 800>

13. A View Editor pops up.  Click the boxes next to "cause" and "deaths" in the top (column selector) box, then click on the box next to SummaryMonth in the bottom box, then click Update view.

<img src = images/view_editor_2.png width = 800>

14. Click on the Charts Tab and Click on the Add Chart Button.  Select "MonthDetail" from the dropdown as the data source for the chart, and type "MonthDetail" as the name of the chart as well.   Click Create chart.

<img src = images/chart_dialog2.png width = 800>

15. Click on Pie  Chart in the Chart Editor.  

<img src = images/chart_editor_2.png width = 800>

Click OK now if you want, but Google chooses the colors on charts independently, so often the colors for the categories on the SummaryMonth chart won't agree with the colors on the MonthDetail chart.  You can click on the "Customize" tab, just as in Google Sheets, to choose the right colors for the data values.  Click OK when you are done.

<img src = images/chart_customize_colors.png width = 800>

16.  Drag the pie chart to wherever you want.  To drag *anything* (image, shape, filter, chart, text) in Galyleo, click on the object when Editing mode is selected (arrow in the top left of the top bar, as it is now).  A "halo" of tools appears around the object, like this:

<img src = images/halo.png width = 800>

Grab the cross symbol for drag; to resize the object, just grab and drag any of the resize knobs at the corners.  The other tools are rotate (bottom left), trash (top right), and menu (top left).  The menu is primarily used to bring objects to the front or send them to the back.  Click anywhere outside of the object to make the halo disappear.

17.  By default, the Dashboard is in Select Mode when you are in the Dashboard Studio and designing the Dashboard.  This means, when you click on a widget, the widget is selected.  For testing, though, you want to interact with the widget.  So click on the hand in the top bar to go into Interaction Mode (clicking on the arrow beside it will put you back into Select Mode)

<img src = images/interaction_select.png width = 800>

18.  Play with the dashboard!  Moving the knobs on the sliders will telescope the x-axis on the column chart; clicking on a bar will select that month for the detail chart.

<img src = images/final_dashboard.png width = 800>

19.  Rename  the dashboard file.  Right-click on the dashboard file in the file menu:

<img src = images/rename-menu.png width = 800>

20.  Type 'nightingale.gd.json' as the file name:

<img src = images/rename-done.png width = 800>

21.  Now it's time to publish the dashboard.  Click on the "Publish" button on the top bar, and a Publish dialog will appear.  Type in "florence.gd.json" in the name box and hit the "Publish" button.

<img src = images/publish_dialog.png width = 800>

22.  An alert box will appear telling you how you can view the dashboard.

<img src = images/publish_success.png width = 800>

23. Click on the lower link, and you will see your dashboard in a new browser tab.

<img src = images/published_dashboard.png width = 800>

24. Click on the upper link, and you will see the JSON form of your dashboard in a new browser tab.

<img src = images/json_dashboard.png width = 800>

25. By default, only you can view a published dashboard.  To share the dashboard, click on the Galyleo Menu and choose Galyleo Service.

<img src = images/galyleo_service.png width = 800>

26. The Galyleo service will appear in a new tab. Click on View Dashboards

<img src = images/galyleo_service_2.png width = 800>

27.  And click on the "Share" button beside the florence.gd.json entry.  This brings up a page which lists Hub users with whom the dashboard is shared.  Click "Remove" next to the ones you no longer wish to share.  If you wish to share with additional users, enter their emails in the text box and click "Add" (they must have Hub accounts).  If you want to share with all Hub users, click the "Shared with Hub" checkbox.  Be sure to click "Save Changes".

<img src = images/share_view.png width = 800>

28.  Congratulations on publishing your first dashboard!
    

