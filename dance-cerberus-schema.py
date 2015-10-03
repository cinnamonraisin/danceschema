dance_cerberus = {
    # Schema definition, based on Cerberus grammar.
    'title': {
        'type': 'string',
        'required': True
    },
    'author': {
        'type': 'string'
    },
    'style': {
        'type': 'string',
        'allowed': ['contra', 'english', 'square', 'mixer', 'other'],
        'required': True
    },
    'formation': {
        'type': 'string'
    },
    'source': {
        'type': 'string'
    },
    'authors_notes': {
        'type': 'string'
    },
    'moves': {
        'type': 'list',
        'schema': { 
            'type': 'dict', 
            'schema' : {
                'section' : {
                    'type' : 'string'
                },
                'elements' : {
                    'type' : 'list',
                    'schema' : {
                        'type' : 'string'
                    }
                }
            }
        }
    },
    'tune': {
        'type': 'string'
    },
    'tune_source': {
        'type': 'string'
    },
    'key': {
        'type': 'string'
    },
    'meter': {
        'type': 'string'
    },
    'date': {
        'type': 'string'
    }
}