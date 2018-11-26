
# FlaskGroup instance to extend the normal CLI with commands related to the Flask app.

from flask.cli import FlaskGroup

from project import app

cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()