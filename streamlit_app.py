import streamlit as st
from textblob import TextBlob
import re

st.title("💅 Article Mood Checker")
st.caption("Paste your content. Prepare to be judged. Gently. Maybe.")

text = st.text_area("Drop your article here, bestie:")

if text:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    word_count = len(text.split())
    vibes = []
    mood_score = 0  # We’ll use this to assign an emoji reaction

    # Mood based on sentiment
    if sentiment > 0.5:
        vibes.append("✨ Radiates positivity — like a brand manager on a good day.")
        mood_score += 2
    elif sentiment > 0:
        vibes.append("🙂 Pleasant, but feels like you're playing it safe.")
        mood_score += 1
    elif sentiment == 0:
        vibes.append("😐 Neutral. Like water. Or toast.")
    else:
        vibes.append("🫠 This feels like a cry for help in paragraph form.")
        mood_score -= 1

    # Keyword sass
    hype_words = ["innovative", "cutting-edge", "synergy", "revolutionary", "leverage"]
    found_hype = [word for word in hype_words if word in text.lower()]
    if found_hype:
        vibes.append(f"📢 Bro chill — you used hype words like {', '.join(found_hype)}. We get it.")
        mood_score -= 1

    # Exclamation point drama
    exclaims = text.count("!")
    if exclaims >= 3:
        vibes.append("😬 Easy on the exclamation marks, champ.")
        mood_score -= 1

    # Word count commentary
    if word_count < 100:
        vibes.append("🫣 This barely counts as an article. Blink and it's gone.")
        mood_score -= 1
    elif word_count > 1000:
        vibes.append("📚 Wow, did you just write a novella? Take a break maybe?")
        mood_score += 1

    # Display results
    st.subheader("💬 Your Article Vibe:")
    for v in vibes:
        st.write(v)

    # 🎭 Final emoji reaction based on mood score
    st.subheader("🎭 Final Vibe Check:")
    if mood_score >= 3:
        st.success("🥰 Your article is thriving. Keep slaying.")
    elif mood_score >= 1:
        st.info("🙂 Pretty good vibes. Maybe zhuzh it up a little.")
    elif mood_score == 0:
        st.warning("😐 Mid. Like office coffee. Not bad, not great.")
    else:
        st.error("🫠 Oh honey... this one needs a rewrite and a hug.")
