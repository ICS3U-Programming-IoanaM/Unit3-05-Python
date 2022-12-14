#!/usr/bin/env python3
# Copyright (c) 2022 Ioana Marinescu All rights reserved.
# Created By: Ioana Marinescu
#
# Date: Oct. 14, 2022
# tells user what month is associated with a their chosen number from 1 - 12


def month_association(month):
    # checks what number is associated with which month and displays the month
    months = {
        1: "1 is January.",
        2: "2 is February.",
        3: "3 is March.",
        4: "4 is April.",
        5: "5 is May.",
        6: "6 is June.",
        7: "7 is July.",
        8: "8 is August.",
        9: "9 is September.",
        10: "10 is October.",
        11: "11 is November.",
        12: "12 is December.",
    }
    return months.get(month, "Error. {} does not represent a month.".format(month))


def main():
    # variables
    month_num = int(input("Enter in a number from 1 - 12: "))

    # prints out month association
    print(month_association(month_num))


if __name__ == "__main__":
    main()
