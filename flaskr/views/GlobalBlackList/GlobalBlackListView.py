from flask_restful import Resource
from flask import Flask, request, jsonify
import base64
import json
from http import HTTPStatus
from ...models.GlobalBlackList import GlobalBlackList
from ...dataContext.sqlAlchemyContext import db
from functools import wraps
from datetime import datetime,timezone
import re
import pytz
import logging
import traceback


class GlobalBlackListView(Resource):
    '''
    Esta clase corresponde a una api para la gestión de la lista negra global
    Attributes:
        logger (loggin): logger para las operaciónes en la api.
    '''

    def queryEmailInBlackList(self,email_to_find):
        '''
        método para consultar un email en la lista negra
        '''
        email_in_list=GlobalBlackList.query.filter_by(email=email_to_find).first()
        return email_in_list



    def get(self,email):
        '''
        api get para la vista GlobalBlackList
        '''
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('default')
        self.logger.info(f'verificando el email')

        '''
        construyendo respuesta
        '''
        email_in_list=self.queryEmailInBlackList(email)

        if email_in_list:
            return {
                'exist':True,
                'reason':email_in_list.reason
            },HTTPStatus.OK
        else:
            return {
                        'exist':False,
                        'reason':None
                    },HTTPStatus.NOT_FOUND
