"""
Calculate test scores
wk3 open source dev 2020-1-23
"""

# The test score program
counter = 0
scoreTotal = 0
testScore = 0

while True:
    testScore = int(input('Enter a test score (0-100, 999 to quit): '))
    if testScore >= 0 and testScore <=100:
        scoreTotal += testScore
        counter += 1
    elif testScore == 999:
        break
    else:
        print('Test score must be between 0 and 100. Score discarded. Please try again')
averageScore = round(scoreTotal / counter)
print('=====================================================================')
print('Total score: ', scoreTotal, '\tAverage score: ', averageScore)
 