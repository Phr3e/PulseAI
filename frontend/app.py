import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("📢 PulseAI - Audience Engagement Demo")

# Show polls
st.subheader("Active Polls")
polls = requests.get(f"{API_URL}/polls/").json()

for poll in polls:
    st.write(f"**{poll['question']}**")
    if st.button(f"Vote {poll['option_a']}", key=f"a{poll['id']}"):
        requests.post(f"{API_URL}/vote/", json={"poll_id": poll["id"], "option": "A"})
        st.success("Voted for Option A")
    if st.button(f"Vote {poll['option_b']}", key=f"b{poll['id']}"):
        requests.post(f"{API_URL}/vote/", json={"poll_id": poll["id"], "option": "B"})
        st.success("Voted for Option B")
    st.progress(poll['votes_a'] + poll['votes_b'])
    st.write(f"Votes: {poll['option_a']} ({poll['votes_a']}), {poll['option_b']} ({poll['votes_b']})")
    st.markdown("---")
