from datetime import time
import pafy
import librosa.display
import matplotlib.pyplot as plt
import librosa
import streamlit as st

st.set_page_config(page_title="Capstone Dev",
                   page_icon=":ballon:", layout="wide",
                   menu_items={
                       'About': 'https://yhhuang.notion.site/Capstone-Home-e9a1f458f2a143049100917f8f66272f'
                   })


def render_waveplot(x, sr):
    st.write('`Waveplot`')
    fig = plt.figure(figsize=(14, 5))
    librosa.display.waveplot(x, sr=sr)
    st.pyplot(fig)


def render_spectrogram(x, sr):
    st.write('`Spectrogram`')
    stft_x = librosa.stft(x)
    fig = plt.figure(figsize=(14, 5))
    Xdb = librosa.amplitude_to_db(abs(stft_x))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar()
    st.pyplot(fig)


def render_chromagram(x, sr):
    st.write('`Chromagram`')
    fig = plt.figure(figsize=(14, 5))
    chromagram = librosa.feature.chroma_stft(x, sr=sr)
    librosa.display.specshow(chromagram, x_axis='time',
                             y_axis='chroma', cmap='coolwarm')
    plt.colorbar()
    st.pyplot(fig)


def display_audio(audio_data, col=None, sr=44000):
    st.audio(audio_data)
    x = librosa.load(audio_data, sr=None)[0]
    render_waveplot(x, sr)
    render_chromagram(x, sr)
    render_spectrogram(x, sr)


st.markdown(""" <style>
# MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


def analyzer_view():
    st.header('Capstone Working Demo')

    user_audio = st.sidebar.file_uploader("Upload Audio 1 (wav)")
    model_audio = st.sidebar.file_uploader("Upload Audio 2 (wav)")

    col1, col2 = st.columns(2)
    col1.subheader("Audio 1")
    col2.subheader("Audio 2")

    if not user_audio:
        user_audio = 'app/src/audios/user.wav'
    if not model_audio:
        model_audio = 'app/src/audios/model.wav'

    with col1:
        display_audio(user_audio)

    with col2:
        display_audio(model_audio)


def about_view():
    st.sidebar.image(
        'https://media.giphy.com/media/3o7ZeltXSmmz7Q5LCo/giphy.gif')
    st.markdown(
        """
        ## Welcome to the Yueh Han's Capstone Demo Page!


        ### Sign up for project update / product waitlist 👇
        """
    )
    st.components.v1.iframe(
        src='https://6icg6d7rllb.typeform.com/to/yz5I5P1l',
        height=600)

    st.markdown("""
    ### Visit [Notion Home Page](https://yhhuang.notion.site/Capstone-Home-e9a1f458f2a143049100917f8f66272f)

    By Yueh Han Huang
    
    [yhhuang@uni.minerva.edu](yhhuang@uni.minerva.edu)
    """)


def resources_view():
    st.subheader("Interesting Video About Pronunciation")
    st.video('https://www.youtube.com/embed/2yzMUs3badc')


def main():
    st.sidebar.subheader("Home")
    website_menu = st.sidebar.selectbox(
        "Select Menu", ("Audio Analyzer", "About", "Resources"))
    if website_menu == "Audio Analyzer":
        analyzer_view()

    if website_menu == "About":
        about_view()

    if website_menu == "Resources":
        resources_view()


if __name__ == '__main__':
    main()
