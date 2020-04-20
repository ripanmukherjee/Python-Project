To download the file from the supplier onto our linux-instance virtual machine we will first grant executable permission to the download_drive_file.sh script.


>>> $  sudo chmod +x ~/download_drive_file.sh
>>> $ ./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
>>> $ tar xf ~/supplier-data.tar.gz

To test out your script, you can install the stress tool.
>>> $ sudo apt install stress

Next, call the tool using a good number of CPUs to fully load our CPU resources:
>>> $ stress --cpu 8

Then run the health_check.py descriptions


Now, you will be setting a cron job that executes the script health_check.py every 60 seconds and sends health status to the respective user.

To set a user cron job use the following command:

>>> $ crontab -e

Enter 1 to open in the nano editor. Now, set the complete path for health_check.py script, and save by clicking Ctrl-o, Enter key, and Ctrl-x.
