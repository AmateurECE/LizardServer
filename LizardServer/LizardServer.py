#!/usr/bin/env python3
###############################################################################
# NAME:             LizardServer.py
#
# AUTHOR:           Ethan D. Twardy <edtwardy@mtu.edu>
#
# DESCRIPTION:      Contains the main method for the Lizard Server application
#
# CREATED:          01/24/2019
#
# LAST EDITED:      02/09/2019
###

###############################################################################
# IMPORTS
###

import firebase_admin
from firebase_admin import credentials

import DownstreamMessaging
# See `ServiceAccountKey.py-Format.md'
from ServiceAccountKey import ServiceAccountKey

###############################################################################
# MAIN
###

def main():
    # This module is not under version control to protect the integrity of my
    # private account key. This module must be generated by the user per the
    # specifications in `ServiceAccountKey.py-Format.md' in order for the
    # server application to function correctly.
    keyLocation = ServiceAccountKey.getPath()
    cred = credentials.Certificate(keyLocation)
    firebase_admin.initialize_app(cred)

    # Read in the registration token
    with open('device.token', 'r') as tokenFile:
        messenger = DownstreamMessaging.Messenger(tokenFile.readline()[:-1])
        code = messenger.sendMessage('title', 'body')
        print('Return code: {}'.format(code))

if __name__ == '__main__':
    main()

##############################################################################