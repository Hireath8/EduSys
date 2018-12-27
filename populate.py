import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EduSys.settings')

import django
django.setup()


from forum.seeds.populate import run_seeding

if __name__ == '__main__':
    run_seeding()