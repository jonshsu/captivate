
# CaptivateIQ Coding Challenge
Jonathan Hsu
10/5/2019

## Overview
For this project I built an interactive spreadsheet using the template provided. You can view the live demo at [https://jonathanhsu.me/OLD/captivate/](https://jonathanhsu.me/OLD/captivate/). Spreadsheet data is stored as  json {"A": {"1": "celldata", ... }, ... }.

The live demo is a static page that gets/updates spreadsheet data through javascript fetches to [https://jsonbin.io](https://jsonbin.io/). I did this because I ran out of free Google Cloud credit for running a Flask app and database, and the single html page worked for this project. The html file is from the the rendered Flask page and I just changed the get/update functions to fetch from jsonbin instead of the server's endpoint.

In the github repo, `index.html` in the root dir is the demo page I uploaded. You can run the server with the same setup instructions as in the original readme provided. I added routes in `server.py` for getting/updating the spreadsheet data through the server. `templates/index.html` contains the same javascript as in index.html. If I were to actually run a server/database for handling the data, I would need to update the route functions in `server.py` to get/put instead of using a global dict. 

### Functionality 
The spreadsheet json is loaded once initially and then replaced/updated whenever the user makes changes. All the actual spreadshet logic is handled by the browser and can be found in the `<script>` tags in either `index.html` file. 

I handle arithmetic expressions by generating a new object
`display_data` from the fetched `raw_data` object. Cells display `display_data`, which holds the parsed/evaluated arithmetic expressions. When you click on a cell, its data is switched to `raw_data` for editing, and you can edit a cell's `raw_data` through the top bar as well. When you de-focus the cell or press enter, the  expression is evaluated, the cell switches to the new `display_data` and sends the new `raw_data` to the server. Here's a flowchart of how user interactions work in my code:


The spreadsheet can handle any number of cell additions (ex. "=A1+B2+B2+C3+..."), and cells with invalid expressions (ex. "=HELLO", "=A1-B1") show up as "Invalid". Cells with circular or self-references show up as "Circular". Here's how evaluating/calculating these expressions works:



Features:
- When a user clicks a cell, 

Python/Flask
Serverless, database, gsheet
  requests go directly to jsonbin.io because I can't host, secret key
  all of the logic is done on frontend inline script
setup/run/demo, website

functionality
  summary behavior/assumptions - like excel/sheets
  logic flowchart
  evalFormula
  demo

Conclusions
  future work, scalability, efficiency
  how I would architect/build an actual collaborative sheets-like environment
    nodejs, CRDT
  related work
    frontend/bootstrap:
      Obviously bootstrap one-day frontend
      Picnichealth react one-day frontend
      Mango forum node.js backend 