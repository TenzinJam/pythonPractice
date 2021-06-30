from Question import Question

question_prompts = [
  "What's your name?\n(a) Tenzin\n(b) Tashi\n(c) Tsering\n\n",
  "What's your age?\n(a) 35\n(b) 40\n(c) 34\n\n",
  "What's your origin?\n(a) Tibetan\n(b) Nepalese\n(c) Hawaiian\n\n",
]

questions = [
  Question(question_prompts[0], "a"),
  Question(question_prompts[1], "c"),
  Question(question_prompts[2], "a")
]

def run_test(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  print("You got "+ str(score) + "/" + str(len(questions)))

run_test(questions)
