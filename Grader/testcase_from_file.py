from Classes import Testcase

def get_test_case():
    with open("inputs.txt", 'r') as f:
        s = f.readlines()
        test_case = Testcase()
        test_case.id = s[0].rstrip()
        test_case.input = s[1].rstrip()
        test_case.timeout = s[2].rstrip()
        return test_case
print(get_test_case())
