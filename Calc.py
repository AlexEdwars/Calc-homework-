import re


def format(f):
    l_n = 0
    r_n = 0
    formula = f.replace(' ', '')
    formula = formula.replace('+-', '-')
    formula = formula.replace('++', '+')
    formula = formula.replace('-+', '-')
    formula = formula.replace('--', '+')
    formula = formula.replace('*+', '*')
    formula = formula.replace('/+', '/')
    formula = formula.replace('**+', '**')
    r = re.findall('\)', f)
    l = re.findall('\(', f)
    for i in l:
        l_n += 1
    for i in r:
        r_n += 1
    if l_n != r_n:
        print('括号错误!!!')
        exit()
    return formula


def operation1(f):
    formula = re.search('(?P<num1>-?\d+\.?\d*)\*\*(?P<num2>-?\d+\.?\d*)', f)
    if formula == None:
        return f
    else:
        num1 = float(formula_history.group('num1'))
        num2 = float(formula_history.group('num2'))
        sums = num1 ** num2
        sums = format(str(sums))
        return sums


def operation2(f):
    formula = re.search('(?P<num1>-?\d+\.?\d*)(?P<operator>[*/])(?P<num2>-?\d+\.?\d*)', f)
    if formula == None:
        return f
    elif re.search('(\*\*)', f) != None:
        return f
    else:
        num1 = float(formula.group('num1'))
        num2 = float(formula.group('num2'))
        operator = formula.group('operator')
        if operator == '*':
            sums = num1 * num2
        else:
            sums = num1 / num2
        sums = format(str(sums))
        return sums


def operation3(f):
    formula = re.search('(?P<num1>-?\d+\.?\d*)(?P<operator>[+\-])(?P<num2>-?\d+\.?\d*)', f)
    if formula == None:
        return f
    elif re.search('[(\*\*)*/]', f) != None:
        return f
    else:
        num1 = float(formula.group('num1'))
        num2 = float(formula.group('num2'))
        operator = formula.group('operator')
        if operator == '+':
            sums = num1 + num2
        else:
            sums = num1 - num2
        sums = format(str(sums))
        return sums


def operation_all(formula):
    while 1:
        if re.search('\d+\.?\d*[(**)*/+\-]-?\d+\.?\d*', formula) != None:
            if re.search('\d+\.?\d*(\*\*)-?\d+\.?\d*', formula) != None:
                ret = operation1(re.search('\d+\.?\d*(\*\*)-?\d+\.?\d*', formula).group())
                formula = formula.replace(re.search('-?\d+\.?\d*(\*\*)-?\d+\.?\d*', formula).group(), ret)
            elif re.search('\d+\.?\d*[*/]-?\d+\.?\d*', formula) != None:
                ret = operation2(re.search('\d+\.?\d*[*/]-?\d+\.?\d*', formula).group())
                formula = formula.replace(re.search('\d+\.?\d*[*/]-?\d+\.?\d*', formula).group(), ret)
            elif re.search('-?\d+\.?\d*[+\-]-?\d+\.?\d*', formula) != None:
                ret = operation3(re.search('-?\d+\.?\d*[+\-]-?\d+\.?\d*', formula).group())
                formula = formula.replace(re.search('-?\d+\.?\d*[+\-]-?\d+\.?\d*', formula).group(), ret)
            else:
                return formula
        else:
            return formula


def determine(f):
    if type(f) != str:
        f = f.group()
    return f


flag = True


while 1:
    flag = True
    formula_input = input('>>>:').strip()
    formula_input = format(formula_input)
    if formula_input == 'e':
        exit()
    elif re.findall('[^0-9+\-*/.(**)]', formula_input):
            print('算式错误!!!')
    else:
        formula_history = format(formula_input)
        formula = formula_history
        while flag:
            ret_history = re.search('\([^()]+\)', formula)
            ret = ret_history
            if ret_history == None:
                flag = False
            else:
                while 1:
                    if type(ret_history) != str:
                        ret_history = ret_history.group()
                    ret_history = format(ret_history)
                    ret = operation_all(ret_history)
                    ret = re.sub('[\(\)]', '', ret)
                    formula = formula.replace(ret_history, ret)
                    formula = format(formula)
                    break
        ret_history = re.search('-?\d+\.?\d*[(**)*/+\-]?-?\d+\.?\d*', formula)
        ret = ret_history
        if ret == None:
            print('算式错误!!!')
        else:
            ret = ret.group()
            while 1:
                if re.search('-?\d+\.?\d*[(**)*/+\-]', str(formula)) == None:
                    formula = formula.replace(ret_history.group(), ret)
                    break
                else:
                   formula = operation_all(formula)
        print(formula)

