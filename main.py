import func_calculate_diversity


func_base = func_calculate_diversity.baseFunction()
func_calculate_diversity = func_calculate_diversity.calculateDiversity()
user_choice = 'user_choice'
while not user_choice.isnumeric():
    user_choice = input('1.计算归一化熵 2.计算香农熵 3.敬请期待')
user_choice = int(user_choice)
if user_choice == 1:
    rows_list = func_base.get_data()
    entropy_list = func_calculate_diversity.calculate_normalized_entropy(rows_list)
    func_base.save_excel(entropy_list, 'normalized_entropy')
elif user_choice == 2:
    rows_list = func_base.get_data()
    entropy_list = func_calculate_diversity.calculate_shannon_entropy(rows_list)
    func_base.save_excel(entropy_list, 'shannon_entropy')
else:
    print('输入错误')