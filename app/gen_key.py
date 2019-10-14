import uuid
from app.queries import check_course_key


def gen_key(size=5):
    key = uuid.uuid4().hex[:6].upper()
    if check_course_key(key):
        return gen_key(size=5)
    return(key)
