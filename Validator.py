# Validator interface
# 유효성 검사 인터페이스
from abc import ABC, abstractclassmethod

class Validator(ABC):
    def validate(self, expression):
        pass

# The Four Fundametal arithmetic Operation (기본 산술연산)
class FourFunction(Validator):
    def validate(self, expression):
        return super().validate(expression)

