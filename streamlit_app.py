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
        return beats[opponent_move]

beats = {'R': 'P', 'P': 'S', 'S': 'R'}
move_mapping = {'Rock': 'R', 'Paper': 'P', 'Scissors': 'S'}
reverse_move_mapping = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

st.title("Rock-Paper-Scissors Strategy Helper")

menu = st.sidebar.selectbox("Menu", ["Play Game", "View History"])

if menu == "Play Game":
    st.write("Enter your previous move and your opponent's move from the last round to get a recommendation.")
    your_move = st.selectbox('Your Last Move', ['Rock', 'Paper', 'Scissors'])
    opponent_move = st.selectbox('Opponent Move', ['Rock', 'Paper', 'Scissors'])

    recommended_move = recommend_next_move(move_mapping[your_move], move_mapping[opponent_move])

    st.write(f"Recommended next move: **{reverse_move_mapping[recommended_move]}**")

    if st.button("Save Round"):
        st.session_state.history.append({
            "Your Move": your_move,
            "Opponent Move": opponent_move,
            "Recommended Move": reverse_move_mapping[recommended_move]
        })
        st.success("Round saved to history!")

elif menu == "View History":
    st.header("Game History and Trends")

    if st.session_state.history:
        st.write(st.session_state.history)
        total_games = len(st.session_state.history)
        st.write(f"Total games played: {total_games}")

        # Calculate success rate if applicable
        wins = sum(1 for game in st.session_state.history if beats[move_mapping[game['your_move']]] == move_mapping[game['opponent_move']])
        success_rate = (total_games - len([game for game in st.session_state.history if recommend_next_move(move_mapping[game['your_move']], move_mapping[game['opponent_move']]) != move_mapping[game['your_move']]])) / total_games * 100
        st.write(f"Success rate of recommendations: {success_rate:.2f}%")
    else:
        st.write("No game history yet. Play some games to view statistics!")

# Record each play
if menu == "Play Game" and st.button("Record Result"):
    st.session_state.history.append({
        "your_move": your_move,
        "opponent_move": opponent_move,
        "recommended_move": reverse_move_mapping[recommended_move]
    })
