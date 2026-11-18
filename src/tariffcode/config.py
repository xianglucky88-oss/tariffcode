
from types import SimpleNamespace

ROOT = __import__("pathlib").Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "tariffcode.db"

SPEC = SimpleNamespace(
    slug="tariffcode",
    fmt="json",
    engine="crawl",
    endpoint="items",
    columns=["id", "name", "value", "status", "ts", "hs"],
    page_size=4,
    int_fields=["value"],
    ts_field="ts",
)
