from cow.common.chains import SupportedChainId
from cow.common.constants import COW_PROTOCOL_SETTLEMENT_CONTRACT_ADDRESS


def hello():
    print(COW_PROTOCOL_SETTLEMENT_CONTRACT_ADDRESS[SupportedChainId.MAINNET])
