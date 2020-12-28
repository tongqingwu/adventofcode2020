import math

DATE = 20201227


def find_loop_by_key_with_subject_and_2020(key, subject):
    remainder = 1
    cnt = 0
    while remainder != key:
        remainder = (remainder * subject) % DATE
        cnt += 1

    print('find loop {}'.format(cnt))

    return cnt


def get_key(subject, loop):
    key = 1
    for i in range(loop):
        key = (key * subject) % DATE

    return key


def main():
    subject = 7

    key = get_key(subject, 8)
    print(key)

    # card_key = 5764801
    # door_key = 17807724

    card_key = 14681524
    door_key = 8987316

    card_loop = find_loop_by_key_with_subject_and_2020(card_key, subject)
    door_loop = find_loop_by_key_with_subject_and_2020(door_key, subject)

    card_new_key = get_key(door_key, card_loop)
    door_new_key = get_key(card_key, door_loop)

    print(card_new_key)
    print(door_new_key)


if __name__ == '__main__':
    main()
