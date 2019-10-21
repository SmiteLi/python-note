import click

@click.command()
@click.option('--count')
@click.option('--name', prompt='you name', help='the person to greet.')
def hello(count, name):

    """get name for a total count times."""
    for x in range(count):
        click.echo('hello %s!' % name)

if __name__ == "__main__":
    hello()
