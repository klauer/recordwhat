from ..record_base import RecordBase

# from .aai import AaiRecord
# from .aao import AaoRecord
# from .acalcout import AcalcoutRecord
# from .ai import AiRecord
# from .ao import AoRecord
# from .asub import AsubRecord
# from .asyn import AsynRecord
# from .bi import BiRecord
# from .bo import BoRecord
# from .busy import BusyRecord
# from .calcout import CalcoutRecord
# from .calc import CalcRecord
# from .compress import CompressRecord
# from .dfanout import DfanoutRecord
# from .digitel import DigitelRecord
# from .epid import EpidRecord
# from .event import EventRecord
# from .fanout import FanoutRecord
# from .histogram import HistogramRecord
# from .longin import LonginRecord
# from .longout import LongoutRecord
# from .mbbiDirect import MbbidirectRecord
# from .mbbi import MbbiRecord
# from .mbboDirect import MbbodirectRecord
# from .mbbo import MbboRecord
# from .mca import McaRecord
# from .motor import MotorRecord
# from .permissive import PermissiveRecord
# from .scalcout import ScalcoutRecord
# from .scaler import ScalerRecord
# from .scanparm import ScanparmRecord
# from .sel import SelRecord
# from .seq import SeqRecord
# from .sscan import SscanRecord
# from .sseq import SseqRecord
# from .state import StateRecord
# from .stringin import StringinRecord
# from .stringout import StringoutRecord
# from .subArray import SubarrayRecord
# from .sub import SubRecord
# from .swait import SwaitRecord
# from .table import TableRecord
# from .timestamp import TimestampRecord
# from .transform import TransformRecord
# from .vme import VmeRecord
# from .vs import VsRecord
# from .waveform import WaveformRecord
#
#
# _record_classes = {}
#
#
# def _register(cls):
#     global _record_classes
#
#     _record_classes[cls._rtyp] = cls
#
#
# def record_class(rtyp):
#     try:
#         return _record_classes[rtyp]
#     except KeyError:
#         raise ValueError('Unrecognized record type: {}'.format(rtyp))
#
#
# _register(AaiRecord)
# _register(AaoRecord)
# _register(AcalcoutRecord)
# _register(AiRecord)
# _register(AoRecord)
# _register(AsubRecord)
# _register(AsynRecord)
# _register(BiRecord)
# _register(BoRecord)
# _register(BusyRecord)
# _register(CalcoutRecord)
# _register(CalcRecord)
# _register(CompressRecord)
# _register(DfanoutRecord)
# _register(DigitelRecord)
# _register(EpidRecord)
# _register(EventRecord)
# _register(FanoutRecord)
# _register(HistogramRecord)
# _register(LonginRecord)
# _register(LongoutRecord)
# _register(MbbidirectRecord)
# _register(MbbiRecord)
# _register(MbbodirectRecord)
# _register(MbboRecord)
# _register(McaRecord)
# _register(MotorRecord)
# _register(PermissiveRecord)
# _register(ScalcoutRecord)
# _register(ScalerRecord)
# _register(ScanparmRecord)
# _register(SelRecord)
# _register(SeqRecord)
# _register(SscanRecord)
# _register(SseqRecord)
# _register(StateRecord)
# _register(StringinRecord)
# _register(StringoutRecord)
# _register(SubarrayRecord)
# _register(SubRecord)
# _register(SwaitRecord)
# _register(TableRecord)
# _register(TimestampRecord)
# _register(TransformRecord)
# _register(VmeRecord)
# _register(VsRecord)
# _register(WaveformRecord)
