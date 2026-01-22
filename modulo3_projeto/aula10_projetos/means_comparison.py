

def different(file1, file2):
    output = list()
    for param in file1.param:
        if all(file1.loc[file1['param'] == param, 'reject'] == 'different means'):
            if all(file2.loc[file2['param'] == param, 'reject'] == 'different means'):
                output.append(param)
    return output
