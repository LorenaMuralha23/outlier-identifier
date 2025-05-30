import click
import processing
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import processing as pc


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


@click.command()
@click.argument("csv-path", required=True)
@click.option("--csv-path", help="remove outliers from your data")
def proccess_outliers(csv_path):
    click.clear()
    outlier_detection_method = inquirer.select(message="Escolha o método de detecção de outliers:",
                                               choices=[
                                                   "1 - IQR (Intervalo Interquartil)",
                                                   "2 - Z-Score",
                                                   "3 - Mad (Desvio Absoluto da Mediana)"
                                               ],
                                               default="1 - IQR (Intervalo Interquartil)",
                                               ).execute()
    pc.proccessing_outliers(csv_path, outlier_detection_method)
