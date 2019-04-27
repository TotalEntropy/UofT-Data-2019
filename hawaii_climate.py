#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
get_ipython().run_line_magic('autosave', '300')


# In[2]:


import numpy as np
import pandas as pd


# In[3]:


import datetime as dt


# # Reflect Tables into SQLAlchemy ORM

# In[4]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# In[5]:


engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# In[6]:


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)


# In[7]:


# We can view all of the classes that automap found
Base.classes.keys()


# In[8]:


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


# In[9]:


# Create our session (link) from Python to the DB
session = Session(engine)


# # Exploratory Climate Analysis

# In[10]:


# Design a query to retrieve the last 12 months of precipitation data and plot
# the results
first_row = session.query(Measurement).first()
first_row.__dict__


# In[11]:


# Calculate the date 1 year ago from the last data point in the database
last_date = str(session.query(Measurement.date).                order_by(Measurement.date.desc()).first())
last_date


# In[12]:


year_ago = (dt.datetime.strptime(last_date, "('%Y-%m-%d',)") -
                                dt.timedelta(days = 365))
#year_ago.date()


# In[13]:


# Perform a query to retrieve the data and precipitation scores
precipitation = session.query(Measurement.date, Measurement.prcp).    order_by(Measurement.date).    filter(Measurement.date >= year_ago.date()).all()


# In[14]:


# Save the query results as a Pandas DataFrame
precipitation_df = pd.DataFrame(precipitation)
#precipitation_df.head()


# In[15]:


# set the index to the date column
precipitation_df = precipitation_df.set_index('date')
#precipitation_df.head()


# In[16]:


# Sort the dataframe by date
precipitation_df = precipitation_df.sort_values(by = 'date')
precipitation_df.columns = ['precipitation']
#precipitation_df.head()


# In[17]:


# Use Pandas Plotting with Matplotlib to plot the data
precipitation_df.plot()


# In[18]:


# Use Pandas to calcualte the summary statistics for the precipitation data
precipitation_df.describe()


# In[19]:


# Design a query to show how many stations are available in this dataset?
first_row = session.query(Station).first()
first_row.__dict__


# In[20]:


session.query(func.count(Station.station).distinct()).all()


# In[21]:


# What are the most active stations? (i.e. what stations have the most rows)?
# List the stations and the counts in descending order.
session.query(Measurement.station, func.count(Measurement.tobs)).    group_by(Measurement.station).    order_by(func.count(Measurement.tobs).desc()).all()


# In[22]:


# Using the station id from the previous query, calculate the lowest
# temperature recorded, highest temperature recorded, and average temperature
# most active station?
results = session.query(func.min(Measurement.tobs),                        func.max(Measurement.tobs)).all()
results.append(session.query(func.avg(Measurement.tobs)).              group_by(Measurement.station).              order_by(func.count(Measurement.tobs).desc()).first())
results


# In[23]:


# Choose the station with the highest number of temperature observations.
# Query the last 12 months of temperature observation data for this station
# and plot the results as a histogram
active_station = session.query(Measurement.station).                    group_by(Measurement.station).                    order_by(func.count(Measurement.tobs).desc()).first()
temp = session.query(Measurement.tobs).                    filter(Measurement.station == active_station.station,                          Measurement.date >= year_ago.date()).all()
temp_df = pd.DataFrame(temp)
temp_df.columns = ['temperature']
temp_df.plot.hist(bins=12)

