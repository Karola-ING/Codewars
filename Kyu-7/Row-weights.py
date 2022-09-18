# https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9

def row_weights(array):
    team_1 = 0
    team_2 = 0
    for index, value in enumerate(array):
        if index % 2 == 0:
            team_1 += value
        else:
            team_2 += value
    return (team_1, team_2)