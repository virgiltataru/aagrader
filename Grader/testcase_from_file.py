from Classes import Testcase

def get_test_case(name= ''):
    if name=='':
        with open("inputs.txt", 'r') as f:
            s = f.readlines()
            test_case = Testcase()
            test_case.id = s[0].rstrip()
            test_case.input = s[1].rstrip().replace(' ', '\n')
            test_case.expected_output= s[2].rstrip().replace(' ', '\n')
            test_case.timeout = int(s[3].rstrip())
            return test_case
    else:
        with open(name, 'r') as f:
            s = f.readlines()
            test_case = Testcase()
            test_case.id = s[0].rstrip()
            test_case.input = s[1].rstrip().replace(' ', '\n')
            test_case.expected_output= s[2].rstrip().replace(' ', '\n')
            test_case.timeout = int(s[3].rstrip())
            return test_case

print(get_test_case())
