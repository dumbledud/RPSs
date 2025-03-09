import streamlit as st

# Define moves and what beats what
beats = {'R': 'P', 'P': 'S', 'S': 'R'}

# Session state initialization
if 'history' not in st.session_state:
    st.session_state.history = []

# Determine next move based on previous round's outcome
def recommend_next_move(your_move, opponent_move):
    if your_move == opponent_move:
        return your_move
    elif beats[your_move] == opponent_move:
        return beats[opponent_move]
    else:
        return beats[your_move]

move_mapping = {'Rock': 'R', 'Paper': 'P', 'Scissors': 'S'}
reverse_move_mapping = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

st.title("Rock-Paper-Scissors Strategy Helper")

# Initialize history storage
if 'history' not in st.session_state:
    st.session_state.history = []

menu = st.sidebar.selectbox("Menu", ["Play Game", "View History"])

if menu == "Play Game":
    st.write("Enter your move and your opponent's move from the last round to get a recommendation.")

    if st.session_state.history:
        last_game = st.session_state.history[-1]
        st.write(f"Last round recorded: You played {last_game['your_move']}, opponent played {last_game['opponent_move']}, recommended was {last_game['recommended_move']}")

    your_move = st.selectbox('Your Move', ['Rock', 'Paper', 'Scissors'])
    opponent_move = st.selectbox('Opponent Move', ['Rock', 'Paper', 'Scissors'])

    recommended_move = recommend_next_move(move_mapping[your_move], move_mapping[opponent_move])
    reverse_move_mapping = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

    if st.button("Record and Recommend Next Move"):
        # Record the current round before recommending next
        st.session_state.history.append({
            "your_move": your_move,
            "opponent_move": opponent_move,
            "recommended_move": reverse_move_mapping[recommended_move]
        })
        st.write(f"Recommended next move: **{reverse_move_mapping[recommended_move]}**")

elif menu == "View History":
    st.header("Game History and Trends")

    if st.session_state.history:
        st.write(st.session_state.history)
        total_games = len(st.session_state.history)
        successful_recommendations = sum(1 for game in st.session_state.history if move_mapping[game['recommended_move']] == recommend_next_move(move_mapping[game['your_move']], move_mapping[game['opponent_move']]))
        success_rate = (successful_recommendations / total_games) * 100
        st.write(f"Total games played: {total_games}")
        st.write(f"Success rate of recommendations: {success_rate:.2f}%")
    else:
        st.write("No games played yet.")

elif menu == "View History":
    st.header("Game History and Trends")
    if st.session_state.history:
        st.table(st.session_state.history)
    else:
        st.write("No game history yet.")
