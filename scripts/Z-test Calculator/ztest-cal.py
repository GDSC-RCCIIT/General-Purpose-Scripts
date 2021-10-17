# Core Pkgs
import streamlit as st
import numpy as np


# -- Z - TEST --

st.title("Z-Test Calculator")
st.write("\n")

opt = st.selectbox("Select the Test Type:", ("One Sample", "Two Sample"))

# -- ONE SAMPLE TEST --
if opt == "One Sample":
    try:
        raw_data = st.text_input("Enter the Data", value=0)
        raw_data = raw_data.strip()
        data = (
            raw_data.replace(" , ", " ")
            .replace(", ", " ")
            .replace(" ,", " ")
            .replace(" ", ",")
            .split(",")
        )
        x = [float(i) for i in data]

    except:
        st.write("Enter Valid Numerical Data!")

    try:
        mu = st.text_input("Enter Population Mean", value=0)
        mu = float(mu)

    except:
        st.write("Enter valid Population Mean!")

    try:
        xbar = np.mean(x)
        sigma = np.std(x, ddof=1)
        n = len(x)

        z_cal = (xbar - mu) / (sigma / np.sqrt(n))

        st.write("Your z - statistic value is: ", np.round(z_cal, 3))

    except:
        st.write(
            "Cannot compute z-statistic value. One or more fields does not contain valid Data."
        )
        st.write("Check for the input field having warnings!")

# -- TWO SAMPLE TEST --
if opt == "Two Sample":
    try:
        raw_data = st.text_input("Enter the Data for First Sample", value=0)
        raw_data = raw_data.strip()
        data = (
            raw_data.replace(" , ", " ")
            .replace(", ", " ")
            .replace(" ,", " ")
            .replace(" ", ",")
            .split(",")
        )
        x1 = [float(i) for i in data]
    except:
        st.write("Enter Valid Numerical Data!")

    try:
        raw_data_2 = st.text_input("Enter the Data for Second Sample", value=0)
        raw_data_2 = raw_data_2.strip()
        data2 = (
            raw_data_2.replace(" , ", " ")
            .replace(", ", " ")
            .replace(" ,", " ")
            .replace(" ", ",")
            .split(",")
        )
        x2 = [float(i) for i in data2]

    except:
        st.write("Enter Valid Numerical Data!")

    try:
        mu_diff = st.text_input("Enter Population Mean Difference", value=0)
        mu_diff = float(mu_diff)

    except:
        st.write("Enter Valid Population Mean!")

    try:
        x1bar = np.mean(x1)
        x2bar = np.mean(x2)
        sigma1 = np.std(x1, ddof=1)
        sigma2 = np.std(x2, ddof=1)

        n1 = len(x1)
        n2 = len(x2)

        se = np.sqrt(((sigma1) ** 2 / n1) + ((sigma2) ** 2 / n2))
        z_cal_2 = ((x1bar - x2bar) - (mu_diff)) / se

        st.write("Your z - statistic value is: ", np.round(z_cal_2, 3))

    except:
        st.write(
            "Cannot compute z-statistic value. One or more fields does not contain valid Data."
        )
        st.write("Check for the input field having warnings!")
