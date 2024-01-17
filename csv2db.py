import sqlite3
import sys
import click
import pandas as pd


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(version='1', prog_name="Convert CSV to SQLite Database.")
@click.option('--csvfile', '-i', help='CSV file', required=True, type=str)
@click.option('--database', '-d', default='database.db', help='Database name.', show_default=True, type=str)
@click.option('--table', '-t', default='data', help='Table name.', show_default=True, type=str)
@click.option('--mode', '-m', type=click.Choice(['fail', 'replace', 'append'], case_sensitive=False),
              help='if data already exist do...', default='fail', show_default=True)
@click.option('--verbose', '-v', is_flag=True, help="Verbose mode.")
def cli(verbose, csvfile, database, table, mode):
    # Check args
    if not database.endswith(".db"):
        database = '{}.db'.format(database)
    if not csvfile.endswith(".csv"):
        csvfile = '{}.csv'.format(csvfile)
    if mode:
        mode = mode.lower()

    # Import data in DataFrame
    if verbose:
        print("[+] Reading file {}".format(csvfile))
    df = pd.read_csv(csvfile)
    if verbose:
        print(df.info(verbose=True))
    # Insert to database
    if verbose:
        print('[+] Insert into "{}" with "{}" as table name\n[+] Using mode : {}'.format(database, table, mode))
    conn = sqlite3.connect(database)
    try:
        df.to_sql(con=conn, name=table, if_exists=mode)
    except ValueError as e:
        print("[!] Error : {}".format(e))
        exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        cli.main(['--help'])
    else:
        cli()
