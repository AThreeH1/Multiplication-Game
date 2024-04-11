import streamlit as st
import pandas as pd
import random
import json
import os
import matplotlib.pyplot as plt

# Function to generate random numbers
def start_game():
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    return num1, num2

# Function to check the answer and update the JSON file
def check_answer(num1, num2, answer, start_time):
    end_time = pd.Timestamp.now()
    elapsed_time = (end_time - start_time).total_seconds()
    if int(answer) == num1 * num2:
        data = {'num1': num1, 'num2': num2, 'time': elapsed_time}
        with open('C:/Games/Multiplication game/data.json', 'a') as file:
            json.dump(data, file)
            file.write('\n')
        return True, elapsed_time
    else:
        return False, 0.0

# Function to plot the graph
def plot_graph():
    if os.path.exists('C:/Games/Multiplication game/data.json'):
        df = pd.read_json('C:/Games/Multiplication game/data.json', lines=True)
        if not df.empty:
            plt.figure(figsize=(10, 6))
            for col in df.columns:
                if col != 'time':
                    continue
                plt.plot(df.index, df[col], marker='o', linestyle='-', label=col)
            plt.title('Time taken for your dumbass to figure out some elementary calculation')
            plt.xlabel('Games')
            plt.ylabel('Time (seconds)')
            plt.legend()
            st.pyplot(plt)
        else:
            st.warning("Nerrdddd")
    else:
        st.warning("Nerrddd")

# Main function
def main():
    st.title('Multiplication Game')

    if 'game_started' not in st.session_state:
        st.session_state.game_started = False

    if not os.path.exists('C:/Games/Multiplication game/data.json'):
        with open('C:/Games/Multiplication game/data.json', 'w') as file:
            pass

    if not st.session_state.game_started:
        st.session_state.game_started = st.button('Start Game')

    if st.session_state.game_started:
        if 'num1' not in st.session_state:
            st.session_state.num1, st.session_state.num2 = start_game()

        if not st.session_state.num1:
            st.session_state.num1, st.session_state.num2 = start_game()

        if 'answer_correct' not in st.session_state:
            st.session_state.answer_correct = False

        if not st.session_state.answer_correct:
            if 'start_time' not in st.session_state:
                st.session_state.start_time = pd.Timestamp.now()

            st.write(f"What is {st.session_state.num1} times {st.session_state.num2}?")
            answer = st.number_input('Your answer:', min_value=0, max_value=9999, step=1)
            submit_button = st.button('Submit')
            if submit_button and answer is not None:
                correct, elapsed_time = check_answer(st.session_state.num1, st.session_state.num2, answer, st.session_state.start_time)
                if correct:
                    st.success(f'Finally, Mr. Smarty Pants figured it out! Time taken: {elapsed_time} seconds')
                    st.session_state.answer_correct = True
                else:
                    st.error('Oh my god, you loser, that is so wrong')
        else:
            play_again = st.button('Play Again')
            if play_again:
                st.session_state.num1, st.session_state.num2 = start_game()
                st.session_state.answer_correct = False
                st.session_state.start_time = pd.Timestamp.now()

    plot_graph()

if __name__ == "__main__":
    main()
