#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:29:39 2021

@author: samhumphries

Builds Streamlit App
"""

#Import Needed Functions
import pandas as pd
import requests
from bs4 import BeautifulSoup

from newspaper import Article

import docx
from docx.enum.dml import MSO_THEME_COLOR_INDEX
from docx import Document
from docx.shared import Inches
from docx.shared import Pt


import re
import tldextract

import dateutil.parser as dp
import dateutil.tz as dtz
import datetime

#Import Streamlit
import streamlit as st

#Import Scraper.py
from Scraper import scraper



#####Build#####

#url_list = ["https://www.cnbc.com/id/100727362/device/rss/rss.html","http://www.npr.org/rss/rss.php?id=1004","https://aljazeera.com/xml/rss/all.xml","http://feeds.bbci.co.uk/news/rss.xml","https://rss.nytimes.com/services/xml/rss/nyt/World.xml"] ##NYT World

st.title("ASP ICYMI Helper Tool")

st.header("Choose Your Sources")

choice1 = st.selectbox('Would You Like to Use CNBC?', 
                      ('Yes', 'No'))
if choice1=='Yes':
    web1 = "https://www.cnbc.com/id/100727362/device/rss/rss.html"
else:
    web1 = ""



choice2 = st.selectbox('Would You Like to Use The New York Times?', 
                      ('Yes', 'No'))

if choice2=='Yes':
    web2 = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
else:
    web2 = ""



choice3 = st.selectbox('Would You Like to Use NPR?', 
                      ('Yes', 'No'))

if choice3=='Yes':
    web3 = "http://www.npr.org/rss/rss.php?id=1004"
else:
    web3 = ""



choice4= st.selectbox('Would You Like to Use BBC?', 
                      ('Yes', 'No'))

if choice4=='Yes':
    web4 = "http://feeds.bbci.co.uk/news/rss.xml"
else:
    web4 = ""



choice5 = st.selectbox('Would You Like to Use Al Jazeera?', 
                      ('Yes', 'No'))

if choice5=='Yes':
    web5 = "https://aljazeera.com/xml/rss/all.xml"
else:
    web5 = ""
    


##########
## Choose Subjects ####
#########

st.header("Choose Your Subjects")


if st.checkbox('American Competitiveness'):
    topic1 = True
else:
    topic1 = False
    
if st.checkbox('Arctic'):
    topic2 = True
else:
    topic2 = False
    
if st.checkbox('Asymmetric Operations'):
    topic3 = True
else:
    topic3 = False

if st.checkbox('Climate Security'):
    topic4 = True
else:
    topic4 = False
    
if st.checkbox('Energy Security'):
    topic5 = True
else:
    topic5 = False
    
if st.checkbox('National Security and Strategy'):
    topic6 = True
else:
    topic6 = False
    
if st.checkbox('Nuclear Security'):
    topic7 = True
else:
    topic7 = False
    
if st.checkbox('US-Russia Relations'):
    topic8 = True
else:
    topic8 = False
    
    
    
    
    
    
    
    
    
    
    
    
    
    

if st.button('Start'):
    scraper(web1,web2,web3,web4,web5, topic1, topic2, topic3, topic4, topic5, topic6,
            topic7, topic8)
    st.write('Complete. Please check your directory for the word document.')