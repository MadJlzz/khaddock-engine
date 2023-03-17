from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class KhaddockBase:
    apiVersion: str
    kind: str
    metadata: KhaddockMetadata
    labels: dict[str, str]


@dataclasses.dataclass
class KhaddockMetadata:
    name: str
    namespace: str


@dataclasses.dataclass
class SailorBase(KhaddockBase):
    specs: SailorSpecs


@dataclasses.dataclass
class SailorSpecs:
    sysctl: dict[str, str | int]
