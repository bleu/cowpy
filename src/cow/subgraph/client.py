from cow.common.chains import Chain
from .queries import TOTALS_QUERY, LAST_DAYS_VOLUME_QUERY, LAST_HOURS_VOLUME_QUERY

import requests

SUBGRAPH_BASE_URL = "https://api.thegraph.com/subgraphs/name/cowprotocol"

SUBGRAPH_PROD_CONFIG = {
    Chain.MAINNET: SUBGRAPH_BASE_URL + "/cow",
    Chain.GNOSIS_CHAIN: SUBGRAPH_BASE_URL + "/cow-gc",
    Chain.SEPOLIA: None,
}

SUBGRAPH_STAGING_CONFIG = {
    Chain.MAINNET: SUBGRAPH_BASE_URL + "/cow-staging",
    Chain.GNOSIS_CHAIN: SUBGRAPH_BASE_URL + "/cow-gc-staging",
    Chain.SEPOLIA: None,
}


class SubgraphApi:
    """
    Subgraph API for CoW Protocol.
    """

    API_NAME = "CoW Protocol Subgraph"

    def __init__(self, chain: Chain):
        """
        Create a new CoW Protocol API instance.

        :param chain: The chain for which the subgraph API will be used.
        """
        self.chain = chain

    def getTotals(self) -> dict:
        """
        Query the totals from TheGraph for the CoW Protocol.

        :returns: The totals for the CoW Protocol.
        """
        return self.runQuery(TOTALS_QUERY)

    def getLastDaysVolume(self, days: int) -> dict:
        """
        Query the volume over the last N days from TheGraph for the CoW Protocol.

        :param days: The number of days to query.
        :returns: The volume for the last N days.
        """
        return self.runQuery(LAST_DAYS_VOLUME_QUERY, {"days": days})

    def getLastHoursVolume(self, hours: int) -> dict:
        """
        Query the volume over the last N hours from TheGraph for the CoW Protocol.

        :param hours: The number of hours to query.
        :returns: The volume for the last N hours.
        """
        return self.runQuery(LAST_HOURS_VOLUME_QUERY, {"hours": hours})

    def runQuery(self, query: str, variables: dict = None) -> dict:
        """
        Run a query against the CoW Protocol Subgraph.

        :param query: GQL query string.
        :param variables: To be passed to the query.
        :returns: Results of the query.
        :raises ValueError: if the URL for the chain is not configured.
        """
        subgraphURL = SUBGRAPH_PROD_CONFIG.get(self.chain)

        if subgraphURL is None:
            raise ValueError(
                "Unsupported Network. The subgraph API is not available for the selected chain."
            )

        try:
            response = requests.post(
                subgraphURL, json={"query": query, "variables": variables}
            )
            response.raise_for_status()
            return response.json()
        except Exception as error:
            print(f"[subgraph:{self.API_NAME}]", error)
            raise ValueError(
                f"Error running query: {query}. Variables: {variables}. API: {subgraphURL}. Inner Error: {error}"
            )
