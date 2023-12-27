from threading import Thread


def printer(func):
    def inner(*args, **kwargs):
        print(func(*args, **kwargs))
        return func(*args, **kwargs)

    return inner


@printer
def reversed_nums(ns: list):
    # l2 = []
    # for i in ns:
    #     l2.append(i)
    # l2.reverse()
    ns.reverse()
    return ns


if __name__ == '__main__':
    nums = list(map(int, input('Enter nums: ').split()))
    # print(nums)
    # print(renums(nums))
    t = Thread(target=reversed_nums, args=(nums, ))
    t.start()
    t.join()

