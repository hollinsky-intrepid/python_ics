# This file was auto generated; Do not modify, if you value your sanity!
import ctypes

# flags
class flags(ctypes.Structure):
    _pack_ = 2
    _fields_ = [
        ('bTapEnSwitch', ctypes.c_uint32, 1), # [Bitfield] 
        ('bTapEnPtp', ctypes.c_uint32, 1), # [Bitfield] 
        ('bEnReportLinkQuality', ctypes.c_uint32, 1), # [Bitfield] 
    ]

# Extra names go here:
# End of extra names

# _U1
class _U1(ctypes.Union):
    _pack_ = 2
    _fields_ = [
        ('flags', flags), 
        ('uFlags', ctypes.c_uint32), 
    ]

# Extra names go here:
# End of extra names

class op_eth_general_settings(ctypes.Structure):
    _pack_ = 2
    _anonymous_ = ("_U1",)
    _fields_ = [
        ('ucInterfaceType', ctypes.c_uint8), 
        ('reserved0', ctypes.c_uint8 * 3), 
        ('tapPair0', ctypes.c_uint16), 
        ('tapPair1', ctypes.c_uint16), 
        ('tapPair2', ctypes.c_uint16), 
        ('tapPair3', ctypes.c_uint16), 
        ('tapPair4', ctypes.c_uint16), 
        ('tapPair5', ctypes.c_uint16), 
        ('_U1', _U1), 
    ]

# Extra names go here:
OP_ETH_GENERAL_SETTINGS = op_eth_general_settings
# End of extra names

