with open ("input.txt", 'r') as f:
    answers = f.readlines()

answers = [answer.strip() if answer != '\n' else '-' for answer in answers]
answers = " ".join(answers)
answers = answers.split('-')

totals_1 = [len(set(answer.replace(' ', ''))) for answer in answers]

totals_2 = [[set(b) for b in answer.split()] for answer in answers]
totals_2 = [set.intersection(*answer) for answer in totals_2]
totals_2 = [len(set(answer)) for answer in totals_2]

print("Part 1", sum(totals_1))
print("Part 2", sum(totals_2))
