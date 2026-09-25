import oracledb

DB_CONFIG = {
    "user": "blog_user",
    "password": "contra",
    "dsn": "localhost/XEPDB1"
}

def conectar_db():
    return oracledb.connect(**DB_CONFIG)
