from flask import Flask

my_awesome_app = Flask(__name__)


@my_awesome_app.route('/', defaults={'path': ''})
@my_awesome_app.route('/<path:path>')
def catch_all(path):
    return '5TxlwLDdy1Jqp91_sUScLFmOrVnDaCjXkFJsiXApqZw.Ej1w25iUPyr7XjksoC2O3tjhvulcwN2sE3Aha8IH8lQ'


if __name__ == '__main__':
    my_awesome_app.run()
