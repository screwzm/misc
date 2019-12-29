
from random import seed
from random import randint
import tabulate
import time

generatedCalc = {}
resultList = []

TOTOL_QUESTION_CNT = 10
correctAnswerCnt = 0
for id in range(TOTOL_QUESTION_CNT):
    while True:
        seed(int(time.time()))
        value1 = randint(0, 10)
        value2 = randint(0, 10)
        expr = f"{value1} + {value2}"
        if expr not in generatedCalc:
            break

    generatedCalc[expr] = False
    expectedResult = eval(expr)
    while True:
        try:
            result = int(input(f"{expr} = "))
            break
        except:
            print("== Print input your answer.")

    currentResultEntry = [id + 1, expr, expectedResult, result, u'\u2713' if bool(result == expectedResult) else u'\u2717']
    if currentResultEntry[-1] == u'\u2713':
        correctAnswerCnt += 1

    generatedCalc[expr] = currentResultEntry
    resultList.append(currentResultEntry)

summary = ['Points', '', '', '', int(correctAnswerCnt/TOTOL_QUESTION_CNT*100)]
resultList.append(summary)
print("==== All Questions Finished ====")
print(tabulate.tabulate(resultList, headers=['ID', 'Question', 'ExpectedAnswer', 'YourAnswer', 'PointGot']))