# https://www.codewars.com/kata/57126304cdbf63c6770012bd

def isDigit(string):
    try:
        float(string)
        return True
    except:
        return False