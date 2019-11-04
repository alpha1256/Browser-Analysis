# Browser-Analysis

This project tracks memory percentage and writes this to a txt file. The data in the file will be use to plot a graph

### Memory Tracker
This program will be tracking memory usuage and will write this to a text file.
In the current implementation to exit the program just enter "CTRL C" which will kill the process. I plan to use timers to schedule when this program should be running. 
To run this program `psutil` needs to be installed. To do this `pip install psutil`


### Memory Graph
This program will create a line chart graph from the previously created text file.
To run this program 'plotly' must be installed. To do this 'pip install plotly==4.2.1'
