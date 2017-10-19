
### Using Gift Card Importer

- Clone the repository

```
   $ git clone https://github.com/codenonprofits/gift-card-importer.git 
```

- Go to project directory
- Create the virtual env (use python 3)

```
$ virtualenv env 
```

- Go to environment
- Install the requirements
```
$ source env/bin/activate
$(env) pip install -r pip-freeze.txt
```

- Change the Parse credentials on settings file `settings.py`
- Run the script passing as parameters the Parse collection name and the file path (xls)

> Note: See the example.xlsx to fill your file with the correct data

```
$(env) python init.py GiftCards /path/to/your/file.xlsx
```

