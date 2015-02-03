#!/usr/bin/env python
# -- coding: utf-8 --

"""
File:           snmp_chart.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    Scripts using pygal.
"""

import pygal
import time

def main():
    """TODO: Docstring for main.
    All script will be below this function.

    """

    # SNMPv3 Connection Parameters
    IP = '1.1.1.1'
    a_user = 'username'
    auth_key = '*********'
    encrypt_key = '**********'
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (IP, 7961)

    # Relevant SNMP OIDs
    in_octets = '1.3.6.1.2.1.2.2.1.10.5'
    out_octets = '1.3.6.1.2.1.2.2.1.16.5'

    # Empty lists to be populated.
    fa4_in_octets = []
    fa4_out_octets = []


    #obtain interface octets
    snmp_data = snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=in_octets)
    fa4_in_octets.append(snmp_extract(snmp_data))

    snmp_data = snmp_get_oid_v3(pynet_rtr1, snmp_user, oid=out_octets)
    fa4_out_octets.append(snmp_extract(snmp_data))

    line_chart = pygal.Line()

    line_chart.title = 'Input/Output Octets'
    line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
    line_chart.add('InBytes', fa4_out_octets)
    line_chart.add('OutBytes', fa4_in_octets)

    line_chart.render_to_file('test.svg')

if __name__ == '__main__':
    main()
