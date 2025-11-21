#!/usr/bin/env python3
"""
Script to create detailed sub-issues for the Sales Pattern Analysis project.
This adds all the granular component-level issues.
"""

import subprocess
import json
import sys

class Colors:
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    YELLOW = '\033[1;33m'
    RED = '\033[0;31m'
    NC = '\033[0m'

def run_command(cmd: list, capture_output: bool = True) -> subprocess.CompletedProcess:
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=capture_output,
            text=True,
            check=True
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}Error running command: {' '.join(cmd)}{Colors.NC}")
        print(f"{Colors.RED}{e.stderr}{Colors.NC}")
        sys.exit(1)

def create_issue(title: str, body: str, labels: list, repo: str) -> str:
    """Create a GitHub issue and return its URL."""
    print(f"\n{Colors.GREEN}Creating issue: {title}{Colors.NC}")

    cmd = [
        'gh', 'issue', 'create',
        '--title', title,
        '--body', body,
        '--repo', repo
    ]

    for label in labels:
        cmd.extend(['--label', label])

    result = run_command(cmd)
    issue_url = result.stdout.strip()
    print(f"Created: {issue_url}")
    return issue_url

def main():
    print(f"{Colors.BLUE}Creating Detailed GitHub Issues{Colors.NC}\n")

    result = run_command(['gh', 'repo', 'view', '--json', 'nameWithOwner'])
    repo_info = json.loads(result.stdout)
    repo = repo_info['nameWithOwner']
    print(f"Repository: {repo}\n")

    issues_created = 0

    # ========================================================================
    # PHASE 4: CLUSTERING - DETAILED BREAKDOWN
    # ========================================================================

    print(f"\n{Colors.BLUE}{'='*70}{Colors.NC}")
    print(f"{Colors.BLUE}PHASE 4: Clustering - Detailed Components{Colors.NC}")
    print(f"{Colors.BLUE}{'='*70}{Colors.NC}")

    create_issue(
        title="[Domain/Clustering] Implement Base Clusterer",
        body="""## Objective
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
- Architecture Plan Section 3.2
- Parent Issue: #26

## Dependencies
- Must complete infrastructure setup first""",
        labels=["domain", "clustering", "phase-4", "critical"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Domain/Clustering] Implement K-Means Clusterer",
        body="""## Objective
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
- Architecture Plan Section 3.2
- Parent Issue: #26

## Dependencies
- Depends on Base Clusterer implementation""",
        labels=["domain", "clustering", "phase-4", "critical"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Domain/Clustering] Implement DBSCAN Clusterer",
        body="""## Objective
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
- Architecture Plan Section 3.2
- Parent Issue: #26

## Dependencies
- Depends on Base Clusterer implementation""",
        labels=["domain", "clustering", "phase-4", "critical"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Domain/Clustering] Implement GMM Clusterer",
        body="""## Objective
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
- Architecture Plan Section 3.2
- Parent Issue: #26

## Dependencies
- Depends on Base Clusterer implementation""",
        labels=["domain", "clustering", "phase-4", "critical"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Domain/Clustering] Implement Cluster Optimizer",
        body="""## Objective
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
- Architecture Plan Section 3.2
- Parent Issue: #26

## Critical for Grading
This is essential for the 30% clustering grade - must justify k selection!""",
        labels=["domain", "clustering", "phase-4", "critical", "high-weight"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Domain/Clustering] Implement Cluster Interpreter",
        body="""## Objective
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
- Architecture Plan Section 3.2
- Parent Issue: #26

## Critical for Grading
Business interpretation is key for the 30% clustering grade!""",
        labels=["domain", "clustering", "phase-4", "critical", "high-weight"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Application/Clustering] Implement Clustering Pipeline",
        body="""## Objective
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
- Architecture Plan Section 3.3
- Parent Issue: #26

## Dependencies
- All clustering components must be complete""",
        labels=["application", "pipeline", "phase-4", "critical"],
        repo=repo
    )
    issues_created += 1

    # ========================================================================
    # PHASE 5: PREDICTIVE MODELING - DETAILED BREAKDOWN
    # ========================================================================

    print(f"\n{Colors.BLUE}{'='*70}{Colors.NC}")
    print(f"{Colors.BLUE}PHASE 5: Predictive Modeling - Detailed Components{Colors.NC}")
    print(f"{Colors.BLUE}{'='*70}{Colors.NC}")

    create_issue(
        title="[Domain/Models] Implement Base Model",
        body="""## Objective
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
- Architecture Plan Section 3.2
- Parent Issue: #28""",
        labels=["domain", "models", "phase-5", "critical"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Domain/Models] Implement Regression Models",
        body="""## Objective
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
- Architecture Plan Section 3.2
- Parent Issue: #28

## Dependencies
- Depends on Base Model implementation""",
        labels=["domain", "models", "phase-5", "critical"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Domain/Models] Implement Ensemble Models",
        body="""## Objective
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
- Architecture Plan Section 3.2, Project Brief Section 4.5
- Parent Issue: #28

## Dependencies
- Depends on Base Model implementation""",
        labels=["domain", "models", "phase-5", "critical", "high-weight"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Domain/Models] Implement Time Series Models",
        body="""## Objective
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
- Architecture Plan Section 3.2, Project Brief Section 4.5
- Parent Issue: #28

## Dependencies
- Depends on Base Model implementation""",
        labels=["domain", "models", "phase-5", "critical"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Domain/Models] Implement Model Factory",
        body="""## Objective
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
- Architecture Plan Section 4.2
- Parent Issue: #28""",
        labels=["domain", "models", "phase-5"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Domain/Models] Implement Model Evaluator",
        body="""## Objective
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
- Architecture Plan Section 3.2
- Parent Issue: #28

## Critical for Grading
Baseline comparison is required for the 30% modeling grade!""",
        labels=["domain", "models", "phase-5", "critical", "high-weight"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Application/Models] Implement Modeling Pipeline",
        body="""## Objective
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
- Architecture Plan Section 3.3
- Parent Issue: #28

## Dependencies
- All model components must be complete""",
        labels=["application", "pipeline", "phase-5", "critical", "high-weight"],
        repo=repo
    )
    issues_created += 1

    # ========================================================================
    # PHASE 6: DASHBOARD - DETAILED BREAKDOWN
    # ========================================================================

    print(f"\n{Colors.BLUE}{'='*70}{Colors.NC}")
    print(f"{Colors.BLUE}PHASE 6: Dashboard - Detailed Components{Colors.NC}")
    print(f"{Colors.BLUE}{'='*70}{Colors.NC}")

    create_issue(
        title="[Presentation/Dashboard] Implement Dashboard Structure",
        body="""## Objective
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
- Architecture Plan Section 3.4
- Parent Issue: #30""",
        labels=["presentation", "dashboard", "phase-6"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Presentation/Dashboard] Implement Overview Page",
        body="""## Objective
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
- Architecture Plan Section 3.4
- Parent Issue: #30""",
        labels=["presentation", "dashboard", "phase-6"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Presentation/Dashboard] Implement Seasonality Page",
        body="""## Objective
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
- Architecture Plan Section 3.4, Project Brief Section 2
- Parent Issue: #30""",
        labels=["presentation", "dashboard", "phase-6"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Presentation/Dashboard] Implement Clusters Page",
        body="""## Objective
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
- Architecture Plan Section 3.4, Project Brief Section 4.4
- Parent Issue: #30""",
        labels=["presentation", "dashboard", "phase-6", "critical"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Presentation/Dashboard] Implement Predictions Page",
        body="""## Objective
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
- Architecture Plan Section 3.4, Project Brief Section 4.5
- Parent Issue: #30""",
        labels=["presentation", "dashboard", "phase-6", "critical"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Presentation/Dashboard] Implement Reusable Components",
        body="""## Objective
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
- Architecture Plan Section 3.4
- Parent Issue: #30""",
        labels=["presentation", "dashboard", "phase-6"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Presentation/Dashboard] Dashboard Testing & Refinement",
        body="""## Objective
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
- Architecture Plan Section 12
- Parent Issue: #30""",
        labels=["presentation", "dashboard", "testing", "phase-6"],
        repo=repo
    )
    issues_created += 1

    # ========================================================================
    # SCRIPTS & USE CASES
    # ========================================================================

    print(f"\n{Colors.BLUE}{'='*70}{Colors.NC}")
    print(f"{Colors.BLUE}Additional Components{Colors.NC}")
    print(f"{Colors.BLUE}{'='*70}{Colors.NC}")

    create_issue(
        title="[Scripts] Create Pipeline Execution Scripts",
        body="""## Objective
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
- Architecture Plan Section 2""",
        labels=["scripts", "phase-2", "phase-3", "phase-4", "phase-5"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Scripts] Create Report Generation Script",
        body="""## Objective
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
- Architecture Plan Section 2""",
        labels=["scripts", "phase-7"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Application] Implement Segment Products Use Case",
        body="""## Objective
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
- Architecture Plan Section 3.3, Project Brief Section 4.4""",
        labels=["application", "use-case", "phase-4"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Application] Implement Predict Demand Use Case",
        body="""## Objective
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
- Architecture Plan Section 3.3, Project Brief Section 4.5""",
        labels=["application", "use-case", "phase-5"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Application] Implement Generate Recommendations Use Case",
        body="""## Objective
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
- Architecture Plan Section 3.3, Project Brief Sections 2, 4.7""",
        labels=["application", "use-case", "phase-7", "critical"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Testing] Write Unit Tests for All Modules",
        body="""## Objective
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
- Architecture Plan Section 6.1""",
        labels=["testing", "phase-1", "phase-2", "phase-3", "phase-4", "phase-5"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Testing] Write Integration Tests for Pipelines",
        body="""## Objective
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
- Architecture Plan Section 6.2""",
        labels=["testing", "phase-2", "phase-3", "phase-4", "phase-5"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Quality] Code Review and Cleanup",
        body="""## Objective
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
- Architecture Plan Section 9.2""",
        labels=["quality", "phase-7"],
        repo=repo
    )
    issues_created += 1

    create_issue(
        title="[Documentation] Create User Guide",
        body="""## Objective
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
- Project Brief Section 6, Deliverable 3""",
        labels=["documentation", "phase-6", "required"],
        repo=repo
    )
    issues_created += 1

    # Summary
    print(f"\n{Colors.GREEN}{'='*70}{Colors.NC}")
    print(f"{Colors.GREEN}Detailed Issue Creation Complete!{Colors.NC}")
    print(f"{Colors.GREEN}{'='*70}{Colors.NC}\n")
    print(f"{Colors.BLUE}Additional issues created: {issues_created}{Colors.NC}")
    print(f"\nRepository: {repo}")
    print(f"\n{Colors.YELLOW}Next Steps:{Colors.NC}")
    print(f"1. View all issues: gh issue list --limit 100")
    print(f"2. Create GitHub Project and add these issues")
    print(f"3. Start working through Phase 1!")

if __name__ == "__main__":
    main()
