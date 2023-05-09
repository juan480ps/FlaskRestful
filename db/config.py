postgresql = {  'host': 'localhost',
                'user': 'jcorrea',
                'passwd': 'jcorrea',
                'db': 'cliente'}

postgresqlConfig = "postgresql://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])