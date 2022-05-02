import abc
from typing import Set

from schedule.adapters import orm
from schedule.domain import model


class AbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()  # type: Set[model.Order]

    def add(self, order: model.Order):
        self._add(order)
        self.seen.add(order)

    def get(self, order_number) -> model.Order:
        order = self._get(order_number)
        if order:
            self.seen.add(order)
        return order

    @abc.abstractmethod
    def _add(self, order: model.Order):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, order_number) -> model.Order:
        raise NotImplementedError
