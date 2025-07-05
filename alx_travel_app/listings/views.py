from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='get',
    operation_description="Health check endpoint"
)
@api_view(['GET'])
def health_check(request):
    """
    Health check endpoint to verify API is running
    """
    return Response({
        'status': 'healthy',
        'message': 'ALX Travel App API is running'
    }, status=status.HTTP_200_OK)