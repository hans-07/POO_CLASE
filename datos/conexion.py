from decouple import config
from peewee import MySQLDatabase


def base_datos():
    return MySQLDatabase(
        config('db', default='pyme_db'),
        **{
            'charset': 'utf8mb4',
            'host': config('host', default='localhost'),
            'port': config('port', cast=int, default=3306),
            'user': config('user', default='root'),
            'password': config('password', default='')
        }
    )
