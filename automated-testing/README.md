# automated-testing
You should replace python3 with python and pip3 with pip if you have Python3 (not Python2) as the default Python

## making sure we are using the latest pip
python3 -m pip install --upgrade pip

## python packages to install
### some basic stuff
pip3 install argparse --upgrade

pip3 install PyYAML --upgrade

pip3 install lxml --upgrade

pip3 install httplib2 --upgrade

### for imaging
pip3 install pillow --upgrade

### no python installation should run without pandas and numpy
pip3 install pandas --upgrade

pip3 install numpy --upgrade

### all Google and Microsoft stuff
pip3 install oauth2client --upgrade

pip3 install PyDrive --upgrade

pip3 install python-docx --upgrade

pip3 install pygsheets --upgrade

pip3 install xlsxwriter --upgrade

pip3 install openpyxl --upgrade

### latex stuff with Jinja templating
pip3 install jinja2 --upgrade

pip3 install latex --upgrade

pip3 install latex2pdf --upgrade

### finally Selenium
pip install selenium --upgrade

## Webdriver locations
Chrome:   https://sites.google.com/a/chromium.org/chromedriver/downloads

Firefox:  https://github.com/mozilla/geckodriver/releases

Edge:     https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Safari:   https://webkit.org/blog/6900/webdriver-support-in-safari-10/

