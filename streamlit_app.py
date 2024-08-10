import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import altair as alt
#import plotly.figure_factory as ff
#import matplotlib.pyplot as plt
url ='https://raw.githubusercontent.com/AbdullahSoli/Usecase-6-Project-3/main/cleaned_RiyadhVillasAqar2.csv'
#df= pd.read_csv('cleaned_RiyadhVillasAqar.csv')
df= pd.read_csv(url)


st.html(
    "<h1>الفلل في الرياض </h1>"
    "<p>مقدمة</p>"
)

# HTML code with autoplay and muted attributes
video_html = """
<video autoplay muted loop style="width: 100%;">
  <source src="https://github.com/AbdullahSoli/Usecase-6-Project-3/blob/main/Riyadh%20City%20Skyline.mp4?raw=true" type="video/mp4">
  Your browser does not support the video tag.
</video>
"""

# Display the video using custom HTML with a smaller height
components.html(video_html, height=500)


st.html(
    "<h1>السؤال الاول ؟ </h1>"
    "<p>شرح</p>"
)

st.html(
    "<h1>السؤال الثاني ؟ </h1>"
    "<p>شرح</p>"
)
data = pd.DataFrame({
    'Labels': ['Maid Room', 'Driver Room'],
    'Sizes': [100, 50]
})

data['Percent'] = (data['Sizes'] / data['Sizes'].sum() * 100).round(2).astype(str) + '%'

arc_chart = alt.Chart(data).mark_arc().encode(
    theta=alt.Theta(field='Sizes', type='quantitative'),
    color=alt.Color(field='Labels', type='nominal'),
    tooltip=[alt.Tooltip(field='Labels', type='nominal'), alt.Tooltip(field='Sizes', type='quantitative'), alt.Tooltip(field='Percent', type='nominal')]
)

text_chart = alt.Chart(data).mark_text(
    radius=100,  
    size=14,    
    dy=-90       
).encode(
    theta=alt.Theta(field='Sizes', type='quantitative'),
    text=alt.Text(field='Percent', type='nominal')
)

label_chart = alt.Chart(data).mark_text(
    radius=100,  
    size=12,    
    dy=-50,      
    color='black'  
).encode(
    theta=alt.Theta(field='Sizes', type='quantitative'),
    text=alt.Text(field='Labels', type='nominal')
)

chart = arc_chart + text_chart + label_chart

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


try:
    # Filter the data based on propertyAge and space
    property_age_lt_10 = df[(df['propertyAge'] < 10) & (df['space'] <= 500)]
    property_age_gt_20 = df[(df['propertyAge'] > 20) & (df['space'] <= 500)]

    # Get the mean price for each group
    price_lt_10 = property_age_lt_10['price'].mean()
    price_gt_20 = property_age_gt_20['price'].mean()

    # Create a DataFrame for Altair
    price_data = pd.DataFrame({
        'Property Age': ['< 10', '> 20'],
        'Mean Price': [price_lt_10, price_gt_20]
    })

    # Create the Altair bar chart
    bar_chart = alt.Chart(price_data).mark_bar().encode(
        x=alt.X('Property Age:N', title='Property Age'),
        y=alt.Y('Mean Price:Q', title='Mean Price'),
        color=alt.Color('Property Age:N', scale=alt.Scale(domain=['<10 ', '> 20'], range=['#4863A0', '#646D7E'])),
        tooltip=[alt.Tooltip('Property Age:N', title='Property Age'), alt.Tooltip('Mean Price:Q', title='Mean Price')]
    ).properties(
        title='مقارنة بين اسعار البيوت بحسب العمر ',
        width=500,
        height=300
    )

    # Display the chart using Streamlit
    st.altair_chart(bar_chart, use_container_width=True)

except Exception as e:
    st.error(f"An error occurred: {e}")


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

st.html(
    "<h1>السؤال السابع ؟ </h1>"
    "<p>Scatter plot example description</p>"
)

# Example scatter plot: relationship between property age and price
scatter_plot = alt.Chart(df).mark_circle(size=60).encode(
    x=alt.X('propertyAge:Q', title='Property Age'),
    y=alt.Y('price:Q', title='Price'),
    color='location:N',
    tooltip=['location:N', 'propertyAge:Q', 'price:Q']
).properties(
    title='Scatter Plot of Property Age vs. Price',
    width=800,
    height=400
)

st.altair_chart(scatter_plot, use_container_width=True)
