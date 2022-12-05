#01 Fruit Energy for the elves
forest = open('C:/Projects/Python/Codecember/01/Elves_energy_input.py', 'r')
each_fruit = [pick.strip() for pick in forest.readlines()]

#Baskets
fruit_basket = []
energy_in_basket = []

#Lets see who has most Fruit Energy
for fruit in each_fruit:
    if fruit== "":
        energy_in_fruit = 0
        for fruit_type in range(0, len(fruit_basket)):
            energy_in_fruit = energy_in_fruit + fruit_basket[fruit_type]
        energy_in_basket.append(energy_in_fruit)
        fruit_basket.clear()
    else:
        fruit_basket.append(int(fruit))
        
print("Most amount of Fruit Energy is " + str(max(energy_in_basket)))
energy_in_basket.sort(reverse=True)
print("Most amount of Fruit Energy in top three is " + str(sum(energy_in_basket[0:3])))
