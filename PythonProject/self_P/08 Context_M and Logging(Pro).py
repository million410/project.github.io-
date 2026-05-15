import logging
import contextlib

# logger = logging.getLogger('School_app')
# logger.setLevel(logging.DEBUG)
#
# # Console (Only Warning+)--
# console = logging.StreamHandler()
# console.setLevel(logging.WARNING)
#
# # File (everything)-
# file_handler = logging.FileHandler('school.log', 'w')
#
# # Formatter--
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# console.setFormatter(formatter)
# file_handler.setFormatter(formatter)
#
# logger.addHandler(console)
# logger.addHandler(file_handler)
#
# logger.debug('debug')
# logger.info('info')
# logger.warning('warning')
# logger.error('error')
'continous'
# logger = logging.getLogger('student_app')
# logger.setLevel(logging.INFO)
#
# # FORMATTER--
# formatter = logging.Formatter('%(asctime)s - %(lineno)d - %(created)f - %(levelname)s - %(message)s')
#
# # Handler-------
# console = logging.StreamHandler()
# console.setFormatter(formatter)
#
# logger.addHandler(console)
#
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# setup Logger

class OnlyInfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO

logger = logging.getLogger("app1")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.addFilter(OnlyInfoFilter())

logger.addHandler(console)

logger.debug("Debug")
logger.info("Info")
logger.error("Error")