from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

class PingView(APIView):
    """
    Simple view to check API responsiveness.
    """
    permission_classes = [AllowAny] # Allow anyone to hit this endpoint

    def get(self, request, *args, **kwargs):
        # You can add more checks here if needed (e.g., database connection)
        return Response({"message": "API is responsive."}, status=status.HTTP_200_OK)
