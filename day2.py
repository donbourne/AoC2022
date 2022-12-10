
choice_scores = {'X': 1, 'Y': 2, 'Z': 3}
outcome_scores = {'win': 6, 'draw': 3, 'lose': 0}


choices = {'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'}, 'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'}, 'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}}

f = open("day2.txt", "rt")
lines = f.readlines()

total_outcome_score = 0
total_choice_score = 0


def get_outcome(a, b):
    if a == 'A' and b == 'X':
        outcome = 'draw'
    elif a == 'A' and b == 'Y':
        outcome = 'win'
    elif a == 'A' and b == 'Z':
        outcome = 'lose'

    if a == 'B' and b == 'X':
        outcome = 'lose'
    elif a == 'B' and b == 'Y':
        outcome = 'draw'
    elif a == 'B' and b == 'Z':
        outcome = 'win'

    if a == 'C' and b == 'X':
        outcome = 'win'
    elif a == 'C' and b == 'Y':
        outcome = 'lose'
    elif a == 'C' and b == 'Z':
        outcome = 'draw'

    return outcome


# 1
print("problem 1")
for line in lines:
    a, b = line.split(' ')
    a = a.strip()
    b = b.strip()

    print(a, b)
    outcome = get_outcome(a, b)
    outcome_score = outcome_scores[outcome]
    choice_score = choice_scores[b]

    print(f'{a} {b}')
    print(f'outcome_score: {outcome_score}')
    print(f'choice_score: {choice_score}')

    total_outcome_score += outcome_score
    total_choice_score += choice_score

print(f'score: {total_outcome_score + total_choice_score}')


#2
print("problem 2")
total_outcome_score = 0
total_choice_score = 0

for line in lines:
    a, b = line.split(' ')
    a = a.strip()
    b = b.strip()

    print(a, b)
    choice = choices[a][b]
    print(f'choice: {choice}')

    outcome = get_outcome(a, choice)
    outcome_score = outcome_scores[outcome]
    choice_score = choice_scores[choice]

    print(f'outcome_score: {outcome_score}')
    print(f'choice_score: {choice_score}')

    total_outcome_score += outcome_score
    total_choice_score += choice_score

print(f'score: {total_outcome_score + total_choice_score}')

