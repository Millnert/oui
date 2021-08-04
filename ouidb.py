#!/usr/bin/python3
""" Class to lookup mac-address vendors """

import re

# pylint: disable=too-few-public-methods

class OUIDB(object):
    """OUI Database Lookup"""
    OUIDB = "oui.txt"
    LOOKUP_VALIDATE_RE = re.compile('^[A-F0-9]{6}$')
    ouidb = {}

    def __init__(self):
        """Initialize the class"""
        self.__parse_ouidb(self.OUIDB)

    def __parse_ouidb(self, ouidb):
        """Parse the oui db into dictionary"""
        fhd = open(ouidb)
        re_m = re.compile('^([A-F0-9]{6}).*\t\t(.*)$')
        for line in fhd.readlines():
            match = re_m.match(line)
            if match is not None:
                self.ouidb[match.groups()[0]] = match.groups()[1]
        fhd.close()

    def lookup(self, mac_addr):
        """Normalize mac_addr to first 6 hex characters, then search in db.
        Returns False if input is not a valid MAC address.
        Returns Vendor string if OUI is in database, or None if it is not."""
        norm_mac_upper = mac_addr.replace(':', '').replace('-', '').replace('.', '').upper()
        lookup_mac = norm_mac_upper[:6]
        if self.LOOKUP_VALIDATE_RE.match(lookup_mac) is None:
            return False
        return self.ouidb.get(lookup_mac)
