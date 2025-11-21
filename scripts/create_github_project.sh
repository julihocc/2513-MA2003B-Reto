#!/bin/bash
# Script to create GitHub project and issues for Sales Pattern Analysis

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Creating GitHub Project for Sales Pattern Analysis${NC}"

# Get repository info
REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
echo "Repository: $REPO"

# Create GitHub Project (Projects V2)
echo -e "\n${GREEN}Creating GitHub Project...${NC}"
PROJECT_ID=$(gh project create \
  --title "Sales Pattern Analysis - Implementation" \
  --owner "@me" \
  --format json | jq -r '.id')

echo "Project created with ID: $PROJECT_ID"

# Function to create issue and add to project
create_issue() {
  local title="$1"
  local body="$2"
  local labels="$3"
  local milestone="$4"

  echo -e "\n${GREEN}Creating issue: $title${NC}"

  # Create issue
  ISSUE_URL=$(gh issue create \
    --title "$title" \
    --body "$body" \
    --label "$labels" \
    ${milestone:+--milestone "$milestone"} \
    --repo "$REPO")

  echo "Created: $ISSUE_URL"
}

# ============================================================================
# PHASE 1: Foundation & Setup
# ============================================================================

create_issue \
  "[Setup] Initialize Project Structure" \
  "## Objective
Create the complete project directory structure according to the architecture plan.

## Tasks
- [ ] Create all main directories (src/, data/, tests/, docs/, etc.)
- [ ] Set up subdirectories for each layer (infrastructure, domain, application, presentation)
- [ ] Create __init__.py files in all package directories
- [ ] Set up data directories (raw/, interim/, processed/, external/, models/)
- [ ] Create scripts/ and notebooks/ directories
- [ ] Verify structure matches architecture plan

## Acceptance Criteria
- All directories from architecture plan exist
- Python package structure is valid
- No import errors when importing empty packages

## Files to Create
- All directory structure
- All __init__.py files

## Reference
- Architecture Plan Section 2" \
  "setup,phase-1" \
  "Phase 1: Foundation"

create_issue \
  "[Setup] Configure Development Environment" \
  "## Objective
Set up development environment with all necessary dependencies and tools.

## Tasks
- [ ] Create requirements.txt with pinned versions
- [ ] Create requirements-dev.txt for development tools
- [ ] Create setup.py for package installation
- [ ] Create pyproject.toml for tool configuration
- [ ] Create .env.example file
- [ ] Create .gitignore file
- [ ] Set up virtual environment documentation
- [ ] Test installation process

