import sys

import click
from loguru import logger

import model
import server
from validate import parse_csv_and_validate


@click.group()
def cli():
    print("Bye")


@cli.command()
@click.option("--data", type=click.Path(exists=True))
@click.option("--output", type=click.Path(exists=False))
@click.option("--test_size", type=click.FloatRange(min=0.0, max=1.0), default=0.33)
@click.option("--random_state", type=click.FLOAT, default=None)
def train(data, output, test_size, random_state):
    logger.info(f"Training on data={data} and saving to {output}")
    valid, invalid = parse_csv_and_validate(data)
    logger.info(f"Done validating. # Valid = {len(valid)} # Invalid = {len(invalid)}")

    m = model.train(valid, test_size=test_size, random_state=random_state)
    model.save(m, output)


@cli.command()
@click.option("--model_file", type=click.Path(exists=True), required=True)
def serve(model_file):
    logger.info("Booting the server...")
    m = model.load(model_file)
    server.serve(m)


if __name__ == "__main__":
    logger.info(f"Called SimpleML with args: {sys.argv}")
    cli()
