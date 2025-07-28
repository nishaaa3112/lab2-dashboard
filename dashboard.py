# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'Department': ['CSE', 'ECE', 'MECH', 'CIVIL'],
    'Placements': [150, 120, 90, 60],
    'Scores': [82.5, 78.2, 74.0, 70.1]
})

st.title("🎓 Dynamic Student Dashboard")

chart_type = st.selectbox("Select chart to display", ["Bar Chart", "Line Chart", "Pie Chart"])

if chart_type == "Bar Chart":
    st.subheader("Placements by Department")
    fig, ax = plt.subplots()
    ax.bar(data['Department'], data['Placements'], color='skyblue')
    st.pyplot(fig)

elif chart_type == "Line Chart":
    st.subheader("Average Scores by Department")
    fig, ax = plt.subplots()
    ax.plot(data['Department'], data['Scores'], marker='o', color='green')
    st.pyplot(fig)

elif chart_type == "Pie Chart":
    st.subheader("Department-wise Placements")
    fig, ax = plt.subplots()
    ax.pie(data['Placements'], labels=data['Department'], autopct='%1.1f%%', startangle=90)
    st.pyplot(fig)

st.subheader("📋 Raw Data")
st.dataframe(data)
