from rest_framework.response import Response
from rest_framework.decorators import api_view
from restapi.models import Fish
from restapi.serializers import FishSerializer

@api_view(['GET'])
def getAllRecords(request):
	fishset = Fish.objects.all().order_by('-timestamp')
	serializer = FishSerializer(fishset, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def createRecords(request):
	serializer = FishSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
# Create your views here.
