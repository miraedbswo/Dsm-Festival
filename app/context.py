from typing import Optional, Type

from pydantic import BaseModel


class _ContextProperty:
    _request_payload: Optional[BaseModel] = None

    @property
    def request_payload(self) -> Optional[BaseModel]:
        return self._request_payload

    @request_payload.setter
    def request_payload(self, value):
        self._request_payload = value


context_property = _ContextProperty()
