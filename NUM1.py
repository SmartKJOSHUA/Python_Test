import random
import string

def random_user_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))


print(random_user_id())  

