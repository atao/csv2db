import sqlite3
import sys

import click
import pandas as pd


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(version='1', prog_name="Convert CSV to SQLite Database.")
@click.option('--csvfile', '-i', help='CSV file', required=True, type=str)
@click.option('--separator', '-sep', default=";", show_default=True, help='CSV field separator.')
@click.option('--chunksize', '-chk', default=10000, show_default=True, help='Number of rows per chunk to process.')
@click.option('--database', '-d', default='database.db', help='Database name.', show_default=True, type=str)
@click.option('--table-name', '-t', default='data', help='Table name.', show_default=True, type=str)
@click.option('--include-index', '-idx', is_flag=True, default=False, show_default=True,
              help='Include index in SQLite Database.')
@click.option('--verbose', '-v', is_flag=True, help="Verbose mode.")
def cli(verbose, csvfile, separator, chunksize, database, table_name, include_index):
    # Check args
    if not database.endswith(".db"):
        database = '{}.db'.format(database)
    if not csvfile.endswith(".csv"):
        csvfile = '{}.csv'.format(csvfile)

    # Create a connection to the SQLite database
    conn = sqlite3.connect(database)
    if verbose:
        print(f"[+] Importing {csvfile} into SQLite database {database}")
    try:
        # Read the CSV file and import data in chunks
        for chunk in pd.read_csv(csvfile, chunksize=chunksize, sep=separator):
            chunk.to_sql(name=table_name, con=conn, if_exists='append', index=include_index)
            conn.commit()  # Commit after each chunk
            if verbose:
                print(f"[+] {len(chunk)} rows added to the database")
    except Exception as e:
        conn.rollback()  # Rollback on error
        if verbose:
            print(f"[!] An error occurred during import: {e}")
    finally:
        conn.close()  # Close the connection

    if verbose:
        print(f"[+] CSV data import process completed.")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        cli.main(['--help'])
    else:
        cli()
