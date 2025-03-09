import streamlit as st

# Define relationships
beats = {'R': 'P', 'P': 'S', 'S': 'R'}

# Function to determine recommended next move based on previous results
def recommend_next_move(your_move, opponent_move):
    if your_move == opponent_move:
        # Tie: stay neutral and repeat your choice
        return your_move
    elif beats[your_move] == opponent_move:
        # You lost: pick what would have beaten your opponent's last move
        return beats[opponent_move]
    else:
        # You won: repeat opponent's move anticipating their shift
        return opponent_move

# Streamlit web app setup
st.title("Rock-Paper-Scissors Strategy Simulator")
st.write("Input your previous moves to receive a recommendation for your next throw.")

# Input from user
your_move = st.selectbox('Your Last Move', ['Rock', 'Paper', 'Scissors'])
opponent_move = st.selectbox('Opponent Move', ['Rock', 'Paper', 'Scissors'])

# Convert inputs to single characters
move_mapping = {'Rock': 'R', 'Paper': 'P', 'Scissors': 'S'}
y_move_char = move_mapping[your_move]
o_move_char = move_mapping[opponent_move]

# Get recommendation
next_move_short = recommend_next_move(your_move=move_mapping[your_move], opponent_move=move_mapping[opponent_move])

# Reverse mapping for full display
reverse_move_mapping = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
st.write(f"Recommended next move: **{reverse_move_mapping[next_move]}**")
