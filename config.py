import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "0\x02\xa6Z?\xcd\xca\x8c\xa4~\xd2fE \xf8\x8d"

    MONGODB_SETTINGS = { 'db' : 'UTA_enrollment' }
