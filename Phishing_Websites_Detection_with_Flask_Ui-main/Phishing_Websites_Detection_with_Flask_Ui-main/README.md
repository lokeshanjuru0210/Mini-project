# Phishing_Websites_Detection_with_Flask_Ui

## Requirements : 

 Mongo DB Atlas database 
 A Computer or laptop with Windows OS along with python 3.8 above.
 Chrome Browser (optional)
 
## Procedure : 

To test or try out our project **Phishing Websites Detection with Flask UI**, simply download or clone this repository.

After Downloading or cloning the repository make sure that all the files are in one directory or folder.

If you are using IDE we suggest to make another project i.e., make **another environment** to keep your working environment **safe**. Now , open terminal(**CMD**)  to that directory where you have all the files. And install requirements.txt using 

**pip install -r requirements.txt**

After completing the installation of all files. Now create your own Mongo DB database (ATLAS) .You can even refer to the below link 
https://docs.atlas.mongodb.com/getting-started/  

After creating your database go to the **"database.py"** file and there change the client URL to your URL. 

Now after changing the client URL perfectly just go to app.py and run it . In terminal or console you will get see one link which is local host i.e., the link of the website which is created by FLASK. 

Opening the link in your browser and insert any URL you can enter the  full URL with the protocol i.e., for sample https://www.google.com

After entering the URL  press check now if it is **not a phishy URL** you will be redirected to the website if you have chrome installed in your pc which  
helps to redirect URL using chrome and if it is phishy URL you will not be redirected and  notified there.

