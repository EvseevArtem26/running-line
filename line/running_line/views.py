from django.http import HttpResponse
from wsgiref.util import FileWrapper
from .utils.generate_video import generate_video
from django.shortcuts import render
from dotenv import load_dotenv
load_dotenv()
import os
import datetime
from pymongo import MongoClient
from pymongo.server_api import ServerApi
print ("URL: ", str(os.getenv('MONGODB_URI')))
client = MongoClient(str(os.getenv('MONGODB_URI')), server_api=ServerApi('1'))


def static_page(request):
    return render(request, './index.html')

def serve_video(request):
    try:
        db = client['running-line']
        collection = db['requests']
        result = collection.insert_one({ 
            "text": request.GET.get('text', ''),
            "time": datetime.datetime.now(datetime.timezone.utc)
        })
        print(result.inserted_id)
    except Exception as e:
        print(e)

    generate_video(request.GET.get('text', ''))
    video_path = "./running_line/video/line.mp4" # Adjust the path to your video file
    file_wrapper = FileWrapper(open(video_path, 'rb'))
    response = HttpResponse(file_wrapper, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename=line.mp4' # Use 'inline' to play in the browser
    return response

