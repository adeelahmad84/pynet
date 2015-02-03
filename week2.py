#!/usr/bin/env python
# -- coding: utf-8 --

"""
File:           snmpv3.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    Testing script using SNMPv3.
"""

from snmp_helper import snmp_get_oid_v3, snmp_extract
import running_cfg_change as run
from email_helper import send_mail as send

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
            ('RunningLastChanged', '1.3.6.1.4.1.9.9.43.1.1.1.0', None),
            ('RunningLastSaved', '1.3.6.1.4.1.9.9.43.1.1.2.0', None),
        )

    bin=[]

    for desc,an_oid,is_count in snmp_oids:
        snmp_data = snmp_get_oid_v3(pynet_rtr2, snmp_user, oid=an_oid[1])
        bin.append(int(snmp_extract(snmp_data)))

    # Determine whether run-start are in sync
    run_save_status = run.determine_run_start_sync_state(bin[0], bin[1])

    if not run_save_status:
       recipient = 'aahmad@caci.co.uk'
       subject = 'Alert: Running-cfg has been changed'
       message = '''
       This is a message to alert you that the running configuration has been changed and not saved.

       Regards

       Team Pynet
       '''

       sender = 'adeelahmad786@gmail.com'

       send(recipient, subject, message, sender)

if __name__ == '__main__':
    main()
