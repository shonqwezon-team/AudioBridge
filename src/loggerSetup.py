import logging, sys, time
from logging import StreamHandler, Formatter

def setup(logger_name: str, level=logging.DEBUG):
	logger = logging.getLogger(logger_name)
	logger.setLevel(level)
	handler = StreamHandler(stream = sys.stdout)
	handler.setFormatter(
		Formatter(
			#fmt = '[%(asctime)s, %(levelname)s] ~ %(threadName)s (%(funcName)s)\t~: %(message)s',
			fmt = '[%(asctime)s, %(levelname)s] ~ (%(funcName)s)\t~: %(message)s',
			datefmt = time.strftime('%d-%m-%y %H:%M:%S')
		)
	)
	logger.addHandler(handler)