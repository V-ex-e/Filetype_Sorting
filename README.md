# Filetype_Sorting
Data sorting


Filetype_SortingAutomation nothing much too explain a reg ex looking for filetype then accordingly creating a folder with filetype as its name. Feel free to change the current source folder with yours and the destination folder of the created folders.

Video preview: https://www.youtube.com/watch?v=vZcyzNghFxE

How to make the script run in the background

Windows: Task Scheduler: Open Task Scheduler (you can search for it in the Start menu). Create a new task. In the "General" tab, provide a name and description for your task. In the "Triggers" tab, create a new trigger to specify when the task should run. In the "Actions" tab, create a new action with the following settings: Action: Start a program Program/script: Path to your Python executable (e.g., C:\Path\To\Python\python.exe) Add arguments (optional): Path to your script (e.g., C:\Path\To\Your\Script.py) Save the task. Now, your script will run in the background based on the schedule you set.

Unix-based Systems (Linux, macOS): Cron Job: Open the terminal. Open the crontab configuration with the command crontab -e. Add a new line at the end of the file with the following format: ruby Copy code

/path/to/python /path/to/your/script.py This line schedules the script to run every minute. You can customize the schedule based on your needs. Save and exit the editor. Now, your script will run in the background according to the schedule you set using cron.
Keep in mind that running a script continuously in the background may have resource implications, and you should consider the impact on system performance. Additionally, make sure your script handles errors gracefully to avoid unexpected behavior.


Scheduling your script:

schtasks /create /tn "Run Regex Script" /tr "C:\Python39\python.exe C:\path\to\your\script\Regex.py" /sc weekly /d MON /st 09:00

schtasks /create /tn "Run Filetype Script" /tr "C:\Python39\python.exe C:\path\to\your\script\Filetype.py" /sc weekly /d MON /st 09:00
