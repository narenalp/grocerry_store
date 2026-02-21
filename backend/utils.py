from passlib.context import CryptContext

# Setup password hashing
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    """Checks if the typed password matches the stored hash"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Converts a plain password into a secure hash"""
    return pwd_context.hash(password)