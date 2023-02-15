#!/usr/bin/env python3
from decouple import config
from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)