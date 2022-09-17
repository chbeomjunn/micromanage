import os
from dotenv import load_dotenv

required_env = ['DATABASE_CONNECTION_URL', 'AUTH0_TENANT_URL', 'AUTH0_AUDIENCE']

for each in required_env:
    env = os.getenv(each)
    if each is None:
        raise ValueError(f'{each} is not set')

load_dotenv()

MONGO_URI = os.getenv('DATABASE_CONNECTION_URL')
AUTH0_URL = os.getenv('AUTH0_TENANT_URL')
AUTH0_AUDIENCE = os.getenv('AUTH0_AUDIENCE')
