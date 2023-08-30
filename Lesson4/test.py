import collections

"""list_of_letters = list('абракадабра')
letter_cnt = collections.Counter(list_of_letters)
print(letter_cnt)

emotion_cnt = collections.Counter({'like':2, 'dislike':3})
print(emotion_cnt)

list_of_letters = list('абракадабра')
letter_cnt = collections.Counter(list_of_letters)
print(letter_cnt)
print(letter_cnt.values())

lst = [9, 1, 1, 4, 9]
print(lst)
deq = collections.deque(lst)
for _ in range(0, len(lst)):
    deq.rotate(-1)
    print(sum(list(deq)[:3:]))"""

in_lst_a = [5, 2, 4, 20, 4, 7, 1, 1, 4]
in_lst_b = [4, 1, 24, 20, 8, 4, 1, 1, 4, 4, 4]
print(collections.Counter(in_lst_a))
print(collections.Counter(in_lst_b))
print(list(collections.Counter(in_lst_a).elements()))
print(list(collections.Counter(in_lst_b).elements()))
common_items = list((collections.Counter(in_lst_a) & collections.Counter(in_lst_b)).elements())
print(common_items)