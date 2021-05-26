from .models import Song,Podcast,Audiobook,Participants,ParticipantsPodcast
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Song
        fields = '__all__'

class PodcastSerializer(serializers.ModelSerializer):
    
    class Meta(object): 
        model = Podcast
        fields = '__all__'

class AudiobookSerializer(serializers.ModelSerializer):
    
    class Meta(object): 
        model = Audiobook
        fields = '__all__'


class ParticipantsSerializer(serializers.ModelSerializer):
    
    class Meta(object): 
        model = Participants
        fields = '__all__'


class ParticipantsPodcastSerializer(serializers.ModelSerializer):
    
    class Meta(object): 
        model = ParticipantsPodcast
        fields = '__all__'