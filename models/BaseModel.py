from sqlalchemy.ext.declarative import declarative_base

from configs.Database import Engine
import sys
# Base Entity Model Schema
EntityMeta = declarative_base()


def init():
    # EntityMeta.metadata.drop_all(bind=Engine)
    # EntityMeta.metadata.create_all(bind=Engine)
    pass