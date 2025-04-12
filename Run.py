import sys
import json
import joblib
import numpy as np

# Load models
model = joblib.load('RandomForest_Model.pkl')
tfidf = joblib.load('TFIDF_RandomForest_Model.pkl')

# Get JSON input from Node.js
input_data = json.loads(sys.argv[1])

# Extract values
Lon = input_data['Lon']
Lat = input_data['Lat']
Pin = input_data['Pin']
Location = input_data['Location']
Des = input_data['Des']
PeopleCount = input_data['PeopleCount']

# Mapping location to number
Loc_Map = {'Urban': 1, 'Rural': 2, 'Remote': 3, 'Hilly': 4, 'Others': 5}
location_num = Loc_Map.get(Location, 5)

# TF-IDF for description
tfidf_features = tfidf.transform([Des]).toarray()

# Combine features
numeric_features = np.array([[location_num, Lat, Lon, PeopleCount, Pin]])
X_input = np.hstack([tfidf_features, numeric_features])

# Predict
prediction = model.predict(X_input)

# Return prediction to Node.js
print(json.dumps(str(prediction[0])))
