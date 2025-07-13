import random

def generator_lotto_numbers():
    numbers = list()    

    while len(numbers) < 6:
        number = random.randint(1,45)
        if number not in numbers:
            numbers.append(number)
    
    return numbers

def generator_lotto_numbers2():
    return random.sample(range(1,46),6) 


if __name__ == "__main__":
    for _ in range(5):
        # lotto_numbers = generator_lotto_numbers()
        lotto_numbers = generator_lotto_numbers2()
        print(sorted(lotto_numbers, reverse=True))