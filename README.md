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
  --version                  Show the version and exit.
  -i, --csvfile TEXT         CSV file  [required]
  -sep, --separator TEXT     CSV field separator.  [default: ;]
  -chk, --chunksize INTEGER  Number of rows per chunk to process.  [default:
                             10000]
  -d, --database TEXT        Database name.  [default: database.db]
  -t, --table-name TEXT      Table name.  [default: data]
  -idx, --include-index      Include index in SQLite Database.
  -v, --verbose              Verbose mode.
  -h, --help                 Show this message and exit.
```

## Quickstart
Just run for example :
```
(.venv) ME > python .\csv2db.py -i .\adresses-31.csv -sep ";" -chk 10000 -d 31 -idx -v
```

Output :
```
[+] Importing .\adresses-31.csv into SQLite database 31.db
[+] 10000 rows added to the database
[+] 10000 rows added to the database
...
[+] 10000 rows added to the database
[+] 5214 rows added to the database
[+] CSV data import process completed.
```