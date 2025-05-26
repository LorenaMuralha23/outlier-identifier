import click


@click.command()
@click.argument("name", default="Astronaut")
def hello_astronaut(name):
    click.echo(f"Hey, {name}! Your are using the outlier_identifier!")
