import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from pathlib import Path
# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='🍿Blockbuster Bytes',
    page_icon=':movie_camera:', # Movie camera emoji
)


st.title("🌍 Blockbuster Bytes: What the World Watches & Pays For 🎥")
st.markdown("### Trends in International TV shows and movies with interactive visuals! 📊") 
st.markdown("")
st.markdown("📺 Ever wondered what global audiences love to watch? Our interactive visuals reveal the trends behind international TV shows and movies—what’s popular and what’s profitable.")
st.markdown("This allows streaming platforms to decide what media to bring onto their platforms that will generate the most profit from its users.")
#what people like to watch what people pay to watch

#tabs for categories
tab1, tab2, = st.tabs(["🎞️ Movies", "📺 TV Shows"])

# Movies tab
with tab1:
    st.header("Movie Data") 
    st.write("")
    st.markdown("""
    Our selected movie data source, **Box Office Mojo**, provides key headers that offer structured insights into international weekend box office earnings for the year 2025, including:

    - **Area**: Represents the country or region where the movie was released.  
    - **Weekend**: Specifies the dates during which earnings were recorded, typically spanning **Friday to Sunday**.  
    - **Releases**: Indicates the total number of movies released in a given market over the specified weekend.  
    - **#1 Release**: Shows the top-performing movie in each region for that weekend.  
    - **Distributor**: Lists the company responsible for distributing the movie in that market.  
    - **Weekend Gross**: Represents the total box office revenue earned in that country or region during the weekend.  
    """)
    st.write("")
    
    genre = st.selectbox("What would you like to learn about:", ["Top Distributors", "Total Weekend Gross By Area", "Most Successful Number #1 Releases", "Weekend Gross Over Time"], key="movie_genre")
    
    if genre == "Top Distributors":
        st.write("")
        st.subheader("🌍 International Top Distributors 🍰")
        st.write("This pie chart shows the market share of major international movie distributors and highlights the dominance of a few key players.")
        st.write("")
        st.write("📌 We levered web-scraped data from Box Office Mojo - a widely recognized source for tracking global movie earnings.")
        st.write("")
        # Correct way to display a local image
        st.image(r"C:\Users\Arohi Shiraskar\Documents\axeHacks25\Screenshot 2025-03-15 151431.png", width=700)
        
        st.write("")
        st.write("📌 Use this button below to interact with the dashboard in the top lefthand corner.")
        st.link_button("📎 Check out the Dashboard", "https://public.tableau.com/views/movies_17420642663690/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link")

    
    elif genre == "Total Weekend Gross By Area":
        st.write("")
        st.subheader("🌎 Weekend Gross Measure by Area 💰")
        st.write("This chart visualizes the total weekend box office revenue by country, with larger blocks representing higher earnings in regions like South Korea, Japan, and the UK.")
        st.write("")
        st.write("📌 We levered web-scraped data from Box Office Mojo - a widely recognized source for tracking global movie earnings.")
        st.write("")
        # Correct way to display a local image
        st.image(r"C:\Users\Arohi Shiraskar\Documents\axeHacks25\Screenshot 2025-03-15 150306.png", width=700)
        
        st.write("")
        st.write("📌 Use this button below to interact with the dashboard in the top righthand corner.")
        st.link_button("📎 Check out the Dashboard", "https://public.tableau.com/views/movies_17420642663690/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link")

    elif genre == "Most Successful Number #1 Releases":
        st.write("")
        st.subheader("🏆 International #1 Releases 🎥")
        st.write("This displays the weekend gross revenue of the most successful #1 movies, with 'Mickey 7' significantly outperforming others.")
        st.write("")
        st.write("📌 We levered web-scraped data from Box Office Mojo - a widely recognized source for tracking global movie earnings.")
        st.write("")
        # Correct way to display a local image
        st.image(r"C:\Users\Arohi Shiraskar\Documents\axeHacks25\Screenshot 2025-03-15 150840.png", width=700)
        
        st.write("")
        st.write("📌 Use this button below to interact with the dashboard in the bottom lefthand corner.")
        st.link_button("📎 Check out the Dashboard", "https://public.tableau.com/views/movies_17420642663690/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link")

    elif genre == "Weekend Gross Over Time":
        st.write("")
        st.subheader("📊 Weekend Gross Over Time ⏳")
        st.write("This chart tracks weekend box office revenue over time, showing fluctuations and peaks that coincide with an increased number of movie releases.")
        st.write("")
        st.write("📌 We levered web-scraped data from Box Office Mojo - a widely recognized source for tracking global movie earnings.")
        st.write("")
        # Correct way to display a local image
        st.image(r"C:\Users\Arohi Shiraskar\Documents\axeHacks25\Screenshot 2025-03-15 150954.png", width=700)
        
        st.write("")
        st.write("📌 Use this button below to interact with the dashboard in the bottom righthand corner.")
        st.link_button("📎 Check out the Dashboard", "https://public.tableau.com/views/movies_17420642663690/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link")




