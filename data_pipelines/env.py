"""All environment variables
Getters and Setters
"""

import os

AZURE_ACCOUNT_NAME = "AZURE_ACCOUNT_NAME"
AZURE_ACCOUNT_KEY = "AZURE_ACCOUNT_KEY"
AZURE_CONNECTION_STRING = "AZURE_CONNECTION_STRING"
AZURE_CONTAINER_NAME = "AZURE_CONTAINER_NAME"

def set_azure_account_name(name:str, env=None):
  if env is None:
    env = os.environ
  env[AZURE_ACCOUNT_NAME] = name

def get_azure_account_name(env=None):
  if env is None:
    env = os.environ
  return(env.get(AZURE_ACCOUNT_NAME)

def set_azure_account_key(key:str, env=None):
  if env is None:
    env = os.environ
  env[AZURE_ACCOUNT_KEY] = key

def get_azure_account_key(env=None):
  if env is None:
    env = os.environ
  return(env[AZURE_ACCOUNT_KEY])

def set_azure_connection_string(env=None):
  if env is None:
    env = os.environ
  try: 
    name = env.get(AZURE_ACCOUNT_NAME)
    key = env.get(AZURE_ACCOUNT_KEY)
    assert name is not None
    assert key is not None
    env[AZURE_CONNECTION_STRING] = "DefaultEndpointsProtocol=https;AccountName={0};AccountKey={1};EndpointSuffix=core.windows.net".format(name, key)

  except AssertionError: print("need to set azure account name and key")

def get_azure_connection_string(env=None):
  if env is None:
    env = os.environ
  return(env[AZURE_CONNECTION_STRING])
  
def set_azure_container_name(container:str, env=None):
  if env is None:
    env = os.environ
  env[AZURE_CONTAINER_NAME] = container

def get_azure_container_name(env=None):
  if env is None:
    env = os.environ
  return(env[AZURE_CONTAINER_NAME])

def load_env_from_file():
    with open(Path('.')/'.env', 'r') as fh:
        vars_dict = dict(
            tuple(line.strip('\n').split('='))
            for line in fh.readlines() if not line.startswith('#')
        )
    os.environ.update(vars_dict)
