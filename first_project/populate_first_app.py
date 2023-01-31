# Setting project or dictionary
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

# Fake Pop script
import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'MarketPlace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name = random.choices(topics))[0]
    t.save()
    return t

def populate(N = 5):

    for entry in range(N):

        #get the topic entry

        top = add_topic()

        # create Fake entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #crate the new webpage entry

        webpg = Webpage.objects.get_or_create(topic = top, name = fake_name, url = fake_url)[0]

        #  Create a Fake access record entry

        acc_rec = AccessRecord.objects.get_or_create(name = webpg, date = fake_date)[0]

if __name__ == '__main__':
    print("Populating Script!")
    populate(20)
    print("Population Done")

