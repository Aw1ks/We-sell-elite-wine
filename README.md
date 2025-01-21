# We-sell-elite-wine
This project downloads data from an excel spreadsheet and from a file image template.html creates a file index.html with the substituted data.
## How to launch
This project uses libraries such as: [datetime](https://docs.python.org/3/library/datetime.html), [pandas](https://pandas.pydata.org/), [http.server](https://docs.python.org/3/library/http.server.html), [jinja2](https://pypi.org/project/Jinja2/) and [collections](https://docs.python.org/3/library/collections.html).
Python3 should already be installed. Use pip (or pip3, there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
## How to check
To check the final result of the project, run the file (main.py ) with the:
```
python' command main.py
```
If you have correctly linked the code to the [excel](https://github.com/Aw1ks/We-sell-elite-wine/blob/main/wine3.xlsx) spreadsheet and configured the file template.htm then a file should be created that looks like index.html
