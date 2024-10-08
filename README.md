# Bike Sharing Analysis Dashboard ✨

This project features an interactive dashboard built with **Streamlit** for analyzing bike-sharing data. The dashboard enables users to explore bike usage patterns categorized by weekdays, holidays versus working days, registered versus casual users, and different usage levels.

## Features

- **Weekday Analysis**: Examine bike usage trends based on different days of the week.
- **Holiday and Working Day Analysis**: Compare bike usage during holidays against regular working days.
- **Registered vs Casual User Analysis**: Analyze the behavior of registered users compared to casual users based on holiday and working day conditions.
- **Usage Category Analysis**: Classify bike usage into categories (low, medium, high) for better insights.

## Setup Environment - Anaconda
```
To set up the environment using Anaconda, run the following commands:
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```
