import streamlit as st
import pandas as pd
from PIL import Image
st.set_page_config(page_title="Video Games Analysis", page_icon="🎮",layout="centered", initial_sidebar_state='expanded')
st.title("📈Video Games Analysis")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

option_1,option_2 = "Play Store Games","Other Platform Games"
dashboard_options = st.sidebar.selectbox("How would you like to be contacted?",(option_1,option_2))
st.sidebar.write('Developed with ❤ by [Nishaanth K](https://www.linkedin.com/in/nishaanth-k)')
if dashboard_options == option_1:
     st.title(option_1)
     @st.cache
     def load_dataset(data_link_play):
          dataset_play = pd.read_csv(data_link_play)
          return dataset_play

     st.subheader("💥**Best Quotes**")
     st.subheader("**❝The worst thing a kid can say about homework is that it is too hard. The worst thing a kid can say about a game is it's too easy.❞**")

     image = Image.open('game.jpg')
     st.image(image, caption='Game Rankings')

#Initialize Data
     data_link_play = "googleplaystore.csv"
     data_play = load_dataset(data_link_play)
     play = data_play[ (data_play.Category == "GAME")]

#Month based production chart
     st.header("📊Month based Production")
     month = play["Last Updated"].astype(str) 
     month = month.str.replace(",", ' ')
     month = month.str.split(expand=True)
     month.columns = ['Month', 'Date', 'Year']
     del month["Date"]
     month = month["Month"] + month["Year"]
     pre=month.value_counts()
     pre=pre.to_frame()
     pre.columns = ["Best Month based on Production"]
     pre=pre[:10]
     st.line_chart(pre)

#Genre count chart
     st.header("📊Genres Contents")
     gen = play["Genres"].value_counts()
     gen=gen.to_frame()
     gen.columns = ["Best Month based on Production"]
     gen=gen[:15]
     st.line_chart(gen)
     
#Install count chart
     st.header("📊Total number of Installs")
     ins = play["Installs"].value_counts()
     ins=ins.to_frame()
     ins.columns = ["Best Installs counts"]
     ins=ins[:13]
     st.line_chart(ins)

#Action genre
     st.title("⚔️Action Genre")
     st.header("Total number of Games")
     st.write(365)
     st.header("Content Rating count")
     act_content = play[play["Category"]=="GAME"]
     act_content = act_content[act_content["Genres"]=="Action"]
     act_content=act_content["Content Rating"].value_counts()
     act_content=act_content.rename("Count")
     st.write(act_content)
     st.header("Top Games Based on Rating")
     act = play[play["Genres"]=="Action"]
     act = act[act["Rating"]==4.7]
     act.reset_index(drop=True, inplace=True)
     act.drop_duplicates(subset="App", inplace = True)
     st.table(act)

#Arcade Genre
     st.title("🎰Arcade Genre")
     st.subheader("Total number of Games")
     st.write(220)
     st.header("Content Rating count")
     act_content = play[play["Category"]=="GAME"]
     act_content = act_content[act_content["Genres"]=="Arcade"]
     act_content=act_content["Content Rating"].value_counts()
     act_content=act_content.rename("Count")
     st.write(act_content)
     st.header("Top Games Based on Rating")
     a = play[play["Genres"]=="Arcade"]
     a =a[a["Rating"]==4.7]
     a.reset_index(drop=True, inplace=True)
     a.drop_duplicates(subset="App", inplace = True)
     st.table(a)

#Racing Genre
     st.title("🚗Racing Genre")
     st.subheader("Total number of Games")
     st.write(98)
     st.header("Content Rating count")
     act_content = play[play["Category"]=="GAME"]
     act_content = act_content[act_content["Genres"]=="Racing"]
     act_content=act_content["Content Rating"].value_counts()
     act_content=act_content.rename("Count")
     st.write(act_content)
     st.header("Top Games Based on Rating")
     a = play[play["Genres"]=="Racing"]
     a = a[a["Rating"]==4.6]
     a.reset_index(drop=True, inplace=True)
     a.drop_duplicates(subset="App", inplace = True)
     st.table(a)

#Adventure Genre
     st.title("🧗Adventure Genre")
     st.subheader("Total number of Games")
     st.write(75)
     st.header("Content Rating count")
     act_content = play[play["Category"]=="GAME"]
     act_content = act_content[act_content["Genres"]=="Adventure"]
     act_content=play["Content Rating"].value_counts()
     act_content=act_content.rename("Count")
     st.write(act_content)
     st.header("Top Games Based on Rating")
     a = play[play["Genres"]=="Adventure"]
     a = a[a["Rating"]==4.6]
     a.reset_index(drop=True, inplace=True)
     a.drop_duplicates(subset="App", inplace = True)
     st.table(a)
     

if dashboard_options == option_2:
     st.title(option_2)
     st.header("⭐️**Spotlight**")
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

     @st.cache
     def load_dataset(data_link):
          dataset = pd.read_csv(data_link)
          return dataset

#Initialized Data
     data_link = "vgsales.csv"
     data = load_dataset(data_link)
     data=data.drop(columns=["JP_Sales","Other_Sales"])
     my_data=data
     data=data[data["Rank"] <= 50]

#Chart-1
     st.header("📊**Top 10 Games Sales**")
     new=data.set_index("Name")
     new=new[new["Rank"]<=10]
     un_1=["Publisher","Platform","Year","Rank","Genre"]
     for news in new:
         news=new.drop(columns=un_1)

     st.area_chart(news)

#chart-2
     st.header("📊**Genre Based in Years**")
     new=data.set_index("Year")
     un_1=["Publisher","Platform","Global_Sales","Rank","Name","NA_Sales","EU_Sales"]
     for news in new:
          news=new.drop(columns=un_1)

     st.bar_chart(news)

#Chart-3
     st.header("📊**Year based Games Sales**")
     new=my_data.set_index("Year")
     un_1=["Publisher","Platform","Rank","Genre","Name","NA_Sales","EU_Sales"]
     for news in new:
         news=new.drop(columns=un_1)

     st.line_chart(news)

#Table
     top=data[data["Rank"]<=25]
     st.header("**♛Top 25 Ranking Games**")
     st.table(top)

#Insights
     st.header("✨**Some of Insights**")
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
