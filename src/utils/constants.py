"""
Project constants and enumerations.
"""

from enum import Enum
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Data paths
DATA_RAW_PATH = PROJECT_ROOT / "data" / "raw"
DATA_INTERIM_PATH = PROJECT_ROOT / "data" / "interim"
DATA_PROCESSED_PATH = PROJECT_ROOT / "data" / "processed"
DATA_EXTERNAL_PATH = PROJECT_ROOT / "data" / "external"
MODELS_PATH = PROJECT_ROOT / "data" / "models"

# Reports paths
REPORTS_PATH = PROJECT_ROOT / "reports"
FIGURES_PATH = REPORTS_PATH / "figures"

# Logs path
LOGS_PATH = PROJECT_ROOT / "logs"

# Random seed for reproducibility
RANDOM_STATE = 42

# Data files
DATA_FILES = {
    "categorias": "categorias.csv",
    "clientes": "clientes.csv",
    "metodos_pago": "metodos_pago.csv",
    "productos": "productos.csv",
    "ventas": "ventas.csv",
}

# Column names
class Columns:
    """Column name constants"""

    # Categorias
    ID_CATEGORIA = "ID_Categoria"
    CATEGORIA = "Categoría"
    DESCRIPCION_CATEGORIA = "Descripción"

    # Clientes
    ID_CLIENTE = "ID_Cliente"
    NOMBRE = "Nombre"
    APELLIDO = "Apellido"
    EMAIL = "Email"
    FECHA_REGISTRO = "Fecha_Resgistro"  # Note: typo in source data
    REGION = "Región"

    # Metodos Pago
    ID_METODO = "ID_Metodo"
    METODO = "Método"
    DESCRIPCION_METODO = "Descripción"

    # Productos
    ID_PRODUCTO = "ID_Producto"
    NOMBRE_PRODUCTO = "Nombre_producto"
    CATEGORIA_PRODUCTO = "Categoría"
    PRECIO_UNITARIO = "Precio_Unitario"
    STOCK = "Stock"

    # Ventas
    ID_VENTA = "ID_Venta"
    FECHA = "Fecha"
    CANTIDAD = "Cantidad"
    METODO_PAGO = "Método_Pago"
    ESTADO = "Estado"


# Valid values
class ValidValues:
    """Valid categorical values"""

    REGIONES = ["Buenos Aires", "Patagonia", "Centro", "Cuyo", "NEA", "NOA"]

    ESTADOS_VENTA = ["Completa", "Pendiente", "Cancelada"]

    METODOS_PAGO = {
        1: "Efectivo",
        2: "Tarjeta de Crédito",
        3: "Tarjeta de Débito",
        4: "Billetera Virtual",
        5: "Transferencia Bancaria",
    }

    CATEGORIAS = [
        "Lácteos",
        "Carnicería",
        "Panadería",
        "Frutas y Verduras",
        "Bebidas",
        "Congelados",
        "Galletitas y Snacks",
        "Conservas",
    ]


# Date formats
DATE_FORMAT_INPUT = "%d/%m/%Y"  # Format in source data
DATE_FORMAT_OUTPUT = "%Y-%m-%d"  # Standard ISO format

# Numeric conversions
DECIMAL_SEPARATOR_INPUT = ","  # Spanish format
DECIMAL_SEPARATOR_OUTPUT = "."  # Standard format

# Encoding
DEFAULT_ENCODING = "utf-8-sig"  # Handles BOM in CSV files

# Data quality thresholds
class QualityThresholds:
    """Data quality thresholds for validation"""

    MAX_NULL_PERCENTAGE = 0.05  # 5% maximum nulls
    MAX_DUPLICATE_PERCENTAGE = 0.01  # 1% maximum duplicates
    MIN_UNIQUE_RATIO = 0.01  # Minimum unique values ratio
    MAX_OUTLIER_PERCENTAGE = 0.05  # 5% maximum outliers


# Model parameters
class ModelConfig:
    """Default model configuration"""

    TEST_SIZE = 0.2
    VAL_SIZE = 0.2
    CV_FOLDS = 5
    RANDOM_STATE = RANDOM_STATE

    # Clustering
    K_RANGE_MIN = 2
    K_RANGE_MAX = 10
    CLUSTERING_ALGORITHMS = ["kmeans", "dbscan", "gmm"]

    # Modeling
    SCORING_METRIC = "neg_mean_absolute_percentage_error"
    N_JOBS = -1  # Use all CPU cores


# Feature engineering
class FeatureConfig:
    """Feature engineering configuration"""

    # Temporal features
    TEMPORAL_FEATURES = [
        "year",
        "month",
        "quarter",
        "day",
        "day_of_week",
        "day_of_year",
        "week_of_year",
        "is_weekend",
        "is_month_start",
        "is_month_end",
    ]

    # RFM
    RFM_QUANTILES = 5

    # Rolling windows (in days)
    ROLLING_WINDOWS = [7, 14, 30, 90]

    # Lag features (in days)
    LAG_PERIODS = [1, 7, 14, 30]


# Visualization
class VisualizationConfig:
    """Visualization configuration"""

    FIGURE_DPI = 100
    FIGURE_SIZE = (12, 6)
    STYLE = "seaborn-v0_8-darkgrid"
    COLOR_PALETTE = "husl"

    # Dashboard
    DASHBOARD_PORT = 8501
    DASHBOARD_TITLE = "Sales Pattern Analysis"


# Logging
class LogConfig:
    """Logging configuration"""

    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    LOG_FILE = "sales_analysis.log"


# Business KPIs
class KPIMetrics:
    """KPI calculation constants"""

    # Sales metrics
    METRICS_SALES = [
        "total_sales",
        "total_units",
        "avg_ticket",
        "num_transactions",
    ]

    # Margin metrics (if cost data available)
    METRICS_MARGIN = [
        "gross_margin",
        "margin_percentage",
    ]

    # Inventory metrics
    METRICS_INVENTORY = [
        "stock_level",
        "turnover_rate",
        "days_of_inventory",
    ]

    # Growth metrics
    METRICS_GROWTH = [
        "yoy_growth",
        "mom_growth",
        "wow_growth",
    ]

    # Customer metrics
    METRICS_CUSTOMER = [
        "customer_count",
        "avg_frequency",
        "customer_lifetime_value",
    ]


# Status messages
class Messages:
    """Standard messages for user feedback"""

    SUCCESS = "Operation completed successfully"
    ERROR = "An error occurred"
    WARNING = "Warning: potential issue detected"
    INFO = "Information"

    LOADING_DATA = "Loading data..."
    CLEANING_DATA = "Cleaning data..."
    TRANSFORMING_DATA = "Transforming data..."
    ENGINEERING_FEATURES = "Engineering features..."
    TRAINING_MODEL = "Training model..."
    EVALUATING_MODEL = "Evaluating model..."


# Export formats
EXPORT_FORMATS = ["csv", "parquet", "pkl", "json"]
