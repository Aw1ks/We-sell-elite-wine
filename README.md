# We-sell-elite-wine
This project downloads data from an excel spreadsheet and from a file image template.html creates a file index.html with the substituted data.
## How to launch
This project uses libraries such as: [os](https://docs.python.org/3/library/os.html), [dotenv](https://betterdatascience-page.pages.dev/python-dotenv/), [datetime](https://docs.python.org/3/library/datetime.html), [pandas](https://pandas.pydata.org/), [http.server](https://docs.python.org/3/library/http.server.html), [jinja2](https://pypi.org/project/Jinja2/) and [collections](https://docs.python.org/3/library/collections.html).
Python3 should already be installed. Use `pip `(or `pip3`, there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
you will need to save the name of your excel spreadsheet in an `.env` file.
```
EXCEL_TABLE=table_name.xlsx
```
## Environment variables
Environment variables are key—value pairs that determine the settings and behavior of the operating system and programs. 
```
EXCEL_TABLE='your excel spreadsheet'
```
## How to check
To check the final result of the project, run the file (main.py ) with the:
```
python main.py
```
If you have correctly linked the code to the excel spreadsheet and configured the file template.htm then a file should be created that looks like index.html
