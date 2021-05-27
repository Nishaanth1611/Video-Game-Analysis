import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(page_title="Best Video Games", page_icon="🎮",layout="centered", initial_sidebar_state='expanded')
st.title("📈Best Video Games on Sales")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.subheader('Developed with ❤ by [Nishaanth K](https://www.linkedin.com/in/nishaanth-k)')

st.subheader("⭐️**Spotlighted**")
col1 , col2 ,col3 = st.beta_columns(3)
col1.subheader("Best Ranked Game")
col1.write("Wii Sports")
col2.subheader("Best Publisher")
col2.write("Electronics Arts")
col3.subheader("Best Global Sales")
col3.write(82.74)

col1.subheader("Best Genre")
col1.write("Action")
col2.subheader("Best Platform")
col2.write("DS")
col3.subheader("Best Year of Sales")
col3.write(2009)

st.subheader("💥**Best Quotes**")
st.subheader("**❝The worst thing a kid can say about homework is that it is too hard. The worst thing a kid can say about a game is it's too easy.❞**")

image = Image.open('game.jpg')
st.image(image, caption='Game Rankings')

@st.cache
def load_dataset(data_link):
    dataset = pd.read_csv(data_link)
    return dataset

data_link = "C:\\Users\\nisht\\streamlit projects\\vgsales.csv"
data = load_dataset(data_link)
data=data.drop(columns=["JP_Sales","Other_Sales"])
my_data=data
data=data[data["Rank"] <= 50]

st.subheader("📊**Top 10 Games Sales**")
new=data.set_index("Name")
new=new[new["Rank"]<=10]
un_1=["Publisher","Platform","Year","Rank","Genre"]
for news in new:
    news=new.drop(columns=un_1)

st.area_chart(news)

st.subheader("📊**Genre Based in Years**")
new=data.set_index("Year")
un_1=["Publisher","Platform","Global_Sales","Rank","Name","NA_Sales","EU_Sales"]
for news in new:
    news=new.drop(columns=un_1)

st.bar_chart(news)

st.subheader("📊**Year based Games Sales**")
new=my_data.set_index("Year")
un_1=["Publisher","Platform","Rank","Genre","Name","NA_Sales","EU_Sales"]
for news in new:
    news=new.drop(columns=un_1)

st.line_chart(news)

top=data[data["Rank"]<=25]
st.header("**♛Top 25 Ranking Games**")
st.table(top)

st.subheader("✨**Some of Insights**")
col1, col2 = st.beta_columns(2)
with col1:
        st.subheader("📌**Top Genre**")
        genre=my_data.value_counts("Genre")
        genre=genre.rename("Max Genre")
        st.write(genre)

with col2:
        st.subheader("📌**Top Publisher**")
        publ=my_data.value_counts("Publisher")
        publ=publ.rename("Max")
        st.write(publ)

col1, col2 = st.beta_columns(2)
with col1:
        st.subheader("📌**Top Year**")
        year=my_data.value_counts("Year")
        year=year.rename("Max Year")
        st.write(year)

with col2:
        st.subheader("📌**Top Platform**")
        plat=my_data.value_counts("Platform")
        plat=plat.rename("Max Releases")
        st.write(plat)