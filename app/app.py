from datetime import time
import pafy
import librosa.display
import matplotlib.pyplot as plt
import librosa
import streamlit as st

# import ffmpeg
# stream = ffmpeg.input('Rhye - Full Performance (Live on KEXP).webm')
# stream = ffmpeg.output(stream, 'Rhye.wav')
# ffmpeg.run(stream)
# https://pythonhosted.org/pafy/#pafy-methods
# https://github.com/mps-youtube/pafy

st.header('CP192 Final Project Demo')
st.subheader('April 2021 by Yueh Han Huang')

# st.image('./ocean.jpeg')

# path of the audio file
audio_data = './diane-official-music-video.wav'

sr = 44000

st.subheader("Option 1. Get Audio From Youtube link")
input_url = st.text_input('Enter some youtube url')

if len(input_url) >= 10:
    st.text('Got your URL! 🥁 Processing...')
    video_url = input_url
else:
    video_url = "https://www.youtube.com/watch?v=pHaoobWUF1w"

# get the video with pafy library
video = pafy.new(video_url)

v_time = video.duration
st.text(f"The duration is {v_time}")

# disply the video
st.video(video_url)

# get the audio from youtube
audio_file = video.getbestaudio()
audio_file.download()
audio_path = f"./{video.title}.{audio_file.extension}"
st.text("The audio is download at path:" + audio_path)
st.subheader('Listen to downloaded audio')
st.audio(audio_path, format='audio/webm')

# list all audio format
#audiostreams = video.audiostreams
# audiostreams = [(a.bitrate, a.extension, a.get_filesize())
#                for a in audiostreams]
# st.write(audiostreams)
st.subheader("Option 2. Directly upload audio sample")
uploaded_file = st.file_uploader("You can also upload a .wav file")
if uploaded_file is not None:
    audio_data = uploaded_file
# This returns an audio time series as a numpy array with a default sampling rate(sr) of 22KHZ
st.audio(audio_data, format='audio/wav')

st.subheader("Upload your own recording of the sample")
# The User Uploaded files
audio_user = "./voitcetube.wav"
uploaded_file2 = st.file_uploader("Upload your speech in .wav file")
if uploaded_file2 is not None:
    audio_user = uploaded_file2
# This returns an audio time series as a numpy array with a default sampling rate(sr) of 22KHZ
st.audio(audio_user, format='audio/wav')

st.header("Sample Audio Result")
# Get the audio display
x = librosa.load(audio_data, sr=None)

fig = plt.figure(figsize=(14, 5))
# plotting the sampled signal
librosa.display.waveplot(x[0], sr=sr)
st.pyplot(fig)

# x: numpy array
X = librosa.stft(x[0])
# converting into energy levels(dB)
Xdb = librosa.amplitude_to_db(abs(X))

fig2 = plt.figure(figsize=(20, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()
st.subheader("Spectrogram with normal axis")
st.pyplot(fig2)

fig3 = plt.figure(figsize=(20, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()
st.subheader("Spectrogram with log-scale axis")
st.pyplot(fig3)

chromagram = librosa.feature.chroma_stft(x[0], sr=sr)
fig4 = plt.figure(figsize=(15, 5))

librosa.display.specshow(chromagram, x_axis='time',
                         y_axis='chroma', cmap='coolwarm')
st.subheader("Chromagram")
st.pyplot(fig4)

st.header("User Recording Result")

# Get the audio display
y = librosa.load(audio_user, sr=sr)
fig = plt.figure(figsize=(14, 5))
# plotting the sampled signal
librosa.display.waveplot(y[0], sr=sr)
st.pyplot(fig)

# x: numpy array
Y = librosa.stft(y[0])
# converting into energy levels(dB)
Xdb = librosa.amplitude_to_db(abs(Y))

fig2 = plt.figure(figsize=(20, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()
st.subheader("Spectrogram with normal axis")
st.pyplot(fig2)

fig3 = plt.figure(figsize=(20, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()
st.subheader("Spectrogram with log-scale axis")
st.pyplot(fig3)

chromagram = librosa.feature.chroma_stft(y[0], sr=sr)
fig4 = plt.figure(figsize=(15, 5))

librosa.display.specshow(chromagram, x_axis='time',
                         y_axis='chroma', cmap='coolwarm')
st.subheader("Chromagram")
st.pyplot(fig4)
