**********************************************************    
    Personal Financial Managing Web Application Prototype
    CSE 6242 Project
    Authors:
        1. Anqi Zou
        2. Holly Williams
        3. Rahul Agrawal
        4. Yi Ding
*********************************************************

Usage
--------
Open index.html in Firefox. For chrome, open chrome with "--allow-file-access-from-files" permission.
The app has been tested for resolutions of 1600x900 and above. Some of the visualizations might not appear
as expected, for lower resolutions.

The other html files are referenced from index.html and can be viewed independently as well.


Directory Structure
-----------------------

./
    index.html - Main file, the home page of the project. This references other files of the project.
    CalendarView.html - "My monthly expenses" view. Calendar-based monthly expense view
    README.txt - This file.
    SplitExpenses.html - "My Split Expenses" view.
    userExpenses.html - "Home" page. Shows expenses for the current user.
    weeklyExpenses.html - "My weekly Expenses" view
    yearlyExpenses.html - "My yearly Expenses" view
    css/
        bootstrap-responsive.css - Twitter bootstrap files
        bootstrap-responsive.min.css - Twitter bootstrap files
        bootstrap.css - Twitter bootstrap files
        bootstrap.min.css - Twitter bootstrap files
        calendar-view.css - css for Calendear view
        font-awesome.min.css - css for icons on Calendar view
    data/  - Simulated data files. See report for schema and data generation details.
        Expenses.csv
        ExpenseUser.csv
        expense_table.txt
        expense_user_table.txt
    data scripts/ - Scripts used for creating simulated expenses
        Categorize.py
        CreateExpenses.py
    font/  - Icons file for category icons (http://fortawesome.github.io/Font-Awesome/)
        ...
    js/ - Javascript files that the projects uses. utils.js & calendar-view.js are created by us. Rest are standard libraries. HTML files contain javascript code as well.
        bootstrap-modal.js
        bootstrap-popover.js
        bootstrap-tooltip.js
        bootstrap.calendar.js
        bootstrap.js
        bootstrap.min.js
        calendar-view.js
        jquery-1.9.1.min.js
        jquery-ui.min.js
        jquery.min.js
        jquery.slimscroll.min.js
        utils.js