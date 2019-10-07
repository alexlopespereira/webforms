all_schemas = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'nome': {
        'type': 'string',
        'required': True,
        'minlength': 3,
        'maxlength': 100
    },
    'endereco': {
        'type': 'string',
        'minlength': 5,
        'maxlength': 200,
    },
    'email': {
        'type': 'string',
        'minlength': 5,
        'maxlength': 255,
    },
    'telefone': {
        'type': 'string',
        'minlength': 8,
        'maxlength': 20,
    },
    'data_nascimento': {
        'type': 'date'
    },
    'anexo': {
        'type': 'binary',
        'maxlength': 10485760
    },
}