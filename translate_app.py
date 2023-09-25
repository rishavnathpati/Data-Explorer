import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title('Dataset Explorer')

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)

        if st.button('Show Summary Statistics'):
            st.write(data.describe())

        if st.button('Show Data Types'):
            st.write(data.dtypes)

        # Add more features here...

if __name__ == "__main__":
    main()
