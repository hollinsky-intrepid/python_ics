# This file was auto generated; Do not modify, if you value your sanity!
import ctypes

class serdescam_settings(ctypes.Structure):
    _pack_ = 2
    _fields_ = [
        ('flags', ctypes.c_uint32), 
        ('mode', ctypes.c_uint8), 
        ('rsvd1', ctypes.c_uint8), 
        ('bitPos', ctypes.c_uint8), 
        ('videoFormat', ctypes.c_uint8), 
        ('resWidth', ctypes.c_uint16), 
        ('resHeight', ctypes.c_uint16), 
        ('frameSkip', ctypes.c_uint8), 
        ('rsvd2', ctypes.c_uint8 * 19), 
    ]

# Extra names go here:
SERDESCAM_SETTINGS = serdescam_settings
# End of extra names

