import streamlit as st
import requests
import json
from zodiac_sign import your_sign


st.set_page_config(
    page_title="Daily Horoscope App",
    page_icon="🔮",)

# App icon & Title
c1, c2 = st.columns([0.3, 2], gap="large")

with c1:
    st.image(
        "icon.png",
        width=100,
    )

with c2:
    st.write("")
    st.write("")
    st.title('DAILY HOROSCOPE APP')

with st.expander("App Details"):
     st.markdown("""
         💫 It gives you real-time horoscope & astrology info based on your zodiac sign.
         \n- Below are the **12 Zodiac signs** categorized based on the main four elements of nature! 🌍
         \n- You can find your zodiac sign **from the sidebar!** 🧙‍♀️
         \n- For more info about zodiac signs --- >  **[Click here](https://www.britannica.com/topic/zodiac)**
         \nHope you have fun! 🙌

     """)

##################################################################
# Checks your zodiac sign
output = your_sign()
st.sidebar.write('🦄 Your sign is : ', output)
##################################################################    

# All 12 Zodiac signs acc. to their elements
col1, col2, col3, col4 = st.columns(4, gap="medium")
with col1:
    st.markdown('***🔥 Fire Signs***')
    st.markdown("""
                 \n♈ Aries : March 21 - April 19
                 \n♌ Leo : July 23 - August 22
                 \n♐ Sagittarius : Nov 22 - Dec 21""")

with col2:
    st.markdown('***🌍 Earth Signs***')
    st.markdown("""
                 \n♉ Taurus : April 20 - May 20
                 \n♍ Virgo : August 23 - Sept 22
                 \n♑ Capricorn : Dec 22 - Jan 19""")

with col3:
    st.markdown('***🍃 Air Signs***')
    st.markdown("""
                 \n♊ Gemini : May 21 - June 21
                 \n♎ Libra : Sept 23 - Oct 23
                 \n♒ Aquarius : Jan 20 - Feb 18""")

with col4:
    st.markdown('***🌊 Water Signs***')
    st.markdown("""
                \n♋ Cancer : June 22 - July 22
                 \n♏ Scorpio: Oct 24 - Nov 21
                 \n♓ Pisces : Feb 19 - March 20""")

####################################################################

st.write("")
st.write("")
st.caption("")
sign = st.selectbox(
    'Select your Zodiac Sign 👇',
    ('', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'))

# Results Function --->
def results(day):
    
    # Parameters added
    selected = (
        ('sign', sign),
        ('day', day),
        )
    
    # Passing the data using API link
    daily = requests.post('https://aztro.sameerkumar.website/', params=selected)

    # Converted to json & retrieved as String
    scope = daily.json()
    data = json.dumps(scope)
    h_scope = json.loads(data)

    # Fetching Description element
    desc  = h_scope['description']
    st.success(desc)
    st.write("")
    
    c5, c6, c7 = st.columns(3, gap="medium")
        
    with c5:
        st.write('📅Date Range:', h_scope['date_range'])
        st.caption("")
        st.write('📅Date:', h_scope['current_date'])
    
    with c6:
        st.write('🧡Compatibility:', h_scope['compatibility'])
        st.caption("")
        st.write('🙄Mood:', h_scope['mood'])
        st.caption("")
        st.write('🌟Color:', h_scope['color'])
    
    with c7:
        st.write('🔢Lucky Number:', h_scope['lucky_number'])
        st.caption("")
        st.write('⌚Lucky Time:', h_scope['lucky_time'])


if st.button('View Results! 🤞'):
    tab1, tab2, tab3 = st.tabs(["TODAY", "YESTERDAY", "TOMORROW"])
    with tab1:
        results('today')
        
    with tab2:
        results('yesterday')
        
    with tab3:
        results('tomorrow')
