import streamlit as st

st.set_page_config(page_title="Capstone Dev",
                   page_icon=":balloon:", layout="wide")
st.header('Capstone Development')
st.write('helloworld')


def main():
    st.sidebar.subheader("Home")
    website_menu = st.sidebar.selectbox("Porject", ("Project 1", "Project 2"))


if __name__ == '__main__':
    main()
