import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

def create_weekday_analysis(df):
    # Analisis penggunaan berdasarkan hari dalam seminggu
    weekday_analysis = df.groupby(by="weekday").agg(
        total_usage=("cnt", "sum"),  
        unique_usage_count=("cnt", "nunique")  
    ).reset_index()
    
    return weekday_analysis

def create_holiday_workingday_analysis(df):
    # Analisis penggunaan berdasarkan libur dan hari kerja
    holiday_workingday_analysis = df.groupby(by=["holiday", "workingday"]).agg(
        total_usage=("cnt", "sum"),  
        unique_usage_count=("cnt", "nunique")  
    ).reset_index()
    
    return holiday_workingday_analysis

def create_registered_casual_analysis(df):
    # Analisis pengguna terdaftar dan kasual berdasarkan libur dan hari kerja
    registered_casual_analysis = df.groupby(by=["holiday", "workingday"]).agg(
        total_registered_usage=("registered", "sum"),  
        total_casual_usage=("casual", "sum")
    ).reset_index()
    
    return registered_casual_analysis

def usage_binned_analysis(df):
    # Analisis kategori penggunaan (rendah, menengah, tinggi)
    bins = [0, 2000, 4000, np.inf]  
    labels = ['Low usage', 'Medium usage', 'High usage']  
    
    df['usage_category'] = pd.cut(df['cnt'], bins=bins, labels=labels, right=False)
    
    binned_df = df.groupby(by='usage_category').cnt.nunique().reset_index()
    
    binned_df.rename(columns={'cnt': 'unique_usage_count'}, inplace=True)
    binned_df['usage_category'] = pd.Categorical(binned_df['usage_category'], categories=labels, ordered=True)
    
    return binned_df

# Load data
day_df = pd.read_csv("D:/dashboard/day_df.csv")

# Convert datetime columns
datetime_columns = ["dteday"]
day_df.sort_values(by="dteday", inplace=True)
day_df.reset_index(inplace=True, drop=True)

for column in datetime_columns:
    day_df[column] = pd.to_datetime(day_df[column])

# Get the min and max dates
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

# Sidebar with date input and image
with st.sidebar:
    st.image("image.png", width=300)  # Increase image width
    start_date, end_date = st.date_input(
        label='Rentang Waktu', 
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Convert start_date and end_date to datetime
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter main DataFrame based on selected date range
main_df = day_df[(day_df["dteday"] >= start_date) & (day_df["dteday"] <= end_date)]

# Generate analysis
weekday_analysis = create_weekday_analysis(main_df)
holiday_workingday_analysis = create_holiday_workingday_analysis(main_df)
registered_casual_analysis = create_registered_casual_analysis(main_df)
binned_df = usage_binned_analysis(main_df)

# Streamlit headers and outputs
st.markdown("### Bike Sharing Analysis :sparkles:")

# Main content image
st.image("image.png", width=400)  # Increased width for main content

# Weekday Analysis
st.subheader('Weekday Analysis')
st.write(weekday_analysis)

# Visualization for Weekday Analysis
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=weekday_analysis, x='weekday', y='total_usage', ax=ax, palette='Blues_d')
ax.set_title("Total Bike Usage by Weekday", fontsize=16)
ax.set_xlabel("Weekday", fontsize=12)
ax.set_ylabel("Total Usage", fontsize=12)
st.pyplot(fig)

# Holiday and Working Day Analysis
st.subheader('Holiday and Working Day Analysis')
st.write(holiday_workingday_analysis)

# Visualization for Holiday and Working Day Analysis
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=holiday_workingday_analysis, x='holiday', y='total_usage', hue='workingday', ax=ax, palette='Paired')
ax.set_title("Total Usage by Holiday and Working Day", fontsize=16)
ax.set_xlabel("Holiday", fontsize=12)
ax.set_ylabel("Total Usage", fontsize=12)
st.pyplot(fig)

# Registered and Casual User Analysis
st.subheader('Registered and Casual User Analysis')
st.write(registered_casual_analysis)

# Visualization for Registered and Casual User Analysis
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=registered_casual_analysis, x='holiday', y='total_registered_usage', hue='workingday', ax=ax, palette='husl')
ax.set_title("Registered User Usage by Holiday and Working Day", fontsize=16)
ax.set_xlabel("Holiday", fontsize=12)
ax.set_ylabel("Total Registered Usage", fontsize=12)
st.pyplot(fig)

# Casual User Analysis
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=registered_casual_analysis, x='holiday', y='total_casual_usage', hue='workingday', ax=ax, palette='husl')
ax.set_title("Casual User Usage by Holiday and Working Day", fontsize=16)
ax.set_xlabel("Holiday", fontsize=12)
ax.set_ylabel("Total Casual Usage", fontsize=12)
st.pyplot(fig)

# Usage Category Analysis
st.subheader('Usage Category Analysis')
st.write(binned_df)

# Visualization for Usage Category Analysis
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=binned_df, x='unique_usage_count', y='usage_category', ax=ax, palette='pastel')
ax.set_title("Unique Usage Count by Usage Category", fontsize=16)
ax.set_xlabel("Unique Usage Count", fontsize=12)
ax.set_ylabel("Usage Category", fontsize=12)
st.pyplot(fig)
