def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token ={'type': 'NUMBER', 'number': number}
    return token, index

def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readCross(line, index):
    token = {'type': 'CROSS'}
    return token, index + 1

def readSlash(line, index):
    token = {'type': 'SLASH'}
    return token, index + 1




def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readCross(line, index)
        elif line[index] == '/':
            (token, index) = readSlash(line, index)


        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens

def evaluate1(tokens): 
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 2
    length = len(tokens)
    while index < length:
        if tokens[index]['type'] == 'NUMBER':
            #if index - 1 == 0:
                #tokens[index]['number'] = tokens[index]['number']
            if tokens[index - 1]['type'] == 'CROSS':
                tokens[index - 2]['number'] = tokens[index]['number']*tokens[index-2]['number']
                k = index
                index -=2
                while k < length-1 :
                 tokens[k - 1] = tokens[k + 1]
                 k += 1
                 
                tokens[length-1]= {'type': 'NUMBER', 'number': 0}
                tokens[length-2] ={'type': 'PLUS'}
               #i = 1
               # while i<length:
                 # print i,tokens[i],length
                 # i += 1
                
               
            elif tokens[index - 1]['type'] == 'SLASH':
                tokens[index - 2]['number'] = tokens[index-2]['number']/tokens[index]['number']
                k = index
                index -=2
                while k < length-1 :
                 tokens[k - 1] = tokens[k + 1]
            
                 k += 1
                 
                tokens[length-1]= {'type': 'NUMBER', 'number': 0}
                tokens[length-2] ={'type': 'PLUS'}
               #i = 1
               # while i<length:
                 # print i,tokens[i],length
                 # i += 1
            

            #else:
               # print 'Invalid syntax'
        index += 1

    return tokens




def evaluate2(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    length = len(tokens)
    while index < length:
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer


while True:

    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    tokens = evaluate1(tokens)
    answer = evaluate2(tokens)
    print "answer = %f\n" % answer
