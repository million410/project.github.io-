# 🧑‍🏫 Learn how to use logging like a pro.

# 1️⃣ Logging Basics----
#----------------------------------------------------------------------
import logging

# Setup Logger
# logging.basicConfig(level=logging.WARNING)

# 📲 log Message
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.exception('This is exception msg.')
# logging.critical("This is a critical message")

# Simple Example------
# a, b = 10, 0
#
# logging.debug(f'Executing: {a}/{b}')
# try:
#     c = a/b
#     logging.info(f'Result: {c}')
# except:
#     logging.error('Something went wrong.')

# 2️⃣🗃️Log to a file---------

# log_format = '%(asctime)s - %(levelname)s - %(message)s'
# log_format = """***[%(levelname)s]***
# Time: %(asctime)s
# Msg : %(message)s
# File: %(filename)s Line : %(lineno)d
# ----------------------------------------------------------"""
# logging.basicConfig(level=logging.DEBUG,
#                     format = log_format,
#                     filename='ef_app.log')
# # Log Message - - - - - - - - - -
# logging.debug('This is a debug msg2.')
# logging.info('This is info msg2.')
# logging.warning('This is warning msg2.')

import logging
from contextlib import contextmanager
# 1. እዚህ ጋር logging.basicConfig አስተካክል...
formatter = '%(asctime)s - %(levelname)s - %(message)s'
# logging.basicConfig(
#     level=logging.DEBUG,
#     format=formatter,
#     filename='system_repair.log'
# )
# @contextmanager
# def file_checker():
#     # 2. እዚህ ጋር የጅማሬ ሎግ ጻፍ...
#     logging.info('Checking file...')
#     try:
#         yield
#     except FileNotFoundError:
#         logging.error('File not found!')
#     except Exception as e:
#         logging.error(f'Unexpected error happened: {e}')
#     finally:
#         # 3. እዚህ ጋር የመጨረሻ ሎግ ጻፍ...
#         logging.info('Checking the file has ended!')
#         pass
#
# # 4. 'with' ብሎኩን በመጠቀም ፋይል ለመክፈት ሞክር እና ስህተቱን በሎግ መዝግብ...
#
# with file_checker():
#     with open('data0.text', 'r') as f:
#         read = f.read()

import logging, requests

# Webhook - is a way for apps to communicate using HTTP POST requests.
# In a nutshell, we can send json data to a URL, and the other app knows what to do

WEBHOOK_SLACK = 'https://hooks.slack.com/triggers/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'
WEBHOOK_DISCARD = 'https://discordapp.com/api/webhooks/1485153489498931200/UCuPEal5Wq9eDiI8sbVx2uCPub3fHluJiLG81VDl-3IJvtAkp9OybCW_YOAuyEQS8Hqr'
