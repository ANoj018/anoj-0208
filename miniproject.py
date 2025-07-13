# Quiz Game: Ask 5 MCQ questions and give final score.
score = 0

print("1) Capital of Nepal?")
print("a) Pokhara")
print("b) Kathmandu")
print("c) Biratnagar")
answer = input("Your answer: ")
if answer == "b":
    score += 1

print("2) 2 + 2 = ?")
print("a) 3")
print("b) 4")
print("c) 5")
answer = input("Your answer: ")
if answer == "b":
    score += 1

print("3) Sun rises from?")
print("a) West")
print("b) South")
print("c) East")
answer = input("Your answer: ")
if answer == "c":
    score += 1

print("4) Which one is a fruit?")
print("a) Carrot")
print("b) Mango")
print("c) Potato")
answer = input("Your answer: ")
if answer == "b":
    score += 1

print("5) Color of the sky?")
print("a) Green")
print("b) Blue")
print("c) Red")
answer = input("Your answer: ")
if answer == "b":
    score += 1

print("Your score is", score, "out of 5")


