import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def welcome_page():
    # Customize page background and text colors
    page_bg_img = '''
    <style>
    body {
        background-color: black;
        color: white;
    }
    h1, h2, h3 {
        color: red;
    }
    p {
        color: black;
    }
    .st-b2 {
        color: black;
    }
    .css-1cpxqw2 a, .css-1cpxqw2, .css-1d391kg {
        color: black !important;
    }
    .st-cp {
        color: black !important;
    }
    .css-qrbaxs, .css-qrbaxs * {
        color: black !important;
    }
    .stButton button {
        background-color: red;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Display an image on the welcome page
    st.image('/mnt/c/Users/Usuario/Downloads/smart meter.jpg', use_column_width=True)

    # Display the content
    st.markdown('<h1>Project Overview: Consumption Prediction</h1>', unsafe_allow_html=True)

    st.markdown('<h2>Objective</h2>', unsafe_allow_html=True)
    st.markdown('<p>The "Consumption Prediction" project is focused on accurately forecasting household energy consumption to optimize energy usage and reduce associated costs. Utilizing advanced machine learning techniques, the project aims to predict total energy consumption by analyzing various factors such as weather conditions, demographic data, and appliance usage.</p>', unsafe_allow_html=True)

    st.markdown('<h2>Dataset: IDEAL Household Energy</h2>', unsafe_allow_html=True)
    st.markdown('<p>The dataset for this project was collected from 255 homes in the UK over a two-year period. It provides comprehensive details on energy usage, environmental conditions, and demographic factors.</p>', unsafe_allow_html=True)

    st.markdown('<h2>Comprehensive Data Capture</h2>', unsafe_allow_html=True)
    st.markdown('<p>The dataset includes the following variables:</p>', unsafe_allow_html=True)
    st.markdown('<ul><li><strong>Electricity and Gas Consumption</strong>: Detailed records of energy usage.</li><li><strong>Environmental Factors</strong>: Temperature and humidity data.</li><li><strong>Demographic Data</strong>: Household size, income levels, and energy awareness.</li><li><strong>Appliance Usage</strong>: Information on the usage patterns of different household appliances.</li></ul>', unsafe_allow_html=True)

    st.markdown('<h2>Longitudinal Approach</h2>', unsafe_allow_html=True)
    st.markdown('<p>Data collection spanned from August 2016 to June 2018, offering a multi-year, seasonal snapshot of household energy consumption patterns.</p>', unsafe_allow_html=True)

    st.markdown('<h2>Data Preprocessing and Model Development</h2>', unsafe_allow_html=True)
    st.markdown('<p>The initial dataset was 200GB in size but was efficiently reduced to 100KB through preprocessing. The objective is to leverage this refined dataset to develop a robust machine learning model capable of predicting household energy consumption in kilowatts based on the input variables.</p>', unsafe_allow_html=True)

    st.markdown('<h2>Project Goals</h2>', unsafe_allow_html=True)
    st.markdown('<ul><li><strong>Accurate Predictions</strong>: Develop a reliable model to forecast energy consumption.</li><li><strong>Cost Optimization</strong>: Enable households to reduce energy costs through better consumption predictions.</li><li><strong>Energy Efficiency</strong>: Support initiatives aimed at optimizing energy usage and enhancing overall efficiency.</li></ul>', unsafe_allow_html=True)

    st.markdown('<p>This project will provide valuable insights and tools for energy management, benefiting both consumers and energy providers.</p>', unsafe_allow_html=True)

def prediction_page():
    st.markdown('<h1>House Consumption Predictor</h1>', unsafe_allow_html=True)

    # For demonstration purposes, we'll create a mock dataframe similar to the original data structure
    data = {
        'location_name_Edinburgh': [1],
        'location_name_Glasgow': [0],
        'location_name_London': [0],
        'hometype_house_or_bungalow': [1],
        'hometype_flat': [0]
    }
    df = pd.DataFrame(data)

    # Sidebar inputs
    st.sidebar.header('User Inputs')
    num_people = st.sidebar.number_input('Number of People', min_value=1, value=1)
    num_rooms = st.sidebar.number_input('Number of Rooms', min_value=1, value=1)
    location = st.sidebar.text_input('Location')
    working_status = st.sidebar.selectbox('Working Status', ['Onsite', 'Work from Home'])
    hometype = st.sidebar.selectbox('Type of House', ['Flat', 'House'])
    start_date = st.sidebar.date_input('Start Date')
    num_days = st.sidebar.number_input('Number of Days', min_value=1, value=7)

    # Convert working status to binary
    working_status_code = 1 if working_status == 'Work from Home' else 0

    # Prepare features for prediction
    features = {
        'residents': num_people,
        'room_count': num_rooms,
        'workingstatus': working_status_code
    }

    # Add location features
    location_columns = [col for col in df.columns if col.startswith('location_name')]
    for col in location_columns:
        features[col] = 1 if col == f'location_name_{location}' else 0

    # Add hometype feature
    hometype_code = 1 if hometype == 'House' else 0
    features['hometype_house_or_bungalow'] = hometype_code

    # Display the "Predict" button
    if st.sidebar.button('Predict'):
        # Generate daily predictions
        date_range = pd.date_range(start=start_date, periods=num_days)
        daily_predictions = []
        for date in date_range:
            # Mock temperature data for each day (this would normally come from a weather API)
            temp_mean = np.random.uniform(-5, 20)
            features['temp_mean'] = temp_mean

            # Mock prediction value
            prediction = 20 + num_people * 2 + num_rooms * 3 + working_status_code * 5 + temp_mean * 1.5
            daily_predictions.append((date, prediction))

        # Create a dataframe for daily predictions
        predictions_df = pd.DataFrame(daily_predictions, columns=['Date', 'Predicted Consumption (kWh)'])

        # Plot the predictions with gradient colors
        st.markdown('<h2>Predicted Consumption Over Time</h2>', unsafe_allow_html=True)

        chart_data = predictions_df.set_index('Date').reset_index()
        bar_chart = alt.Chart(chart_data).mark_bar().encode(
            x='Date:T',
            y='Predicted Consumption (kWh):Q',
            color=alt.Color('Predicted Consumption (kWh):Q', scale=alt.Scale(scheme='viridis'))
        ).properties(
            width=700,
            height=400
        )
        st.altair_chart(bar_chart, use_container_width=True)

if __name__ == '__main__':
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Welcome", "Prediction"])
    if page == "Welcome":
        welcome_page()
    else:
        prediction_page()
