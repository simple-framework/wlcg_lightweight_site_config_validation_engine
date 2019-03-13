import config_validation_engine
import click


@click.command()
@click.option('--schema',help='Schema in YAML format to be used for validating the configuration')
@click.option('--config', help= 'Configuration file to be validated against the scecified schema')
def config_validation(schema, config):
    click.echo(config_validation_engine.validate(schema,config))

if __name__ == '__main__':
    config_validation()