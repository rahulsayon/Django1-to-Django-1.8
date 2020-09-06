import random
import string

from django.conf import settings


SHORTCODE_MIN = getattr(settings,"SHORTCODE_MIN",6)

def code_generator(size=SHORTCODE_MIN,chasr=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chasr) for _ in range(size) )