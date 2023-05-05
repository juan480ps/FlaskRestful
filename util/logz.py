import logging, os
from rich.logging import RichHandler
from rich.traceback import install
install()

def create_logger(log):
    """Create a logger for use in all cases."""
    loglevel = os.environ.get('LOGLEVEL', 'INFO').upper()
    rich_handler = RichHandler(rich_tracebacks = True, markup = True)
    logging.basicConfig(level = loglevel, 
                        format = '%(message)s',                        
                        datefmt = "[%Y/%m/%d %H:%M;%S]",
                        #handlers = [rich_handler],
                        filename = './util/testGene.log')
    return logging.debug('rich' )


# import logging

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler('app.log')
# handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.debug('debug')


# import logging

# logger = logging.getLogger(__name__)

# def some_function():
#     logger.debug('Se ha llamado a la función some_function.')
