from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    name: str
    serial_number: str
    make: str
    model: str
