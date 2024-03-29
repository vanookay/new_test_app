import random
import string


def generate_unique_id() -> str:
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(256))
