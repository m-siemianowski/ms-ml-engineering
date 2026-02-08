import warnings

warnings.filterwarnings(
    "ignore",
    category=DeprecationWarning,
    module="xgboost.*"
)

warnings.filterwarnings(
    "ignore",
    category=DeprecationWarning,
    module="pkg_resources.*"
)
