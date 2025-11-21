"""
Central configuration management using Pydantic.
"""

import os
from pathlib import Path
from typing import List, Optional

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or defaults.

    To use custom settings, create a .env file in the project root.
    """

    # Project
    project_name: str = Field(default="sales-pattern-analysis", alias="PROJECT_NAME")
    environment: str = Field(default="development", alias="ENVIRONMENT")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    # Random seed
    random_state: int = Field(default=42, alias="RANDOM_STATE")

    # Paths (relative to project root)
    data_raw_path: str = Field(default="data/raw", alias="DATA_RAW_PATH")
    data_interim_path: str = Field(default="data/interim", alias="DATA_INTERIM_PATH")
    data_processed_path: str = Field(default="data/processed", alias="DATA_PROCESSED_PATH")
    data_external_path: str = Field(default="data/external", alias="DATA_EXTERNAL_PATH")
    models_path: str = Field(default="data/models", alias="MODELS_PATH")

    # Kaggle
    kaggle_username: Optional[str] = Field(default=None, alias="KAGGLE_USERNAME")
    kaggle_key: Optional[str] = Field(default=None, alias="KAGGLE_KEY")

    # Model Training
    test_size: float = Field(default=0.2, alias="TEST_SIZE")
    val_size: float = Field(default=0.2, alias="VAL_SIZE")
    cv_folds: int = Field(default=5, alias="CV_FOLDS")
    enable_hyperparameter_tuning: bool = Field(
        default=True, alias="ENABLE_HYPERPARAMETER_TUNING"
    )

    # Clustering
    clustering_algorithms: str = Field(
        default="kmeans,dbscan,gmm", alias="CLUSTERING_ALGORITHMS"
    )
    k_range_min: int = Field(default=2, alias="K_RANGE_MIN")
    k_range_max: int = Field(default=10, alias="K_RANGE_MAX")

    # Dashboard
    dashboard_port: int = Field(default=8501, alias="DASHBOARD_PORT")
    dashboard_host: str = Field(default="localhost", alias="DASHBOARD_HOST")

    # Logging
    log_file: str = Field(default="logs/app.log", alias="LOG_FILE")
    log_max_bytes: int = Field(default=10485760, alias="LOG_MAX_BYTES")  # 10MB
    log_backup_count: int = Field(default=5, alias="LOG_BACKUP_COUNT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        extra = "allow"

    @property
    def clustering_algorithms_list(self) -> List[str]:
        """Get clustering algorithms as a list."""
        return [algo.strip() for algo in self.clustering_algorithms.split(",")]

    @property
    def k_range(self) -> range:
        """Get k range for clustering."""
        return range(self.k_range_min, self.k_range_max + 1)

    def get_path(self, path_name: str) -> Path:
        """
        Get a Path object for a configured path.

        Args:
            path_name: Name of the path setting (e.g., 'data_raw_path')

        Returns:
            Path object

        Example:
            >>> settings = Settings()
            >>> raw_path = settings.get_path('data_raw_path')
        """
        path_str = getattr(self, path_name)
        return Path(path_str)


# Create global settings instance
settings = Settings()


# Helper functions
def get_settings() -> Settings:
    """Get the global settings instance."""
    return settings


def reload_settings() -> Settings:
    """Reload settings from environment."""
    global settings
    settings = Settings()
    return settings
