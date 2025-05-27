import streamlit as st
from textblob import TextBlob
import re

st.title("💅 Article Mood Checker")
st.caption("Paste your content. Prepare to be judged. Fairly, of course.")

text = st.text_area("Drop your article here, bestie:")

if text:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    word_count = len(text.split())
    vibes = []
    mood_score = 0

    # ✨ Sentiment-based mood
    if sentiment > 0.5:
        vibes.append("✨ Sunshine vibes. You sound like you believe in Mondays.")
        mood_score += 2
    elif sentiment > 0:
        vibes.append("🙂 Polite. Pleasant. Like a LinkedIn post nobody reacts to.")
        mood_score += 1
    elif sentiment == 0:
        vibes.append("😐 Neutral. As exciting as a printer manual.")
    else:
        vibes.append("🫠 Is everything okay? Do you need a hug and a rewrite?")
        mood_score -= 1

    # 📢 Hype word detector
    hype_words = ["innovative", "cutting-edge", "synergy", "revolutionary", "leverage"]
    found_hype = [word for word in hype_words if word in text.lower()]
    if found_hype:
        vibes.append(f"📢 Chill bestie — you used hype words like {', '.join(found_hype)}. We get it.")
        mood_score -= 1

    # ❗ Exclamation mark drama
    exclaims = text.count("!")
    if exclaims >= 3:
        vibes.append("😬 Okay Shakespeare, maybe tone down the drama.")
        mood_score -= 1

    # 🧮 Word count sass
    st.subheader("🧮 Word Count Commentary")
    st.write(f"Total words: **{word_count}**")
    if word_count < 50:
        st.warning("🫣 This isn’t an article, it’s a tweet thread in denial.")
        mood_score -= 1
    elif word_count < 200:
        st.warning("👀 Giving low-effort listicle intro energy.")
        mood_score -= 1
    elif word_count < 600:
        st.info("📄 Feels like a safe, mid-length blog post. Respectable.")
    elif word_count < 1000:
        st.success("📝 Solid! You’re in the SEO sweet spot.")
        mood_score += 1
    else:
        st.success("📚 Wow. A whole TED Talk. Hope it slaps.")
        mood_score += 2

    # 💬 Final vibe commentary
    st.subheader("💬 Vibe Commentary")
    for v in vibes:
        st.write(v)

    # 🎭 Final emoji reaction
    st.subheader("🎭 Final Mood Reaction")
    if mood_score >= 3:
        st.success("🥰 Slay. Your article is giving thought leader realness.")
    elif mood_score >= 1:
        st.info("😌 Not bad. Bit safe. Needs more ✨oomph✨.")
    elif mood_score == 0:
        st.warning("😐 Mid. Would skim. Might forget.")
    else:
        st.error("🫠 Throw it in Google Docs, let it sit, try again tomorrow.")
