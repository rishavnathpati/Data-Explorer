import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

        plot_type = st.selectbox('Choose a type of plot', ['Histogram', 'Box Plot', 'Pie Chart', 'Scatter Plot', 'Heatmap'])
        if plot_type == 'Histogram':
            column_to_visualize = st.selectbox('Choose a column to visualize', data.select_dtypes(include=[np.number]).columns)
            fig, ax = plt.subplots()
            ax.hist(data[column_to_visualize])
            st.pyplot(fig)
        elif plot_type == 'Box Plot':
            column_to_visualize = st.selectbox('Choose a column to visualize', data.select_dtypes(include=[np.number]).columns)
            fig, ax = plt.subplots()
            ax.boxplot(data[column_to_visualize].dropna())
            st.pyplot(fig)
        elif plot_type == 'Pie Chart':
            column_to_visualize = st.selectbox('Choose a column to visualize', data.select_dtypes(include=['object']).columns)
            fig, ax = plt.subplots()
            data[column_to_visualize].value_counts().plot(kind='pie', ax=ax)
            st.pyplot(fig)
        elif plot_type == 'Scatter Plot':
            columns_to_visualize = st.multiselect('Choose two columns to visualize', data.select_dtypes(include=[np.number]).columns)
            if len(columns_to_visualize) != 2:
                st.warning('Please select exactly two columns for scatter plot.')
            else:
                fig, ax = plt.subplots()
                ax.scatter(data[columns_to_visualize[0]], data[columns_to_visualize[1]])
                st.pyplot(fig)
        elif plot_type == 'Heatmap':
            numeric_data = data.select_dtypes(include=[np.number])
            corr = numeric_data.corr()
            fig, ax = plt.subplots()
            sns.heatmap(corr, annot=True, ax=ax)
            st.pyplot(fig)

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
