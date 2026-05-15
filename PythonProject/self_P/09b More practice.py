import logging
from mimetypes import init

class SmartFilter(logging.Filter):
    def __init__(self, handler_type):
        super().__init__()
        self.handler_type = handler_type

    def filter(self, record):
        # record.name = 'app.payment' ---> to filter logger name also --
        # ሁኔታ 1: ለኮንሶል ከሆነ "User" የሚል ቃል ይፈልጋል
        if self.handler_type == "console":
            return "login" in record.getMessage()

        # ሁኔታ 2: ለፋይል ከሆነ "Dev" የሚል ቃል ይፈልጋል
        if self.handler_type == "file":
            return record.levelno == logging.ERROR

        return True
logger = logging.getLogger('log5')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')

console = logging.StreamHandler()
console.setFormatter(formatter)
console.addFilter(SmartFilter('console'))

file = logging.FileHandler('pay.log', 'w', 'utf-8')
file.setFormatter(formatter)
file.addFilter(SmartFilter('file'))

logger.addHandler(console)
logger.addHandler(file)

logger.info("User login success")
logger.info("Payment done")
logger.error("Payment unsuccessful!")

class TransactionFilter(logging.Filter):
    def __init__(self, handler_type):
        super().__init__()
        self.handler_type = handler_type
    def filter(self, record):
        if self.handler_type == 'console':
            return 'transaction' in record.getMessage().lower()
        if self.handler_type == 'file':
            return record.levelno == logging.ERROR
        return record.name == 'bank_app'

logger = logging.getLogger('bank_app')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s - %(message)s')

console = logging.StreamHandler()
console.setFormatter(formatter)
console.addFilter(TransactionFilter('console'))

file = logging.FileHandler('bank_app.log', 'w', 'utf-8')
file.setFormatter(formatter)
file.addFilter(TransactionFilter('file'))

logger.addHandler(console)
logger.addHandler(file)

logger.info("Transaction started")
logger.error("Transaction failed")
logger.info("User login")