from loguru import logger 
from pathlib import Path
import sys

class Settings:
    def __init__(self):
        self.VARIAVEL_GLOBAL:str = 'TESTE VARIÁVEL SETTINGS'

settings = Settings()

DIR_LOG:str = Path('logs/log_api.log')

logger.remove()
logger.add(DIR_LOG, level="INFO", 
    retention="10 days",
    format="""<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>""")

#logger.add(sys.stdout, level="DEBUG", colorize=True,
logger.add(sys.stdout, level="INFO", colorize=True,
    format="""<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"""       
    )