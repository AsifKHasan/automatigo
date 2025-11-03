# what it does

*gsuite-operations* is a Python project that allows one to work on (one or more) Google sheets or Google Drive folders from a shell/terminal with a script named ```work-with-gsuite.sh```. The script has a Windows counterpart ```work-with-gsuite.bat``` with the same behaviour.


# what you need before you can work with it

* Python installed. 3.8+ should work, but the later the Python version is the better
* start shell/terminal at the root folder where you have cloned *gsuite-operations*
* ```pip install -r requirements.txt``` to install the packages required
* a ```../conf/data.yml``` file that you can copy from ```../conf/data/yml.dist```. This is the configuration file telling the script what to do and what are the inputs for desired tasks
* a Google Service aacount credential json file under ```../conf/``` as specified in the *credential-json* element in the config file

Once the above are in place, you can just run
    
```./work-with-gsuite.sh -f```
    
to work on one or more Google Drive folders specified as a list under _drive-folders_ element inside the config file 

or

```./work-with-gsuite.sh gsheet-name```

to work on one Google sheet named _sheet-name_ as specified in the command line

or just

```./work-with-gsuite.sh```

to work on one one or more google sheets whose names are specified in a list under _gsheets_ element inside the config file


# what _work_ can be done on Google Drive folders

Work on (one or more) google drive folder(s). _Work_ means

1. list drive files recursively along with properties like name, parent folder, id, ownership, size, mime type etc.

    ```./work-with-gsuite.sh -f```

    > the option ```-f``` means the script will work on google drive folders, not one or more google sheets or any other object. The folder id's on which the work will be done must be specified as list in ```../conf/data.yml``` under *drive-folders* element.


# what _work_ can be done on Google Sheets

Perform some _Tasks_ on a single google sheet, or on multiple google sheets in batches. _Tasks_ that you can do are many

## cell linking and ordering


## worksheet duplication, removal, renaming


## worksheet creation, formatting and related tasks


## trailing blank row removal, review-notes, column sizing


## add rows and columns


## work on ranges etc.


## find and replace in worksheets


