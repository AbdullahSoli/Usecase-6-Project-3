import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
#import plotly.figure_factory as ff
#import matplotlib.pyplot as plt
url ='https://raw.githubusercontent.com/AbdullahSoli/Project-3-streamlit/main/cleaned_RiyadhVillasAqar2.csv'
#df= pd.read_csv('cleaned_RiyadhVillasAqar.csv')
df= pd.read_csv(url)


st.html(
    "<h1>الفلل في الرياض </h1>"
    "<p>مقدمة</p>"
)

st.image("https://github.com/AbdullahSoli/Usecase-6-Project-3/blob/main/Riyadh-City-Skyline.gif")
#st.video("https://github.com/AbdullahSoli/Usecase-6-Project-3/blob/main/Riyadh%20City%20Skyline.mp4")


st.html(
    "<h1>السؤال الاول ؟ </h1>"
    "<p>شرح</p>"
)
data = pd.DataFrame({
    'labels': ['Maid Room', 'Driver Room'],
    'sizes': [df['maidRoom'].sum(), df['driverRoom'].sum()]
})

st.html(
    "<h1>السؤال الثاني ؟ </h1>"
    "<p>شرح</p>"
)
chart = alt.Chart(data).mark_arc().encode(
    theta=alt.Theta(field='sizes', type='quantitative'),
    color=alt.Color(field='labels', type='nominal'),
    tooltip=[alt.Tooltip(field='labels', type='nominal'), alt.Tooltip(field='sizes', type='quantitative')]
).properties(
    title='Maid Room and Driver Room'
)


st.altair_chart(chart, use_container_width=True)


# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)

st.html(
    "<h1>السؤال الثالث ؟ </h1>"
    "<p>شرح</p>"
)
avg_price_rooms = df.groupby('location')['price'].mean().reset_index()

# Create the Altair bar chart
chart = alt.Chart(avg_price_rooms).mark_bar().encode(
    x=alt.X('location:N', title='Location'),
    y=alt.Y('price:Q', title='Average Price'),
    tooltip=['location:N', 'price:Q']
).properties(
    title='Average Price of Room Objects by Location'
).configure_axis(
    labelAngle=45  # Rotate x-axis labels for better readability
)
st.altair_chart(chart, use_container_width=True)


avg_price_5_rooms = df[df['rooms'] == 5].groupby('location')['price'].mean().reset_index()
avg_price_5_rooms.columns = ['location', 'average_price']
bar_chart = alt.Chart(avg_price_5_rooms).mark_bar().encode(
    x=alt.X('location:N', title='Location', sort='-y'),
    y=alt.Y('average_price:Q', title='Average Price'),
    tooltip=['location:N', 'average_price:Q']  
).properties(
    title='Average Price for 5 Room Objects by Location',
    width=800,
    height=400
)
st.altair_chart(bar_chart, use_container_width=True)


avg_price_4_rooms = df[df['rooms'] == 4].groupby('location')['price'].mean().reset_index()
avg_price_4_rooms.columns = ['location', 'average_price']
bar_chart = alt.Chart(avg_price_4_rooms).mark_bar().encode(
    x=alt.X('location:N', title='Location', sort='-y'),
    y=alt.Y('average_price:Q', title='Average Price'),
    tooltip=['location:N', 'average_price:Q']  
).properties(
    title='Average Price for 4 Room Objects by Location',
    width=800,
    height=400
)
st.altair_chart(bar_chart, use_container_width=True)


st.html(
    "<h1>السؤال الرابع ؟ </h1>"
    "<p>شرح</p>"
)
duplex_counts = df['duplex'].value_counts().reset_index()
duplex_counts.columns = ['duplex', 'count']
pie_chart = alt.Chart(duplex_counts).mark_arc().encode(
    theta=alt.Theta(field='count', type='quantitative', title='Count'),
    color=alt.Color(field='duplex', type='nominal', title='Duplex'),
    tooltip=['duplex:N', 'count:Q']  
).properties(
    title='Distribution of Duplex Values',
    width=400,
    height=400
).configure_arc(
    outerRadius=150
)
st.altair_chart(pie_chart, use_container_width=True)


st.html(
    "<h1>السؤال الخامس ؟ </h1>"
    "<p>شرح</p>"
)
property_age_lt_10 = len(df[df['propertyAge'] < 10])
property_age_gt_20 = len(df[df['propertyAge'] > 20])
data = {
    'Property Age Group': ['Property Age < 10', 'Property Age > 20'],
    'Count': [property_age_lt_10, property_age_gt_20]
}
df_counts = pd.DataFrame(data)
bar_chart = alt.Chart(df_counts).mark_bar().encode(
    x=alt.X('Property Age Group:N', title='Property Age'),
    y=alt.Y('Count:Q', title='Count'),
    color='Property Age Group:N',
    tooltip=['Property Age Group:N', 'Count:Q']  
).properties(
    title='توزيع العقارات حسب العمر ',
    width=400,
    height=300
)
st.altair_chart(bar_chart, use_container_width=True)
pie_chart = alt.Chart(df_counts).mark_arc().encode(
    theta=alt.Theta(field='Count', type='quantitative', title='Count'),
    color=alt.Color(field='Property Age Group', type='nominal', title='Property Age Group'),
    tooltip=['Property Age Group:N', 'Count:Q']  # عرض التفاصيل عند التفاعل مع القطاعات
).properties(
    title='توزيع العقارات حسب العمر',
    width=400,
    height=400
).configure_arc(
    outerRadius=150
)

# عرض الرسم البياني في Streamlit
st.altair_chart(pie_chart, use_container_width=True)





st.html(
    "<h1>السؤال السادس ؟ </h1>"
    "<p>شرح</p>"
)

property_counts = df['location'].value_counts().reset_index()
property_counts.columns = ['location', 'count']


top_10_locations = property_counts.head(10)
donut_chart = alt.Chart(top_10_locations).mark_arc(innerRadius=100).encode(
    theta=alt.Theta(field='count', type='quantitative', title='Count'),
    color=alt.Color(field='location', type='nominal', title='Location'),
    tooltip=['location:N', 'count:Q']  # عرض التفاصيل عند التفاعل مع القطاعات
).properties(
    title='توزيع المنازل حسب المناطق',
    width=400,
    height=400
).configure_arc(
    outerRadius=150
)


bar_chart = alt.Chart(top_10_locations).mark_bar().encode(
    x=alt.X('location:N', title='Location', sort='-y'),
    y=alt.Y('count:Q', title='Count'),
    color='location:N',
    tooltip=['location:N', 'count:Q']  
).properties(
    title='توزيع المنازل حيب المناطق',
    width=400,
    height=300
)

# عرض الرسوم البيانية في Streamlit
st.altair_chart(donut_chart, use_container_width=True)
st.altair_chart(bar_chart, use_container_width=True)
