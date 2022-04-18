import os
from django.conf import settings
import joblib

hand_gesture_detector = os.path.join(settings.BASE_DIR, 'ml_model')


def detector(data):
    loaded_model = joblib.load(hand_gesture_detector)

    return loaded_model.predict(data)