## Acceptance Criteria
- \`pip install -r requirements.txt\` works without errors
- All specified libraries install correctly
- Virtual environment can be created and activated

## Reference
- Architecture Plan Section 10.1" \
  "setup,phase-1" \
  "Phase 1: Foundation"

create_issue \
  "[Setup] Configure Logging System" \
  "## Objective
Implement centralized logging configuration for the entire project.

## Tasks
- [ ] Create config/logging_config.yaml
- [ ] Implement src/utils/logger.py with get_logger() function
- [ ] Configure log levels (DEBUG, INFO, WARNING, ERROR)
- [ ] Set up log formatting (timestamp, level, module, message)
- [ ] Configure file and console handlers
- [ ] Add log rotation configuration
- [ ] Create examples of logging usage
- [ ] Write unit tests for logger

## Acceptance Criteria
- Logging can be configured via YAML
- Logs write to both console and file
- Log levels work correctly
- Module-specific loggers can be created

## Files to Create
- config/logging_config.yaml
- src/utils/logger.py
- tests/unit/test_logger.py

## Reference
- Architecture Plan Section 7.1" \
  "setup,phase-1" \
  "Phase 1: Foundation"

create_issue \
  "[Setup] Implement Configuration Management" \
  "## Objective
Create centralized configuration system using Pydantic and environment variables.

## Tasks
- [ ] Create config/settings.py with Settings class
- [ ] Configure path settings (data, models, logs)
- [ ] Configure project constants (random seed, test size, etc.)
- [ ] Set up environment variable loading from .env
- [ ] Create config/model_params.yaml for model hyperparameters
- [ ] Implement config validation
- [ ] Create configuration documentation
- [ ] Write unit tests

## Acceptance Criteria
- Settings load from .env file
- Default values work when .env doesn't exist
- YAML config files parse correctly
- Type validation works via Pydantic

## Files to Create
- config/settings.py
- config/model_params.yaml
- .env.example
- src/infrastructure/config_manager.py
- tests/unit/test_config.py

## Reference
- Architecture Plan Sections 5.1, 5.2" \
  "setup,phase-1" \
  "Phase 1: Foundation"

create_issue \
  "[Infrastructure] Implement Data Loader Module" \
  "## Objective
Create flexible data loading system supporting multiple sources.

## Tasks
- [ ] Create abstract DataLoader base class
- [ ] Implement KaggleDataLoader
- [ ] Implement LocalDataLoader (CSV, Parquet)
- [ ] Add error handling and retry logic
- [ ] Add connection pooling where applicable
- [ ] Implement data versioning support
- [ ] Add logging for all operations
- [ ] Write comprehensive unit tests

## Acceptance Criteria
- Can load from Kaggle datasets
- Can load from local files (CSV, Parquet)
- Errors are handled gracefully with retries
- All operations are logged
- Data loader can be swapped via strategy pattern

## Files to Create
- src/infrastructure/data_loader.py
- tests/unit/test_data_loader.py
- tests/fixtures/sample_data.csv

## Reference
- Architecture Plan Section 3.1" \
  "infrastructure,phase-1" \
  "Phase 1: Foundation"

create_issue \
  "[Infrastructure] Implement Data Validator" \
  "## Objective
Create comprehensive data validation system for schema and quality checks.

## Tasks
- [ ] Create DataValidator class
- [ ] Implement schema validation (types, columns, constraints)
- [ ] Implement quality validation (nulls, duplicates, ranges)
- [ ] Implement business rule validation
- [ ] Create ValidationReport, QualityReport classes
- [ ] Add configurable validation rules
- [ ] Generate detailed validation reports
- [ ] Write unit tests with edge cases

## Acceptance Criteria
- Schema mismatches are detected
- Data quality issues are identified
- Business rules can be validated
- Detailed reports are generated
- Validation is configurable

## Files to Create
- src/infrastructure/data_validator.py
- tests/unit/test_data_validator.py

## Reference
- Architecture Plan Section 3.1" \
  "infrastructure,phase-1" \
  "Phase 1: Foundation"

create_issue \
  "[Infrastructure] Implement Model Repository" \
  "## Objective
Create model persistence system for saving and loading trained models.

## Tasks
- [ ] Create ModelRepository class
- [ ] Implement save() method with metadata
- [ ] Implement load() method
- [ ] Add model versioning
- [ ] Store model metadata (params, metrics, date)
- [ ] Support multiple model formats (pickle, joblib, ONNX)
- [ ] Add model registry functionality
- [ ] Write unit tests

## Acceptance Criteria
- Models can be saved with metadata
- Models can be loaded reliably
- Versioning works correctly
- Multiple formats are supported

## Files to Create
- src/infrastructure/model_repository.py
- tests/unit/test_model_repository.py

## Reference
- Architecture Plan Section 3.1" \
  "infrastructure,phase-1" \
  "Phase 1: Foundation"

# ============================================================================
# PHASE 2: Data Preparation
# ============================================================================

create_issue \
  "[Domain] Implement Data Cleaning Module" \
  "## Objective
Create comprehensive data cleaning system with multiple strategies.

## Tasks
- [ ] Create DataCleaner class
- [ ] Implement handle_missing_values() with multiple strategies
- [ ] Implement remove_duplicates()
- [ ] Implement handle_outliers() (IQR, Z-score, Isolation Forest)
- [ ] Create CleaningStrategy interface
- [ ] Implement specific strategies (MeanImputation, MedianImputation, etc.)
- [ ] Add cleaning operation logging
- [ ] Generate CleaningReport
- [ ] Write comprehensive unit tests

## Acceptance Criteria
- Multiple imputation strategies work
- Outliers can be detected and handled
- All operations are logged
- Cleaning report is detailed and actionable

## Files to Create
- src/domain/preprocessing/cleaner.py
- src/domain/preprocessing/strategies.py
- tests/unit/test_cleaner.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,preprocessing,phase-2" \
  "Phase 2: Data Preparation"

create_issue \
  "[Domain] Implement Data Transformation Module" \
  "## Objective
Create data transformation system for encoding and normalization.

## Tasks
- [ ] Create DataTransformer class
- [ ] Implement normalize() (Min-Max, Standard, Robust)
- [ ] Implement encode_categorical() (One-hot, Label, Target)
- [ ] Implement discretize() for binning
- [ ] Add inverse transforms where applicable
- [ ] Store transformation parameters
- [ ] Add transformation logging
- [ ] Write unit tests

## Acceptance Criteria
- Multiple normalization methods work
- Categorical encoding is correct
- Transformations can be inverted
- Parameters are stored for consistency

## Files to Create
- src/domain/preprocessing/transformer.py
- tests/unit/test_transformer.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,preprocessing,phase-2" \
  "Phase 2: Data Preparation"

create_issue \
  "[Domain] Implement Temporal Feature Engineering" \
  "## Objective
Create temporal feature engineering for time-based analysis.

## Tasks
- [ ] Create TemporalFeatureEngineer class
- [ ] Implement extract_date_features() (year, month, week, etc.)
- [ ] Implement create_seasonality_features() (sine/cosine encoding)
- [ ] Implement create_lag_features()
- [ ] Implement create_rolling_features() (mean, std, min, max)
- [ ] Add holiday detection (optional)
- [ ] Write unit tests with time series data

## Acceptance Criteria
- Date features extracted correctly
- Cyclical features properly encoded
- Lag and rolling features work
- All features have proper naming

## Files to Create
- src/domain/features/temporal.py
- tests/unit/test_temporal_features.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,features,phase-2" \
  "Phase 2: Data Preparation"

create_issue \
  "[Domain] Implement RFM Feature Engineering" \
  "## Objective
Create RFM (Recency, Frequency, Monetary) analysis features.

## Tasks
- [ ] Create RFMFeatureEngineer class
- [ ] Implement calculate_rfm()
- [ ] Implement create_rfm_segments()
- [ ] Add RFM scoring (1-5 scale)
- [ ] Create customer segmentation logic
- [ ] Add visualization helpers
- [ ] Write unit tests

## Acceptance Criteria
- RFM metrics calculated correctly
- Segments are meaningful and distinct
- Scores are properly scaled

## Files to Create
- src/domain/features/rfm.py
- tests/unit/test_rfm_features.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,features,phase-2" \
  "Phase 2: Data Preparation"

create_issue \
  "[Domain] Implement Aggregation Features" \
  "## Objective
Create aggregation feature engineering for grouping operations.

## Tasks
- [ ] Create AggregationFeatureEngineer class
- [ ] Implement group-by aggregations (by zone, category, sector)
- [ ] Implement cumulative features
- [ ] Implement ratio and percentage features
- [ ] Implement year-over-year, month-over-month growth
- [ ] Add feature naming conventions
- [ ] Write unit tests

## Acceptance Criteria
- Aggregations work for multiple dimensions
- Growth calculations are correct
- Feature names are descriptive

## Files to Create
- src/domain/features/aggregations.py
- tests/unit/test_aggregations.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,features,phase-2" \
  "Phase 2: Data Preparation"

create_issue \
  "[Application] Implement Data Preparation Pipeline" \
  "## Objective
Orchestrate full data preparation workflow from raw to processed data.

## Tasks
- [ ] Create DataPreparationPipeline class
- [ ] Implement load step
- [ ] Implement validate step
- [ ] Implement clean step
- [ ] Implement transform step
- [ ] Implement feature engineering step
- [ ] Implement save step
- [ ] Add checkpoint/resume capability
- [ ] Add progress tracking
- [ ] Generate preparation report
- [ ] Write integration tests

## Acceptance Criteria
- Pipeline runs end-to-end without errors
- Each step is logged
- Intermediate results can be saved
- Final data is validated
- Report documents all transformations

## Files to Create
- src/application/pipelines/data_preparation_pipeline.py
- tests/integration/test_data_preparation_pipeline.py

## Reference
- Architecture Plan Section 3.3" \
  "application,pipeline,phase-2" \
  "Phase 2: Data Preparation"

create_issue \
  "[Data] Download and Document Raw Data" \
  "## Objective
Download data from Kaggle and create comprehensive data dictionary.

## Tasks
- [ ] Download dataset from Kaggle
- [ ] Place in data/raw/
- [ ] Explore data structure and contents
- [ ] Create data dictionary with all fields
- [ ] Document data types, ranges, meanings
- [ ] Document relationships between tables
- [ ] Identify potential data quality issues
- [ ] Calculate basic statistics

## Acceptance Criteria
- Data downloaded and saved
- Data dictionary is complete
- All fields documented
- Initial quality assessment done

## Files to Create
- data/raw/* (dataset files)
- docs/data_dictionary.md
- scripts/download_data.py

## Reference
- Architecture Plan Section 11, Phase 1" \
  "data,documentation,phase-1,phase-2" \
  "Phase 2: Data Preparation"

# ============================================================================
# PHASE 3: EDA
# ============================================================================

create_issue \
  "[Domain] Implement EDA Service" \
  "## Objective
Create comprehensive exploratory data analysis orchestration service.

## Tasks
- [ ] Create EDAService class
- [ ] Implement distribution analysis
- [ ] Implement correlation analysis
- [ ] Implement time series analysis (trend, seasonality)
- [ ] Implement segmentation analysis (by zone, sector, category)
- [ ] Implement payment method analysis
- [ ] Generate summary statistics
- [ ] Create visualization methods
- [ ] Write unit tests

## Acceptance Criteria
- All major EDA operations available
- Results are well-structured
- Visualizations are clear and informative
- Service is easy to use

## Files to Create
- src/domain/analytics/eda_service.py
- tests/unit/test_eda_service.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,analytics,phase-3" \
  "Phase 3: EDA"

create_issue \
  "[Domain] Implement Time Series Analysis" \
  "## Objective
Create time series decomposition and seasonality analysis.

## Tasks
- [ ] Create TimeSeriesAnalyzer class
- [ ] Implement decompose() (trend, seasonal, residual)
- [ ] Implement detect_seasonality()
- [ ] Implement stationarity tests (ADF, KPSS)
- [ ] Implement autocorrelation analysis (ACF, PACF)
- [ ] Create calendar heatmaps
- [ ] Add forecasting baseline methods
- [ ] Write unit tests

## Acceptance Criteria
- Decomposition works correctly
- Seasonality is properly detected
- Statistical tests run correctly
- Visualizations are informative

## Files to Create
- src/domain/analytics/time_series.py
- tests/unit/test_time_series.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,analytics,phase-3" \
  "Phase 3: EDA"

create_issue \
  "[Domain] Implement KPI Calculator" \
  "## Objective
Create comprehensive KPI calculation system.

## Tasks
- [ ] Create KPICalculator class
- [ ] Implement sales KPIs (total, units, ticket average)
- [ ] Implement margin KPIs (gross margin, margin %)
- [ ] Implement inventory KPIs (rotation, days of inventory)
- [ ] Implement growth KPIs (YoY, MoM)
- [ ] Implement market share by category/sector
- [ ] Implement payment method distribution
- [ ] Add KPI definitions and formulas
- [ ] Write unit tests

## Acceptance Criteria
- All specified KPIs can be calculated
- Formulas are correct and documented
- KPIs work at different aggregation levels
- Results are properly formatted

## Files to Create
- src/domain/analytics/kpi_calculator.py
- tests/unit/test_kpi_calculator.py
- docs/kpi_definitions.md

## Reference
- Architecture Plan Section 3.2, Project Brief Section 1" \
  "domain,analytics,phase-3" \
  "Phase 3: EDA"

create_issue \
  "[Application] Implement EDA Pipeline" \
  "## Objective
Create orchestrated EDA workflow that generates comprehensive analysis.

## Tasks
- [ ] Create EDAPipeline class
- [ ] Implement univariate analysis step
- [ ] Implement bivariate analysis step
- [ ] Implement multivariate analysis step
- [ ] Implement temporal analysis step
- [ ] Implement segmentation analysis step
- [ ] Generate EDA report with findings
- [ ] Save all visualizations
- [ ] Write integration tests

## Acceptance Criteria
- Pipeline produces comprehensive EDA
- All key questions are answered
- Visualizations are saved
- Report is actionable

## Files to Create
- src/application/pipelines/eda_pipeline.py
- tests/integration/test_eda_pipeline.py

## Reference
- Architecture Plan Section 3.3" \
  "application,pipeline,phase-3" \
  "Phase 3: EDA"

create_issue \
  "[Notebooks] Create EDA Notebook" \
  "## Objective
Create comprehensive exploratory data analysis notebook with insights.

## Tasks
- [ ] Create notebook structure with clear sections
- [ ] Perform univariate analysis (distributions)
- [ ] Perform bivariate analysis (correlations)
- [ ] Analyze time series patterns
- [ ] Analyze by zone/sector/category
- [ ] Analyze payment methods
- [ ] Create calendar heatmaps for seasonality
- [ ] Document key findings and insights
- [ ] Add business interpretation
- [ ] Export key visualizations

## Acceptance Criteria
- Notebook runs without errors
- All analyses are complete
- Insights are clearly documented
- Visualizations are publication-quality
- Business recommendations included

## Files to Create
- notebooks/03_eda.ipynb
- reports/figures/eda_*.png

## Reference
- Architecture Plan Phase 3, Project Brief Section 4.3" \
  "notebooks,phase-3,high-priority" \
  "Phase 3: EDA"

# ============================================================================
# PHASE 4: Clustering
# ============================================================================

create_issue \
  "[Domain] Implement Base Clusterer" \
  "## Objective
Create abstract base class for clustering algorithms.

## Tasks
- [ ] Create BaseClusterer abstract class
- [ ] Define fit() abstract method
- [ ] Define predict() abstract method
- [ ] Implement calculate_metrics() (Silhouette, Davies-Bouldin, Calinski-Harabasz)
- [ ] Add common attributes (labels_, metrics_)
- [ ] Add random state handling
- [ ] Write base tests

## Acceptance Criteria
- Abstract class follows proper OOP patterns
- All subclasses can inherit common functionality
- Metrics calculation works for all algorithms

## Files to Create
- src/domain/clustering/base_clusterer.py
- tests/unit/test_base_clusterer.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,clustering,phase-4,critical" \
  "Phase 4: Clustering"

create_issue \
  "[Domain] Implement K-Means Clusterer" \
  "## Objective
Implement K-Means clustering algorithm wrapper.

## Tasks
- [ ] Create KMeansClusterer class extending BaseClusterer
- [ ] Implement fit() method
- [ ] Implement predict() method
- [ ] Add hyperparameter configuration
- [ ] Implement elbow method calculation
- [ ] Add inertia tracking
- [ ] Write comprehensive unit tests

## Acceptance Criteria
- K-Means clustering works correctly
- Hyperparameters can be tuned
- Metrics are calculated properly
- Well-tested with various datasets

## Files to Create
- src/domain/clustering/kmeans_clusterer.py
- tests/unit/test_kmeans_clusterer.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,clustering,phase-4,critical" \
  "Phase 4: Clustering"

create_issue \
  "[Domain] Implement DBSCAN Clusterer" \
  "## Objective
Implement DBSCAN clustering algorithm wrapper.

## Tasks
- [ ] Create DBSCANClusterer class extending BaseClusterer
- [ ] Implement fit() method
- [ ] Implement predict() method
- [ ] Add eps and min_samples tuning
- [ ] Handle noise points appropriately
- [ ] Add density-based metrics
- [ ] Write unit tests

## Acceptance Criteria
- DBSCAN clustering works correctly
- Noise points are handled
- Parameters can be tuned
- Appropriate for varying density clusters

## Files to Create
- src/domain/clustering/dbscan_clusterer.py
- tests/unit/test_dbscan_clusterer.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,clustering,phase-4,critical" \
  "Phase 4: Clustering"

create_issue \
  "[Domain] Implement GMM Clusterer" \
  "## Objective
Implement Gaussian Mixture Model clustering wrapper.

## Tasks
- [ ] Create GMMClusterer class extending BaseClusterer
- [ ] Implement fit() method with EM algorithm
- [ ] Implement predict() with probabilities
- [ ] Add covariance type configuration
- [ ] Implement BIC/AIC calculation
- [ ] Add soft clustering support
- [ ] Write unit tests

## Acceptance Criteria
- GMM clustering works correctly
- Probabilistic assignments available
- Information criteria calculated
- Handles overlapping clusters well

## Files to Create
- src/domain/clustering/gmm_clusterer.py
- tests/unit/test_gmm_clusterer.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,clustering,phase-4,critical" \
  "Phase 4: Clustering"

create_issue \
  "[Domain] Implement Cluster Optimizer" \
  "## Objective
Create system for finding optimal number of clusters.

## Tasks
- [ ] Create ClusterOptimizer class
- [ ] Implement elbow_method()
- [ ] Implement silhouette_analysis()
- [ ] Implement gap_statistic()
- [ ] Implement recommend_k() combining multiple methods
- [ ] Create comparison visualizations
- [ ] Add justification reports
- [ ] Write unit tests

## Acceptance Criteria
- Multiple optimization methods work
- Recommendation is data-driven
- Visualizations clearly show optimal k
- Justification is documented

## Files to Create
- src/domain/clustering/cluster_optimizer.py
- tests/unit/test_cluster_optimizer.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,clustering,phase-4,critical" \
  "Phase 4: Clustering"

create_issue \
  "[Domain] Implement Cluster Interpreter" \
  "## Objective
Create business interpretation system for cluster results.

## Tasks
- [ ] Create ClusterInterpreter class
- [ ] Implement profile_clusters() with statistical summaries
- [ ] Implement name_clusters() with business-friendly names
- [ ] Implement compare_clusters() side-by-side
- [ ] Add characteristic features identification
- [ ] Generate interpretation reports
- [ ] Create cluster visualizations (2D/3D projections)
- [ ] Write unit tests

## Acceptance Criteria
- Clusters have clear statistical profiles
- Names are meaningful and descriptive
- Comparisons highlight key differences
- Reports are actionable for business

## Files to Create
- src/domain/clustering/cluster_interpreter.py
- tests/unit/test_cluster_interpreter.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,clustering,phase-4,critical" \
  "Phase 4: Clustering"

create_issue \
  "[Application] Implement Clustering Pipeline" \
  "## Objective
Orchestrate full clustering workflow from features to insights.

## Tasks
- [ ] Create ClusteringPipeline class
- [ ] Implement feature selection step
- [ ] Implement scaling step
- [ ] Implement dimensionality reduction (PCA/UMAP) if needed
- [ ] Implement optimal k selection
- [ ] Implement multi-algorithm comparison
- [ ] Implement best model selection
- [ ] Implement cluster profiling
- [ ] Generate clustering report
- [ ] Write integration tests

## Acceptance Criteria
- Pipeline runs end-to-end
- Best algorithm is selected with justification
- Clusters are well-separated
- Business interpretation is clear

## Files to Create
- src/application/pipelines/clustering_pipeline.py
- tests/integration/test_clustering_pipeline.py

## Reference
- Architecture Plan Section 3.3" \
  "application,pipeline,phase-4,critical" \
  "Phase 4: Clustering"

create_issue \
  "[Notebooks] Create Clustering Experiments Notebook" \
  "## Objective
Experiment with clustering algorithms and document findings.

## Tasks
- [ ] Create structured experiment notebook
- [ ] Try K-Means with different k values
- [ ] Try DBSCAN with different parameters
- [ ] Try GMM with different components
- [ ] Compare algorithm performance
- [ ] Visualize clusters in 2D/3D
- [ ] Profile each cluster statistically
- [ ] Interpret clusters for business
- [ ] Select final clustering approach
- [ ] Document justification

## Acceptance Criteria
- All three algorithms tested
- Optimal k selected with evidence
- Best algorithm chosen with justification
- Clusters have business meaning
- Silhouette score > 0.5

## Files to Create
- notebooks/04_clustering_experiments.ipynb

## Reference
- Project Brief Section 4.4, Architecture Plan Phase 4" \
  "notebooks,phase-4,critical,high-weight" \
  "Phase 4: Clustering"

# ============================================================================
# PHASE 5: Predictive Modeling
# ============================================================================

create_issue \
  "[Domain] Implement Base Model" \
  "## Objective
Create abstract base class for predictive models.

## Tasks
- [ ] Create BaseModel abstract class
- [ ] Define train() abstract method
- [ ] Define predict() abstract method
- [ ] Implement evaluate() with multiple metrics (RMSE, MAE, MAPE, R²)
- [ ] Implement cross_validate() with time series CV
- [ ] Add parameter storage
- [ ] Add feature importance interface
- [ ] Write base tests

## Acceptance Criteria
- Abstract class follows proper OOP patterns
- All models can inherit common functionality
- Evaluation metrics are consistent

## Files to Create
- src/domain/models/base_model.py
- tests/unit/test_base_model.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,models,phase-5,critical" \
  "Phase 5: Predictive Modeling"

create_issue \
  "[Domain] Implement Regression Models" \
  "## Objective
Implement linear and regularized regression models.

## Tasks
- [ ] Create LinearRegressor class
- [ ] Create RidgeRegressor class
- [ ] Create LassoRegressor class
- [ ] Create ElasticNetRegressor class
- [ ] Implement feature importance extraction
- [ ] Add coefficient interpretation
- [ ] Add regularization parameter tuning
- [ ] Write unit tests for each

## Acceptance Criteria
- All regression variants work
- Feature importance available
- Regularization improves performance
- Models prevent overfitting

## Files to Create
- src/domain/models/regression/linear_regressor.py
- src/domain/models/regression/regularized_regressor.py
- tests/unit/test_regression_models.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,models,phase-5,critical" \
  "Phase 5: Predictive Modeling"

create_issue \
  "[Domain] Implement Ensemble Models" \
  "## Objective
Implement tree-based and boosting ensemble models.

## Tasks
- [ ] Create RandomForestModel class
- [ ] Create XGBoostModel class
- [ ] Create LightGBMModel class
- [ ] Implement feature importance extraction
- [ ] Add early stopping
- [ ] Add hyperparameter search spaces
- [ ] Implement SHAP values integration (optional)
- [ ] Write unit tests

## Acceptance Criteria
- All ensemble models work correctly
- Feature importance is extracted
- Hyperparameters can be tuned
- Models handle non-linearity well

## Files to Create
- src/domain/models/ensemble/random_forest.py
- src/domain/models/ensemble/xgboost_model.py
- src/domain/models/ensemble/lightgbm_model.py
- tests/unit/test_ensemble_models.py

## Reference
- Architecture Plan Section 3.2, Project Brief Section 4.5" \
  "domain,models,phase-5,critical" \
  "Phase 5: Predictive Modeling"

create_issue \
  "[Domain] Implement Time Series Models" \
  "## Objective
Implement specialized time series forecasting models.

## Tasks
- [ ] Create ARIMAModel class
- [ ] Create ProphetModel class (Facebook Prophet)
- [ ] Create ExponentialSmoothingModel class
- [ ] Implement automatic parameter selection
- [ ] Add seasonality handling
- [ ] Add trend handling
- [ ] Implement forecast intervals
- [ ] Write unit tests

## Acceptance Criteria
- Time series models work correctly
- Seasonality is captured
- Forecast intervals are provided
- Models handle trends appropriately

## Files to Create
- src/domain/models/time_series/arima_model.py
- src/domain/models/time_series/prophet_model.py
- src/domain/models/time_series/exponential_smoothing.py
- tests/unit/test_time_series_models.py

## Reference
- Architecture Plan Section 3.2, Project Brief Section 4.5" \
  "domain,models,phase-5,critical" \
  "Phase 5: Predictive Modeling"

create_issue \
  "[Domain] Implement Model Factory" \
  "## Objective
Create factory pattern for easy model instantiation.

## Tasks
- [ ] Create ModelFactory class
- [ ] Implement create_model() method
- [ ] Support all model types
- [ ] Load default parameters from config
- [ ] Add model registry
- [ ] Add model type validation
- [ ] Write unit tests

## Acceptance Criteria
- All models can be created via factory
- Parameters load from config
- Unknown model types raise clear errors
- Easy to add new models

## Files to Create
- src/domain/models/model_factory.py
- tests/unit/test_model_factory.py

## Reference
- Architecture Plan Section 4.2" \
  "domain,models,phase-5" \
  "Phase 5: Predictive Modeling"

create_issue \
  "[Domain] Implement Model Evaluator" \
  "## Objective
Create comprehensive model evaluation and comparison system.

## Tasks
- [ ] Create ModelEvaluator class
- [ ] Implement compare_models() with side-by-side comparison
- [ ] Implement residual_analysis() with plots
- [ ] Implement feature_importance_analysis()
- [ ] Implement create_baseline() (mean, median, seasonal naive)
- [ ] Add statistical significance tests
- [ ] Generate evaluation reports
- [ ] Write unit tests

## Acceptance Criteria
- Models can be compared fairly
- Baseline models work correctly
- Residual analysis identifies issues
- Reports are comprehensive and clear

## Files to Create
- src/domain/models/model_evaluator.py
- tests/unit/test_model_evaluator.py

## Reference
- Architecture Plan Section 3.2" \
  "domain,models,phase-5,critical" \
  "Phase 5: Predictive Modeling"

create_issue \
  "[Application] Implement Modeling Pipeline" \
  "## Objective
Orchestrate full predictive modeling workflow.

## Tasks
- [ ] Create ModelingPipeline class
- [ ] Implement temporal train/test split
- [ ] Implement baseline creation step
- [ ] Implement multi-model training
- [ ] Implement hyperparameter tuning (GridSearch/RandomSearch)
- [ ] Implement cross-validation
- [ ] Implement model comparison
- [ ] Implement best model selection
- [ ] Implement final evaluation on test set
- [ ] Generate modeling report
- [ ] Save best model
- [ ] Write integration tests

## Acceptance Criteria
- Pipeline runs end-to-end
- Best model is selected with justification
- Performance exceeds baseline
- Cross-validation prevents overfitting
- MAPE < 15%, R² > 0.7 (if feasible)

## Files to Create
- src/application/pipelines/modeling_pipeline.py
- tests/integration/test_modeling_pipeline.py

## Reference
- Architecture Plan Section 3.3" \
  "application,pipeline,phase-5,critical" \
  "Phase 5: Predictive Modeling"

create_issue \
  "[Notebooks] Create Modeling Experiments Notebook" \
  "## Objective
Experiment with predictive models and document findings.

## Tasks
- [ ] Create structured experiment notebook
- [ ] Create baseline models (mean, median, seasonal naive)
- [ ] Train linear regression models
- [ ] Train regularized models (Ridge, Lasso, ElasticNet)
- [ ] Train ensemble models (RF, XGBoost, LightGBM)
- [ ] Train time series models (ARIMA, Prophet, ETS)
- [ ] Perform hyperparameter tuning
- [ ] Compare all models with metrics
- [ ] Analyze feature importance
- [ ] Analyze residuals
- [ ] Select final model with justification
- [ ] Generate predictions on test set

## Acceptance Criteria
- All model types tested
- Baseline comparison included
- Best model selected with evidence
- Metrics documented (RMSE, MAE, MAPE, R²)
- Model beats baseline significantly

## Files to Create
- notebooks/05_modeling_experiments.ipynb

## Reference
- Project Brief Section 4.5, Architecture Plan Phase 5" \
  "notebooks,phase-5,critical,high-weight" \
  "Phase 5: Predictive Modeling"

# ============================================================================
# PHASE 6: Dashboard & Visualization
# ============================================================================

create_issue \
  "[Presentation] Implement Dashboard Structure" \
  "## Objective
Create main Streamlit dashboard structure with navigation.

## Tasks
- [ ] Create main app.py file
- [ ] Set up page configuration
- [ ] Implement sidebar navigation
- [ ] Create page structure (Overview, Seasonality, Clusters, Predictions)
- [ ] Add common layout components
- [ ] Implement data caching
- [ ] Add error handling
- [ ] Add loading states

## Acceptance Criteria
- Dashboard launches without errors
- Navigation works smoothly
- Layout is responsive
- Caching improves performance

## Files to Create
- src/presentation/dashboard/app.py
- src/presentation/dashboard/__init__.py

## Reference
- Architecture Plan Section 3.4" \
  "presentation,dashboard,phase-6" \
  "Phase 6: Dashboard"

create_issue \
  "[Presentation] Implement Overview Page" \
  "## Objective
Create KPI overview dashboard page.

## Tasks
- [ ] Create overview.py page
- [ ] Display key KPIs (sales, units, ticket avg, margin)
- [ ] Add time period filters
- [ ] Add zone/sector/category filters
- [ ] Create sales trend chart
- [ ] Create category distribution chart
- [ ] Create payment method distribution
- [ ] Add growth indicators (YoY, MoM)
- [ ] Make interactive with filters

## Acceptance Criteria
- All key KPIs visible
- Filters work correctly
- Charts update based on filters
- Layout is clean and professional

## Files to Create
- src/presentation/dashboard/pages/overview.py

## Reference
- Architecture Plan Section 3.4" \
  "presentation,dashboard,phase-6" \
  "Phase 6: Dashboard"

create_issue \
  "[Presentation] Implement Seasonality Page" \
  "## Objective
Create seasonality analysis dashboard page.

## Tasks
- [ ] Create seasonality.py page
- [ ] Display time series decomposition (trend, seasonal, residual)
- [ ] Create calendar heatmap
- [ ] Show seasonal patterns by category/zone
- [ ] Add month-over-month comparison
- [ ] Add year-over-year comparison
- [ ] Highlight peak and valley periods
- [ ] Add filters for different dimensions

## Acceptance Criteria
- Seasonality is clearly visible
- Decomposition plots are informative
- Calendar heatmap shows patterns
- Insights are actionable

## Files to Create
- src/presentation/dashboard/pages/seasonality.py

## Reference
- Architecture Plan Section 3.4, Project Brief Section 2" \
  "presentation,dashboard,phase-6" \
  "Phase 6: Dashboard"

create_issue \
  "[Presentation] Implement Clusters Page" \
  "## Objective
Create cluster insights dashboard page.

## Tasks
- [ ] Create clusters.py page
- [ ] Display cluster visualization (2D projection)
- [ ] Show cluster profiles table
- [ ] Display cluster characteristics
- [ ] Add cluster comparison view
- [ ] Show cluster distribution
- [ ] Highlight actionable insights per cluster
- [ ] Add drill-down capability

## Acceptance Criteria
- Clusters are clearly visualized
- Profiles are comprehensive
- Business insights are clear
- Interactive exploration works

## Files to Create
- src/presentation/dashboard/pages/clusters.py

## Reference
- Architecture Plan Section 3.4, Project Brief Section 4.4" \
  "presentation,dashboard,phase-6,critical" \
  "Phase 6: Dashboard"

create_issue \
  "[Presentation] Implement Predictions Page" \
  "## Objective
Create demand predictions dashboard page.

## Tasks
- [ ] Create predictions.py page
- [ ] Display actual vs predicted chart
- [ ] Show prediction intervals/confidence bands
- [ ] Add forecast horizon selector
- [ ] Display model performance metrics
- [ ] Show feature importance
- [ ] Add scenario analysis (what-if)
- [ ] Export predictions functionality

## Acceptance Criteria
- Predictions are clearly displayed
- Confidence intervals shown
- Model performance transparent
- Forecasts are exportable

## Files to Create
- src/presentation/dashboard/pages/predictions.py

## Reference
- Architecture Plan Section 3.4, Project Brief Section 4.5" \
  "presentation,dashboard,phase-6,critical" \
  "Phase 6: Dashboard"

create_issue \
  "[Presentation] Implement Reusable Components" \
  "## Objective
Create reusable dashboard components for consistency.

## Tasks
- [ ] Create charts.py with common chart functions
- [ ] Create filters.py with filter components
- [ ] Create metrics.py with KPI display components
- [ ] Create tables.py with formatted table components
- [ ] Add consistent styling
- [ ] Add docstrings and examples
- [ ] Write component tests

## Acceptance Criteria
- Components are reusable across pages
- Styling is consistent
- Components are well-documented
- Easy to use and extend

## Files to Create
- src/presentation/dashboard/components/charts.py
- src/presentation/dashboard/components/filters.py
- src/presentation/dashboard/components/metrics.py
- src/presentation/dashboard/components/tables.py

## Reference
- Architecture Plan Section 3.4" \
  "presentation,dashboard,phase-6" \
  "Phase 6: Dashboard"

create_issue \
  "[Presentation] Dashboard Testing & Refinement" \
  "## Objective
Test dashboard with real users and refine based on feedback.

## Tasks
- [ ] Conduct user testing with stakeholders
- [ ] Gather feedback on usability
- [ ] Identify pain points
- [ ] Refine layout and navigation
- [ ] Optimize performance (caching, lazy loading)
- [ ] Add tooltips and help text
- [ ] Ensure mobile responsiveness (if applicable)
- [ ] Final polish and bug fixes

## Acceptance Criteria
- Dashboard is intuitive to use
- No major bugs
- Performance is acceptable (<5s load time)
- Users can find insights in <5 minutes

## Reference
- Architecture Plan Section 12" \
  "presentation,dashboard,testing,phase-6" \
  "Phase 6: Dashboard"

# ============================================================================
# DOCUMENTATION & REPORTING
# ============================================================================

create_issue \
  "[Documentation] Create Data Dictionary" \
  "## Objective
Document all data fields, types, and meanings.

## Tasks
- [ ] Document all raw data fields
- [ ] Add data types for each field
- [ ] Add valid ranges/values
- [ ] Document relationships between tables
- [ ] Add business context for each field
- [ ] Document derived features
- [ ] Add examples where helpful

## Acceptance Criteria
- All fields documented
- Clear and comprehensive
- Easy to reference

## Files to Create
- docs/data_dictionary.md

## Reference
- Project Brief Section 6, Deliverable 1" \
  "documentation,phase-2,required" \
  "Phase 2: Data Preparation"

create_issue \
  "[Documentation] Create Cleaning Log" \
  "## Objective
Document all data cleaning decisions and transformations.

## Tasks
- [ ] Document null value treatment decisions
- [ ] Document duplicate removal decisions
- [ ] Document outlier handling decisions
- [ ] Document transformation decisions (encoding, scaling)
- [ ] Add before/after statistics
- [ ] Justify each decision
- [ ] Make reproducible

## Acceptance Criteria
- All cleaning steps documented
- Decisions are justified
- Process is reproducible
- Bitácora meets project requirements

## Files to Create
- docs/cleaning_log.md

## Reference
- Project Brief Sections 4.2, 6, Criterion 1" \
  "documentation,phase-2,required,high-priority" \
  "Phase 2: Data Preparation"

create_issue \
  "[Documentation] Create Technical Document" \
  "## Objective
Write comprehensive technical documentation (PDF/Markdown).

## Tasks
- [ ] Write objective section
- [ ] Document data sources and preparation
- [ ] Document cleaning and feature engineering
- [ ] Document EDA findings
- [ ] Document clustering methodology and results
- [ ] Document modeling methodology and results
- [ ] Add limitations section
- [ ] Add recommendations section
- [ ] Include key visualizations
- [ ] Format professionally

## Acceptance Criteria
- Document is comprehensive
- Methodology is clear
- Results are well-presented
- Recommendations are actionable
- Meets rubric requirements (15% + 15% + 30% + 30%)

## Files to Create
- reports/technical_doc.md
- reports/technical_doc.pdf

## Reference
- Project Brief Section 6, Deliverable 1" \
  "documentation,phase-7,required,critical" \
  "Phase 7: Documentation"

create_issue \
  "[Documentation] Create User Guide" \
  "## Objective
Create user guide for dashboard and code execution.

## Tasks
- [ ] Write installation instructions
- [ ] Document environment setup
- [ ] Explain how to run each pipeline
- [ ] Explain dashboard usage
- [ ] Add troubleshooting section
- [ ] Include screenshots
- [ ] Add FAQ section

## Acceptance Criteria
- Guide is clear and complete
- New user can follow it successfully
- All common issues addressed

## Files to Create
- docs/user_guide.md

## Reference
- Project Brief Section 6, Deliverable 3" \
  "documentation,phase-6,required" \
  "Phase 6: Dashboard"

create_issue \
  "[Documentation] Create README" \
  "## Objective
Create comprehensive README for the repository.

## Tasks
- [ ] Add project overview
- [ ] Add installation instructions
- [ ] Add quick start guide
- [ ] Document project structure
- [ ] Add usage examples
- [ ] Link to detailed documentation
- [ ] Add badges (optional)
- [ ] Add contributing guidelines (optional)

## Acceptance Criteria
- README is clear and professional
- Quick start works for new users
- Links to all documentation

## Files to Create
- README.md

## Reference
- Project Brief Section 6, Deliverable 2" \
  "documentation,phase-1,required" \
  "Phase 1: Foundation"

create_issue \
  "[Presentation] Create Executive Presentation" \
  "## Objective
Create executive presentation (10-12 slides).

## Tasks
- [ ] Create slide: Problem statement
- [ ] Create slide: Approach/methodology
- [ ] Create slides: 3-5 key findings
- [ ] Create slide: Expected impact
- [ ] Create slide: Action plan
- [ ] Add key visualizations
- [ ] Keep business-focused (not too technical)
- [ ] Design professionally

## Acceptance Criteria
- 10-12 slides total
- Clear narrative flow
- Findings are impactful
- Recommendations are concrete
- Visually professional

## Files to Create
- reports/presentation.pdf
- reports/presentation.pptx

## Reference
- Project Brief Section 6, Deliverable 4" \
  "documentation,presentation,phase-7,required" \
  "Phase 7: Documentation"

# ============================================================================
# USE CASES & RECOMMENDATIONS
# ============================================================================

create_issue \
  "[Application] Implement Analyze Seasonality Use Case" \
  "## Objective
Create use case for analyzing seasonality patterns.

## Tasks
- [ ] Create AnalyzeSeasonalityUseCase class
- [ ] Identify seasonal patterns by category/zone
- [ ] Detect peak and valley periods
- [ ] Calculate seasonality strength
- [ ] Generate actionable insights
- [ ] Create visualization outputs
- [ ] Write unit tests

## Acceptance Criteria
- Seasonality is accurately detected
- Insights are actionable
- Can be called from dashboard or scripts

## Files to Create
- src/application/use_cases/analyze_seasonality.py
- tests/unit/test_analyze_seasonality.py

## Reference
- Architecture Plan Section 3.3, Project Brief Section 2" \
  "application,use-case,phase-3" \
  "Phase 3: EDA"

create_issue \
  "[Application] Implement Segment Products Use Case" \
  "## Objective
Create use case for product/zone segmentation based on clusters.

## Tasks
- [ ] Create SegmentProductsUseCase class
- [ ] Apply clustering to products/zones
- [ ] Generate segment profiles
- [ ] Identify segment characteristics
- [ ] Create segment recommendations
- [ ] Write unit tests

## Acceptance Criteria
- Segments are meaningful
- Recommendations are specific
- Can be integrated into dashboard

## Files to Create
- src/application/use_cases/segment_products.py
- tests/unit/test_segment_products.py

## Reference
- Architecture Plan Section 3.3, Project Brief Section 4.4" \
  "application,use-case,phase-4" \
  "Phase 4: Clustering"

create_issue \
  "[Application] Implement Predict Demand Use Case" \
  "## Objective
Create use case for demand forecasting.

## Tasks
- [ ] Create PredictDemandUseCase class
- [ ] Load trained model
- [ ] Prepare input features
- [ ] Generate predictions
- [ ] Calculate confidence intervals
- [ ] Format output for consumption
- [ ] Write unit tests

## Acceptance Criteria
- Predictions are accurate
- Confidence intervals provided
- Easy to use from dashboard/scripts

## Files to Create
- src/application/use_cases/predict_demand.py
- tests/unit/test_predict_demand.py

## Reference
- Architecture Plan Section 3.3, Project Brief Section 4.5" \
  "application,use-case,phase-5" \
  "Phase 5: Predictive Modeling"

create_issue \
  "[Application] Implement Generate Recommendations Use Case" \
  "## Objective
Create use case for generating business recommendations.

## Tasks
- [ ] Create GenerateRecommendationsUseCase class
- [ ] Combine insights from EDA, clustering, predictions
- [ ] Generate supply/inventory recommendations
- [ ] Generate operational efficiency recommendations
- [ ] Generate commercial planning recommendations
- [ ] Format recommendations with specifics (what, where, when, how much)
- [ ] Write unit tests

## Acceptance Criteria
- Recommendations are concrete and actionable
- Address all three business fronts (supply, operations, commercial)
- Backed by data insights

## Files to Create
- src/application/use_cases/generate_recommendations.py
- tests/unit/test_generate_recommendations.py

## Reference
- Architecture Plan Section 3.3, Project Brief Sections 2, 4.7" \
  "application,use-case,phase-7,critical" \
  "Phase 7: Documentation"

# ============================================================================
# TESTING & QUALITY
# ============================================================================

create_issue \
  "[Testing] Set Up Testing Framework" \
  "## Objective
Configure comprehensive testing framework.

## Tasks
- [ ] Configure pytest
- [ ] Set up test directory structure
- [ ] Configure test coverage (pytest-cov)
- [ ] Set up fixtures for sample data
- [ ] Configure continuous integration (optional)
- [ ] Add test running scripts
- [ ] Document testing approach

## Acceptance Criteria
- pytest runs successfully
- Coverage reports generate
- Easy to run all tests
- Test structure matches source structure

## Files to Create
- pytest.ini or pyproject.toml [tool.pytest]
- tests/conftest.py
- tests/fixtures/sample_data.py
- scripts/run_tests.sh

## Reference
- Architecture Plan Section 6" \
  "testing,setup,phase-1" \
  "Phase 1: Foundation"

create_issue \
  "[Testing] Write Unit Tests for All Modules" \
  "## Objective
Ensure comprehensive unit test coverage (>80%).

## Tasks
- [ ] Write tests for infrastructure layer
- [ ] Write tests for preprocessing module
- [ ] Write tests for features module
- [ ] Write tests for analytics module
- [ ] Write tests for clustering module
- [ ] Write tests for models module
- [ ] Write tests for utilities
- [ ] Achieve >80% code coverage

## Acceptance Criteria
- All modules have unit tests
- Edge cases covered
- Coverage >80%
- All tests pass

## Reference
- Architecture Plan Section 6.1" \
  "testing,unit-tests,phase-1,phase-2,phase-3,phase-4,phase-5" \
  ""

create_issue \
  "[Testing] Write Integration Tests for Pipelines" \
  "## Objective
Test end-to-end pipeline workflows.

## Tasks
- [ ] Write integration test for data preparation pipeline
- [ ] Write integration test for EDA pipeline
- [ ] Write integration test for clustering pipeline
- [ ] Write integration test for modeling pipeline
- [ ] Use sample data for tests
- [ ] Test error handling
- [ ] Verify output quality

## Acceptance Criteria
- All pipelines tested end-to-end
- Tests use realistic data
- Error cases covered
- Tests run in reasonable time (<5 min total)

## Files to Create
- tests/integration/test_data_preparation_pipeline.py
- tests/integration/test_eda_pipeline.py
- tests/integration/test_clustering_pipeline.py
- tests/integration/test_modeling_pipeline.py

## Reference
- Architecture Plan Section 6.2" \
  "testing,integration-tests,phase-2,phase-3,phase-4,phase-5" \
  ""

create_issue \
  "[Quality] Code Review and Cleanup" \
  "## Objective
Final code review, cleanup, and quality improvements.

## Tasks
- [ ] Run code linting (flake8/black)
- [ ] Fix all linting issues
- [ ] Review code for best practices
- [ ] Remove commented-out code
- [ ] Remove debug statements
- [ ] Check for hardcoded values
- [ ] Ensure consistent naming
- [ ] Add missing docstrings
- [ ] Check type hints

## Acceptance Criteria
- No linting errors
- Code follows PEP 8
- All functions documented
- Type hints present
- No hardcoded values

## Reference
- Architecture Plan Section 9.2" \
  "quality,phase-7" \
  "Phase 7: Documentation"

# ============================================================================
# SCRIPTS & AUTOMATION
# ============================================================================

create_issue \
  "[Scripts] Create Data Download Script" \
  "## Objective
Create script to download data from Kaggle.

## Tasks
- [ ] Create download_data.py script
- [ ] Add Kaggle API integration
- [ ] Add error handling
- [ ] Add progress indication
- [ ] Verify downloaded data
- [ ] Add logging

## Acceptance Criteria
- Script downloads data successfully
- Errors handled gracefully
- Progress is visible

## Files to Create
- scripts/download_data.py

## Reference
- Architecture Plan Phase 1" \
  "scripts,phase-1" \
  "Phase 1: Foundation"

create_issue \
  "[Scripts] Create Pipeline Execution Scripts" \
  "## Objective
Create convenient scripts to run each pipeline.

## Tasks
- [ ] Create run_data_preparation.py
- [ ] Create run_eda.py
- [ ] Create run_clustering.py
- [ ] Create run_modeling.py
- [ ] Create run_all_pipelines.py (master script)
- [ ] Add command-line arguments
- [ ] Add logging and progress
- [ ] Add error handling

## Acceptance Criteria
- Each pipeline can be run independently
- Arguments allow customization
- Progress is logged
- Errors are clear

## Files to Create
- scripts/run_data_preparation.py
- scripts/run_eda.py
- scripts/run_clustering.py
- scripts/run_modeling.py
- scripts/run_all_pipelines.py

## Reference
- Architecture Plan Section 2" \
  "scripts,phase-2,phase-3,phase-4,phase-5" \
  ""

create_issue \
  "[Scripts] Create Report Generation Script" \
  "## Objective
Create script to generate final technical report.

## Tasks
- [ ] Create generate_report.py script
- [ ] Aggregate results from all pipelines
- [ ] Generate visualizations
- [ ] Compile markdown document
- [ ] Convert to PDF (optional: pandoc/weasyprint)
- [ ] Add timestamp and metadata

## Acceptance Criteria
- Report generates automatically
- All sections included
- Visualizations embedded
- PDF output available

## Files to Create
- scripts/generate_report.py

## Reference
- Architecture Plan Section 2" \
  "scripts,phase-7" \
  "Phase 7: Documentation"

# ============================================================================
# FINAL DELIVERABLES
# ============================================================================

create_issue \
  "[Deliverable] Final Code Review & Reproducibility Check" \
  "## Objective
Ensure code is fully reproducible and meets all requirements.

## Tasks
- [ ] Clone repository in fresh environment
- [ ] Follow setup instructions
- [ ] Run all pipelines end-to-end
- [ ] Verify all outputs are generated
- [ ] Check all tests pass
- [ ] Verify dashboard launches
- [ ] Review all documentation
- [ ] Check acceptance criteria from project brief

## Acceptance Criteria
- Code runs end-to-end without errors
- All deliverables present
- Documentation is complete
- Acceptance criteria checked off

## Reference
- Project Brief Section 7" \
  "deliverable,phase-7,critical" \
  "Phase 7: Documentation"

create_issue \
  "[Deliverable] Package Final Submission" \
  "## Objective
Package all deliverables for final submission.

## Tasks
- [ ] Verify technical document (PDF/MD) is complete
- [ ] Verify code repository is organized and documented
- [ ] Verify dashboard is functional
- [ ] Verify executive presentation is complete
- [ ] Create submission checklist
- [ ] Check all acceptance criteria
- [ ] Zip or package if needed
- [ ] Submit by deadline

## Acceptance Criteria
- All 4 deliverables present and complete
- All acceptance criteria met
- Submission is professional
- Submitted before Dec 1

## Reference
- Project Brief Sections 6, 7" \
  "deliverable,phase-7,critical" \
  "Phase 7: Documentation"

echo -e "\n${GREEN}All issues created successfully!${NC}"
echo -e "${BLUE}Total issues created: ~60${NC}"
echo ""
echo "To view the project:"
echo "  gh project list --owner @me"
echo ""
echo "To view all issues:"
echo "  gh issue list --limit 100"
