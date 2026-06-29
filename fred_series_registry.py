"""Central registry for FRED series expected in canonical prices_long."""

from dataclasses import dataclass


FREQUENCY_DAILY = "daily"
FREQUENCY_WEEKLY = "weekly"
FREQUENCY_MONTHLY = "monthly"
FREQUENCY_QUARTERLY = "quarterly"

FRED_FREQUENCY_LAG_DAYS = {
    FREQUENCY_WEEKLY: 14,
    FREQUENCY_MONTHLY: 75,
    # FRED quarterly observations are dated at quarter start, while GDP is
    # released late in the following quarter. A 210-day lag avoids false stale
    # flags between the Q1 and Q2 GDP releases.
    FREQUENCY_QUARTERLY: 210,
}


@dataclass(frozen=True)
class FredSeries:
    code: str
    name: str
    category: str
    frequency: str
    update_group: str
    active: bool = True
    required: bool = False
    table: str = "prices_long"
    allowed_lag_days: int | None = None


FRED_SERIES_REGISTRY = {
    "DGS2": FredSeries("DGS2", "2-Year Treasury", "treasury_yields", FREQUENCY_DAILY, "wide", required=True),
    "DGS5": FredSeries("DGS5", "5-Year Treasury", "treasury_yields", FREQUENCY_DAILY, "narrow", required=True),
    "DGS10": FredSeries("DGS10", "10-Year Treasury", "treasury_yields", FREQUENCY_DAILY, "wide", required=True),
    "DGS30": FredSeries("DGS30", "30-Year Treasury", "treasury_yields", FREQUENCY_DAILY, "wide", required=True),
    "T10Y2Y": FredSeries("T10Y2Y", "10Y-2Y Spread", "treasury_yields", FREQUENCY_DAILY, "wide", required=True),
    "DFII5": FredSeries("DFII5", "5-Year TIPS Real Yield", "treasury_yields", FREQUENCY_DAILY, "narrow", required=True),
    "DFII10": FredSeries("DFII10", "10-Year TIPS Real Yield", "treasury_yields", FREQUENCY_DAILY, "narrow", required=True),
    "DFII30": FredSeries("DFII30", "30-Year TIPS Real Yield", "treasury_yields", FREQUENCY_DAILY, "narrow", required=True),
    "THREEFYTP10": FredSeries("THREEFYTP10", "10Y Term Premium (Kim-Wright)", "term_premium", FREQUENCY_DAILY, "tier2", allowed_lag_days=21),
    "FEDFUNDS": FredSeries("FEDFUNDS", "Fed Funds Rate", "fed_policy", FREQUENCY_MONTHLY, "wide", required=True),
    "DFEDTARU": FredSeries("DFEDTARU", "Fed Target Upper", "fed_policy", FREQUENCY_DAILY, "wide", required=True),
    "DFEDTARL": FredSeries("DFEDTARL", "Fed Target Lower", "fed_policy", FREQUENCY_DAILY, "wide", required=True),
    "CPIAUCSL": FredSeries("CPIAUCSL", "CPI All Items", "inflation", FREQUENCY_MONTHLY, "wide", required=True),
    "CPILFESL": FredSeries("CPILFESL", "Core CPI", "inflation", FREQUENCY_MONTHLY, "wide", required=True),
    "T5YIE": FredSeries("T5YIE", "5Y Breakeven Inflation", "inflation", FREQUENCY_DAILY, "wide", required=True),
    "T10YIE": FredSeries("T10YIE", "10Y Breakeven Inflation", "inflation", FREQUENCY_DAILY, "wide", required=True),
    "BAMLH0A0HYM2": FredSeries("BAMLH0A0HYM2", "High Yield Spread", "credit_spreads", FREQUENCY_DAILY, "wide", required=True),
    "BAMLC0A0CM": FredSeries("BAMLC0A0CM", "Corporate Spread", "credit_spreads", FREQUENCY_DAILY, "wide", required=True),
    "BAMLC0A4CBBB": FredSeries("BAMLC0A4CBBB", "BBB Corporate Spread", "credit_spreads", FREQUENCY_DAILY, "fred_bonds"),
    "BAMLC0A1CAAA": FredSeries("BAMLC0A1CAAA", "AAA Corporate Spread", "credit_spreads", FREQUENCY_DAILY, "fred_bonds"),
    "BAMLC0A2CAA": FredSeries("BAMLC0A2CAA", "AA Corporate Spread", "credit_spreads", FREQUENCY_DAILY, "fred_bonds"),
    "BAMLC0A3CA": FredSeries("BAMLC0A3CA", "A Corporate Spread", "credit_spreads", FREQUENCY_DAILY, "fred_bonds"),
    "BAMLC0A1CAAAEY": FredSeries("BAMLC0A1CAAAEY", "AAA Corporate Effective Yield", "credit_yields", FREQUENCY_DAILY, "fred_bonds"),
    "BAMLC0A2CAAEY": FredSeries("BAMLC0A2CAAEY", "AA Corporate Effective Yield", "credit_yields", FREQUENCY_DAILY, "fred_bonds"),
    "BAMLC0A3CAEY": FredSeries("BAMLC0A3CAEY", "A Corporate Effective Yield", "credit_yields", FREQUENCY_DAILY, "fred_bonds"),
    "BAMLC0A4CBBBEY": FredSeries("BAMLC0A4CBBBEY", "BBB Corporate Effective Yield", "credit_yields", FREQUENCY_DAILY, "fred_bonds"),
    "BAMLH0A0HYM2EY": FredSeries("BAMLH0A0HYM2EY", "High Yield Effective Yield", "credit_yields", FREQUENCY_DAILY, "fred_bonds"),
    "BAMLC1A0C13YEY": FredSeries("BAMLC1A0C13YEY", "1-3 Year Corporate Yield", "credit_yields", FREQUENCY_DAILY, "fred_bonds"),
    "BAMLC2A0C35YEY": FredSeries("BAMLC2A0C35YEY", "3-5 Year Corporate Yield", "credit_yields", FREQUENCY_DAILY, "fred_bonds"),
    "BAMLC8A0C15PY": FredSeries("BAMLC8A0C15PY", "15+ Year Corporate Yield", "credit_yields", FREQUENCY_DAILY, "fred_bonds"),
    "AAA": FredSeries("AAA", "Moodys Aaa Corporate Bond Yield", "credit_yields", FREQUENCY_MONTHLY, "fred_bonds"),
    "BAA": FredSeries("BAA", "Moodys Baa Corporate Bond Yield", "credit_yields", FREQUENCY_MONTHLY, "fred_bonds"),
    "AAA10Y": FredSeries("AAA10Y", "Moodys Aaa-10Y Treasury Spread", "credit_spreads", FREQUENCY_MONTHLY, "fred_bonds"),
    "BAA10Y": FredSeries("BAA10Y", "Moodys Baa-10Y Treasury Spread", "credit_spreads", FREQUENCY_MONTHLY, "fred_bonds"),
    "UNRATE": FredSeries("UNRATE", "Unemployment Rate", "labor", FREQUENCY_MONTHLY, "tier2"),
    "PAYEMS": FredSeries("PAYEMS", "Nonfarm Payrolls", "labor", FREQUENCY_MONTHLY, "tier2"),
    "CIVPART": FredSeries("CIVPART", "Labor Force Participation", "labor", FREQUENCY_MONTHLY, "tier2"),
    "U6RATE": FredSeries("U6RATE", "U6 Unemployment", "labor", FREQUENCY_MONTHLY, "tier2"),
    "GDP": FredSeries("GDP", "GDP", "economic_activity", FREQUENCY_QUARTERLY, "tier2"),
    "GDPC1": FredSeries("GDPC1", "Real GDP", "economic_activity", FREQUENCY_QUARTERLY, "tier2"),
    "UMCSENT": FredSeries("UMCSENT", "Consumer Sentiment", "economic_activity", FREQUENCY_MONTHLY, "tier2"),
    "RSXFS": FredSeries("RSXFS", "Retail Sales", "economic_activity", FREQUENCY_MONTHLY, "tier2"),
    "WALCL": FredSeries("WALCL", "Fed Balance Sheet", "liquidity", FREQUENCY_WEEKLY, "tier2"),
    "RRPONTSYD": FredSeries("RRPONTSYD", "Reverse Repo", "liquidity", FREQUENCY_DAILY, "tier2"),
    "WTREGEN": FredSeries("WTREGEN", "Treasury General Account", "liquidity", FREQUENCY_WEEKLY, "tier2"),
    "STLFSI4": FredSeries("STLFSI4", "Financial Stress Index", "financial_stress", FREQUENCY_WEEKLY, "tier2"),
    "TEDRATE": FredSeries("TEDRATE", "TED Spread", "financial_stress", FREQUENCY_DAILY, "tier2", active=False),
    "DCOILWTICO": FredSeries("DCOILWTICO", "WTI Crude Oil", "commodities", FREQUENCY_DAILY, "tier2", allowed_lag_days=7),
    # Removed from FRED; FRED blog notes older gold fixing graphs are now static.
    "GOLDAMGBD228NLBM": FredSeries("GOLDAMGBD228NLBM", "Gold Price", "commodities", FREQUENCY_DAILY, "tier2", active=False),
    "DCOILBRENTEU": FredSeries("DCOILBRENTEU", "Brent Crude", "commodities", FREQUENCY_DAILY, "tier2", allowed_lag_days=7),
    "DEXCHUS": FredSeries("DEXCHUS", "CNY/USD", "forex", FREQUENCY_DAILY, "tier2", allowed_lag_days=10),
    "DEXJPUS": FredSeries("DEXJPUS", "JPY/USD", "forex", FREQUENCY_DAILY, "tier2", allowed_lag_days=10),
    "DEXUSEU": FredSeries("DEXUSEU", "USD/EUR", "forex", FREQUENCY_DAILY, "tier2", allowed_lag_days=10),
    "INTDSRBRM193N": FredSeries("INTDSRBRM193N", "Brazil SELIC Rate", "brazil_rates", FREQUENCY_MONTHLY, "tier2"),
    "IRSTCI01BRM156N": FredSeries("IRSTCI01BRM156N", "Brazil CDI Rate", "brazil_rates", FREQUENCY_MONTHLY, "tier2"),
    "INTGSTBRM193N": FredSeries("INTGSTBRM193N", "Brazil T-Bill Rate", "brazil_rates", FREQUENCY_MONTHLY, "tier2"),
    "ECBDFR": FredSeries("ECBDFR", "ECB Deposit Rate", "euro_rates", FREQUENCY_DAILY, "tier2"),
    "ECBESTRVOLWGTTRMDMNRT": FredSeries("ECBESTRVOLWGTTRMDMNRT", "Euro STR (overnight)", "euro_rates", FREQUENCY_DAILY, "tier2"),
    "ECBMRRFR": FredSeries("ECBMRRFR", "ECB Main Refi Rate", "euro_rates", FREQUENCY_DAILY, "tier2"),
    "ECBMLFR": FredSeries("ECBMLFR", "ECB Marginal Lending Rate", "euro_rates", FREQUENCY_DAILY, "tier2"),
}


