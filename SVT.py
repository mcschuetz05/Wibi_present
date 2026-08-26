import random
import streamlit as st


st.set_page_config(
    page_title="CARAT, SCOUPS, HOSHI!",
    page_icon="💎"
)

st.title(" Happy Birthday, Wibi ❤️")
st.write("💎 Let's play CARAT, SCOUPS, HOSHI! 🐯")

st.markdown("""
### Rules

- Carats can run faster than Scoups
- But Carats are drawn into Hoshi's tiger cult 🐯
- And Scoups is the leader, so Hoshi must omit  
  *(if he ever does... 👀)*
- First to win **3 rounds** is the winner! 🥳
""")


possibilities = ["carat", "scoups", "hoshi"]

wins_against = {
    "carat": "scoups",
    "scoups": "hoshi",
    "hoshi": "carat"
}


# -------------------------
# GAME STATE
# -------------------------

if "won" not in st.session_state:
    st.session_state.won = 0

if "lost" not in st.session_state:
    st.session_state.lost = 0

if "phase" not in st.session_state:
    st.session_state.phase = "game"

if "last_result" not in st.session_state:
    st.session_state.last_result = ""


# -------------------------
# GAME
# -------------------------

if st.session_state.phase == "game":

    st.subheader(
        f"Score: {st.session_state.won} - {st.session_state.lost}"
    )

    choice = st.radio(
        "Make your choice:",
        possibilities,
        format_func=str.capitalize,
        horizontal=True
    )

    if st.button("Play! 🎮"):

        fate = random.choice(possibilities)

        if choice == fate:

            st.session_state.last_result = (
                f"🤝 I played {fate.capitalize()} — it's a tie!"
            )

        elif wins_against[choice] == fate:

            st.session_state.won += 1

            st.session_state.last_result = (
                f"🎉 I played {fate.capitalize()} — you won!"
            )

        else:

            st.session_state.lost += 1

            st.session_state.last_result = (
                f"😈 I played {fate.capitalize()} — you lost!"
            )

        if (
            st.session_state.won >= 3
            or st.session_state.lost >= 3
        ):
            st.session_state.phase = "test"

        st.rerun()

    if st.session_state.last_result:
        st.info(st.session_state.last_result)


# -------------------------
# CARAT TEST
# -------------------------

elif st.session_state.phase == "test":

    st.subheader(
        f"Final score: {st.session_state.won} - {st.session_state.lost}"
    )

    st.write("Nice game! 😌")

    test = st.text_input(
        "Now SAY THE NAME:"
    )

    if st.button("Submit answer 💎"):

        if test.upper().startswith("SEVENTEEN"):

            st.session_state.phase = "success"
            st.rerun()

        else:

            st.session_state.phase = "failed"
            st.rerun()


# -------------------------
# SUCCESS
# -------------------------

elif st.session_state.phase == "success":

    st.success("CORRECT! 💎")

    st.write("""
Here we go:

seungcheol! jeonghan! jisoo! junhui! soonyoung! wonwoo!
jihun! myungho! mingyu! seokmin! seungkwan! hansol! chan!
hansol! seungkwan! seokmin! mingyu! myungho!

### SEVENTEEEEEEEEEEEEEN!!! 🎉💎
""")

    if st.button("Play again 🔄"):

        st.session_state.won = 0
        st.session_state.lost = 0
        st.session_state.last_result = ""
        st.session_state.phase = "game"

        st.rerun()


# -------------------------
# WRONG ANSWER
# -------------------------

elif st.session_state.phase == "failed":

    st.error("Are you even a Carat... ? 🤨")

    if st.button("Redeem yourself 😭"):

        st.session_state.won = 0
        st.session_state.lost = 0
        st.session_state.last_result = ""
        st.session_state.phase = "game"

        st.rerun()
