# automated-testing

# preparation and configuration
assuming you are in the directory ```gsheet-selenium```, if not cd to the directory
1. run ```pip install -r requirements.txt --upgrade```
2. make sure you have a directory named ```drivers``` under ```gsheet-selenium```, if not create one
3. from the webdriver locations download webdrivers for at least Chrome and Firefox for your OS and keep them under ```drivers``` directory
4. make sure you have a ```credential.json``` file under ```gsheet-selenium/conf```, if not ask for one and put it there
5. make a copy of ```gsheet-selenium/conf/config.yml.dist``` to ```gsheet-selenium/conf/config.yml```
6. edit ```gsheet-selenium/conf/config.yml``` as per your test specification

  * line 30 *test/data/gsheet* should be the gsheet name of your test spec

  * line 32 *test/data/module* you should specify the exact module name (.py file name without extension) for this test spec, you will find module files under ```src/helper/gsheet``` folder. Normally the module is named very much after the test spec
  * line 34 *test/data/class* you should specify the class name for this test spec, you will find module files under ```src/helper/gsheet``` folder

  * line 38 *test/driver/module* you should specify the exact module name (.py file name without extension) for this test spec, you will find module files under ```src/helper/selenium``` folder. Normally the module is named very much after the test spec
  * line 40 *test/driver/class* you should specify the class name for this test spec, you will find module files under ```src/helper/selenium``` folder

  * line 44 *test/log-writer/module* you may specify as *helper.xlsx.xlsx_writer* if you do not have any custom writer for this test spec
  * line 46 *test/log-writer/class* you may specify as *XlsxLogWriter* if you do not have any custom writer for this test spec

## Webdriver locations
* Chrome:   https://sites.google.com/chromium.org/driver/
* Firefox:  https://github.com/mozilla/geckodriver/releases
* Edge:     https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
* Safari:   https://webkit.org/blog/6900/webdriver-support-in-safari-10/


# running the tests
You can find a sample test spec named NBR-UMS__test-spec__login at https://docs.google.com/spreadsheets/d/1G0z_Al6d_zubtsjeWeEqwTsgAqUdHoeXE4UGZdjJWHU
1. if you are in Linux, run ```selenium-from-gsheet.sh```
2. if you are in Windows, run ```selenium-from-gsheet.bat```
