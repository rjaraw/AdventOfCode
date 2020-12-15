day15_input = '14,8,16,0,1,17'

spoken_nums = [int(x) for x in day15_input.split(',')]
n = 1

spoken_dict = {}

while n < 30000000:
    if n < len(spoken_nums):
        current_num = spoken_nums[n-1]
        spoken_dict[current_num] = n
    elif n == len(spoken_nums):
        current_num = spoken_nums[n-1]
    if n >= len(spoken_nums):
        if current_num in spoken_dict:
            previous_num = current_num
            current_num = n - spoken_dict[current_num]
            spoken_dict[previous_num] = n
        else:
            spoken_dict[current_num] = n
            current_num = 0
    n += 1

print('{}: {}'.format(n, current_num))
