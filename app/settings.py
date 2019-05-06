# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
from app.curr_schema import schema

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
# MONGO_USERNAME = 'dbuser'
# MONGO_PASSWORD = 'test'
# MONGO_AUTH_SOURCE = 'admin'  # needed if --auth mode is enabled

MONGO_DBNAME = 'apitest'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

people = {
    'item_title': 'person',
    'schema': schema
}

form = {
    'item_title': 'form',
    'schema': schema
}

DOMAIN = {
    'people': people,
}

URL_PREFIX="api"