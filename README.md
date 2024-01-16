# csv2db
📋 Convert CSV to SQLite Database.

## Purpose

Easily transform a csv file into a SQLite database.

## Requirements
```
pip install -r requirements.txt
```

## Usage and options

```
Usage: csv2db.py [OPTIONS]

Options:
  --version                       Show the version and exit.
  -i, --csvfile TEXT              CSV file  [required]
  -d, --database TEXT             Database name.  [default: database.db]
  -t, --table TEXT                Table name.  [default: data]
  -m, --mode [fail|replace|append]
                                  if data already exist do  [default: fail]
  -v, --verbose                   Verbose mode.
  -h, --help                      Show this message and exit.
```

## Quickstart
Just run for example :
```python
csv2db.py --csvfile mycsv.csv --database mycsv.db --table mydata --mode replace --verbose
```

Output :
```
[+] Reading file mycsv.csv
[+] Using columns : Index(['ID', 'Logged At', 'Not Before', 'Not After', 'Common Name',
       'Matching Identities', 'Issuer Name'],
      dtype='object')
[+] Insert into "mycsv.db" with "mydata" as table name
[+] Using mode : replace
```