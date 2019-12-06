from django.db import models
from . import predict
from . import content
from . import Generate

class UserMessage(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class BotMessage(models.Model):
    Answer_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def showrecommendation(item_id, num):
        products = content.recommend(item_id, num)
        for p in products:
            print (Generate.generate_text(p, 5, GenModel, max_seq_len))

        return