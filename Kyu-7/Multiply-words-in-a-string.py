# https://www.codewars.com/kata/5ace2d9f307eb29430000092

def modify_multiply(st, loc, num):
    
    example = st.split()

    result = [example[loc]] * num 

    end = '-'.join(result)

    return end



print(modify_multiply("This is a string",3 ,5))
