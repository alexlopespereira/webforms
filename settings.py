# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
# MONGO_USERNAME = 'dbuser'
# MONGO_PASSWORD = 'test'
# MONGO_AUTH_SOURCE = 'admin'  # needed if --auth mode is enabled

MONGO_DBNAME = 'apitest'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'firstname': {
        'type': 'string',
        'required': True,
        'minlength': 1,
        'maxlength': 10
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        'unique': True,
    }
}

people = {
    'item_title': 'person',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },
    'schema': schema
}

form_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'firstname': {
        'type': 'string',
        'required': True,
        'minlength': 1,
        'maxlength': 10
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        'unique': True,
    }
}

# "schema": {
# 				"formulario": {
# 				  "type": "array",
# 				  "items": {
# 					"type": "object",
# 					"properties": {
# 					  "nick": {
# 						"type": "string",
# 						"title": "Nome do Campo",
# 						"required": True
# 					  },
# 					  "tipo": {
# 						"type": "string",
# 						"list": [ "Número Inteiro", "Número Real", "Texto", "Arquivo Anexo", "Falso/Verdadeiro" ],
# 						"required": True
# 					  }
# 					}
# 				  }
# 				}
# 			  }

form = {
    'item_title': 'form',
    'schema': form_schema
}

DOMAIN = {
    'people': people,
}

URL_PREFIX="api"