import logging, os
from logging.handlers import RotatingFileHandler
from rich.logging import RichHandler
from rich.traceback import install
install()

def create_logger(metodo, mensaje):
    # """Create a logger for use in all cases."""
    # loglevel = os.environ.get('LOGLEVEL', 'INFO').upper()
    # rich_handler = RichHandler(rich_tracebacks = True, markup = True)
    # logging.basicConfig(level = loglevel, 
    #                     format = '%(message)s',                        
    #                     datefmt = "[%Y/%m/%d %H:%M;%S]",
    #                     #handlers = [rich_handler],
    #                     filename = './util/testGene.log')
    
    # logger = logging.getLogger(__name__)
    # logger.setLevel(logging.DEBUG)
    # #logger.addHandler(handler)
    # logger.debug(log)
    #return logging.debug('rich' )
    
    
    
    logging.basicConfig(filemode = "w+" )
    
    
    logger = logging.getLogger('Metodo: ' + metodo)
    logger.setLevel(logging.DEBUG)
    
    fh = logging.FileHandler('log.log')
    fh.setLevel(logging.DEBUG)
    

    fh = RotatingFileHandler('log.log', maxBytes = 1024,#5*1024*1024, 
                                backupCount = 0)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    fh.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.info(mensaje)
    
    
    logger.handlers.clear()
    fh.close()
    
    
    