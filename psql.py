from data_pipelines import env

import pyodbc
import pandas as pd
import os

CONNECTION_STRING = env.CONNECTION_STRING
CONNECTION_STRING = os.getenv(CONNECTION_STRING)

def pyodbc_query(query):
