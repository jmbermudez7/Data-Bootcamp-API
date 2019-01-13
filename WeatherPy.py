#!/usr/bin/env python
# coding: utf-8

# # WeatherPy
# ----
# 
# ### Analysis
# * As expected, the weather becomes significantly warmer as one approaches the equator (0 Deg. Latitude). More interestingly, however, is the fact that the southern hemisphere tends to be warmer this time of year than the northern hemisphere. This may be due to the tilt of the earth.
# * There is no strong relationship between latitude and cloudiness. However, it is interesting to see that a strong band of cities sits at 0, 80, and 100% cloudiness.
# * There is no strong relationship between latitude and wind speed. However, in northern hemispheres there is a flurry of cities with over 20 mph of wind.
# 
# ---
# 
# #### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[17]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import datetime
import json
import requests
import csv


# Import API key
import api_keys

# Incorporated citipy to determine city based on latitude and longitud
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# ## Generate Cities List

# In[18]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# ### Perform API Calls
# * Perform a weather check on each city using a series of successive API calls.
# * Include a print log of each city as it'sbeing processed (with the city number and city name).
# 

# In[19]:


url = "http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric"
response_json= requests.get(url).json()
print("Server Response: " + str(response_json))


# ### Convert Raw Data to DataFrame
# * Export the city data into a .csv.
# * Display the DataFrame

# In[20]:


with open('cities.csv', mode='w') as city_frame:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


# In[ ]:


pd.read_csv('cities.csv')
head(5)


# ### Plotting the Data
# * Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.
# * Save the plotted figures as .pngs.

# #### Latitude vs. Temperature Plot

# In[ ]:


plt.scatter(x="Latitude", y= "Max Temperature", alpha=0.5,)
plt.xlabel("Latitude")
plt.ylabel("Max Temperature")
plt.legend(loc='upper left')
plt.show()


# #### Latitude vs. Humidity Plot

# In[ ]:


plt.scatter(x="Latitude", y= "Hummidity", alpha=0.5,)
plt.xlabel("Latitude")
plt.ylabel("Hummidity")
plt.legend(loc='upper left')
plt.show()


# #### Latitude vs. Cloudiness Plot

# In[ ]:


plt.scatter(x="Latitude", y= "Cloudliness", alpha=0.5,)
plt.xlabel("Latitude")
plt.ylabel("Max Temperature")
plt.legend(loc='upper left')
plt.show()


# #### Latitude vs. Wind Speed Plot

# In[ ]:


plt.scatter(x="Latitude", y= "Wind Speed", alpha=0.5,)
plt.xlabel("Latitude")
plt.ylabel("Wind Speed")
plt.legend(loc='upper left')
plt.show()


# In[ ]:





# In[ ]:




