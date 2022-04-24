from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from core.hand_gesture_detector import detector

import numpy as np
import pandas as pd

from core.models import MLModel
from core.serializers import MLResponseSerializer


@api_view(['POST'])
def get_ml(request):
    if request.method == 'POST':
        data = []
        add_data = []
        for key, value in request.data.items():
            if int(key) == 21:
                add_data.append(1)
            else:
                add_data.append(value[0])
                add_data.append(value[1])
                add_data.append(value[2])

        data.append(add_data)
        column_name = [str(i) for i in range(0, 60)]
        column_name.append('hand')

        df = pd.DataFrame(data, columns=column_name)
        print(detector(df))
        serializer = MLResponseSerializer(data={'result': str(detector(df))})
        if serializer.is_valid():
            print(1)
            print(serializer.data)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
