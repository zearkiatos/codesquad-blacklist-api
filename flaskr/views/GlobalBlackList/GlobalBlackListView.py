import uuid
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

        try:
            # Verificar si el correo ya está en la lista negra
            if GlobalBlackList.query.filter_by(email=email_to_add).first():
                return {'message': 'El correo ya está en la lista negra'}, 409

            # Agregar el correo a la lista negra
            new_entry = GlobalBlackList(
                email=email_to_add,
                app_uuid=app_uuid,
                reason=blocked_reason,
                ip_address=request.remote_addr
            )
            db.session.add(new_entry)
            db.session.commit()

            return {'message': 'Correo agregado a la lista negra correctamente'}, 201
        except Exception as e:
            self.logger.error(f'Error al agregar correo a la lista negra: {e}')
            return {'message': 'Error interno al procesar la solicitud'}, 500

