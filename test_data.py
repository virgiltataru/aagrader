from Classes import Testcase


tc1 = Testcase()
tc1.id = "1"
tc1.input = '23\n34'
tc1.timeout = 1

tc2 = Testcase()
tc2.id = "2"
tc2.input = """21\n34"""
tc2.timeout = 1
python3_source_code_add_two_numbers = """
number1 = input()
number2 = input()

sum = int(number1) + int(number2)
print(sum)
"""
