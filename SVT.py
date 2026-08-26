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
# SESSION STATE
# -------------------------

if "won" not in st.session_state:
    st.session_state.won = 0

if "lost" not in st.session_state:
    st.session_state.lost = 0

if "last_result" not in st.session_state:
    st.session_state.last_result = ""

if "game_over" not in st.session_state:
    st.session_state.game_over = False


# -------------------------
# SCORE
# -------------------------

st.subheader(
    f"YOU  {st.session_state.won} : {st.session_state.lost}  Buck-Tschakkalakka"
)

st.write("Your progress:")

st.progress(st.session_state.won / 3)

st.caption(f"{st.session_state.won} / 3 wins")


# -------------------------
# GAME
# -------------------------

if not st.session_state.game_over:

    st.write("### Make your choice:")

    col1, col2, col3 = st.columns(3)

    with col1:
        carat = st.button(
            "💎 CARAT",
            use_container_width=True
        )

    with col2:
        scoups = st.button(
            "🍒 SCOUPS",
            use_container_width=True
        )

    with col3:
        hoshi = st.button(
            "🐯 HOSHI",
            use_container_width=True
        )

    choice = None

    if carat:
        choice = "carat"

    elif scoups:
        choice = "scoups"

    elif hoshi:
        choice = "hoshi"

    if choice:

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
            st.session_state.game_over = True

        st.rerun()


# -------------------------
# LAST ROUND RESULT
# -------------------------

if st.session_state.last_result:

    if "you won" in st.session_state.last_result:

        st.success(
            st.session_state.last_result
        )

    elif "you lost" in st.session_state.last_result:

        st.error(
            st.session_state.last_result
        )

    else:

        st.warning(
            st.session_state.last_result
        )


# -------------------------
# GAME OVER
# -------------------------

if st.session_state.game_over:

    if st.session_state.won == 3:

        st.balloons()

        st.success(
            "YOU WON THE GAME! 💎🎉"
        )

    else:

        st.error(
            "You lost the game 😭"
        )

    st.write("## Now SAY THE NAME 👀")

    test = st.text_input(
        "SAY THE NAME!"
    )

    if st.button("Submit 💎"):

        if test.upper().startswith("SEVENTEEN"):

            st.balloons()

            st.success(
                "CORRECT! 💎"
            )

            st.markdown("""

seungcheol!  
jeonghan!  
jisoo!  
junhui!  
soonyoung!  
wonwoo!  
jihun!  
myungho!  
mingyu!  
seokmin!  
seungkwan!  
hansol!  
chan!

### SEVENTEEEEEEEEEEEEEN!!! 🎉
""")

        elif test:

            st.error(
                "Are you even a Carat...? 🤨"
            )


# -------------------------
# RESTART
# -------------------------

st.divider()

if st.button("🔄 Restart Game"):

    st.session_state.won = 0
    st.session_state.lost = 0
    st.session_state.last_result = ""
    st.session_state.game_over = False

    st.rerun()
