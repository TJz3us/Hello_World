import score_analyzer_functions_Hicks_Barrow




x = int(input("How many grades are there?"))
for i in range (x):
    # input for name
    y = input("Give me student names")
    # input for number grade
    t = int(input("Give a number grade"))
    # set the letter grade using scoreanalize and save it to a variable
    letter = score_analyzer_functions_Hicks_Barrow.scoreanalize()
    # use the three variables in studentrecordbuilder to print your data
    print(score_analyzer_functions_Hicks_Barrow.stedentrecordbuilder(y, t, letter))
