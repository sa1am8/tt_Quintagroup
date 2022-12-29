### INTRODUCTION ###

***

This repository created as Test Task in Quintagroup Company. Executing main file (main.py) makes API requests, that 
returns in console as grouped information in this order:

* Information about every task (separated by 2 empty lines), that had been found in 
every workspace related to this api_key like:
    > id - 63ac2dea0820e00afea3fd6c
name - TestTask 3
projectId - 63ac1e810820e00afea2ba94
assigneeIds - []
assigneeId - None
userGroupIds - []
estimate - PT0S
status - ACTIVE
duration - PT1M7S
billable - True
hourlyRate - None
costRate - None

* Total time duration of all tasks (summing from every workspace)
  > Total time duration:  1:26:17

* Total time duration of all tasks grouped by date
  > 2022-12-29 - 0:00:04
  
  > 2022-12-28 - 1:26:13


### ABOUT SOLUTION ###

***

In this solution I used FOP principles. Used requests library to use API methods.
In additional.py I created a few get_links() functions, to order separate from main.py all strings written by API.
Also here determinated global variables.

Main.py starts by getting information about every workspace (by provided api_key).
After that for evey user in each workspace opens every time_entry in order to get time duration for all task grouped by day.
Then, for every project it gets whole information about and counting sum duration.

After all manipulations, code execution prints information mentioned in INTRODUCTION

Also there oop_solution.py file, that contains unfinished code solution using OOP principles.
I will try end this solution variant too, but i am not sure. Winter Holidays are coming.

### SETUP ###

***

For setup run next command:

> pip install -r requirements.txt

Then you need to create file "secret" in this directory, include your secret key API.
Following instructions can be performed by next command:

> echo "YOUR_API_KEY_HERE" > secret

### RUNNING ###

***

After successful setup run next command:

> python main.py 
