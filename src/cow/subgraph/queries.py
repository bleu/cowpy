TOTALS_QUERY = """
  query Totals {
    totals {
      tokens
      orders
      traders
      settlements
      volumeUsd
      volumeEth
      feesUsd
      feesEth
    }
  }
"""
""" GraphQL query for the total number of tokens, orders, traders, settlements, volume, and fees. """

LAST_DAYS_VOLUME_QUERY = """
  query LastDaysVolume($days: Int!) {
    dailyTotals(orderBy: timestamp, orderDirection: desc, first: $days) {
      timestamp
      volumeUsd
    }
  }
"""
""" GraphQL query for the total volume over the last N days. """

LAST_HOURS_VOLUME_QUERY = """
  query LastHoursVolume($hours: Int!) {
    hourlyTotals(orderBy: timestamp, orderDirection: desc, first: $hours) {
      timestamp
      volumeUsd
    }
  }
"""
""" GraphQL query for the total volume over the last N hours. """
