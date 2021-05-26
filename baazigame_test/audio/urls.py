from django.contrib import admin
from django.urls import path
from .views import CreateAudioFile,DeleteAudioFile,GetAudioFiles,UpdateAudioFiles




urlpatterns = [
    path('create_audio', CreateAudioFile.as_view()),
    path('delete_audio', DeleteAudioFile.as_view()),
    path('get_audio', GetAudioFiles.as_view()),
    path('update_audio',UpdateAudioFiles.as_view())
    
]
