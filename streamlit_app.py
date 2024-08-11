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
    "<h1>         !! هل امتلاك فيلا في الرياض مستحيل         </h1>"
  
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
    "<br>"
    "<h6>  العديد من الناس يتمنى امتلاك فيلا في الرياض وانا واحد منهم  ولكن هناك عائق كبير وهو في الأسعار المبالغة ، وهي من أكبر المشاكل في الرياض بسبب التطور الكبير مما ادى الى ارتفاع الاسعار لكن لكل مشكلة حل ف قررنا ان نستلم الموضوع بجدية و نحلل لماذا هنالك ارتفاع في الأسعار بشكل كبير.  </h6>"
)



avg_price_rooms = df.groupby('location')['price'].mean().reset_index()

# Create the Altair bar chart
chart = alt.Chart(avg_price_rooms).mark_bar().encode(
    x=alt.X('location:N', title='Location'),
    y=alt.Y('price:Q', title='Average Price'),
    tooltip=['location:N', 'price:Q']
).properties(
    title='Average Price  by Location'
).configure_axis(
    labelAngle=45  # Rotate x-axis labels for better readability
)
st.altair_chart(chart, use_container_width=True)


st.html(
   "<br>"
    "<p>لاحظنا أن أكثر الأسعار ارتفاعا في شمال الرياض و وجدنا أن المطار و أكاديمية طويق جامعة الأميرة نورة وجامعة الإمام محمد بن سعود و بوليفارد  الرياض يكون قريب من الشمال مما أدى الى ارتفاع الاسعار بشكل ملحوظ كما نلاحظ في الرسم البياني</p>"
)

st.html(
   "<br>"
   "<br>"
    "<p>  اتاني فضول حول ما إذا كان الناس ترغب في غرفة ل السائق و غرفة للخادمة أو تكتفي بالخادمة اريد معرف طبيعة الناس في الشراء لكي ابني عليها تفسير منطقي للغاية   </p>"
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
  
    "<p> نلاحظ في الرسم الدائرة الاعلى ان الناس لا يهتمون بشكل كبير في السائق بل العكس يهتمون في الخادمة ، وبعد طرح الأسئلة على  الناس لماذا يفضلون الخادمة على السائق ، و وجدتهم يقولون ان مهام السائق ممكن يقوم بعملها الاب و الابن و الأخ و الزوج فلا داعي ان يكون هناك سائق بعكس الخادمة .  </p>"
)

st.html(
    "<br>"
    "<br>"
    "<p>لنفترض أن نريد نحسب متوسط الفلل ل ٥ و ٤ غرف فكيف يكون الفرق بين كل منطقة عن الأخرى </p>"
   
)
# avg_price_rooms = df.groupby('location')['price'].mean().reset_index()

# # Create the Altair bar chart
# chart = alt.Chart(avg_price_rooms).mark_bar().encode(
#     x=alt.X('location:N', title='Location'),
#     y=alt.Y('price:Q', title='Average Price'),
#     tooltip=['location:N', 'price:Q']
# ).properties(
#     title='Average Price  by Location'
# ).configure_axis(
#     labelAngle=45  # Rotate x-axis labels for better readability
# )
# st.altair_chart(chart, use_container_width=True)


avg_price_5_rooms = df[df['rooms'] == 5].groupby('location')['price'].mean().reset_index()
avg_price_5_rooms.columns = ['location', 'average_price']
bar_chart = alt.Chart(avg_price_5_rooms).mark_bar().encode(
    x=alt.X('location:N', title='Location', sort='-y'),
    y=alt.Y('average_price:Q', title='Average Price'),
    tooltip=['location:N', 'average_price:Q']  
).properties(
    title='Average Price for 5 Room Objects by Location',
    width=800,
    height=450
).configure_axis(
    labelAngle=45  # Rotate x-axis labels for better readability
)
st.altair_chart(bar_chart, use_container_width=True)



