# GitHub Issues Summary - Sales Pattern Analysis

**Total Issues Created: 64**
**Repository:** [julihocc/2513-MA2003B-Reto](https://github.com/julihocc/2513-MA2003B-Reto)

---

## 📊 Issue Distribution by Phase

| Phase | Count | Issues | Grade Weight | Priority |
|-------|-------|--------|--------------|----------|
| **Phase 1: Foundation** | 11 | #1-11 | Setup | Start Here |
| **Phase 2: Data Prep** | 8 | #12-19 | 15% | High |
| **Phase 3: EDA** | 6 | #20-25 | 15% | High |
| **Phase 4: Clustering** | 10 | #26-27, #35-41, #58 | **30%** | **CRITICAL** ⭐ |
| **Phase 5: Modeling** | 10 | #28-29, #42-48, #59 | **30%** | **CRITICAL** ⭐ |
| **Phase 6: Dashboard** | 9 | #30, #49-55, #64 | 10% | Medium |
| **Phase 7: Docs/Delivery** | 7 | #31-34, #57, #60, #63 | Required | **CRITICAL** ⭐ |
| **Supporting** | 3 | #56, #61-62 | - | Ongoing |

---

## 🎯 Quick Start Guide

### Step 1: Create GitHub Project Board

1. Visit: https://github.com/julihocc/2513-MA2003B-Reto/projects/new
2. Choose **"Board"** template
3. Name it: **"Sales Pattern Analysis - Implementation"**
4. Add description from project brief

### Step 2: Add Issues to Project

```bash
# View all issues
gh issue list --limit 100

# Add issues to project (after creating it)
# Go to each issue and manually add to project via GitHub UI
# OR use GitHub CLI once project is created
```

### Step 3: Organize Project Board

**Suggested Columns:**
- 📋 **Backlog** - Not started
- 🏗️ **Phase 1-2** - Foundation & Data
- 🔍 **Phase 3** - EDA
- 🎯 **Phase 4** - Clustering (30%)
- 🤖 **Phase 5** - Modeling (30%)
- 📊 **Phase 6** - Dashboard
- 📝 **Phase 7** - Documentation
- ✅ **Done**

**OR simpler columns:**
- 📋 Todo
- 🏃 In Progress
- 👀 Review
- ✅ Done

---

## 📋 Detailed Issue List

### 🏗️ **Phase 1: Foundation & Setup** (Start Here!)

| Issue | Title | Priority |
|-------|-------|----------|
| #1 | [Setup] Initialize Project Structure | 🔴 Start |
| #2 | [Setup] Configure Development Environment | 🔴 Start |
| #3 | [Setup] Configure Logging System | High |
| #4 | [Setup] Implement Configuration Management | High |
| #5 | [Infrastructure] Implement Data Loader Module | High |
| #6 | [Infrastructure] Implement Data Validator | High |
| #7 | [Infrastructure] Implement Model Repository | Medium |
| #8 | [Data] Download and Document Raw Data | 🔴 Start |
| #9 | [Scripts] Create Data Download Script | High |
| #10 | [Testing] Set Up Testing Framework | High |
| #11 | [Documentation] Create README | Medium |

**Start with:** #1, #2, #8 (project structure, environment, data)

---

### 🔧 **Phase 2: Data Preparation**

| Issue | Title | Priority |
|-------|-------|----------|
| #12 | [Domain] Implement Data Cleaning Module | High |
| #13 | [Domain] Implement Data Transformation Module | High |
| #14 | [Domain] Implement Temporal Feature Engineering | High |
| #15 | [Domain] Implement RFM Feature Engineering | Medium |
| #16 | [Domain] Implement Aggregation Features | High |
| #17 | [Application] Implement Data Preparation Pipeline | High |
| #18 | [Documentation] Create Data Dictionary | 🔴 Required |
| #19 | [Documentation] Create Cleaning Log (Bitácora) | 🔴 Required |

**Critical for grading:** #19 (Cleaning Log = 15% of grade)

---

### 🔍 **Phase 3: Exploratory Data Analysis**

| Issue | Title | Priority |
|-------|-------|----------|
| #20 | [Domain] Implement EDA Service | High |
| #21 | [Domain] Implement Time Series Analysis | High |
| #22 | [Domain] Implement KPI Calculator | High |
| #23 | [Application] Implement EDA Pipeline | High |
| #24 | [Notebooks] Create EDA Notebook | 🔴 High |
| #25 | [Application] Implement Analyze Seasonality Use Case | Medium |

**Critical for grading:** #24 (EDA Notebook = 15% of grade)

---

### 🎯 **Phase 4: Clustering (30% OF GRADE!) ⭐⭐⭐**

| Issue | Title | Priority |
|-------|-------|----------|
| #26 | [Domain] Implement Complete Clustering System | 🔴 Parent |
| #27 | [Notebooks] Create Clustering Experiments Notebook | 🔴🔴🔴 CRITICAL |
| #35 | [Domain/Clustering] Implement Base Clusterer | 🔴 Critical |
| #36 | [Domain/Clustering] Implement K-Means Clusterer | 🔴 Critical |
| #37 | [Domain/Clustering] Implement DBSCAN Clusterer | 🔴 Critical |
| #38 | [Domain/Clustering] Implement GMM Clusterer | 🔴 Critical |
| #39 | [Domain/Clustering] Implement Cluster Optimizer | 🔴🔴 Critical |
| #40 | [Domain/Clustering] Implement Cluster Interpreter | 🔴🔴 Critical |
| #41 | [Application/Clustering] Implement Clustering Pipeline | 🔴 Critical |
| #58 | [Application] Implement Segment Products Use Case | Medium |

**MOST CRITICAL:** #27 (Clustering Notebook) - This is worth 30% of your grade!

**Key Success Metrics:**
- Silhouette score > 0.5
- Test K-Means, DBSCAN, and GMM
- Strong justification for algorithm selection
- Clear business interpretation of clusters

---

### 🤖 **Phase 5: Predictive Modeling (30% OF GRADE!) ⭐⭐⭐**

| Issue | Title | Priority |
|-------|-------|----------|
| #28 | [Domain] Implement Complete Modeling System | 🔴 Parent |
| #29 | [Notebooks] Create Modeling Experiments Notebook | 🔴🔴🔴 CRITICAL |
| #42 | [Domain/Models] Implement Base Model | 🔴 Critical |
| #43 | [Domain/Models] Implement Regression Models | 🔴 Critical |
| #44 | [Domain/Models] Implement Ensemble Models | 🔴 Critical |
| #45 | [Domain/Models] Implement Time Series Models | 🔴 Critical |
| #46 | [Domain/Models] Implement Model Factory | Medium |
| #47 | [Domain/Models] Implement Model Evaluator | 🔴🔴 Critical |
| #48 | [Application/Models] Implement Modeling Pipeline | 🔴 Critical |
| #59 | [Application] Implement Predict Demand Use Case | Medium |

**MOST CRITICAL:** #29 (Modeling Notebook) - This is worth 30% of your grade!

**Key Success Metrics:**
- MAPE < 15% (if feasible)
- R² > 0.7 (if feasible)
- Must compare against baseline
- Cross-validation required
- Test multiple model types

---

### 📊 **Phase 6: Dashboard (10% of grade)**

| Issue | Title | Priority |
|-------|-------|----------|
| #30 | [Presentation] Implement Complete Dashboard | 🔴 Parent |
| #49 | [Presentation/Dashboard] Implement Dashboard Structure | High |
| #50 | [Presentation/Dashboard] Implement Overview Page | High |
| #51 | [Presentation/Dashboard] Implement Seasonality Page | High |
| #52 | [Presentation/Dashboard] Implement Clusters Page | 🔴 Critical |
| #53 | [Presentation/Dashboard] Implement Predictions Page | 🔴 Critical |
| #54 | [Presentation/Dashboard] Implement Reusable Components | Medium |
| #55 | [Presentation/Dashboard] Dashboard Testing & Refinement | Medium |
| #64 | [Documentation] Create User Guide | Medium |

**Key Success Metric:** Users can find insights in < 5 minutes

---

### 📝 **Phase 7: Documentation & Delivery (REQUIRED)**

| Issue | Title | Priority |
|-------|-------|----------|
| #31 | [Documentation] Create Complete Technical Document | 🔴🔴🔴 REQUIRED |
| #32 | [Presentation] Create Executive Presentation | 🔴🔴 REQUIRED |
| #33 | [Deliverable] Final Reproducibility Check | 🔴🔴 REQUIRED |
| #34 | [Deliverable] Package Final Submission | 🔴🔴 REQUIRED |
| #57 | [Scripts] Create Report Generation Script | Medium |
| #60 | [Application] Implement Generate Recommendations Use Case | 🔴 Critical |
| #63 | [Quality] Code Review and Cleanup | High |

**DEADLINE:** December 1, 2025

---

### 🔧 **Supporting Tasks (Ongoing)**

| Issue | Title | Priority |
|-------|-------|----------|
| #56 | [Scripts] Create Pipeline Execution Scripts | High |
| #61 | [Testing] Write Unit Tests for All Modules | High |
| #62 | [Testing] Write Integration Tests for Pipelines | High |

**Target:** >80% test coverage

---

## 🎯 Recommended Implementation Order

### **Week 1: Foundation & Data (Nov 21-27)**
1. ✅ **Day 1-2:** #1, #2, #8, #9 (Setup + Download Data)
2. ✅ **Day 3-4:** #3, #4, #10, #11 (Config, Logging, Tests, README)
3. ✅ **Day 5-7:** #5, #6, #12, #13, #18, #19 (Infrastructure + Data Prep + Documentation)

### **Week 2: EDA & Start Clustering (Nov 28 - Dec 4)**
1. ✅ **Day 1-2:** #14, #15, #16, #17 (Feature Engineering + Pipeline)
2. ✅ **Day 3-4:** #20, #21, #22, #23, #24 (EDA - 15% of grade!)
3. ✅ **Day 5-7:** #35, #36, #37, #38 (Start Clustering implementations)

### **Week 3: Clustering & Modeling (Dec 5-11)** ⚠️ CRITICAL WEEK
1. ✅ **Day 1-2:** #39, #40, #41 (Cluster Optimizer, Interpreter, Pipeline)
2. ✅ **Day 3-4:** #27 (Clustering Notebook - 30% of grade!)
3. ✅ **Day 5-7:** #42, #43, #44, #45 (Start Model implementations)

### **Week 4: Modeling & Dashboard (Dec 12-18)** ⚠️ CRITICAL WEEK
1. ✅ **Day 1-2:** #46, #47, #48 (Model Factory, Evaluator, Pipeline)
2. ✅ **Day 3-4:** #29 (Modeling Notebook - 30% of grade!)
3. ✅ **Day 5-7:** #49, #50, #51, #52, #53 (Dashboard)

### **Week 5: Final Push (Dec 19-25)**
1. ✅ **Day 1-2:** #54, #55, #64 (Dashboard completion)
2. ✅ **Day 3-4:** #60, #31 (Recommendations + Technical Doc)
3. ✅ **Day 5-7:** #32, #33, #63 (Presentation + Review + Cleanup)

### **Week 6: Buffer & Submission (Dec 26-30)**
1. ✅ **Day 1-3:** Final testing, reproducibility check (#33)
2. ✅ **Day 4-5:** Final polish and packaging (#34)
3. ✅ **Day 6:** **SUBMIT by Dec 1!** (leave buffer for issues)

---

## 🚨 Critical Path (DO NOT SKIP!)

These issues are make-or-break for your grade:

1. **#19** - Cleaning Log (Bitácora) - **15% of grade**
2. **#24** - EDA Notebook - **15% of grade**
3. **#27** - Clustering Experiments Notebook - **30% of grade** ⭐⭐⭐
4. **#29** - Modeling Experiments Notebook - **30% of grade** ⭐⭐⭐
5. **#31** - Technical Document - **Required deliverable**
6. **#32** - Executive Presentation - **Required deliverable**
7. **#33** - Reproducibility Check - **Required for acceptance**
8. **#34** - Final Submission - **Must be done by Dec 1**

**Combined weight of critical notebooks: 90% of your grade!**

---

## 📊 Useful Commands

### View Issues by Phase
```bash
gh issue list --label "phase-1"
gh issue list --label "phase-4" --label "critical"
```

### View Critical Issues Only
```bash
gh issue list --label "critical"
gh issue list --label "high-weight"
gh issue list --label "required"
```

### View by Component
```bash
gh issue list --label "clustering"
gh issue list --label "models"
gh issue list --label "dashboard"
```

### Close an Issue
```bash
gh issue close <issue-number> --comment "Completed: [brief description]"
```

---

## 📈 Progress Tracking

You can track overall progress with this command:
```bash
gh issue list --state closed --json number,title --jq 'length' && echo "issues completed out of 64"
```

Or by phase:
```bash
gh issue list --label "phase-1" --state closed --json number | jq 'length'
```

---

## 🎓 Grading Rubric Reminder

| Criterion | Weight | Key Issues |
|-----------|--------|------------|
| Data Quality & Traceability | 15% | #19 (Cleaning Log) |
| EDA & Substantive Findings | 15% | #24 (EDA Notebook) |
| Clustering | 30% | #27 (Clustering Notebook), #39, #40 |
| Predictive Modeling | 30% | #29 (Modeling Notebook), #47 |
| Dashboard & Storytelling | 10% | #30, #52, #53 |

**Total: 100%**

**Required Deliverables (Acceptance Criteria):**
- ✅ Technical Document (#31)
- ✅ Reproducible Code (All)
- ✅ Dashboard (#30)
- ✅ Executive Presentation (#32)

---

## 🔗 Quick Links

- **All Issues:** https://github.com/julihocc/2513-MA2003B-Reto/issues
- **Project Board:** (Create at https://github.com/julihocc/2513-MA2003B-Reto/projects/new)
- **Architecture Plan:** [ARCHITECTURE_PLAN.md](./ARCHITECTURE_PLAN.md)
- **Project Brief:** [Proyecto_ Análisis de Patrones de Ventas.md](./Proyecto_%20Análisis%20de%20Patrones%20de%20Ventas.md)

---

**Last Updated:** November 21, 2025
**Deadline:** December 1, 2025
**Status:** Ready to start! 🚀
