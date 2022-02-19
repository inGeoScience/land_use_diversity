import func_calculate_Entropy


user_choice = 'user_choice'
while not user_choice.isnumeric():
    user_choice = input('1.计算归一化熵 2.计算香农熵 3.敬请期待')
user_choice = int(user_choice)
if user_choice == 1:
    func_calculate_shannon = func_calculate_Entropy.calculateNormalizedEntropy()
    rows_list = func_calculate_shannon.get_data()
    entropy_list = func_calculate_shannon.calculate_shannon_entropy(rows_list)
    func_calculate_shannon.save_excel(entropy_list)
elif user_choice == 2:
    pass
else:
    print('输入错误')