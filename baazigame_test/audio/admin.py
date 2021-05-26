
from .models import Song,Podcast,Audiobook,Participants,ParticipantsPodcast

from django.contrib import admin

admin.site.register(Song)
admin.site.register(Audiobook)
admin.site.register(Podcast)
admin.site.register(Participants)
admin.site.register(ParticipantsPodcast)


# Register your models here.
