
# from textblob import TextBlob
# import pandas as pd
# import streamlit as st
# import cleantext
# import emoji
# from PIL import Image
# import os

# st.title("Sentiment Web Analyzer")

# # ----------- Image Section -----------
# img_path = "twitter image.jpg"   # apni image ka naam yahan likho

# if os.path.exists(img_path):
#     background_image = Image.open(img_path)
#     st.image(background_image, width="stretch")
# else:
#     st.warning("Image not found. Skipping background.")

# # ----------- Header -----------
# st.header("Now Scale Your Thoughts")

# # ----------- Text Analyzer -----------
# with st.expander("Analyze Your Text"):
#     text = st.text_input("Text here:")

#     if text:
#         blob = TextBlob(text)
#         p = round(blob.sentiment.polarity, 2)
#         st.write('Polarity :', p)

#         if p >= 0.1:
#             st.write(emoji.emojize("Positive Speech :grinning_face_with_big_eyes:"))
#         elif p == 0.0:
#             st.write(emoji.emojize("Neutral Speech :zipper-mouth_face:"))
#         else:
#             st.write(emoji.emojize("Negative Speech :disappointed_face:"))

#         st.write('Subjectivity :', round(blob.sentiment.subjectivity, 2))


# # ----------- Clean Text -----------
# pre = st.text_input('Clean Your Text: ')
# if pre:
#     st.write(
#        cleantext.clean(
#     pre,
#     extra_spaces=True,
#     stopwords=True,
#     lowercase=True,
#     numbers=True,
#     punct=True
# )
#     )

# # ----------- Excel Analyzer -----------
# with st.expander('Analyze Excel files'):
#     st.write("_**Note**_ : Your file must contain the column Name 'Tweets' that contain the text to be analyzed.")
#     upl = st.file_uploader('Upload file')

#     def score(x):
#         blob1 = TextBlob(x)
#         return blob1.sentiment.polarity

#     def analyze(x):
#         if x >= 0.5:
#             return 'Positive'
#         elif x <= -0.5:
#             return 'Negative'
#         else:
#             return 'Neutral'

#     if upl:
#         df = pd.read_excel(upl)

#         df['score'] = df['Tweets'].apply(score)
#         df['analysis'] = df['score'].apply(analyze)

#         st.write(df.head(10))

#         @st.cache_data
#         def convert_df(df):
#             return df.to_csv(index=False).encode('utf-8')

#         csv = convert_df(df)

#         st.download_button(
#             label="Download data as CSV",
#             data=csv,
#             file_name='sentiment.csv',
#             mime='text/csv',
#         )

# # ----------- Footer -----------
# st.write("\n" * 15)
# st.markdown("<hr style='border: 2px solid black;'>", unsafe_allow_html=True)
# st.write("Copy© 2026 Zainab Fatima | Made With ❤️ in Pakistan")


from textblob import TextBlob
import pandas as pd
import streamlit as st
import emoji
from PIL import Image
import os
import re

st.title("Sentiment Web Analyzer")

# ----------- Image Section -----------
img_path = "twitter image.jpg"

if os.path.exists(img_path):
    background_image = Image.open(img_path)
    st.image(background_image, width="stretch")
else:
    st.warning("Image not found. Skipping background.")

# ----------- Header -----------
st.header("Now Scale Your Thoughts")

# ----------- Text Analyzer -----------
with st.expander("Analyze Your Text"):
    text = st.text_input("Text here:")

    if text:
        blob = TextBlob(text)
        p = round(blob.sentiment.polarity, 2)
        st.write('Polarity :', p)

        if p >= 0.1:
            st.write(emoji.emojize("Positive Speech :grinning_face_with_big_eyes:"))
        elif p == 0.0:
            st.write(emoji.emojize("Neutral Speech :zipper-mouth_face:"))
        else:
            st.write(emoji.emojize("Negative Speech :disappointed_face:"))

        st.write('Subjectivity :', round(blob.sentiment.subjectivity, 2))


# ----------- Clean Text (FIXED) -----------
pre = st.text_input('Clean Your Text: ')
if pre:
    cleaned = re.sub(r'[^a-zA-Z\s]', '', pre)   # remove punctuation & numbers
    cleaned = cleaned.lower()                  # lowercase
    st.write(cleaned)


# ----------- Excel Analyzer -----------
with st.expander('Analyze Excel files'):
    st.write("_**Note**_ : Your file must contain the column Name 'Tweets' that contain the text to be analyzed.")
    upl = st.file_uploader('Upload file')

    def score(x):
        blob1 = TextBlob(x)
        return blob1.sentiment.polarity

    def analyze(x):
        if x >= 0.5:
            return 'Positive'
        elif x <= -0.5:
            return 'Negative'
        else:
            return 'Neutral'

    if upl:
        df = pd.read_excel(upl)

        df['score'] = df['Tweets'].apply(score)
        df['analysis'] = df['score'].apply(analyze)

        st.write(df.head(10))

        @st.cache_data
        def convert_df(df):
            return df.to_csv(index=False).encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv',
        )

# ----------- Footer -----------
st.write("\n" * 15)
st.markdown("<hr style='border: 2px solid black;'>", unsafe_allow_html=True)
st.write("Copy© 2026 Zainab Fatima | Made With ❤️ in Pakistan")