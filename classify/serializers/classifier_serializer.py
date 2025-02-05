from rest_framework import serializers

class NumberSerializer(serializers.Serializer):
    """Serializer to validate the incoming number."""
    number = serializers.IntegerField() # Ensures the incoming value is an integer.

    def validate_number(self, value):
        """Ensure the number is a non-negative integer."""
        if value < 0:
            raise serializers.ValidationError("Number must be a non-negative integer.")
        return value 

