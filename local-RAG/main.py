#Run this if it is main file
import os
from question_answer import question_answer


def main():
    os.system('clear')
    print("Start Interacting with Ollama")
    question_answer("TikTok-Profile-Scripts-analytics.csv")


if __name__ == "__main__":
    main()
