from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.auth.jwt_handler import JWTHandler
from src.config.security import auth_algorithm, auth_secret_key

security = HTTPBearer()

def has_access(required_roles: list[int]):
    def role_checker(credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
        try:
            token = credentials.credentials
            jwt_handler = JWTHandler(auth_secret_key, auth_algorithm)
            payload = jwt_handler.decode_token(token)
            
            if payload['id_rol'] not in required_roles:
                raise HTTPException(status_code=403, detail="Access denied")
            
            return payload
        except HTTPException as exc:
            raise exc
        except Exception as e:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    
    return role_checker
