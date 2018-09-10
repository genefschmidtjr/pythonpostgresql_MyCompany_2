from dataclasses import dataclass
@dataclass
class ProductDTO:
    '''Class for keeping track of an item in inventory.'''
    id: int
    name: str
    definition: str
    deleted: bool
    active: bool


