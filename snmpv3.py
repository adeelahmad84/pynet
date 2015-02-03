#!/usr/bin/env python
# -- coding: utf-8 --

"""
File:           snmpv3.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    Testing script using SNMPv3.
"""

import snmp_helper

def main():
    """TODO: Docstring for main.
    All script will be below this function.

    """
    IP = '50.242.94.227'
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (IP, 7961)
    pynet_rtr2 = (IP, 8061)

    snmp_oids = (
            ('sysname', '1.3.6.1.2.1.1.5.0', None),
            ('sysUptime', '1.3.6.1.2.1.1.3.0', None),
            ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5', None),
            ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
            ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5', True),
            ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True),
            ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5', True),
        )

    for desc,an_oid,is_count in snmp_oids:
        snmp_data = snmp_helper.snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=an_oid)
        output = snmp_helper.snmp_extract(snmp_data)
        print "%s %s" % (desc, output)


if __name__ == '__main__':
    main()
