# Algorithmic Economy

## Understanding Visibility as a Scarce Economic Resource on YouTube

_A Computational Social Science Research Project_

---

# Abstract

Digital platforms have transformed visibility into one of the most valuable resources of the modern economy.

Every day, millions of videos compete for a limited amount of user attention, yet only a small fraction receive widespread visibility. This unequal allocation of visibility has important consequences because visibility can subsequently be converted into economic, political, social and cultural value.

This project introduces the **Algorithmic Economy**, a conceptual framework that treats platform algorithms as allocators of scarce digital visibility rather than merely recommendation systems.

Using data collected directly from the YouTube Data API v3, this research investigates how visibility is distributed, what characteristics are associated with highly visible content, and whether visibility patterns can be modelled computationally.

---

# The Algorithmic Economy

Traditional economies allocate scarce resources such as:

- Land
- Labour
- Capital

Digital platforms allocate a different scarce resource:

> **Visibility**

Within the Algorithmic Economy,

```
Platform Algorithms
            │
            ▼
Allocate Visibility
            │
            ▼
Generate Attention
            │
            ▼
Produce Engagement
            │
            ▼
Create Economic,
Political,
Social and
Cultural Value
```

Visibility therefore functions as a form of digital capital.

---

# Research Problem

Millions of videos are uploaded to YouTube every day, yet only a very small proportion achieve widespread visibility.

Although considerable research has examined recommendation systems, platform governance, engagement prediction and content monetization, comparatively little attention has been devoted to understanding **visibility itself** as a scarce economic resource allocated through algorithmic systems.

Understanding how visibility is distributed—and the characteristics associated with highly visible content—is therefore increasingly important for creators, businesses, policymakers and researchers.

---

# Research Objectives

This project aims to:

1. Examine how visibility is distributed across YouTube.
2. Identify content categories associated with greater visibility.
3. Investigate content characteristics associated with visibility.
4. Examine the relationship between visibility and engagement.
5. Build machine learning models capable of predicting highly visible content.
6. Interpret the findings through the Algorithmic Economy framework.

---

# Research Questions

## RQ1

### Which content categories receive the greatest visibility?

Metrics

- Views
- Visibility distributions
- Category comparisons

Outputs

- Category rankings
- Distribution plots
- Statistical comparisons

---

## RQ2

### How is visibility distributed across YouTube's discovery ecosystem?

Questions

- Which content categories dominate different discovery mechanisms?
- Which discovery mechanisms expose highly visible content?
- Is visibility distributed equally across discovery mechanisms?

Outputs

- Cross-tabulations
- Distribution analysis
- Discovery comparisons

---

## RQ3

### Which content characteristics are associated with visibility?

Variables

- Category
- Duration
- Publication time
- Tags
- Discovery source

Outputs

- Correlation analysis
- Statistical testing
- Feature relationships

---

## RQ4

### Does video duration influence visibility?

Questions

- Do shorter videos receive greater visibility?
- Is there an optimal duration?
- Does duration influence engagement after visibility?

Outputs

- Duration distributions
- Visibility comparisons
- Engagement comparisons

---

## RQ5

### Can highly visible content be predicted?

Definition

Highly visible videos are operationally defined as videos whose view counts fall within the **top 10%** of the dataset.

Outputs

- Binary classification
- Model evaluation
- Feature importance
- Prediction pipeline

---

## RQ6

### What does YouTube appear to reward?

Questions

- Which characteristics are consistently associated with visibility?
- Which characteristics contribute most to engagement after visibility?
- What patterns characterize highly visible videos?

Outputs

- Feature importance
- Model interpretation
- Algorithmic Economy discussion

---

# Dataset

The dataset was collected directly from the **YouTube Data API v3** using a custom-built collection pipeline.

Videos were sampled through multiple discovery mechanisms:

- Trending
- Search
- Recent uploads

Each record contains:

- Video metadata
- Channel information
- Publication timestamp
- Duration
- Category
- Tags
- Views
- Likes
- Comments

Rather than representing the complete YouTube ecosystem, the dataset provides a structured sample of videos observed through different discovery mechanisms.

---

# Data Processing

## Cleaning

- Duplicate removal
- Missing value handling
- Data validation

## Feature Engineering

### Temporal Features

- Hour
- Day
- Month

### Duration Features

- Seconds
- Minutes

### Visibility Features

- Views
- Log Views

### Engagement Features

- Likes
- Comments
- Engagement Rate
- Like Rate
- Comment Rate

### Content Features

- Category
- Tag Count
- Tag Presence

### Visibility Label

A binary visibility label is created using the 90th percentile of view counts.

- High Visibility
- Low Visibility

---

# Methodology

```
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Exploratory Analysis
        │
        ▼
Statistical Analysis
        │
        ▼
Machine Learning
        │
        ▼
Algorithmic Economy Interpretation
```

---

# Repository Structure

```
collectors/
src/
    config.py
    query/
    utils/

data/
    raw/
    processed/

notebooks/

outputs/

README.md
```

---

# Current Progress

- ✅ Data collection pipeline completed
- ✅ Feature engineering completed
- ✅ Exploratory analysis underway
- 🔄 Statistical analysis underway
- 🔄 Machine learning in progress
- 🔄 Research manuscript in preparation

---

# Machine Learning

Planned models include

- Logistic Regression
- Random Forest
- XGBoost

Evaluation metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

# Expected Contributions

## Empirical

Provides one of the few computational analyses of visibility allocation using publicly collected YouTube data.

## Methodological

Demonstrates a reproducible pipeline for studying digital platforms using API-collected data.

## Conceptual

Introduces the **Algorithmic Economy**, a framework that conceptualizes platform algorithms as allocators of scarce digital visibility.

---

# Limitations

- API sampling cannot observe the complete YouTube ecosystem.
- Recommendation systems remain proprietary.
- Visibility allocation cannot be directly observed.
- Observed relationships should not be interpreted as causal algorithmic rules.

---

# Future Work

- Expand beyond 100,000 videos.
- Incorporate NLP features.
- Compare multiple countries.
- Extend the framework to TikTok, Instagram and X.
- Study longitudinal changes in visibility allocation.

---

# Author

**Innocent Josiah Patrick**

Computational Social Science • Machine Learning • Digital Sociology • Platform Studies
