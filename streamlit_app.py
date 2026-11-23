import json
import streamlit as st

st.set_page_config(page_title="Short-Form Content Studio", page_icon="🎬", layout="wide")

st.title("🎬 Short-Form Content & Script Planner")
st.caption("Plan hooks, spoken scripts, visual shot lists, and captions—no heavy AI model downloads required.")

col1, col2 = st.columns(2)

with col1:
    niche = st.text_input("Topic / Niche", value="Practical Money & Productivity Tips")
    audience = st.text_input("Target Viewer", value="Busy working professionals")
    duration = st.selectbox("Target Length", ["30 seconds", "45 seconds", "60 seconds"])
    tone = st.selectbox("Delivery Style", ["Direct & Practical", "Story-Driven", "Myth vs. Reality"])

with col2:
    hook = st.text_area(
        "Opening Hook (First 3 Seconds)",
        value="Most people waste hours doing this manually—here is a 30-second fix.",
        height=80,
    )
    key_points = st.text_area(
        "Core Points (One point per line)",
        value="1. State the common mistake clearly.\n2. Show the simple step-by-step fix.\n3. End with one clear takeaway.",
        height=120,
    )
    cta = st.text_input("Ending Call-to-Action", value="Save this for later and share with someone who needs it.")

st.subheader("Visual Shot List & Voiceover Notes")
shot_notes = st.text_area(
    "What appears on screen vs. what you say",
    value="0-3s: Hook on screen + direct voiceover\n3-20s: Step-by-step demonstration or B-roll\n20-30s: Summary card + CTA",
    height=100,
)

script_draft = f"""HOOK (0-3s):
{hook}

BODY ({duration} | Tone: {tone} | Audience: {audience}):
{key_points}

VISUAL / B-ROLL PLAN:
{shot_notes}

OUTRO / CTA:
{cta}
"""

st.subheader("Ready-to-Use Script")
st.code(script_draft, language="text")

package_data = {
    "niche": niche,
    "audience": audience,
    "duration": duration,
    "tone": tone,
    "hook": hook,
    "key_points": [line.strip() for line in key_points.splitlines() if line.strip()],
    "shot_notes": shot_notes,
    "cta": cta,
}

st.download_button(
    label="Download Content Plan (JSON)",
    data=json.dumps(package_data, indent=2),
    file_name="reel_content_plan.json",
    mime="application/json",
)
