import streamlit as st


def your_sign():
    st.sidebar.header('💫CHECK YOUR ZODIAC HERE!')
    day = st.sidebar.slider('Select your 🎂 date 👇', 1, 31)
    
    month = st.sidebar.select_slider(
        'Select your 👶 month 👇',
        options=['', 'Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'August', 'Sept', 'Oct', 'Nov', 'Dec'])
    
    # Cases for prediction of the zodiac signs
    if month == 'Dec':
        zodiac = 'Sagittarius' if (day < 22) else 'Capricorn'
        
    elif month == 'Jan':
        zodiac = 'Capricorn' if (day < 20) else 'Aquarius'
        
    elif month == 'Feb':
        zodiac = 'Aquarius' if (day < 19) else 'Pisces'
        
    elif month == 'March':
        zodiac = 'Pisces' if (day < 21) else 'Aries'
        
    elif month == 'April':
        zodiac = 'Aries' if (day < 20) else 'Taurus'
        
    elif month == 'May':
        zodiac = 'Taurus' if (day < 21) else 'Gemini'
        
    elif month == 'June':
        zodiac = 'Gemini' if (day < 21) else 'Cancer'
        
    elif month == 'July':
        zodiac = 'Cancer' if (day < 23) else 'Leo'
        
    elif month == 'August':
        zodiac = 'Leo' if (day < 23) else 'Virgo'
        
    elif month == 'Sept':
        zodiac = 'Virgo' if (day < 23) else 'Libra'
        
    elif month == 'Oct':
        zodiac = 'Libra' if (day < 23) else 'Scorpio'
        
    elif month == 'Nov':
        zodiac = 'Scorpio' if (day < 22) else 'Sagittarius'

    else:
        zodiac = ''

    return zodiac