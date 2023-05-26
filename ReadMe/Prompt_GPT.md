# General Questions
Don't respond until I ask you to respond. I'm going to paste you my code files.
Here is my python code. 
Here is my TimerQT.ui file. 
Here is my TimerQTWin2.ui file. 

# Create the QT designer file TimerQT.ui

Create a designer "TimerQT.ui" file for the following requirements:

- Row 1: 
  - Frame 1 with a label named "segment_label".
  - QLabel named "segment_timer".
  - Button named "segment_reset_btn".

- Row 2: 
  - Frame 2 with a label named "total_time_Label".
  - QLabel named "total_timer".
  - Button named "all_reset_btn".

- Row 3: 
  - Frame 3 with a button named "stop_start_btn".

- Row 4: 
  - Frame 4 with a tablewidget named "user_input".
  - It has 3 columns: "Segment", "Segment Time", and "Total Time".
  - Column 2 and column 3 are QLCDNumber.
  - At the bottom of the table, there is a button named "table_reset_btn".

# Create the Python Code

1. Create a Python code with the designer UI file called "TimerQT.ui" using PyQt6. This file defines the user interface layout for the main window of the application.
2. Implement Timer 1 as an up timer counter with hours, minutes, and seconds displayed in the QLabel widget "segment_timer".
3. Implement Timer 2 as an up timer counter with hours, minutes, and seconds displayed in the QLabel widget "total_timer".
4. Initialize both Timer 1 and Timer 2 with a time value of 0.
5. When the "all_reset_btn" button is clicked, reset both Timer 1 and Timer 2 to 0, and update the UI accordingly. Also, reflect the reset state in the "stop_start_btn" button.
6. When the "segment_reset_btn" button is clicked, only Timer 1 should be reset to 0.
7. Implement the "start_stop" method to control the timers. When the "stop_start_btn" button is clicked, it should start or stop both timers accordingly. Update the UI to reflect the current state.
8. Extend the functionality of the "segment_reset_btn" button. In addition to resetting Timer 1, display a user prompt text box to get the segment name. Save the entered text in column 1 of the "user_input" table. Also, save the current value of Timer 1 in column 2. Calculate and display the cumulative total time for each row in column 3.
9. Implement validation for column 2 in the "user_input" table. When the user edits a cell, store the current value. If the entered time format (hours, minutes, and seconds) is invalid, show a message box indicating the incorrect format and restore the previous value.
10. Update the total time in column 3 of all rows in the "user_input" table whenever any value is changed. Ensure that changes in column 2 adhere to the time format.
11. The "table_reset_btn" button should clear the contents of the "user_input" table.
12. Create a separate window called "SecondWindow" by creating a new class that loads the corresponding "TimerQTWin2.ui" file. This window will display additional timer information.
13. Update the code to synchronize the "segment_timer" and "total_timer" labels between the main window and the "SecondWindow". Both windows should reflect the same timer values.
14. Implement code to check for the presence of a second monitor. If a second monitor is detected, open the "SecondWindow" in full screen on the second monitor. Otherwise, display both windows side by side with the same size, accommodating single monitor systems.
15. Ensure that if the QMainWindow is closed, the "SecondWindow" is also closed.