# TV Shows tab
with tab2:
    st.header("TV Shows")
    st.write("")
    st.markdown("""
    Our data source was a **web-connected Tableau source** that provides insights about TV shows dating back to **1947**.

    - **Origin country**: The country where the TV show originated.  
    - **Year**: The year the TV show was released.  
    - **Sum(Vote Count)**: The total number of votes for the show.   
    """)

    st.write("")
    options = st.selectbox(
        "What information are you interested in?",
        ["International Map: Earliest Years of TV Shows", "USA Popularity Pie Chart", "International Popularity and Vote Average", "International Shows First Air Date"],
        key="tv_map",
    )

    # Show Tableau visualization only when "World Map" is selected
    if options == "International Map: Earliest Years of TV Shows":
        st.write("")
        st.subheader("🗺️ Geospatial Map :earth_americas:")
        st.write("The map identifies the country of origin and highlights the earliest year of films that can be purchased. For example, the latest of films a streaming platform can purchase. ")
        st.write("")
        st.write("📌 We levered a webconnector Tableau Desktop - where we found a TV show database that was integrated to create our dashboard.")
        st.write("")
        # Correct way to display a local image
        st.image(r"C:\Users\Arohi Shiraskar\Documents\axeHacks25\Screenshot 2025-03-15 at 2.19.32 PM.png", width=700)
        
        st.write("")
        st.write("📌 Use this button below to interact with the dashboard in the bottom righthand corner.")
        st.link_button("📎 Check out the Dashboard", "https://public.tableau.com/views/Book2_17420545845690/TVshows?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link")


    #Code for Pie Chart
    elif options == "USA Popularity Pie Chart":
        st.write("")
        st.subheader("🏆 Comparing Popularity by Ratings 🎖️")
        st.write("")
        st.markdown("""   
        ### 📊 **Pie Chart:**
        - **Origin country**: Filtered for the **U.S.**, displaying shows in the **United States**.  
        - **Original name (show)**: The name of the TV show.  
        """)
                    
        st.write("The pie chart gives a brief analysis of popular TV shows in the USA and their popularity vote scaled in hundreds.")
        st.write("")
        st.write("📌 We levered a webconnector Tableau Desktop - where we found a TV show database that was integrated to create our dashboard.")
        st.write("")
        # Correct way to display a local image
        st.image(r"C:\Users\Arohi Shiraskar\Documents\axeHacks25\pie chart .png", width=700)
        
        st.write("")
        st.write("📌 Use this button below to interact with the dashboard in the top lefthand corner.")
        st.link_button("📎 Check out the Dashboard", "https://public.tableau.com/views/Book2_17420545845690/TVshows?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link")

    #Code for Scatterplot
    elif options == "International Popularity and Vote Average":
        st.write("")
        st.subheader("🌟 Comparing International Popularity by Ratings 🔢")
        st.write("")
        st.markdown("""
        ### 🔢 **Scatter Plot:**
        - **Name**: The name of the TV show.  
        - **Sum(Popularity)**: The total popularity score of the show.  
        - **Sum(Vote Average)**: The average vote rating of the show.  
        """)
        st.write("This scatter plot measures TV show vote averages vs. their popularity for shows internationally.")
        st.write("")
        st.write("📌 We levered a webconnector Tableau Desktop - where we found a TV show database that was integrated to create our dashboard.")
        st.write("")
        # Correct way to display a local image
        st.image(r"C:\Users\Arohi Shiraskar\Documents\axeHacks25\Screenshot 2025-03-15 at 2.19.06 PM.png", width=700)
        
        st.write("")
        st.write("📌 Use this button below to interact with the dashboard in the bottom lefthand corner.")
        st.link_button("📎 Check out the Dashboard", "https://public.tableau.com/views/Book2_17420545845690/TVshows?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link")


    #Barchart code
    elif options == "International Shows First Air Date":
        st.write("")
        st.subheader("📡 Comparing International Air Dates 📆")
        st.write("This stacked bar chart represents TV shows and is organized by their release year and popularity vote.")
        st.write("")
        st.write("📌 We levered a webconnector Tableau Desktop - where we found a TV show database that was integrated to create our dashboard.")
        st.write("")
        # Correct way to display a local image
        st.image(r"C:\Users\Arohi Shiraskar\Documents\axeHacks25\Screenshot 2025-03-15 at 2.18.20 PM.png", width=700)
        
        st.write("")
        st.write("📌 Use this button below to interact with the dashboard in the bottom righthand corner.")
        st.link_button("📎 Check out the Dashboard", "https://public.tableau.com/views/Book2_17420545845690/TVshows?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link")


