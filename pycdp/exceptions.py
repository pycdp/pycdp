from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from pycdp import Target


class PYCDPException(Exception):
    """
    Base exception class for all pycdp exceptions.
    """


class InvalidRPCResponse(PYCDPException):
    """
    Exception raised when an invalid rpc response is received.
    """


class NoTargetFound(PYCDPException):
    """
    Exception raised when no target is found.
    """


class NoTargetFoundMatchingCondition(NoTargetFound):
    """
    Exception raised when no target is found matching the given condition.
    """


def raise_invalid_rpc_response(rpc_response: dict):
    """
    Raises an InvalidRPCResponse exception.
    """
    raise InvalidRPCResponse(
        f'Invalid rpc response. '
        f'Response: {rpc_response}'
    )


def raise_no_target_found():
    """
    Raises a NoTargetFound exception.
    """
    raise NoTargetFound(
        f'No target found.'
    )


def raise_no_target_found_matching_condition(condition: Callable[[Target], bool]):
    """
    Raises a NoTargetFoundMatchingCondition exception.
    """
    raise NoTargetFoundMatchingCondition(
        f'No target found matching the given condition. Condition: {condition.__name__}'
    )
