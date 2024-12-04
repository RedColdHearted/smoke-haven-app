from dataclasses import dataclass

@dataclass(frozen=True)
class NumericStat:
    count: int
    avg: float
    maximum: float
    minimum: float