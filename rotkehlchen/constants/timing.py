from typing import Final

ETH_DAO_FORK_TS: Final = 1469020840  # 2016-07-20 13:20:40 UTC
BTC_BCH_FORK_TS: Final = 1501593374  # 2017-08-01 13:16:14 UTC
BCH_BSV_FORK_TS: Final = 1542304352  # 2018-11-15 18:52:00 UTC

ROTKEHLCHEN_SERVER_TIMEOUT: Final = 5
ROTKEHLCHEN_SERVER_BACKUP_TIMEOUT: Final = ROTKEHLCHEN_SERVER_TIMEOUT * 30
GLOBAL_REQUESTS_TIMEOUT: Final = 5  # perhaps consolidate this and the one above?

HOUR_IN_SECONDS: Final = 3600
DAY_IN_SECONDS: Final = 24 * HOUR_IN_SECONDS
WEEK_IN_SECONDS: Final = DAY_IN_SECONDS * 7
MONTH_IN_SECONDS: Final = WEEK_IN_SECONDS * 4
YEAR_IN_SECONDS: Final = 31536000  # 60 * 60 * 24 * 365

# For queries that are attempted multiple times:
ENS_UPDATE_INTERVAL: Final = DAY_IN_SECONDS

ETH_PROTOCOLS_CACHE_REFRESH: Final = DAY_IN_SECONDS * 3
DATA_UPDATES_REFRESH: Final = DAY_IN_SECONDS
EVMLIKE_ACCOUNTS_DETECTION_REFRESH: Final = DAY_IN_SECONDS
ENS_AVATARS_REFRESH: Final = DAY_IN_SECONDS
SPAM_ASSETS_DETECTION_REFRESH: Final = HOUR_IN_SECONDS * 6
AUGMENTED_SPAM_ASSETS_DETECTION_REFRESH: Final = DAY_IN_SECONDS
OWNED_ASSETS_UPDATE: Final = HOUR_IN_SECONDS
AAVE_V3_ASSETS_UPDATE: Final = WEEK_IN_SECONDS