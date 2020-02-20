#!/usr/bin/env python
# coding: utf-8

# In[1]:


import firebase_admin
from firebase_admin import credentials, firestore, db
#from firebase_admin import credentials
import os

#os.chdir('/home/heisenberg/UwinEmotions')
private_key_name = 'uwinemotions-firebase-adminsdk-y223w-53aacd7b6b.json'
cred = credentials.Certificate(private_key_name)
firebase_admin.initialize_app(cred, {'databaseURL': 'https://uwinemotions.firebaseio.com'})


# In[6]:


db = firestore.client()

doc_ref = db.collection('locations').document('1')
doc = doc_ref.get()

if doc.exists:
    location  = doc.to_dict()['location']
    emotion = doc.to_dict()['emotions']
    print(doc.id)
    print(location)
    print(emotion)
    
    


# In[7]:


import firebase_admin
doc_ref = db.collection('location')
#doc_ref.to_dict()


users_ref = db.collection('locations')
docs = users_ref.stream()
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
  


# In[ ]:





# In[ ]:




