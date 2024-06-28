def dateCalculte(startDate, reqMonth):
    year, month, day = map(int, startDate.split("."))
    day += reqMonth * 28 - 1

    if day > 28:
        if day % 28 == 0:
            month += day //28 -1
            day = 28
        else:
            month += day // 28
            day = day % 28
    if month > 12:
        if month % 12 == 0:
            year += month //12 -1
            month = 12
        else :
            year += month // 12
            month = month % 12
    return "{0}.{1:02}.{2:02}".format(year, month, day)

def solution(today, terms, privacies):
    answer = []
    termR = [tuple(term.split()) for term in terms]
    for i in range(len(privacies)):

        startDate, thisTerm = privacies[i].split()
        filteredTerm = list(filter(lambda a: a[0] == thisTerm, termR))
        dueDate = dateCalculte(startDate, int(filteredTerm[0][1]))
        if today >= dueDate:
            answer.append(i+1)
    return answer

print(solution( "2020.05.15", ["A 1"], ["2001.01.10 A", "2001.01.10 A"]))