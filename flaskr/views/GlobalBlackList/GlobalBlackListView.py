import uuid
from http import HTTPStatus
from flask_restful import Resource, reqparse
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
from ...middlewares.authMiddleware import *
from sqlalchemy.sql import func
from ...utils.logger import Logger

log = Logger()

config = Config()


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


    @require_bearer_token
    def get(self,email):
        '''
        api get para la vista GlobalBlackList
        '''
        log.info('Verifying email')

        '''
        construyendo respuesta
        '''
        email_in_list=self.queryEmailInBlackList(email)
        try:

            if email_in_list:
                log.info('Email was found')
                return {
                    'exist':True,
                    'reason':email_in_list.reason
                },HTTPStatus.OK
            else:
                log.info('Email was not found')
                return {
                            'exist':False,
                            'reason':None
                        },HTTPStatus.NOT_FOUND
        except Exception as ex:
            log.error(f'Some error occurred trying to add an email in a blacklist: {e}')
        
        
    @require_bearer_token    
    def post(self):
        '''
        API para agregar un correo a la lista negra.
        Método POST
        Parámetros de solicitud:
        - email (String): Correo
        - app_uuid (String): UUID de la aplicación a registar
        - blocked_reason (String): Razón por la cual se bloquea el correo.
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True, help='Email is required')
        parser.add_argument('app_uuid', type=str, required=True, help='App UUID is required')
        parser.add_argument('blocked_reason', type=str, required=True, help='Blocked reason is required')
        args = parser.parse_args()

        email_to_add = args['email']
        app_uuid = args['app_uuid']
        blocked_reason = args['blocked_reason']

        log.info('Receiving request to add an email in the blacklist')

        try:
            # Verificar si el correo ya está en la lista negra
            if GlobalBlackList.query.filter_by(email=email_to_add).first():
                return {'message': 'El correo ya está en la lista negra'}, HTTPStatus.CONFLICT

            # Agregar el correo a la lista negra
            new_entry = GlobalBlackList(
                email=email_to_add,
                app_uuid=app_uuid,
                reason=blocked_reason,
                ip_address=request.remote_addr
            )
            db.session.add(new_entry)
            db.session.commit()

            return {'message': 'Correo agregado a la lista negra correctamente'}, HTTPStatus.CREATED
        except Exception as e:
            log.error(f'Some error occurred trying to add an email in a blacklist: {e}')
            return {'message': 'Error interno al procesar la solicitud'}, HTTPStatus.INTERNAL_SERVER_ERROR


class ErrorsListView(Resource):
    '''
    Esta clase corresponde a una api para la generación intencionada de errores
    Attributes:
        logger (loggin): logger para las operaciónes en la api.
    '''
     
    def get(self):
        '''
        api get para la vista GlobalBlackList
        '''
        log.info('calculate divizion')
        value=10/0
        return {'result': f'{value}'}, HTTPStatus.OK 