# avg_price_5_rooms = df[df['rooms'] == 5].groupby('location')['price'].mean().reset_index()
# avg_price_5_rooms.columns = ['location', 'average_price']
# bar_chart = alt.Chart(avg_price_5_rooms).mark_bar().encode(
#     x=alt.X('location:N', title='Location', sort='-y'),
#     y=alt.Y('average_price:Q', title='Average Price'),
#     tooltip=['location:N', 'average_price:Q']  
# ).properties(
#     title='Average Price for 5 Room Objects by Location',
#     width=800,
#     height=400
# ).configure_axis(
#     labelAngle=45  # Rotate x-axis labels for better readability
# )
# st.altair_chart(bar_chart, use_container_width=True)


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
).configure_axis(
    labelAngle=45  # Rotate x-axis labels for better readability
)
st.altair_chart(bar_chart, use_container_width=True)

st.html(
  
    "<p>كما نلاحظ أن شمال الرياض تقريبا ضعف شرق الرياض الذي يحتل المركز الثاني   </p>"
   
)
st.html(
    "<br>"
    "<br>"
    "<p>طيب كم نسبة الفيلا الدوبلكس عن غيرها ، طرحنا هذا السؤال بسبب ملاحظاتنا لكثرتها أثناء تجولنا في الأحياء السكنية لماذا هناك الكثير منها  </p>"
   
)

duplex_counts = df['duplex'].map({1: 'Villa', 0: 'Duplex'}).value_counts().reset_index()
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
  
    "<p>وأوضحت بحوثنا إلى أن الفيلا الدوبليكس هي الأكثر بسبب ارتفاع سعر الاراضي مما ادى إلى توجه الناس إلى المساحات الصغيرة.</p>"
)

st.html(
    "<br>"
    "<br>"
    "<h5>هل الفيلا اللي عمرها كبير تكون ارخص من الفيلا  الجديدة ؟</h5>"
    "<p>اذا كنت تبحث عن فيلا عمرها كبير ليكون سعرها معقول بسبب تزايد الاسعار ، اتينا ب احصائية معدل أسعار الفيلا القديمة و الجديدة  كما ترى .</p>"
)


import pandas as pd
import altair as alt
import streamlit as st

try:
    # Filter the data based on propertyAge and space
    property_age_lt_10 = df[(df['propertyAge'] < 10) & (df['space'] <= 500)]
    property_age_gt_20 = df[(df['propertyAge'] > 20) & (df['space'] <= 500)]

    # Get the mean price for each group
    price_lt_10 = property_age_lt_10['price'].mean()
    price_gt_20 = property_age_gt_20['price'].mean()

    # Create a DataFrame for Altair with new column names
    price_data = pd.DataFrame({
        'عمر الملكية': ['أقل من 10 سنوات', 'أكبر من 20 سنة'],
        'متوسط السعر': [price_lt_10, price_gt_20]
    })
    

    # Create the Altair bar chart
#     bar_chart = alt.Chart(price_data).mark_bar().encode(
#         x=alt.X('عمر الملكية:N', title='عمر الملكية'),
#         y=alt.Y('متوسط السعر:Q', title='متوسط السعر'),
#         color=alt.Color('عمر الملكية:N', scale=alt.Scale(domain=['أقل من 10 سنوات', 'أكبر من 20 سنة'], range=['#4863A0', '#646D7E'])),
#         tooltip=[alt.Tooltip('عمر الملكية:N', title='عمر الملكية'), alt.Tooltip('متوسط السعر:Q', title='متوسط السعر')]
#     ).properties(
#         title=' مقارنة بين أسعار الفيلل بحسب العمر العقار',
#         width=500,
#         height=300
#     ).configure_axis(
#     labelAngle=45  # Rotate x-axis labels for better readability
# )

    bar_chart = alt.Chart(price_data).mark_bar().encode(
        x=alt.X('عمر الملكية:N', title='Property Age'),
        y=alt.Y('متوسط السعر:Q', title='Average price'),
        color=alt.Color('عمر الملكية:N', scale=alt.Scale(domain=['أقل من 10 سنوات', 'أكبر من 20 سنة'], range=['#4863A0', '#646D7E'])),
        tooltip=[alt.Tooltip('عمر الملكية:N', title='Property Age Years'), alt.Tooltip('متوسط السعر:Q', title='متوسط السعر')]
    ).properties(
        title='مقارنة بين أسعار الفلل بحسب العمر',
        width=500,
        height=500
    ).configure_axis(
    labelAngle=45  # Rotate x-axis labels for better readability
)




