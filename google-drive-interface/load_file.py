from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from dotenv import load_dotenv
import os
load_dotenv('../.env')

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)

upload_file_list = ['data_report.html', 'report_data_plot.html']
for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': os.environ.get("GDRIVE_FOLDER_ID")}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.