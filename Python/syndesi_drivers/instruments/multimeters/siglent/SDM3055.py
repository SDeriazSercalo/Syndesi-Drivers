from .. import IAmmeter, IVoltmeter
from syndesi.adapters import IAdapter, IP, VISA
from ....protocols import SCPI

# https://int.siglent.com/upload_file/user/SDM3055/SDM3055_RemoteManual_RC06035-E01A.pdf

class SDM3055(IVoltmeter, IAmmeter):
    def __init__(self, adapter : IAdapter) -> None:
        """
        Siglent SDM3055 5½ digit multimeter

        Parameters
        ----------
        adpater : IAdapter
            Adapter to use, both IP and VISA are allowed
        """
        super().__init__()

        assert isinstance(adapter, IP) or isinstance(adapter, VISA), "Invalid adapter"
        self._prot = SCPI(adapter)


    def measureDC(self) -> float:
        """
        Make a DC voltage measurement
        """
        self._prot.write(b'CONF:DC')
        self._prot.write(b'INIT')
        self._prot.write(b'*TRG')
        output = float(self._prot.query(b'FETC?'))
        return output
    
    def measureAC(self) -> float:
        """
        Make an AC voltage measurement
        """
        self._prot.write(b'CONF:AC')
        self._prot.write(b'INIT')
        self._prot.write(b'*TRG')
        output = float(self._prot.query(b'FETC?'))
        return output