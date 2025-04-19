# Цей код чомусь виводить пустий список []

from utils import *
from models import *
print(list(filter(lambda str: not ("_" in str), dir())))



# Перевіряв чи правильно все зробив, в такому випадку все працює
#  
# from models.admin import create_admin
# from models.user import create_user
# from utils.formatter import format_string
# from utils.logger import log_in_file

# result = [create_admin.__name__, create_user.__name__, format_string.__name__, log_in_file.__name__]
# print(result)


