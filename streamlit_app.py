import streamlit as st

# Define moves and what beats what
beats = {'R': 'P', 'P': 'S', 'S': 'R'}

def recommend_next_move(your_move, opponent_move):
    if your_move == opponent_move:
        return your_move
    elif beats[your_move] == opponent_move:
        return beats[opponent_move]
    else:
        return opponent_move

st.title("Rock-Paper-Scissors Strategy Helper")

your_move = st.selectbox('Your Last Move', ['Rock', 'Paper', 'Scissors'])
opponent_move = st.selectbox('Opponent Move', ['Rock', 'Paper', 'Scissors'])

move_mapping = {'Rock': 'R', 'Paper': 'P', 'Scissors': 'S'}

recommended_move = recommend_next_move(move_mapping[your_move], move_mapping[opponent_move])

reverse_move_mapping = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
st.write(f"Recommended next move: **{reverse_move_mapping[recommended_move]}**")
