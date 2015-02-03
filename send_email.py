#!/usr/bin/env python
# -- coding: utf-8 --

"""
File:           send_email.py
Author:         Adeel Ahmad
Email:          adeelahmad84@me.com
Github:         https://github.com/adeelahmad84
Description:    srcipt to send email.
"""
import email_helper

def main():
    """TODO: Docstring for main.
    All script will be below this function.

    """
    recipient = 'aahmad@caci.co.uk'
    subject = 'test message'
    message = '''
    This is a fictional test message.

    Regards,

    Adeel
    '''

    sender = 'adeelahmad786@gmail.com'

    email_helper.send_mail(recipient, subject, message, sender)

if __name__ == '__main__':
    main()
