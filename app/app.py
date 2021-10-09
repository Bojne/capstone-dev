from datetime import time
import pafy
import librosa.display
import matplotlib.pyplot as plt
import librosa
import streamlit as st

st.set_page_config(page_title="Capstone Dev",
                   page_icon=":balloon:", layout="wide")
st.header('Capstone Working Demo')


def display_audio(audio_data, col=None, sr=44000):
    x = librosa.load(audio_data, sr=None)
    fig = plt.figure(figsize=(14, 5))
    plt.title('Spectrogram')
    librosa.display.waveplot(x[0], sr=sr)
    if col is not None:
        return col.pyplot(fig)
    else:
        return st.pyplot(fig)


def plot_spectrogram(sr=44000
                     ):
    return None


def main():
    st.sidebar.subheader("Home")
    website_menu = st.sidebar.selectbox(
        "Porject", ("Audio Analyzer", "About"))
    user_audio = st.sidebar.file_uploader("Upload a .wav file of your speech")
    model_audio = st.sidebar.file_uploader(
        "Upload a .wav file of model speech")
    col1, col2 = st.columns(2)
    col1.subheader("Audio 1")
    col2.subheader("Audio 2")
    if user_audio:
        display_audio(user_audio, col1)
    if model_audio:
        display_audio(model_audio, col2)


if __name__ == '__main__':
    main()


# path of the audio file
audio_data = '../audios/model.wav'


# list all audio format
#audiostreams = video.audiostreams
# audiostreams = [(a.bitrate, a.extension, a.get_filesize())
#                for a in audiostreams]
# st.write(audiostreams)
# st.subheader("Option 2. Directly upload audio sample")
# if uploaded_file is not None:
#     audio_data = uploaded_file
# # This returns an audio time series as a numpy array with a default sampling rate(sr) of 22KHZ
# st.audio(audio_data, format='audio/wav')

# st.subheader("Upload your own recording of the sample")
# # The User Uploaded files
# audio_user = "../audios/user.wav"
# if uploaded_file2 is not None:
# audio_user = uploaded_file2
# This returns an audio time series as a numpy array with a default sampling rate(sr) of 22KHZ
# st.audio(audio_user, format='audio/wav')


# st.header("Sample Audio Result")
# # Get the audio display

# # plotting the sampled signal

# # x: numpy array
# X = librosa.stft(x[0])
# # converting into energy levels(dB)
# Xdb = librosa.amplitude_to_db(abs(X))

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
