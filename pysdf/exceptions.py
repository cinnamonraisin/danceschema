'''Exception classes for SDF'''


class sdfError(Exception):
    '''Root SDF exception class.'''
    pass


class SchemaError(sdfError):
    '''Exceptions relating to schema validation'''
    pass


class ParameterError(sdfError):
    '''Exceptions relating to function and method parameters.'''
    pass
