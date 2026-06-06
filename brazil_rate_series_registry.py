"""Brazil interest-rate series expected in canonical prices_long."""

from dataclasses import dataclass


FREQUENCY_DAILY = "daily"
FREQUENCY_MONTHLY = "monthly"

BRAZIL_RATE_FREQUENCY_LAG_DAYS = {
    FREQUENCY_MONTHLY: 75,
}


@dataclass(frozen=True)
class BrazilRateSeries:
    code: str
    name: str
    source: str
    frequency: str
    required: bool = True
    table: str = "prices_long"
    allowed_lag_days: int | None = None


BRAZIL_RATE_SERIES_REGISTRY = {
    "B3_DI_1M": BrazilRateSeries("B3_DI_1M", "B3 DI curve 1M", "B3", FREQUENCY_DAILY),
    "B3_DI_3M": BrazilRateSeries("B3_DI_3M", "B3 DI curve 3M", "B3", FREQUENCY_DAILY),
    "B3_DI_6M": BrazilRateSeries("B3_DI_6M", "B3 DI curve 6M", "B3", FREQUENCY_DAILY),
    "B3_DI_1Y": BrazilRateSeries("B3_DI_1Y", "B3 DI curve 1Y", "B3", FREQUENCY_DAILY),
    "B3_DI_2Y": BrazilRateSeries("B3_DI_2Y", "B3 DI curve 2Y", "B3", FREQUENCY_DAILY),
    "B3_DI_5Y": BrazilRateSeries("B3_DI_5Y", "B3 DI curve 5Y", "B3", FREQUENCY_DAILY),
    "B3_DI_10Y": BrazilRateSeries("B3_DI_10Y", "B3 DI curve 10Y", "B3", FREQUENCY_DAILY),
    "BCB_SELIC": BrazilRateSeries("BCB_SELIC", "BCB SELIC Target Rate", "BCB", FREQUENCY_DAILY),
    "BCB_CDI": BrazilRateSeries("BCB_CDI", "BCB CDI Rate", "BCB", FREQUENCY_DAILY, allowed_lag_days=5),
    "INTDSRBRM193N": BrazilRateSeries("INTDSRBRM193N", "Brazil SELIC Rate", "FRED", FREQUENCY_MONTHLY),
    "IRSTCI01BRM156N": BrazilRateSeries("IRSTCI01BRM156N", "Brazil CDI Rate", "FRED", FREQUENCY_MONTHLY),
    "INTGSTBRM193N": BrazilRateSeries("INTGSTBRM193N", "Brazil T-Bill Rate", "FRED", FREQUENCY_MONTHLY),
}


B3_DI_SERIES = {
    code: series.name
    for code, series in BRAZIL_RATE_SERIES_REGISTRY.items()
    if series.source == "B3"
}

BCB_RATE_SERIES = {
    code: series.name
    for code, series in BRAZIL_RATE_SERIES_REGISTRY.items()
    if series.source == "BCB"
}


def active_brazil_rate_series() -> dict[str, BrazilRateSeries]:
    """Return active Brazil rate registry members expected in prices_long."""
    return {
        code: series
        for code, series in BRAZIL_RATE_SERIES_REGISTRY.items()
        if series.table == "prices_long"
    }
