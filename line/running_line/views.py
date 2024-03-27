from django.http import HttpResponse
from wsgiref.util import FileWrapper
from .utils.generate_video import generate_video
from django.shortcuts import render

def static_page(request):
    return render(request, './index.html')

def serve_video(request):
    generate_video(request.GET.get('text', ''))
    video_path = "./running_line/video/line.mp4" # Adjust the path to your video file
    file_wrapper = FileWrapper(open(video_path, 'rb'))
    response = HttpResponse(file_wrapper, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename=line.mp4' # Use 'inline' to play in the browser
    return response

