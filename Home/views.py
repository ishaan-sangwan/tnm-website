from django.shortcuts import render,HttpResponse,redirect
from .models import Event
from .serializers import EventSerializer, ParticipationSerializer
from rest_framework.views import Response, APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        print(request.user)
        events = Event.objects.all().values()
        context = {"events":events,"superuser":request.user.is_superuser}
        return render(request, "Home.html",context=context)
    else:

        return redirect("/Login/")

class HomeAPI(APIView):
    def get(self, request):
        queryset = Event.objects.all()
        try:
            serializer = EventSerializer(queryset, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=HTTP_400_BAD_REQUEST)

