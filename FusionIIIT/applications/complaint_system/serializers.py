from rest_framework import serializers
from applications.complaint_system.models import StudentComplain
from applications.globals.models import User

class StudentComplainSerializers(serializers.ModelSerializer):

    class Meta:
        model=StudentComplain
        fields=('__all__')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('__all__')
from rest_framework import serializers
from .models import StudentComplain, Caretaker
from applications.globals.models import ExtraInfo

# Added StudentComplainSerializer
class StudentComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentComplain
        fields = "__all__"

# Added CaretakerSerializer
class CaretakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caretaker
        fields = "__all__"

# Optionally, add ExtraInfoSerializer if needed
class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = "__all__"
from rest_framework import serializers
from .models import StudentComplain, Caretaker
from applications.globals.models import ExtraInfo

# Serializer for StudentComplain (already added previously)
class StudentComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentComplain
        fields = '__all__'

# Serializer for Caretaker (already added previously)
class CaretakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caretaker
        fields = '__all__'

# Serializer for Feedback submission
class FeedbackSerializer(serializers.Serializer):
    feedback = serializers.CharField()
    rating = serializers.IntegerField()



# Serializer for Resolve Pending complaints
class ResolvePendingSerializer(serializers.Serializer):
    yesorno = serializers.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    comment = serializers.CharField(required=False, allow_blank=True)
# serializers.py

from rest_framework import serializers
from .models import StudentComplain, Caretaker, Workers
from applications.globals.models import ExtraInfo


# Serializer for StudentComplain (already added previously)
class StudentComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentComplain
        fields = '_all_'

# Serializer for Workers (added to handle Workers model)
class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = '_all_'

















