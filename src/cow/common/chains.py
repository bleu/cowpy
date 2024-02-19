from enum import Enum


class Chain(Enum):
    """
    Supported chains and their respective `chainId` for the SDK.
    """

    MAINNET = 1
    GNOSIS_CHAIN = 100
    SEPOLIA = 11155111
