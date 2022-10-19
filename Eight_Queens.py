import random
import time


def main():
    total_switch= 0
    total_restart= 0
    print("Node\t\t\t\t\t   Restart Counts\tSwitch Counts\t Time")
    print("------------------------   ---------------\t-------------\t ----")
    total_start = time.time()
    for i in range(15):
        start = time.time()
        a = [0, 0, 0, 0, 0, 0, 0, 0]
        h = 9999
        restart_counter = -1
        switch_counter = 0

        while h != 0:
            restart_counter += 1
            testt, switch_counter = hill_climbing(a, switch_counter)
            h = value(testt)
        stop = time.time()

        total_switch += switch_counter
        total_restart += restart_counter
        print(testt, " " ,restart_counter, "\t\t\t   " , switch_counter, "\t\t\t\t" , ("{:.6f}".format(stop-start)))
    total_stop = time.time()
    print("--------------------------------------------------------------------------------------------------")
    print("Averages:", "\t\t\t\t  ", "{:.2f}".format(total_restart/15), "\t\t\t", "{:.2f}".format(total_switch/15),"\t\t\t", "{:.2f}".format((total_stop-total_start)/15))


def random_node(node):  # create random node case
    for i in range(8):
        node[i] = random.randint(1, 8)  # list indexes represent rows random values represent columns
    return node


def hill_climbing(node, switch_counter):
    # run h_ca
    main_node = random_node(node)
    while (True):
        flag = is_it_global_min(main_node)
        if (flag):
            return main_node, switch_counter
        successors = generate_successors(main_node)
        best_index, best_value = selectbestnode(successors)
        current_value = value(main_node)
        if (best_value >= current_value):
            return main_node, switch_counter

        main_node[best_index // 8] = (best_index % 8) + 1
        switch_counter += 1


def is_it_global_min(node):  # check is the node global min
    if value(node) == 0:
        return True
    return False


def generate_successors(node):  # create all neighbor cases
    successors = [0] * 64

    for i in range(64):

        mod = i % 8
        result = i // 8
        if mod == 0:
            temp = node.copy()
            its_self = node[result]

        temp[result] = mod + 1
        if mod + 1 != its_self:  # if node itself value is max so that means insignificant case
            successors[i] = value(temp)
        else:
            successors[i] = 9999
    return successors


def selectbestnode(successors):  # return best node index and best node's h value
    best_node = successors[0]
    best_index = 0
    rand_list = []
    for i in range(len(successors)):
        if successors[i] < best_node:
            best_node = successors[i]

    for i in range(len(successors)):
        if successors[i] == best_node:
            rand_list.append(i)
    best_index = random.choice(rand_list)
    best_node = successors[best_index]
    return best_index, best_node


def value(node):  # calculate h value for node
    h = 0
    for i in range(8):
        k = i + 1
        for l in range(7 - i):
            if (abs(i - k) == abs(node[i] - node[k])) or (node[i] == node[k]):
                h += 1
            k += 1
    return h


main()
