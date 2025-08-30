questions = (
    "What is the capital of Australia?: ",
    "Which element has the chemical symbol 'Fe'?: ",
    "Who painted the Mona Lisa?: ",
    "Which planet has the most moons?: ",
    "What is the largest ocean on Earth?: "
)
options = (
    ("A. Sydney", "B. Melbourne", "C. Canberra", "D. Perth"),
    ("A. Fluorine", "B. Iron", "C. Francium", "D. Fermium"),
    ("A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"),
    ("A. Saturn", "B. Jupiter", "C. Uranus", "D. Neptune"),
    ("A. Atlantic Ocean", "B. Indian Ocean", "C. Southern Ocean", "D. Pacific Ocean")
)
answers = ("C","B","C","A","D")
guesses = []
score = 0
q_no = 0

for question in questions:
    print(question)
    for option in options[q_no]:
            print(option)
    guess = input("ENTER OPTION :").upper()
    guesses.append(guess)
    if guess == answers[q_no]:
          print("CORRECT")
          score += 1
    else:
          print("INCORRECT")
          print(f"CORRECT ANSWER : {answers[q_no]}")
    q_no+=1

print(f"TOTAL SCORE = {score} / {q_no}")
accuracy = (score / q_no) * 100
print(f"ACCURACY = {accuracy} %")


        
