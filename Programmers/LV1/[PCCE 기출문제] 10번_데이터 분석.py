def solution(data, ext, val_ext, sort_by):
    column = ["code", "date", "maximum", "remain"]
    ind = column.index(ext)
    sort_ind = column.index(sort_by)
    answer = []
    for d in data:
        if d[ind]<val_ext:
            answer.append(d)
    return sorted(answer, key = lambda x:x[sort_ind])