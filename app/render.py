import librosa.display
import matplotlib.pyplot as plt
import librosa
import streamlit as st
import parselmouth


def render_waveplot(x, sr):
    st.write("`Waveplot`")
    fig = plt.figure(figsize=(14, 5))
    librosa.display.waveplot(x, sr=sr)
    st.pyplot(fig)


def render_spectrogram(x, sr):
    st.write("`Spectrogram`")
    stft_x = librosa.stft(x)
    fig = plt.figure(figsize=(14, 5))
    Xdb = librosa.amplitude_to_db(abs(stft_x))
    librosa.display.specshow(Xdb, sr=sr, x_axis="time", y_axis="log")
    plt.colorbar()
    st.pyplot(fig)


def render_chromagram(x, sr):
    st.write("`Chromagram`")
    fig = plt.figure(figsize=(14, 5))
    chromagram = librosa.feature.chroma_stft(x, sr=sr)
    librosa.display.specshow(
        chromagram, x_axis="time", y_axis="chroma", cmap="coolwarm"
    )
    plt.colorbar()
    st.pyplot(fig)


def render_pitch_diagram(x):
    st.write("`Pitch Plot`")
    sound = parselmouth.Sound(x)
    pitch_track = sound.to_pitch().selected_array["frequency"]
    fig = plt.figure(figsize=(14, 5))
    plt.plot([float("nan") if x == 0.0 else x for x in pitch_track], ".")
    st.pyplot(fig)
