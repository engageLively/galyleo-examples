# Techniques for Table Creation using the Galyleo Table Library
This tutorial demonstrates the various techniques for creating Galyleo Tables, saving them, and loading them from disk.

# What You'll Learn
1. Creating a Galyleo Table
2. Loading it with data from a dictionary; from JSON; from a Pandas Dataframe
3. Saving the table to disk
4. Loading from disk

# Prerequisites
None

# Uses
1. A Jupyter Notebook

# A Galyleo Table
A Galyleo Table is the foundation of a Galyleo Dashboard; all data are contained in Tables.  A Table is a dictionary with
fields "columns" and "rows".  The columns field is a list of dictionaries.  Each dictionary has two fields, "name", and "type".
The "type" field must be one of the Galyleo types, defined in the library galyleo.galyleo_constants: GALYLEO_NUMBER, GALYLEO_BOOLEAN, GALYLEO_STRING, GALYLEO_DATE, GALYLEO_DATETIME, GALYLEO_TIME_OF_DAY. 

The "rows" field of a table consists of a list of lists.  To be valid, a table must obey the following:

1. The length of each row must be equal to the length of the columns: `[len(row) == len(columns) for row in rows]`
2. The type of the jth element of each row must match the type declared in the jth column `[matchType(row[j], column[j]["type"]) for j in range(len(row))]`

where a float or int matches GALYLEO_NUMBER, True or False matches GALYLEO_BOOLEAN, and anything matches GALYLEO_STRING.
Here is an example table:
```
    {
        "columns": [{"name": "name", "type": GALYLEO_STRING}, {"name": "age", "type": GALYLEO_NUMBER}]
        "rows": [['tom', 23], ['teresa', 22], ['jill', 36], ['jack', 47], ['dick', 33], ['jennifer', 47], ['harry', 28], ['meghan', 23]]
    }
```

