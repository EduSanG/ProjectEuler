digits_dict = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

tens_dict = {
    0: '',
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

exceps_dict = {
    'tenone': 'eleven',
    'tentwo': 'twelve',
    'tenthree': 'thirteen',
    'tenfour': 'fourteen',
    'tenfive': 'fifteen',
    'tensix': 'sixteen',
    'tenseven': 'seventeen',
    'teneight': 'eighteen',
    'tennine': 'nineteen',
}

def number_to_string(n):
    digits_arr = list(map(int, str(n)))[::-1]
    hundreds = f'{digits_dict[digits_arr[2]]}hundredand' if len(digits_arr) > 2 else ''
    tens = f'{tens_dict[digits_arr[1]]}' if len(digits_arr) > 1 else ''
    digits = f'{digits_dict[digits_arr[0]]}'

    if hundreds is not '' and tens == '' and digits == '':
        hundreds = hundreds.replace('hundredand', 'hundred')

    result = f'{hundreds}{tens}{digits}'
    for key, value in exceps_dict.items():
        result = result.replace(key, value)

    return result

def main(): 
    acc_string = ''
    for i in range(1,1000):
        acc_string += number_to_string(i)

    for num in [number_to_string(x) for x in range(1,200)]:
        print(num)
    acc_string+='onethousand'
    return len(list(acc_string))