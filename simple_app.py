# simple_app.py
import streamlit as st
import numpy as np
import cv2
import av

from streamlit_webrtc import webrtc_streamer, VideoTransformerBase

st.title("✅ Simple Streamlit App Test")
st.write("If you're seeing this, installation worked!")

# Optional: include webcam preview for sanity check
class EchoTransformer(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(key="test", video_transformer_factory=EchoTransformer)
