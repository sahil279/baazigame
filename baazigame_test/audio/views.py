from django.shortcuts import render
from .models import Song ,Podcast,Audiobook,Participants,ParticipantsPodcast
from .serializer import SongSerializer,PodcastSerializer,AudiobookSerializer,ParticipantsSerializer,ParticipantsPodcastSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
# Create your views here.


def response_format(success, message, data=None, pagination_data=None):
    obj = {
        'message': message
    }
    if success:
        obj['data'] = data
        obj['type'] = "success"
    else:
        obj['type'] = "failed"
    if pagination_data is not None:
        obj.update(pagination_data)
    return obj
class CreateAudioFile(APIView):
    
    
    
     
    def post(self, request):
        try:
            file_type = request.data['audioFileType'] 
            

            if file_type =='Song':
                name = request.data['name'] 
                duration = request.data['duration'] 
                data = Song.objects.create(name=name,duration=duration)
            if file_type =='Podcast':
                name = request.data['name'] 
                host = request.data['host']
                duration = request.data['duration'] 
                Participants_id = request.data['Participants_id']
                podcast_object = Podcast.objects.create(name=name,host=host,duration=duration)
                
                if Participants_id:
                    for i in Participants_id:
                        
                        Participants_object = Participants.objects.get(id=i)
                        ParticipantPodcast_object= ParticipantsPodcast.objects.create(Participants=Participants_object,Podcast=podcast_object)
                
            if file_type =='Audiobook':
                narrator = request.data['narrator']
                author = request.data['author']
                duration = request.data['duration'] 
                title=request.data['title'] 
                data = Audiobook.objects.create(narrator=narrator,author=author,duration=duration,title=title)
                
                

            msg="{} Added Successfully".format(file_type)
            context = response_format(success=True, message=msg)
            return Response(context, status.HTTP_200_OK)

        except Exception as E:
            print(f'[ERROR] CreateAudioFile :  {E}')
            msg="failed to add a AUDIO"
            context = response_format(success=False, message=msg)
            return Response(context, status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteAudioFile(APIView):
    

    def delete(self, request):
        try:
            data = request.data
            
            file_type= request.data['audioFileType']
            file_id= request.data['audioFileID']
            
            if file_type =='Podcast':
                file_object = Podcast.objects.get_active_by_id(id=file_id)
                
                file_object.delete_active()
            if file_type =='Song':
                file_object = Song.objects.get_active_by_id(id=file_id)
                
                file_object.delete_active()
            if file_type =='Audiobook':
                file_object = Audiobook.objects.get_active_by_id(id=file_id)
                
                file_object.delete_active()
            msg = "{} file have been deleted".format(file_type)
            context = response_format(success=True, message=msg)
            return Response(context, status.HTTP_200_OK)




        except Exception as e:
            
            msg = "something went wrong"
            context = response_format(success=False, message=msg)
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetAudioFiles(APIView):
    
    def get(self, request):    
        try:
            file_type = request.GET.get('audioFileType')
            file_id = request.GET.get('audioFileID',None)
            if file_type =='Song':
                if file_id:
                    song_object = Song.objects.get_active_by_id(id=file_id)
                    data = SongSerializer(song_object).data
                else:
                    song_object  = Song.objects.filter_active()
                    data = SongSerializer(song_object,many=True).data

                
            if file_type =='Podcast':
                if file_id:
                    podcast_object =  Podcast.objects.get_active_by_id(id=file_id)
                    data = PodcastSerializer(podcast_object).data
                    Participants_object  = ParticipantsPodcast.objects.filter(Podcast = podcast_object)
                    data['Participants'] = ParticipantsSerializer(Participants_object,many=True).data
                else:
                    podcast_object  = Podcast.objects.filter_active()
                    data = PodcastSerializer(podcast_object,many=True).data

                    for i in data:
                        
                        podcast_object =  Podcast.objects.get_active_by_id(id=i['id'])
                        Participants_object  = ParticipantsPodcast.objects.filter(Podcast = podcast_object)

                        i['Participants'] = ParticipantsPodcastSerializer(Participants_object,many=True).data
                
            if file_type =='Audiobook':
                
                if file_id:
                    Audiobook_object = Audiobook.objects.get_active_by_id(id=file_id)
                    data = AudiobookSerializer(Audiobook_object).data
                else:
                    Audiobook_object  = Audiobook.objects.filter_active()
                    data = AudiobookSerializer(Audiobook_object,many=True).data
                
                
        


            
            msg="all audio details"
            context = response_format(success=True, message=msg,data=data)
            return Response(context, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            msg = "error"
            context = response_format(success=False, message=msg)
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class UpdateAudioFiles(APIView):
    
    def put(self, request):
        try:
            file_type = request.GET.get('audioFileType')
            file_id = request.GET.get('audioFileID')
            print(file_type,file_id)
            if file_type =='Song':
                s_object = Song.objects.get(id=file_id)
                s_object.name = request.data['name'] 
                s_object.duration = request.data['duration'] 
                s_object.save()

            if file_type =='Podcast':
                p_object = Podcast.objects.get(id=file_id)
                
                p_object.name = request.data['name'] 
                p_object.host = request.data['host']
                p_object.duration = request.data['duration'] 
                
                p_object.save()

                
            if file_type =='Audiobook':
                a_object = Audiobook.objects.get(id=file_id)
                a_object.narrator = request.data['narrator']
                a_object.author = request.data['author']
                a_object.duration = request.data['duration'] 
                a_object.title=request.data['title'] 
                a_object.save()

            context = response_format(success=True, message=msg)
            return Response(context, status=status.HTTP_200_OK)

            
                

        
        except Exception as e:
            msg = "something went wrong" + str(e)
            context = response_format(success=False, message=msg)
            return Response(context, status.HTTP_500_INTERNAL_SERVER_ERROR)
