from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt

def self_user_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        verify_jwt_in_request()

        if kwargs.get('id') != get_jwt():
            return {'msg': 'Unauthorized user'}, 403

        return func(*args, **kwargs)
    return wrapper

def self_provider_only():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):

            verify_jwt_in_request()

            if 'provider' != get_jwt()['role'].lower():
                return {'msg': 'Unauthorized user'}, 403
            
            return fn(*args, **kwargs)
        
        return decorator
    
    return wrapper

def self_admin_only():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):

            verify_jwt_in_request()

            if 'provider' != get_jwt()['role'].lower():
                return {'msg': 'Unauthorized user'}, 403
            
            return fn(*args, **kwargs)
        
        return decorator
    
    return wrapper