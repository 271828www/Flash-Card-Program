def error_of_tolerance (true_answer, user_answer):
    difference = 0
    pre_check = len(true_answer) - len(user_answer)
    if pre_check > 0:
        difference += pre_check
    if pre_check < 0:
        pass
    i = 0
    while i < len(true_answer) and i < len(user_answer):
        if true_answer[i] != user_answer[i]:
            difference += 1
        i += 1
    return (difference/len(true_answer))*100