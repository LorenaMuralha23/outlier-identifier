import click
import processing


@click.command()
@click.argument("name", default="Astronaut")
def hello_astronaut(name):
    click.echo(f"Hey, {name}! Your are using the outlier_identifier!")


@click.command()
@click.argument("csv_path", required=True)
@click.option("--csv_path", help="import your .csv file")
def import_csv_command(csv_path):
    click.echo("Ok! Importing csv...")
    processing.read_csv(csv_path)
