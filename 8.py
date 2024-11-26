
def chack_in_interval(what_to_ask, min_value, max_value, ):
    current_value = int(input(what_to_ask))
    if min_value < current_value < max_value:
        return True
    return False


def squares(n):
    print(n*n)


squares(5)
result = chack_in_interval("enter your age:", 0, 20)
if result:
    print('your age has been entered')
# chack_in_interval("enter your experience:", 2, 10)
