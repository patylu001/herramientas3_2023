# This is a sample Python script.

import plotly.express as px
import pandas as pd
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st


df = px.data.gapminder()
st.dataframe(df)
listaPaises = df["country"].unique().tolist()
#st.write(listaPaises)
#
pais = "Canada"
with st.sidebar:
    pais = st.selectbox("Paises", listaPaises)
    st.write(pais)

datosPais = df.query("country == '" + pais + "'")
fig = px.bar(datosPais, x='year', y='pop')
st.plotly_chart(fig, use_container_width=True)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    st.header("Hola desde Streamlit!")
    st.subheader("Probando..1..2..3")
    st.write("Hola, soy Paty!")
    st.write("Hola, soy Paty!")
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Hi Paty!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
