# sudo pip install requests
# sudo pip install python-firebase

from firebase import firebase
firebase = firebase.FirebaseApplication('https://sensingdata-80c3d.firebaseio.com/', None)
result = firebase.get('/Taipei/temperaturehumidity', None)
print result