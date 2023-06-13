postgresql = {  'host': 'localhost',
                'user': 'postgres',
                'passwd': 'postgres',
                'db': 'cliente'}

postgresqlConfig = "postgresql://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])