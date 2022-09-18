# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b

def is_human_number_a_whole_number(human_years):
    try:
        int(human_years)
        return True
    except:
        return False

def human_years_to_cat_years(human_years):
    cat_years = 0
    if human_years == 1:
        cat_years = 15
    if human_years == 2:
        cat_years = 24
    if human_years >= 3:
        cat_years = 24 + (4 * (human_years - 2))
    return cat_years

def human_years_to_dog_years(human_years):
    dog_years = 0
    if human_years == 1:
        dog_years = 15
    if human_years == 2:
        dog_years = 24
    if human_years >= 3:
        dog_years = 24 + (5 * (human_years - 2))
    return dog_years

def human_years_cat_years_dog_years(human_years):
    
    if is_human_number_a_whole_number(human_years):
        cat_years = human_years_to_cat_years(human_years)
        dog_years = human_years_to_dog_years(human_years)
        print(human_years, cat_years, dog_years)
        return [human_years, cat_years, dog_years]
        
    else:
        print('Provide a whole number.')

human_years_cat_years_dog_years(4)