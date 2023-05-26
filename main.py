import streamlit as st
from Bots import runExcelQuery
import pandas as pd

# df = pd.read_csv("./Coursera_merged.csv");
# result_save = df.to_pickle("Coursera_merged." + '.pkl',compression='bz2')


st.title("Demo")
col1, col2 = st.columns(2)
with col1:
    with st.container():
        st.header("Querying Tabular Data")
        st.markdown(
            "Basic excel query tool"
        )
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            dataframe = pd.read_csv(uploaded_file)

            course_name = st.text_input(
                "Enter Query",
                placeholder="Enter Query",
                help="Enter Query",
            )
            if st.button("Run Query"):
              st.write(runExcelQuery(course_name,dataframe))
