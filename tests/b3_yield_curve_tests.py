import unittest
from io import BytesIO
from zipfile import ZipFile

from fetch_b3_yield_curve import extract_taxaswap_text, parse_taxaswap_rates


def _zip_bytes(name, payload):
    buffer = BytesIO()
    with ZipFile(buffer, "w") as zf:
        zf.writestr(name, payload)
    return buffer.getvalue()


def _taxaswap_row(seq, code, name, cal_days, biz_days, rate):
    scaled_rate = round(rate * 10_000_000)
    return (
        f"{seq:06d}"
        f"00101"
        f"20260605"
        f"{code:<5}"
        f"{name:<17}"
        f"{cal_days:05d}"
        f"{biz_days:05d}"
        f"+{scaled_rate:014d}"
        f"M{cal_days:05d}"
    )


class B3TaxaSwapParserTests(unittest.TestCase):
    def test_extracts_text_from_nested_sfx_payload(self):
        text = _taxaswap_row(1, "T1PRE", "DIxPRE", 31, 21, 14.354) + "\r\n"
        inner = b"MZ" + (b"\x00" * 64) + _zip_bytes("TaxaSwap.txt", text.encode("latin1"))
        outer = _zip_bytes("TS260605.ex_", inner)

        self.assertEqual(extract_taxaswap_text(outer), text)

    def test_parses_t1pre_rates_by_business_days(self):
        text = "\r\n".join(
            [
                _taxaswap_row(1, "T1PRE", "DIxPRE", 31, 21, 14.354),
                _taxaswap_row(2, "T1DIC", "DI X IPCA", 31, 21, 7.83),
                _taxaswap_row(3, "T1PRE", "DIxPRE", 88, 62, 14.349),
            ]
        )

        self.assertEqual(parse_taxaswap_rates(text), {21: 14.354, 62: 14.349})


if __name__ == "__main__":
    unittest.main()
