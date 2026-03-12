def is_valid_domino_chain(dominoes):
    prev_tile = dominoes[0]
    result = True
    for i in range(1,len(dominoes)):
        if prev_tile[1] == dominoes[i][0]:
            prev_tile = dominoes[i]
        else: return False

    return result

if __name__ == '__main__':
    print(is_valid_domino_chain([[1, 3], [3, 6], [6, 5]]))
    print('------')
    print(is_valid_domino_chain([[6, 2], [3, 4], [4, 1]]))
    print('------')
    print(is_valid_domino_chain([[2, 5], [5, 6], [5, 1]]))
    print('------')
    print(is_valid_domino_chain([[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]]))
    print('------')
    print(is_valid_domino_chain([[2, 3], [3, 3], [3, 6], [6, 1], [1, 4], [3, 5], [5, 5], [5, 4], [4, 2], [2, 2]]))