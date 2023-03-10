from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Review


class ListReviewsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Review.objects.all().exists():
            print('Reviews List')
            return Response({'reviews': 'test'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No reviews found'}, status=status.HTTP_404_NOT_FOUND)

