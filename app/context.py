from typing import Optional, Type

from pydantic import BaseModel


class _ContextProperty:
    _request_payload: Optional[BaseModel] = None

    @property
    def request_payload(self) -> Optional[BaseModel]:
        return self.request_payload.get()

    @request_payload.setter
    def request_payload(self, value: Type[BaseModel]):
        self.request_payload.set(value)


context_property = _ContextProperty()
