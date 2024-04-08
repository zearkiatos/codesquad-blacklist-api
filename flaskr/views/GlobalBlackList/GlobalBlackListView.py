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
        if email_in_list:
            return True
        else:
            return False


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
        email_is_in_list=self.queryEmailInBlackList(email)

        return {
            'result':email_is_in_list
        },HTTPStatus.OK
        
    def post(self):
        '''
        api post para agregar un correo a la lista negra
        '''
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('default')
        self.logger.info(f'Agregando correo a la lista negra')

        try:
            data = request.get_json()
            email_to_add = data.get('email')

            if not email_to_add:
                return {'message': 'El correo no se proporcionó en la solicitud'}, HTTPStatus.BAD_REQUEST

            # Verificar si el correo ya está en la lista negra
            if self.queryEmailInBlackList(email_to_add):
                return {'message': 'El correo ya está en la lista negra'}, HTTPStatus.CONFLICT

            # Obtener la dirección IP del cliente que hace la solicitud
            ip_address = request.remote_addr

            # Agregar el correo a la lista negra con los atributos adicionales
            new_entry = GlobalBlackList(
                email=email_to_add,
                app_uuid=uuid.uuid4(),
                ip_address=ip_address,
                createdAt=func.now()
            )
            db.session.add(new_entry)
            db.session.commit()

            return {'message': 'Correo agregado a la lista negra correctamente'}, HTTPStatus.CREATED

        except Exception as e:
            self.logger.error(f'Error al agregar correo a la lista negra: {e}')
            return {'message': 'Error interno al procesar la solicitud'}, HTTPStatus.INTERNAL_SERVER_ERROR

