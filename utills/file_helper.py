
from config.config import Config

def valid_file(file_name):
    if not file_name:
        return False

    allowed_extensions = Config.ALLOWED_EXTENSIONS

    if not allowed_extensions:
        return False

    return (
        '.' in file_name
        and file_name.rsplit('.', 1)[1].lower()
        in allowed_extensions
    )
