#! /usr/bin/python3
# -*- coding:utf8 -*-

# Copyright 2021 Robina Li. BSD 3-Clause License All Rights Reserved.
# @file : http_service.py
# @desc : Service for HTTP

import requests
import inspect
import logging

class Http_service(object):
    def __init__(self, logging_level=logging.INFO):
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging_level)

    def send_request(self, data:dict={"ip": "", "url":"", "header":[], "type":"","body":""}) -> tuple:
        http_ip = data["ip"]

        url = "http://" + http_ip + data["url"]

        my_header = data["header"]

        logging.info (f"{self.__class__.__name__} {inspect.currentframe().f_lineno} {inspect.stack()[0][3]} ---------- http request ----------------")

        logging.info (f'{self.__class__.__name__} {inspect.currentframe().f_lineno} {inspect.stack()[0][3]} posting to {url}')
        logging.info (f'{self.__class__.__name__} {inspect.currentframe().f_lineno} {inspect.stack()[0][3]} headers are {my_header}')
        logging.info (f'{self.__class__.__name__} {inspect.currentframe().f_lineno} {inspect.stack()[0][3]} IP is {http_ip}')
        logging.info (f'{self.__class__.__name__} {inspect.currentframe().f_lineno} {inspect.stack()[0][3]} type is {data["type"]}')
        logging.info (f'{self.__class__.__name__} {inspect.currentframe().f_lineno} {inspect.stack()[0][3]} body is {data["body"]}')

        if (data["type"] == "put") :
            r = requests.put(url, data=data["body"], headers=my_header)
        elif (data["type"] == "get") :
            r = requests.get(url, headers=my_header)
        elif (data["type"] == "post") :
            r = requests.post(url, data=data["body"], headers=my_header)
        elif (data["type"] == "delete") :
            r = requests.delete(url, data=data["body"], headers=my_header)

        logging.info (f"{self.__class__.__name__} {inspect.currentframe().f_lineno} {inspect.stack()[0][3]} ---------- http response ----------------")
        logging.info (f'{self.__class__.__name__} {inspect.currentframe().f_lineno} {inspect.stack()[0][3]} status_code is {type(r.status_code)}{r.status_code}')
        logging.info (f'{self.__class__.__name__} {inspect.currentframe().f_lineno} {inspect.stack()[0][3]} reason is {type(r.reason)}{r.reason}')
        logging.info (f'{self.__class__.__name__} {inspect.currentframe().f_lineno} {inspect.stack()[0][3]} text is {type(r.text)}{r.text}')

        if (r.status_code == 200):
            return r.status_code, r.text
        else:
            return r.status_code, r.reason