# Remote Presidential Elections
This demo shows how to use Remote, or Virtual, Tables.  A Remote Table is a table that is served by a Galyleo Table Server.  A demonstration server, which gives the Presidential Election Data, has been set up at https://engagelively.wl.r.appspot.com/, and we'll use that to set this up.   To run this demo:
1. In the Launcher, launch a new Galyleo Table file 
2. Open RemoteElections.ipynb
3. Note that the tables in the JSON file are empty
4. Execute the cells in the Notebook
5. Note that the tables are now there.  Create a few visual elements -- the file remote-elections.gd.json has two, to give you a feel for how it is done.

The important thing  is that _nothing in Galyleo changes with Remote, or Virtual, Tables, aside from the fact that the <rows> tag in a table definition has been replaced by a <connector> tag, which contains the URL and polling information.
Note also that Remote and local tables can be mixed freely and easily.