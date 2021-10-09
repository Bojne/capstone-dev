from datetime import time
import pafy
import librosa.display
import matplotlib.pyplot as plt
import librosa
import streamlit as st

st.set_page_config(page_title="Capstone Dev",
                   page_icon="🧈", layout="wide",
                   menu_items={
                       'About': 'https://yhhuang.notion.site/Capstone-Home-e9a1f458f2a143049100917f8f66272f'
                   })


def display_audio(audio_data, col=None, sr=44000):
    x = librosa.load(audio_data, sr=None)
    fig = plt.figure(figsize=(14, 5))
    plt.title('Spectrogram')
    librosa.display.waveplot(x[0], sr=sr)
    if col is not None:
        col.pyplot(fig)
    else:
        st.pyplot(fig)


def spectrogram():
    # x: numpy array
    X = librosa.stft(x[0])
    # converting into energy levels(dB)
    Xdb = librosa.amplitude_to_db(abs(X))
    fig2 = plt.figure(figsize=(20, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()
    st.subheader("Spectrogram with normal axis")
    st.pyplot(fig2)


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


def plot_spectrogram(sr=44000
                     ):
    return None


def analyzer_view():
    st.header('Capstone Working Demo')
    user_audio = st.sidebar.file_uploader("Upload Audio 1 (wav)")
    model_audio = st.sidebar.file_uploader("Upload Audio 2 (wav)")

    col1, col2 = st.columns(2)
    col1.subheader("Audio 1")
    col2.subheader("Audio 2")

    if not user_audio:
        user_audio = 'src/audios/user.wav'
    if not model_audio:
        model_audio = 'src/audios/model.wav'

    display_audio(user_audio, col1)
    display_audio(model_audio, col2)


def about_view():
    st.markdown(
        """
        ## Welcome to the capstone!

        ### Visit [Notion Home Page](https://yhhuang.notion.site/Capstone-Home-e9a1f458f2a143049100917f8f66272f)
        
        ### Sign up for project update / product waitlist 👇
        """
    )
    st.components.v1.iframe(
        src='https://6icg6d7rllb.typeform.com/to/yz5I5P1l',
        height=600)


def main():
    st.sidebar.subheader("Home")
    website_menu = st.sidebar.selectbox(
        "Select Menu", ("Audio Analyzer", "About"))
    if website_menu == "Audio Analyzer":
        analyzer_view()

    if website_menu == "About":
        about_view()


if __name__ == '__main__':
    main()


# path of the audio file
audio_data = '../audios/model.wav'


# st.header("Sample Audio Result")
# # Get the audio display

# # plotting the sampled signal


# fig3 = plt.figure(figsize=(20, 5))
# librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
# plt.colorbar()
# st.subheader("Spectrogram with log-scale axis")
# st.pyplot(fig3)

# chromagram = librosa.feature.chroma_stft(x[0], sr=sr)
# fig4 = plt.figure(figsize=(15, 5))

# librosa.display.specshow(chromagram, x_axis='time',
#                          y_axis='chroma', cmap='coolwarm')
# st.subheader("Chromagram")
# st.pyplot(fig4)

# st.header("User Recording Result")

# # Get the audio display
# y = librosa.load(audio_user, sr=sr)
# fig = plt.figure(figsize=(14, 5))
# # plotting the sampled signal
# librosa.display.waveplot(y[0], sr=sr)
# st.pyplot(fig)

# # x: numpy array
# Y = librosa.stft(y[0])
# # converting into energy levels(dB)
# Xdb = librosa.amplitude_to_db(abs(Y))

# fig2 = plt.figure(figsize=(20, 5))
# librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
# plt.colorbar()
# st.subheader("Spectrogram with normal axis")
# st.pyplot(fig2)

# fig3 = plt.figure(figsize=(20, 5))
# librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
# plt.colorbar()
# st.subheader("Spectrogram with log-scale axis")
# st.pyplot(fig3)

# chromagram = librosa.feature.chroma_stft(y[0], sr=sr)
# fig4 = plt.figure(figsize=(15, 5))

# librosa.display.specshow(chromagram, x_axis='time',
#                          y_axis='chroma', cmap='coolwarm')
# st.subheader("Chromagram")
# st.pyplot(fig4)


col1, col2 = st.columns(2)