def fred_series_map(update_group: str) -> dict[str, str]:
    """Return code -> name for active registry members in an updater group."""
    return {
        code: series.name
        for code, series in FRED_SERIES_REGISTRY.items()
        if series.active and series.update_group == update_group
    }


def active_prices_long_fred_series() -> dict[str, FredSeries]:
    """Return active FRED registry members expected in prices_long."""
    return {
        code: series
        for code, series in FRED_SERIES_REGISTRY.items()
        if series.active and series.table == "prices_long"
    }


def fred_descriptions(codes=None) -> dict[str, str]:
    """Return descriptions for registry codes, optionally filtered."""
    selected = {code.upper() for code in codes} if codes else None
    return {
        code: series.name
        for code, series in FRED_SERIES_REGISTRY.items()
        if selected is None or code in selected
    }


FRED_UPDATE_WIDE_SERIES = fred_series_map("wide")
FRED_NARROW_ONLY_SERIES = fred_series_map("narrow")
FRED_TIER2_SERIES = fred_series_map("tier2")
FRED_BOND_SERIES = {
    code: series.name
    for code, series in FRED_SERIES_REGISTRY.items()
    if series.active
    and (
        series.update_group == "fred_bonds"
        or code in {"BAMLH0A0HYM2", "BAMLC0A0CM"}
    )
}
