import streamlit as st
import requests
import json

# App icon & Title
c1, c2 = st.columns([0.3, 2])

with c1:
    st.image(
        "icon.jpg",
        width=90,
    )

with c2:
    st.caption("")
    st.title('DAILY HOROSCOPE APP')

with st.expander("App Details"):
     st.markdown("""
         💫 It gives you real-time horoscope & astrology info based on your zodiac sign.
         \nBelow are the **12 Zodiac signs** categorized based on the main four elements of nature! 🌍
         \nYou can find your sign according to your *birthday month* & check your horoscope 🧙‍♀️
         \nFor more info --- >  **[zodiac signs](https://www.britannica.com/topic/zodiac)**
         \nHave fun here! 🙌
     """)

##################################################################
# All 12 Zodiac signs acc. to their elements
col1, col2, col3, col4 = st.columns([8,9,8,9])
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

# Input process
c3, c4 = st.columns([5,5])
with c3:
    st.caption("")
    sign = st.selectbox(
        'Select your Zodiac Sign 👇',
        ('', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'))
with c4:
    st.caption("")
    day = st.selectbox('Select one day 👇',
    ('', 'today', 'yesterday', 'tomorrow'))

# Selected data
selected = (
('sign', sign),
('day', day),
)



#####################################################################

# Output
if st.button('View Results! 🤞'):
    # Passing the data using API link
    daily = requests.post('https://aztro.sameerkumar.website/', params=selected)

    # Converted to json & retrieved as String
    scope = daily.json()
    data = json.dumps(scope)
    h_scope = json.loads(data)

    # Fetching Description element
    desc  = h_scope['description']
    st.success(desc)
    
    c5, c6, c7 = st.columns([4,6,6])
    
    with c5:
        st.write('📅Date Range:', h_scope['date_range'])
        st.write('📅Date:', h_scope['current_date'])
    
    with c6:
        st.write('✨Compatibility:', h_scope['compatibility'])
        st.write('🙄Mood:', h_scope['mood'])
        st.write('🌟Color:', h_scope['color'])
    
    with c7:
        st.write('🔢Lucky Number:', h_scope['lucky_number'])
        st.write('⌚Lucky Time:', h_scope['lucky_time'])