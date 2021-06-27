def BruteForce(A, B, left_index, right_index):
    global SUCCESS  # 全局状态，表示是否有解
    global SUM  # 线段总长度
    global R  # 结果数组
    B_prime = B[:]
    dis = 0  # 与已放置的线段的长度差
    left_status = False  # 线段放置在左侧是否可行
    right_status = False  # 线段放置在右侧是否可行

    # 判断最终是否成功
    if (len(B) == 1 or len(B) == 2) and len(A) == 0:
        for r in range(left_index, right_index):
            R[r] = B[0]
        SUCCESS = True
        return True

    # 当前需要放置的线段长度
    current_num = A[0]

    # 放左边
    if left_index != 0:
        dis = current_num - left_index
    else:
        dis = current_num
    if dis in B_prime:
        B_prime.remove(dis)
        left_status = BruteForce(A[1:], B_prime, left_index + dis, right_index)
        if left_status and SUCCESS:
            for r in range(left_index, left_index + dis):
                R[r] = dis

    # 如果左边不成功，再放右边
    if not left_status:
        if right_index != SUM:
            dis = current_num - (SUM - right_index)
        else:
            dis = current_num
        if dis in B:
            B.remove(dis)
            right_status = BruteForce(A[1:], B, left_index, right_index - dis)
            if right_status and SUCCESS:
                for r in range(right_index - dis, right_index):
                    R[r] = dis

    # 左边或者右边，有一侧可以放置则成功
    return left_status or right_status


if __name__ == '__main__':
    A = [2, 14, 8, 8, 9, 7, 13, 3]
    B = [2, 1, 4, 3, 6]
    # A = [1, 14, 12, 3, 7, 8, 9, 6, 11, 4, 12, 3, 13, 2, 5, 10]
    # B = [1, 1, 2, 1, 2, 2, 1, 2, 3]
    SUCCESS = False
    SUM = 0
    for num in B:
        SUM += num
    R = [0] * SUM
    A.sort()
    BruteForce(A[:len(A) // 2], B, 0, SUM)

    res = []
    for r in R:
        if r in B:
            B.remove(r)
            res.append(r)
    print("顺序为：" + str(res))