#  bar_chart = alt.Chart(price_data).mark_bar().encode(
#         x=alt.X('عمر الملكية:N', title='عمر الملكية'),
#         y=alt.Y('متوسط السعر:Q', title='متوسط السعر'),
#         color=alt.Color('عمر الملكية:N', scale=alt.Scale(domain=['أقل من 10', 'أكثر من 20'], range=['#4863A0', '#646D7E'])),
#         tooltip=[alt.Tooltip('عمر الملكية:N', title='عمر الملكية'), alt.Tooltip('متوسط السعر:Q', title='متوسط السعر')]
#     ).properties(
#         title='مقارنة بين أسعار البيوت بحسب العمر',
#         width=500,
#         height=300
#     ).configure_axis(
#     labelAngle=45  # Rotate x-axis labels for better readability
# )


    

    # Display the chart using Streamlit
    st.altair_chart(bar_chart, use_container_width=True)



except Exception as e:
    st.error(f"An error occurred: {e}")

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

st.html(

    "<p>كما تشاهد  ان الفيلا الحديثة تكون اغلى من القديمة بسبب استخدام العوازل و جودة البناء احدث و حداثة المواد المستخدمة </p>"
)


st.html(
    "<br>"
    "<br>"
    "<h4>كم عدد الفلل المطروحة في الخمس مناطق ؟ </h4>"
   
)

property_counts = df['location'].value_counts().reset_index()
property_counts.columns = ['location', 'count']


top_10_locations = property_counts.head(10)
donut_chart = alt.Chart(top_10_locations).mark_arc(innerRadius=100).encode(
    theta=alt.Theta(field='count', type='quantitative', title='Count'),
    color=alt.Color(field='location', type='nominal', title='Location'),
    tooltip=['location:N', 'count:Q']  # عرض التفاصيل عند التفاعل مع القطاعات
).properties(
    title='توزيع الفلل حسب المناطق',
    width=400,
    height=400
).configure_arc(
    outerRadius=150
)


bar_chart = alt.Chart(top_10_locations).mark_bar().encode(
    x=alt.X('location:N', title='الموقع', sort='-y'),
    y=alt.Y('count:Q', title='عدد الفلل'),
    color='location:N',
    tooltip=['location:N', 'count:Q']  
).properties(
    title='توزيع الفلل حسب المناطق',
    width=500,
    height=420
).configure_axis(
    labelAngle=45  # Rotate x-axis labels for better readability
)


# عرض الرسوم البيانية في Streamlit
st.altair_chart(donut_chart, use_container_width=True)
st.altair_chart(bar_chart, use_container_width=True)

st.html(
    "<h4>ماذا !!😱  انا لا اصدق ان شمال الرياض لم تكن الاول </h4>"
    "<p>كما تشاهدون ان المنطقة الغربية تحتل المرتبة الاولى بعدد الفلل يزيد عن 13 ألف وحدة سكنية </p>"
)

# Example scatter plot: relationship between property age and price
# scatter_plot = alt.Chart(df).mark_circle(size=60).encode(
#     x=alt.X('propertyAge:Q', title='Property Age'),
#     y=alt.Y('price:Q', title='Price'),
#     color='location:N',
#     tooltip=['location:N', 'propertyAge:Q', 'price:Q']
# ).properties(
#     title='Scatter Plot of Property Age vs. Price',
#     width=800,
#     height=400
# )

# st.altair_chart(scatter_plot, use_container_width=True)


st.html(
    "<br>"
    "<br>"
    "<br>"
    "<br>"
    "<h6>وفي الختام لاحظنا لماذا هناك فرق كبير في الأسعار وعرفنا سبب ارتفاع الأسعار وطبيعة الأشخاص في الشراء، وقد يكون التقرير مفيداً لك في حالة الشراء أو الاستثمار للتعرف على متطلبات الأشخاص. </h6>"
    "<br>"
    "<br>"
  #  "<h2><a href="https://sa.aqar.fm/"> مصدر البيانات</a></h2>"
    "<h2>  sa.aqar.fm    مصدر البيانات </h2>"

)
