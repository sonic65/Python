number_list = range(-5, 5)
less_than_zerg = filter(lambda x: x < 0, number_list)
print(list(less_than_zerg))