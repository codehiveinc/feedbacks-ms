class PaginationResponseEntity:
    def __init__(
        self, items: object, page_number: int, page_size: int, total_items: int
    ):
        self.items = items
        self.page_number = page_number
        self.page_size = page_size
        self.total_items = total_items

    def to_dict(self) -> dict:
        return {
            "items": [item.to_dict() for item in self.items],
            "page_number": self.page_number,
            "page_size": self.page_size,
            "total_items": self.total_items,
        }
