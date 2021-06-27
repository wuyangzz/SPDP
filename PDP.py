import math
import sys


def practical_pdp(L, n):
    max_element, solution = max(L), []
    solution.append(0)

    # while L is not empty
    while L:

        # gets the maximum distance of L
        max_dist = max(L)

        x1, x2 = max_element - max_dist, max_dist
        x1_chosen, x2_chosen = True, True
        diff_dists_x1, diff_dists_x2 = [], []

        # checks if x1 is a valid choice
        for e in solution:
            dist = abs(e - x1)
            diff_dists_x1.append(dist)
            if dist not in L:
                x1_chosen = False
                break

        # if x1 not is a valid choice
        if not x1_chosen:
            # checks if x2 is a valid choice
            for e in solution:
                dist = abs(e - x2)
                diff_dists_x2.append(dist)
                if dist not in L:
                    x2_chosen = False
                    break

        # checks the choices
        if not x1_chosen and not x2_chosen:
            return None
        else:
            if x1_chosen:
                solution.append(x1)  # add solution
                for dist in diff_dists_x1:  # removes the distances
                    L.remove(dist)
            else:
                solution.append(x2)  # add solution
                for dist in diff_dists_x2:  # removes the distances
                    L.remove(dist)

    solution.sort()  # sort numbers
    return solution  # return the solution


if __name__ == "__main__":

    len_params, L = len(sys.argv), []

    for i in range(1, len_params):
        L.append(int(sys.argv[i]))

    len_L = len(L)

    # |D| = (n * (n-1)) / 2
    # n^2 - n - 2 * len_l = 0
    # n = (1 + sqrt(1 + 8 * len_l)) / 2
    delta = math.sqrt(1 + 8 * len_L)
    n = (1 + delta) / 2

    solution = practical_pdp(L, int(n))
    if solution:
        print(' '.join(str(e) for e in solution))
    else:
        print('No solution')
