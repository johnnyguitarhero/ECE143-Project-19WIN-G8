import pandas as pd
import numpy as np

def Category_map( instr ):
    '''
    This function re-assign categories of apps from Google Play. We generally use 
    Apple Store standards. This is mainly used for apply function of pandas.
    
    Arg:
        instr: input string
    Return:
        outstr: output string
    '''
    assert isinstance(instr,str)
    
    mapping = {'BOOKS_AND_REFERENCE':'Book','BUSINESS':'Business','COMICS':'Book','EDUCATION':'Education',              'ENTERTAINMENT':'Entertainment','EVENTS':'Entertainment','FINANCE':'Finance',               'FOOD_AND_DRINK':'Food & Drink','GAME':'Games','HEALTH_AND_FITNESS':'Health & Fitness',              'LIFESTYLE':'Lifestyle','BEAUTY':'Lifestyle','HOUSE_AND_HOME':'Lifestyles','MEDICAL':'Medical',              'MAPS_AND_NAVIGATION':'Navigation','NEWS_AND_MAGAZINES':'News','ART_AND_DESIGN':'Photo & Video',               'PHOTOGRAPHY':'Photo & Video',              'VIDEO_PLAYERS':'Photo & Video','PRODUCTIVITY':'Productivity','SHOPPING':'Shopping',              'COMMUNICATION':'Social Networking','DATING':'Social Networking','SOCIAL':'Social Networking',              'SPORTS':'Sports','TRAVEL_AND_LOCAL':'Travel','TOOLS':'Utilities','PERSONALIZATION':'Utilities',              'WEATHER':'Weather','Reference':'Book'}
    if instr in mapping.keys():
        outstr = mapping[instr]
    else:
        outstr = instr
    
    return outstr

def Size_map( instr ):
    '''
    This function converted string with k, KB, MB, GB
    to actual numbers
    
    Arg:
        instr: input string
    Return:
        size: size in MB
    '''
    
    if isinstance(instr,str):
        if instr != 'Varies with device':
            if instr[-1] == 'k':
                size = float(instr[:-1])/1024
            elif instr[-2:] == 'KB':
                size = float(instr[:-3])/1024
            elif instr[-2:] == 'MB':
                size = float(instr[:-3])
            elif instr[-2:] == 'GB':
                size = float(instr[:-3])*1024
            else:
                size = float(instr[:-1])
        else:
            size = 0 
    else:
        size = instr/1024/1024
    return size

def Rating_map( x ):
    '''
    This function converted rating string to actual numbers
    
    Arg:
        instr: input string
    Return:
        rate: rating
    '''
    if isinstance(x,str):
        rate = float(x.split(',')[0])
    else:
        rate = x
    return rate

def Rating_num( x ):
    '''
    This function converted num of rating in strings to actual numbers
    
    Arg:
        instr: input string
    Return:
        ratenum: num of rating
    '''
    
    if isinstance(x,str):
        ratestr = x.split(' ')[1]
        if ratestr[-1] == 'K':
            ratenum = float(ratestr[:-1])*1000
        elif ratestr[-1] == 'M':
            ratenum = float(ratestr[:-1])*1000000
        else:
            ratenum = float(ratestr)
    else:
        ratenum = x
    return ratenum

def Price_map( x ):
    '''
    This function converted price in strings to actual numbers
    
    Arg:
        x: input string or number
    Return:
        p: price
    '''
    
    if isinstance(x,str):
        x = x.split('\n')[0]
        if x[0] == '$':
            p = float(x[1:])
        elif x == 'Free':
            p = 0.0
        else:
            p = float(x)
    else:
        p = x
        
    return p
        

