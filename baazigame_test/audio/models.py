from django.db import models

# Create your models here.


class ActiveFilterManager(models.Manager):
    def filter_active(self, *args, **kwargs):
        return super().filter(*args, active=True, **kwargs)

    def get_active_by_id(self, id, *args, **kwargs):
        return super().get(id=id, active=True, *args, **kwargs)

class SongManager(ActiveFilterManager):
    pass

class PodcastManager(ActiveFilterManager):
    pass


class AudiobookManager(ActiveFilterManager):
    pass



class Song(models.Model):
    name = models.CharField(max_length=100, null=False)
    duration = models.PositiveIntegerField(null=False)
    uploaded_time = models.DateTimeField(auto_now_add=True, null=False)

    active = models.BooleanField(default=True)
    objects = SongManager()
    def delete_active(self):
        self.active = False
        self.save()
class Podcast(models.Model):
    name = models.CharField(max_length=100, null=False)
    duration = models.PositiveIntegerField(null=False)
    uploaded_time = models.DateTimeField(auto_now_add=True, null=True)
    host = models.CharField(max_length=100, null=False)
    active = models.BooleanField(default=True)
    objects = PodcastManager()

    def delete_active(self):
        self.active = False
        self.save()


class Participants(models.Model):
    name = models.CharField(max_length=100, null=False)


class ParticipantsPodcast(models.Model):
    Participants = models.ForeignKey(Participants, on_delete=models.CASCADE)
    Podcast = models.ForeignKey(Podcast,on_delete=models.CASCADE)
    

class Audiobook(models.Model):
    title = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    narrator =  models.CharField(max_length=100, null=False)
    duration = models.PositiveIntegerField(null=False)
    uploaded_time = models.DateTimeField(auto_now_add=True, null=True)

    active = models.BooleanField(default=True)
    objects = AudiobookManager()
    def delete_active(self):
        self.active = False
        self.save()