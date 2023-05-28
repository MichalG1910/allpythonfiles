# Project Name
E_Rates
https://www.flynerd.pl/2018/06/jak-napisac-dobre-readme-projektu-na-githubie.html

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- The application is used to download/visualize current and historical exchange rates from a given time period published by the National Bank of Poland (NBP). It uses the bank's API (api.nbp.pl).
- The aim of the project was to expand the knowledge and consolidate the author's skills in programming in Python and to use in practice knowledge of SQL and Postgresql databases.


## Technologies Used
- python 3.11.2
- PostgreSQL 15.2
- Tkinter 8.6
- Matplotlib 3.5.2


## Features
List the ready features here:
- Works on operating systems: Linux, Windows
- Three working modes:
  - online - all necessary data are downloaded from NBP servers (database is not required)
  - online with a database - after starting, it creates/updates the database. All data later is retrieved from this current database.
  - offline - runs without internet connection. All data is taken from the database.
- Available in two themes: dark and light
- Current tables: average exchange rates, bid/ask exchange rates
- Generating charts of exchange rates in relation to PLN in various display configurations:
  - 1 currency rate chart in the main window
  - from 1 to 15 currency charts in one fullscreen window
  - from 1 to all published exchange rates on one chart in a fullscreen window
  - with a trend line,
  - with min/max value
  - each generated graph can be saved in .png format in default directory "Reports"
  - available time periods: 30 days, 60 days, 90 days, half a year, one year, 2 years, 5 years, 10 years, 15 years
- Generating reports in a given time period (start date, end date):
  - in .txt format with full tables for each day
  - in .csv format (ready to be imported into a spreadsheet)
  - each generated report is saved in the default directory "Reports"  


## Screenshots
![dark mode main window](https://github.com/MichalG1910/allpythonfiles/img/dark_mode_main_window.png)
![light mode main window](https://github.com/MichalG1910/allpythonfiles/img/light_mode_main_window.png)
![15 charts in fullscreen mode](https://github.com/MichalG1910/allpythonfiles/img/15_charts.png)
![one multichart in fullscreen mode](https://github.com/MichalG1910/allpythonfiles/img/one_multichart.png)




## Setup
What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located?

Proceed to describe how to install / setup one's local environment / get started with the project.


## Usage
How does one go about using it?
Provide various use cases and code examples here.

`write-your-code-here`


## Project Status
Project is: _in progress_ / _complete_ / _no longer being worked on_. If you are no longer working on it, provide reasons why.


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2


## Acknowledgements
Give credit here.
- This project was inspired by...
- This project was based on [this tutorial](https://www.example.com).
- Many thanks to...


## Contact
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
