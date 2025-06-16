import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as pt



#import my csv file
st.title("DIABETES_ANALYSIS")
df = pd.read_csv("diabetes.csv")
st.markdown("# FIRST FIVE")
st.write(df.head())

st.markdown("### blood pressure")
st.write(df["BloodPressure"])
