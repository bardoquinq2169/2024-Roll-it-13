# create lines to hold user and computer scores
user_scores = []
comp_scores = []

# loop six times - for testing purposes, ask the user to enter the
# score for the user and the computer for each round
for item in range(0, 6):
    user_score = int(input("Enter the user score: "))
    comp_score = int(input("Enter the computer score: "))

    # add user and computer score to lists!
    user_scores.append(user_score)
    comp_scores.append(comp_score)

# calculate the lowest, highest and average
# scores and display then.

# sort the lists
user_scores.sort()
comp_scores.sort()

print("user scores: ", user_scores)
print("computer scores: ", comp_scores)
