# -*- coding: utf-8 -*-

###########################################################################
#    Copyright (C) 2003 by Wido Depping
#    <wido.depping@tu-clausthal.de>
#
# Copyright: See COPYING file that comes with this distribution
#
###########################################################################

from qt import *

class DateHelper(object):
    """A class for doing some date calculations.
    """
    unixBirth = None

###############################################################################

    def __init__(self):
        # setting the date for the birth of unix
        self.unixBirth = QDate (1970, 1, 1)
        
###############################################################################

    def is_valid_date (self, year=1970, month=1, day=1):
        """Test  if a given date is valid. Default date is the birth of unix.
        
        If the date is valid 1 is returned, else 0.
        """
        dummyDate = QDate (year, month, day)
        if dummyDate.isValid ():
            return 1
        else:
            return 0
            
###############################################################################

    def date_to_unix (self, year, month, day):
        """ Calculates the days since the birth of unix until the given date.
        
        The result is an integer. If the given date is not valid, return None.
        """
        
        if self.is_valid_date (year, month, day):
            tmpDate = QDate (year, month, day)
            diff = self.unixBirth.daysTo (tmpDate)
            return diff
            
        
###############################################################################

    def dateduration_to_unix (self, days):
        """Converts the current date plus 'days' into an integer which represents the days since 
        the birth of unix. 
        """
    
        curDate = QDate ()
        tmpDays = self.unixBirth.daysTo (curDate.currentDate ())
        return tmpDays + days
