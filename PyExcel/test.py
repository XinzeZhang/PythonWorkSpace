# -*- coding: UTF-8 -*-

"""
this is a  test.py for dealing excel
"""

import pyexcel as pe


def test():
    """
    try to deal excel
    """

    '''
    records = pe.get_records(file_name="PyExcel\\target.xlsx")

    for record in records:
        print("%s %d"%(record['ID'], record['Grade']))
    '''

    arraysteam = pe.get_array(file_name="PyExcel\\teamwork.xlsx")
    arraystarget = pe.get_array(file_name="PyExcel\\target.xlsx")

    # for array0 in arraysteam:
    #     for arrayunit in arraystarget:
    #         if(array0[1] == arrayunit[1]):
    #             arrayunit.append(array0[3])
    #             array0.append('Done')
    #             break

    for array0 in arraysteam:
        print(array0)
    print()
    print("----------------")
    print()
    for arrayunit in arraystarget:
        print(arrayunit)

    # pe.save_as(array=arraysteam, dest_file_name="PyExcel\\teamwork1.xlsx")
    # pe.save_as(array=arraystarget, dest_file_name="PyExcel\\combine.xlsx")


test()
