#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2021 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : http_service_tests.py
# @desc : Service for HTTP

import sys
sys.path.insert(0, '../')

from tools.http_service import Http_service
import inspect
import logging

class Http_service_tests(object):
    def __init__(self, logging_level=logging.DEBUG):
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging_level)

    def test_sequence(self):
        self.test_http_post()

    def test_http_post(self, data:dict = {"ip": "", "url":"", "header":[], "type":"post","body":""}) -> tuple:
        http_service = Http_service(logging_level=logging.DEBUG)
        status_code, text =  http_service.send_request(data)
        logging.info(
            f'{self.__class__.__name__} {inspect.currentframe().f_lineno} {inspect.stack()[0][3]} status_code is {type(status_code)}{status_code}')
        logging.info(
            f'{self.__class__.__name__} {inspect.currentframe().f_lineno} {inspect.stack()[0][3]} text is {type(text)}{text}')

if __name__=="__main__":
    http_service_tests = Http_service_tests(logging_level=logging.DEBUG)
    http_service_tests.test_sequence()
    del http_service_tests