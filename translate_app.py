import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

        filter_condition = st.sidebar.text_input('Filter rows (e.g., age > 30)')
        if filter_condition:
            data = data.query(filter_condition)
            st.write(data)

        column_operation = st.sidebar.text_input('Column operation (e.g., age * 2)')
        if column_operation:
            column, operation = column_operation.split()
            data[column] = data[column].apply(lambda x: eval(operation))
            st.write(data)

        column_to_visualize = st.selectbox('Choose a column to visualize', data.columns)
        plt.hist(data[column_to_visualize])
        st.pyplot()

        transformation = st.text_input('Data transformation (e.g., age = age * 2)')
        if transformation:
            column, operation = transformation.split(' = ')
            data[column] = data[column].apply(lambda x: eval(operation))
            st.write(data)

        if st.button('Download Data as CSV'):
            csv = data.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="transformed_data.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
