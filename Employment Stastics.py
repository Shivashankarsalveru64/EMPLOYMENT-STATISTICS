#!/usr/bin/env python
# coding: utf-8

# # Employment Statistics: Data Preprocessing and Exploratory Analysis.

# ## Importing Libraries

# In[26]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# ## Importing Dataset

# In[27]:


df=pd.read_csv("Unemployment in India.csv")


# ## Data Analysis

# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


print(df.info())


# In[7]:


df.describe()


# In[8]:


df.nunique()


# In[9]:


df.isnull().sum()


# In[10]:


df.duplicated().sum()


# In[11]:


df = df.drop_duplicates()


# In[12]:


df.duplicated().sum()


# In[13]:


df.isnull().sum()


# In[14]:


df = df.dropna()
df


# In[15]:


df.isnull().sum()


# In[16]:


df.info()


# In[17]:


df.columns = df.columns.str.strip()
df['Date'] = df['Date'].str.strip()
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df =df.drop(['Date'],axis = 1)
df


# In[18]:


df['Employment Rate (%)'] = (df['Estimated Employed'] / df['Estimated Labour Participation Rate (%)']) * 100
df


# ## EDA (Exploratory Data Analysis)

# In[19]:


plt.figure(figsize=(15,6))
sns.countplot(x="Area",data=df)
plt.xticks(rotation = 45)
plt.show()


# # RESULT:
# The above graph represents that the dataset consists of more of urban data.
# The above graph also represents that the Urban area has more unemployment rate compared to Rural area.

# In[20]:


plt.figure(figsize=(15,6))
sns.countplot(data=df, x="Region", color="skyblue")
plt.xticks(rotation = 45)
plt.show()


# # Result:
# The above plot represents the histplot of region column of the dataset.Also we can conclude that many states have almost consists of the equal number of datapoints.

# In[21]:


# Distribution plot of unemployment rate
plt.figure(figsize=(10, 6))
sns.boxplot(df['Estimated Unemployment Rate (%)'])
plt.title('Distribution of Unemployment Rate')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Frequency')
dist_plot = plt.gcf()
plt.show()


# # Result:
# The above plot represents the hist plot of the unemployment rate column of the employement dataset
# 

# In[22]:


# Time series plot of unemployment rate
plt.figure(figsize=(10, 6))
sns.lineplot(x='Month', y='Estimated Unemployment Rate (%)', data=df)
plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unempl0oyment Rate (%)')
time_series_plot = plt.gcf()
plt.show()


# # Result:
# The above plot represents the line plot between the date and unemployement columns of the employement dataset.

# In[23]:


# Box plot of unemployment rate by region
plt.figure(figsize=(10, 6))
sns.boxplot(x='Region', y='Estimated Unemployment Rate (%)', data=df)
plt.title('Unemployment Rate by Region')
plt.xlabel('Region')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation = 45)
box_plot = plt.gcf()
plt.show()


# # Result:
# The above plot represents the box plot between the region and estimated unemployement rate columns of the unemployement dataset . 

# In[24]:


andhra_pradesh_data = df[df['Region'] == 'Andhra Pradesh']


# In[25]:


plt.figure(figsize=(15, 6))
sns.lineplot(x=andhra_pradesh_data.index, y='Estimated Unemployment Rate (%)', data=andhra_pradesh_data)
plt.title('Unemployment Rate in Andhra Pradesh')
plt.xlabel('Index')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.show()


# # Result :
# The above plot represents the andhra pradesh state unemployement rate .

# # Conclusion:
# From the above data analysis , we can analyse the dataset which is used in the above programming.From the above analysis, we can easily understand the causes of unemployement and which region has maximum unemployement rate.
