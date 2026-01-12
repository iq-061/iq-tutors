from django.db import models

class ContactTicket(models.Model):
    authorName = models.CharField(max_length=100)
    email = models.CharField(max_length=300)
    lesson_type_choices = {
        "1_TO_1": "1 to 1",
        "FOCUS_GROUP": "Focus Group"
    }
    lessonType = models.CharField(max_length=12, choices=lesson_type_choices)
    year_group_choices = {
        "7" : "7",
        "8" : "8",
        "9" : "9",
        "10" : "10",
        "11" : "11",
    }
    yearGroup = models.CharField(max_length=2, choices=year_group_choices)
    desc = models.TextField()

