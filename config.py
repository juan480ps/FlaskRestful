postgresql = {  'host': 'localhost',
                'user': 'jcorrea',
                'passwd': 'jcorrea',
                'db': 'cliente'}

postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])