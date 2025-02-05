from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.classifier_serializer import NumberSerializer
from .services.classifier import classify_number
from .utils.numbers_api import get_number_fact

class NumberClassificationView(APIView):
    """API View to classify a number and fetch a fun fact."""

    def post(self, request):
        serializer = NumberSerializer(data=request.data)

        if serializer.is_valid():
            number = serializer.validated_data["number"]
            classification = classify_number(number)  # Get number properties
            fun_fact = get_number_fact(number)  # Fetch fun fact

            return Response(
                {
                    "number": number,
                    "classification": classification,
                    "fun_fact": fun_fact,
                },
                status=status.HTTP_200_OK,
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

