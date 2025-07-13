import random

def guess_number():
    random_number = random.randint(1,100)
    print(f"컴퓨터가 생성한 숫자는:{random_number}")
    guess_count = 0

    while True:
        guess_count += 1
        try:
            user_guess = int(input("1부터 100사이의 숫자를 입력하세요.:"))
        except ValueError:
            print("숫자를 입력하세요")
            continue

        print(user_guess)   
        if random_number > user_guess       :
            print("조금 더 큰 숫자를 입력하세요")
        elif random_number < user_guess:
            print("조금 더 작은 숫자를 입력하세요")
        else:
            print(f"정답입니다, {guess_count}번에 맞췄네요")
            break


if __name__ == "__main__":
    guess_number()