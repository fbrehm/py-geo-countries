#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: © 2015 by Frank Brehm, Berlin
@summary: 2-letter, 3-letter, and numerical codes for countries.
"""

# Standard modules

__author__ = 'Frank Brehm <frank@brehm-online.com>'
__copyright__ = '(C) 2015 by Frank Brehm, Berlin'
__contact__ = 'frank@brehm-online.com'
__version__ = '0.1.0'
__license__ = 'LGPLv3+'

# Global variables

CNT_I_CODE2 = 0
CNT_I_CODE3 = 1
CNT_I_NUMCODE = 2
CNT_I_COUNTRY = 3
CNT_I_FLAG = 4

CNT_F_REGULAR = 0x01
CNT_F_OLD = 0x02
CNT_F_REGION = 0x04
CNT_F_ANY = CNT_F_REGULAR | CNT_F_OLD | CNT_F_REGION


# =============================================================================
class Country(object):
    """
    Class for data of a country.
    """

    # -------------------------------------------------------------------------
    def __init__(
        self, name, two_letter=None, three_letter=None,
            numcode=None, flag=CNT_F_REGULAR):

        self._name = name.strip()
        self._two_letter = two_letter
        self._three_letter = three_letter
        self._numcode = None
        if numcode is not None:
            self._numcode = int(numcode)
        self._flag = flag

    # -------------------------------------------------------------------------
    @property
    def name(self):
        """The literal country name in English language"""
        return self._name

    # -------------------------------------------------------------------------
    @property
    def two_letter(self):
        """The 2-letter code of the country."""
        return self._two_letter

    # -------------------------------------------------------------------------
    @property
    def three_letter(self):
        """The 3-letter code of the country."""
        return self._three_letter

    # -------------------------------------------------------------------------
    @property
    def numcode(self):
        """The numeric code of the country."""
        return self._numcode

    # -------------------------------------------------------------------------
    @property
    def flag(self):
        """A flag describing the type of country."""
        return self._flag


# =============================================================================
def country_codes(key, flag=CNT_F_REGULAR):
    pass


# =============================================================================
def country(key, flag=CNT_F_REGULAR):

    cdata = country_codes(key, flag)
    if cdata is None:
        return None
    return cdata.country


# =============================================================================

if __name__ == "__main__":

    pass

# =============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
