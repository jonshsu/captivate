# CaptivateIQ Coding Challenge
Jonathan Hsu
10/6/2019

## Overview
For this project I built an interactive spreadsheet using the template provided. You can view the live demo at [https://captivate-spreadsheet.herokuapp.com/](https://captivate-spreadsheet.herokuapp.com/) and all my code is in this repo. The 'Load Demo' button loads a sheet with some test values. 

I haven't used Flask before so this was a fun way to learn. I modified the starter code `app.py` with new api methods and kept the frontend `templates/index.html` mostly the same apart from some ids. Spreadsheet data is stored as  json {"A": {"1": "celldata", ... }, ... } locally and in the database, and all the spreadsheet logic happens in the browser through the `static/script.js` file. I am using Heroku and Heroku Postgres to run this project. 

You can run the server with the same setup instructions as in the original prompt's readme but you'll have to configure/migrate the database yourself. 

### Functionality 
The spreadsheet data json is stored as a text entry in the `spreadsheetdata` table, and the POST/GET server endpoints in `app.py` update and retrieve the string. 

In `static/script.js`, the spreadsheet json is loaded into `raw_data` once initially. When the user makes changes, `raw_data` is sent back to the database to replace/update the data. `display_data` is generated from `raw_data` and stores the results of the evaluated expressions. 

Cells display the parsed/evaluated expressions in `display_data`. When you click on a cell, its data is switched to `raw_data` for editing, and you can edit a cell's `raw_data` through the top bar as well. When you de-focus the cell or press enter, the  expression is evaluated, the cell switches to the new `display_data` and sends the new `raw_data` to the server. [This](https://i.imgur.com/6rg8Vvo.png) is a diagram I drew to keep track of event flow/handlers. 

The spreadsheet can handle any number of cell additions (ex. "=A1+B2+B2+C3+..."), and cells with invalid expressions (ex. "=HELLO", "=A1-B1") show up as "Invalid". Cells with circular or self-references show up as "Circular". Calculating/evaluating the expression happens in `evalFormula()`. The function recursively evaluates cell values and returns the total. 


### Conclusions
Overall this was a pretty fun project! I liked working on the spreadsheet logic and learning how to configure/use Flask. 

Some inefficiencies:
- replacing the entire sheet data on each cell change
- re-calculating recursed expressions for each cell (use dp instead)

Features I could add:
- add support for more expressions
- unique sheets by url
- more excel-like UI
- increased size 

Other considerations:
- using different tools (react, node/express, sql)
- collaborative editing
- testing