import streamlit as st
from googletrans import Translator
from gtts import gTTS
import tempfile
import os
import webbrowser
import urllib.parse

st.title("Language Translation App")

# User input for text to be translated
text_to_translate = st.text_area("Enter text to translate:", "Hello, how are you?")

# Language options
language_options = {
    "English": "en", "Spanish": "es", "French": "fr", "German": "de", "Japanese": "ja",
    "Korean": "ko", "Chinese (Simplified)": "zh-CN", "Urdu": "ur", "Afrikaans": "af", "Albanian": "sq",
    "Amharic": "am", "Arabic": "ar", "Armenian": "hy", "Azerbaijani": "az", "Basque": "eu", "Belarusian": "be",
    "Bengali": "bn", "Bosnian": "bs", "Bulgarian": "bg", "Catalan": "ca", "Cebuano": "ceb", "Chichewa": "ny",
    "Corsican": "co", "Croatian": "hr", "Czech": "cs", "Danish": "da", "Dutch": "nl", "Esperanto": "eo",
    "Estonian": "et", "Filipino": "tl", "Finnish": "fi", "Frisian": "fy", "Galician": "gl", "Georgian": "ka",
    "Greek": "el", "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha", "Hawaiian": "haw", "Hebrew": "iw",
    "Hindi": "hi", "Hmong": "hmn", "Hungarian": "hu", "Icelandic": "is", "Igbo": "ig", "Indonesian": "id",
    "Irish": "ga", "Italian": "it", "Javanese": "jw", "Kannada": "kn", "Kazakh": "kk", "Khmer": "km", "Kinyarwanda": "rw",
    "Kurdish (Kurmanji)": "ku", "Kyrgyz": "ky", "Lao": "lo", "Latin": "la", "Latvian": "lv", "Lithuanian": "lt",
    "Luxembourgish": "lb", "Macedonian": "mk", "Malagasy": "mg", "Malay": "ms", "Malayalam": "ml", "Maltese": "mt",
    "Maori": "mi", "Marathi": "mr", "Mongolian": "mn", "Nepali": "ne", "Norwegian": "no", "Pashto": "ps",
    "Persian": "fa", "Polish": "pl", "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro", "Russian": "ru",
    "Samoan": "sm", "Scots Gaelic": "gd", "Serbian": "sr", "Sesotho": "st", "Shona": "sn", "Sindhi": "sd",
    "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so", "Sundanese": "su", "Swahili": "sw",
    "Swedish": "sv", "Tajik": "tg", "Tamil": "ta", "Telugu": "te", "Thai": "th", "Turkish": "tr", "Turkmen": "tk",
    "Ukrainian": "uk", "Uyghur": "ug", "Uzbek": "uz", "Vietnamese": "vi", "Welsh": "cy", "Xhosa": "xh",
    "Yiddish": "yi", "Yoruba": "yo", "Zulu": "zu",
    # Additional languages
    "Lao": "lo", "Latvian": "lv", "Lithuanian": "lt", "Luxembourgish": "lb", "Macedonian": "mk",
    "Malagasy": "mg", "Malay": "ms", "Malayalam": "ml", "Maltese": "mt", "Maori": "mi", "Marathi": "mr",
    "Mongolian": "mn", "Nepali": "ne", "Norwegian": "no", "Pashto": "ps", "Persian": "fa", "Polish": "pl",
    "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro", "Russian": "ru", "Samoan": "sm", "Scots Gaelic": "gd",
    "Serbian": "sr", "Sesotho": "st", "Shona": "sn", "Sindhi": "sd", "Sinhala": "si", "Slovak": "sk",
    "Slovenian": "sl", "Somali": "so", "Sundanese": "su", "Swahili": "sw", "Swedish": "sv", "Tajik": "tg",
    "Tamil": "ta", "Telugu": "te", "Thai": "th", "Turkish": "tr", "Turkmen": "tk", "Ukrainian": "uk",
    "Uyghur": "ug", "Uzbek": "uz", "Vietnamese": "vi", "Welsh": "cy", "Xhosa": "xh", "Yiddish": "yi",
    "Yoruba": "yo", "Zulu": "zu"
}

# Select translation language
target_language = st.selectbox("Select target language:", list(language_options.keys()))

# Select input language
input_language = st.selectbox("Select input language:", list(language_options.keys()))

# Translator instance
translator = Translator()

# Translate text
target_language_code = language_options[target_language]
input_language_code = language_options[input_language]
translated_text = translator.translate(text_to_translate, src=input_language_code, dest=target_language_code)

# Display translated text
st.subheader("Translated Text:")
st.write(translated_text.text)

# Reverse translation
reverse_translation = st.checkbox("Reverse Translation")
if reverse_translation:
    reversed_text = translator.translate(translated_text.text, dest=input_language_code)
    st.subheader("Reversed Text:")
    st.write(reversed_text.text)

# Language detection for the input text
#detected_language = translator.detect(text_to_translate).lang
#st.subheader("Detected Language:")
#st.write(detected_language)

# Character Count
character_count = len(text_to_translate)
st.subheader("Character Count:")
st.write(character_count)

# Word Count
word_count = len(text_to_translate.split())
st.subheader("Word Count:")
st.write(word_count)

# Text-to-Speech
text_to_speech = st.checkbox("Text-to-Speech")
if text_to_speech:
    with tempfile.NamedTemporaryFile(delete=False) as temp_wav:
        tts = gTTS(translated_text.text, lang=target_language_code)
        tts.save(temp_wav.name)
        st.audio(temp_wav.name, format='audio/wav', start_time=0)

# Save Translations to a File
save_translation_to_file = st.button("Save Translation to File")
if save_translation_to_file:
    file_name = 'translated_text.txt'
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(translated_text.text)
    st.success(f"Translation saved to {file_name}!")
    

# Share Translated Text
share_text = st.button("Share Translated Text")
if share_text:
    # Share on WhatsApp
    whatsapp_url = f'https://wa.me/?text={urllib.parse.quote(translated_text.text)}'
    st.write(f"Share on [WhatsApp]({whatsapp_url})")

    # Share on Facebook
    facebook_url = f'https://www.facebook.com/sharer/sharer.php?u={urllib.parse.quote(translated_text.text)}'
    st.write(f"Share on [Facebook]({facebook_url})")

    # Share on Messenger
    messenger_url = f'https://www.facebook.com/dialog/send?link={urllib.parse.quote(translated_text.text)}'
    st.write(f"Share on [Messenger]({messenger_url})")

# Copy Translated Text to Clipboard
copy_to_clipboard = st.button("Copy to Clipboard")
if copy_to_clipboard:
    st.text(translated_text.text)
    st.success("Translated text copied to clipboard!")
    


