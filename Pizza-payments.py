def michael_pays(costs):

    if costs <= 5:
        michael_pays = round(costs, 2)
    if costs > 5:
        new_costs = costs / 3
        if new_costs <= 10:
            michael_pays = round(new_costs*2, 2)
        else:
            michael_pays = round(costs - 10, 2)


    return michael_pays

