#!/usr/bin/env python

# written for python 3

"""
code for working on the general circle problem
"""

import sys

import click


def init_naive_array(n):
    """ return a list that is n long
    """
    result = list()
    for i in range(1, n+1):
        result.append(i)
    return result


def reduce_circle(circle, k, current_step):
    """ cycle around the circle

    steps go from 1 to k.

    Return:
        reduced list: list
        current step: int
    """
    circle_reduced = circle
    pop_indexes = list()

    for index, value in enumerate(circle):
        step = (current_step + index) % k
        if step == 0:
            pop_indexes.append(index)

    current_step = step + 1
    pop_indexes.reverse()

    for index in pop_indexes:
        circle_reduced.pop(index)

    return circle_reduced, current_step


@click.command()
@click.argument('kill_count')
@click.argument('number_in_circle')
def main(kill_count, number_in_circle):
    """ run program interactively
    """
    k = int(kill_count)
    n = int(number_in_circle)
    step = 1

    the_circle = init_naive_array(n)
    # print("initial circle: {}".format(the_circle))

    while len(the_circle) > 1:
        the_circle, step = reduce_circle(the_circle, k, step)
        # print("the_reduced_circle: {}".format(the_circle))
        # print("current step: {}".format(step))

    print(the_circle[0])


if __name__ == "__main__":
    sys.exit(main())
