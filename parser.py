keyword = '<System.Web.Services.Protocols.SoapDocumen'
print('f')
path1 = 'reference.txt'
path = 'test_file.txt'

def parser(path):

    return_list = []

    unopened = open(path, 'r')
    string = unopened.read()

    split_string = string.split('\n', )

    c = 0
    printstr = ''

    for i in range(len(split_string)):
        if keyword in split_string[i]:
            print('\n' + split_string[i])
            print('\n' + split_string[i + 1])
            temp_function_name = split_string[i + 1].strip().split(' ')

            function_name = ''
            for char in temp_function_name[2]:
                if char == '(':
                    break
                function_name += char
            print('function_name')
            print(function_name)

            string2 = split_string[i + 1]
            parantheses = ''
            for j in range(len(string2)):
                if '(' in string2[j:j + 1]:
                    j += 1
                    parantheses += ' '
                    while string2[j: j + 1] != ')':
                        parantheses += string2[j: j + 1]
                        j += 1
            parameters = parantheses.split(',')
            parameter_list = []

            for k in range(len(parameters)):
                split_on_space = parameters[k].split(' ')
                parameter_list.append({split_on_space[4]: split_on_space[2]})
            print('paramaterlist:')
            print(parameter_list)
            return_list.append({function_name : parameter_list})
    return return_list


returnval = parser(path1)
print(returnval)