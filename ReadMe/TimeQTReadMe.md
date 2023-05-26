# Install in NORMAL terminal
pip install PyQt6 PyQt6-tools pyqt6-plugins
Once PyQt6 is installed, locate the installation folder. 
It is typically located in the Python installation's Scripts or bin directory.
use to get the directory
~~~
pip show PyQt6
~~~

add the below paths to system's PATH environment variable.
~~~
C:\Users\Shane\AppData\Local\Programs\Python\Python311\Scripts\
C:\Users\Shane\AppData\Local\Programs\Python\Python311\Lib\site-packages\PyQt6
~~~

Open the Start menu and search for "Environment Variables" or "Edit the system environment variables".
Click on the "Edit the system environment variables" option that appears in the search results. 
This will open the System Properties dialog.

In the System Properties dialog, click on the "Environment Variables" button. This will open the Environment Variables dialog.

In the Environment Variables dialog, locate the "Path" variable under the "System variables" section and select it. Click on the "Edit" button.

The Edit Environment Variable dialog will open. Here, you can add or modify the paths in the variable value.

Add the path to the PyQt6 installation folder to the list of paths.
C:\Users\Shane\AppData\Local\Programs\Python\Python311\Scripts\
C:\Users\Shane\AppData\Local\Programs\Python\Python311\Lib\site-packages\PyQt6

Click "OK" to save the changes in the Edit Environment Variable dialog, then click "OK" again in the Environment Variables dialog.

Restart your computer for the changes to take effect.
## Designer file is in directory
C:\Users\Shane\AppData\Local\Programs\Python\Python311\Lib\site-packages\PySide6

#  Install on terminal in enviroment
cntrl shift P to make a enviroment in vs code.
~~~
pip install screeninfo
pip install PyQt6 PyQt6-tools QT-PyQt-PySide-Custom-Widgets
~~~

## for images you need to edit the .ui file
~~~
<string notr="true">border-image: url(:/Resources/GM_Logo_400x63.png);</string>
~~~
to (take out ':/')
~~~
<string notr="true">border-image: url(Resources/GM_Logo_400x63.png);</string>
~~~

# Create Executable Applications in Python. https://pyinstaller.org/en/stable/
# for my project
~~~
pyinstaller --onefile --name Timer --windowed --add-data "Icons;Icons" --add-data "TimerQT.ui;." --add-data "TimerQTwin2.ui;." Timer1.py
~~~

# Other PyInstaller commands
~~~
pip install pyinstaller
pip install --upgrade pyinstaller
pip uninstall typing

pyinstaller Timer1.py --onefile --name MyExecutable --windowed       # makes a name for your exe "MyExecutable" and --window No Terminal window opens
pyinstaller Timer1.py --onefile                                      # Terminal window will open with the GUI
pyinstaller --add-data "TimerQT.ui;." Timer1.py                      # creates directory
pyinstaller --add-data "Icons:Icons" Timer1.py
pyinstaller --add-data 'src/README.txt:.' myscript.py
~~~

Icons/gravity-media-logo-1920.png