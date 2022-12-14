#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
from os.path import realpath, dirname
import psycopg2
from psycopg2 import Error

from audiobridge.common import config

logger = logging.getLogger('logger')
db_conf = config.Database()

class DataBase():
	"""Интерфейс для работы с базой данных PostgreSql.
	"""
	def __init__(self):
		"""Инициализация класса DataBase.
		"""
		# Инициализация объекта подключения
		self.conn = None
		self.connect_db()

	#Подключение к базе данных
	def connect_db(self):
		"""Подключение к базе данных.
		"""
		try:
			logger.debug(f'Connecting to {db_conf.DB_NAME}')
			self.conn = psycopg2.connect(
				user     = db_conf.PG_USER,
				password = db_conf.PG_PASSWORD,
				host     = db_conf.PG_HOST,
				port     = db_conf.PG_PORT,
				database = db_conf.DB_NAME)
			self.conn.autocommit=True
		except (Exception, Error) as er:
			logger.error(f'Connection to database failed: {er}')
			logger.debug('Closing the program...')
			sys.exit()
		else:
			logger.debug('Database was connected successfully')
			self.create_tables()

	#Создание таблиц, если они отсутствуют
	def create_tables(self):
		"""Создание необходимых таблиц в случае их отсутствия.
		"""
		try:
			with self.conn.cursor() as curs:
				curs.execute(open(realpath(dirname(__file__) + "/scripts/init_tables.sql"), "r").read())

		except (Exception, Error) as er:
			#Закрытие освобождение памяти + выход из программы для предотвращения рекурсии и настройки PostgreSQL на хосте
			logger.error(f'Tables creation failed: {er}')
			if self.conn:
				self.conn.close()
				logger.debug('Connection was closed')
			logger.debug('Closing the program...')
			sys.exit()
		else:
			logger.debug(f'Tables are ready to use')
