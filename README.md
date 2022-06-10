
# Hand Tracking

In this project I use Python Django Framework for creating backend side of hand tracking system.
For machine learning part I have used my machine learning model that is at the bottom of readme file.


## API Usage

#### POST Machine Learning model data 

```http
  POST /get-ml/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `1` | `Array` | **Required**. x,y and z coordinates |
| `2` | `Array` | **Required**. x,y and z coordinates |
...
| `20` | `Array` | **Required**. x,y and z coordinates |


## Start 

Python 3 or greater must be installed

```python 
git clone https://github.com/emrecoskun705/hand_tracking_django.git
cd ./hand_tracking_django
pip install ./requriments.txt 
python manage.py runserver
```


## Related Projects

[Mobile App](https://github.com/emrecoskun705/hand_tracking_app)
[Machine Learning Model](https://github.com/emrecoskun705/hand_tracking)




  
