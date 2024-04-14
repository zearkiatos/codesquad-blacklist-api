from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.orm import validates
import re
from ..dataContext.sqlAlchemyContext import db
import uuid
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, DateTime


class GlobalBlackList(db.Model):
    __tablename__ = 'GlobalBlackList'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    email=db.Column(db.String(500), nullable=False)
    app_uuid= db.Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False)
    reason=db.Column(db.String(255))
    ip_address=db.Column(db.String(16), nullable=False)
    createdAt = db.Column(DateTime, default=func.now(),nullable=False)
    

   
    def __init__(self, email, app_uuid, reason, ip_address):
        self.email = email
        self.app_uuid = app_uuid
        self.reason = reason
        self.ip_address = ip_address



class GlobalBlackListSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = GlobalBlackList
        include_relationships = True
        load_instance = True