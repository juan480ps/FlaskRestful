class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class ContribuyenteAlreadyExistsError(Exception):
    pass

class UpdatingContribuyenteError(Exception):
    pass

class DeletingContribuyenteError(Exception):
    pass

class ContribuyenteNotExistsError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "ContribuyenteAlreadyExistsError": {
         "message": "Contribuyente with given name already exists",
         "status": 400
     },
     "UpdatingContribuyenteError": {
         "message": "Updating Contribuyente added by other is forbidden",
         "status": 403
     },
     "DeletingContribuyenteError": {
         "message": "Deleting Contribuyente added by other is forbidden",
         "status": 403
     },
     "ContribuyenteNotExistsError": {
         "message": "Contribuyente with given id doesn't exists",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "User with given email address already exists",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}