Algorithmic Economy
Understanding Visibility as a Scarce Economic Resource on YouTube

A Computational Social Science Research Project

Abstract

Digital platforms have transformed visibility into an increasingly important resource in the contemporary digital economy.

Millions of videos compete for users' limited attention, yet visibility is distributed unevenly across content, creators, categories, and discovery pathways. This unequal distribution has important implications because visibility can subsequently facilitate attention, engagement, influence, and economic value.

This research introduces the Algorithmic Economy, a conceptual framework that treats digital visibility as a scarce resource whose distribution is shaped by platform algorithms and subsequently converted into different forms of value.

Using computational social science methods and data collected directly through the YouTube Data API v3, the study examines the distribution of video visibility, investigates characteristics associated with highly visible content, and develops machine-learning models for predicting highly visible videos.

The empirical analysis focuses on YouTube while the conceptual framework is intended to provide a broader theoretical lens for studying algorithmically mediated digital economies.

The Algorithmic Economy

Traditional economies allocate scarce resources such as:

Land
Labour
Capital

Digital platforms introduce another increasingly important resource:

Visibility

Within the Algorithmic Economy:

Platform Algorithms
│
▼
Visibility Allocation
│
▼
User Exposure
│
▼
Attention
│
▼
Engagement
│
▼
Economic, Political,
Social & Cultural Value

The framework therefore conceptualizes visibility as a form of digital capital: a resource that provides opportunities for content, creators, organizations, and other digital actors to attract attention and generate subsequent forms of value.

Research Problem

The enormous volume of content uploaded to digital platforms creates a fundamental problem of information abundance. Not every piece of content can receive equivalent exposure.

Platform algorithms therefore play an important role in determining which content is surfaced to users through recommendation, search, trending systems, and other forms of platform-mediated discovery.

Although existing scholarship has examined recommendation systems, platform governance, creator labour, attention, and monetization, this research focuses specifically on visibility as a scarce resource within the digital economy.

The study asks how visibility is distributed, which characteristics are associated with higher levels of visibility, and whether these patterns can be identified computationally.

Research Objectives

The study aims to:

Examine how visibility is distributed across YouTube content categories.
Examine how visibility varies across the discovery pathways represented in the dataset.
Identify content characteristics associated with higher levels of visibility.
Examine the relationship between video duration and visibility.
Develop machine-learning models capable of predicting highly visible content.
Interpret the empirical findings through the Algorithmic Economy framework.

## Research Questions

# RQ1 — Visibility Across Categories

Which YouTube content categories receive the greatest visibility?

The analysis examines:

View distributions
Mean views
Median views
Category-level differences
Distributional inequality

Statistical analysis includes:

ANOVA
Eta squared
Post-hoc comparisons

Status: Completed

# RQ2 — Content Characteristics and Visibility

Which observable content characteristics are associated with higher levels of visibility?

The analysis examines characteristics including:

Content category
Video duration
Publication time
Tags
Temporal characteristics
Discovery pathway

The objective is to determine which observable characteristics are systematically associated with differences in video visibility.

# RQ3 — Video Duration and Visibility

How is video duration associated with visibility on YouTube?

The analysis investigates:

The distribution of video duration
The relationship between duration and views
Differences in visibility across duration groups
Whether particular duration ranges are associated with higher visibility

Status: Pending

## RQ4 — Predicting Highly Visible Content

Can highly visible YouTube videos be predicted from observable content characteristics?

Highly visible videos are operationally defined as videos whose view counts fall within the top 10% of the study dataset.

The analysis uses machine-learning classification models to investigate whether observable characteristics can distinguish highly visible from less-visible videos.

Planned models include:

Logistic Regression
Random Forest
XGBoost

Evaluation will include:

Accuracy
Precision
Recall
F1 Score
ROC-AUC

Status: Pending

Dataset

The dataset was collected directly from the YouTube Data API v3 using a custom-built data collection pipeline.

The current dataset contains:

17,249 unique videos
36 variables

Variables include:

Video ID
Title
Description
Publication timestamp
Category
Duration
Channel information
Views
Likes
Comments
Engagement rate
Discovery source
Collection method
Collection region
Tags
Temporal features
Derived visibility features

The dataset does not represent the complete YouTube ecosystem. Instead, it constitutes a structured sample of videos obtained through the discovery mechanisms implemented in the research data-collection pipeline.

Data Collection

V1 used three YouTube API discovery mechanisms:

- Trending
- Search-based collection
- Recent-upload collection

The multiple collection pathways were designed to reduce dependence on a single discovery mechanism and provide different views of the YouTube content environment.

Importantly, these pathways are research sampling mechanisms, not direct measurements of YouTube's complete internal recommendation ecosystem.

Algorithmic Economy II uses the `video_id` column of the current [processed dataset](data/processed/youtube_clean.csv) as its sampling frame. The 17,249 videos in this file define the extension's cohort.

Data Processing
Data Cleaning

The preprocessing pipeline includes:

Duplicate removal
Missing-value assessment
Data validation
Variable standardization
Data-type conversion
Feature Engineering
Temporal Features
Publication hour
Publication day
Publication month
Duration Features
Duration in seconds
Duration in minutes
Visibility Features
Views
Log-transformed views
Engagement Features
Likes
Comments
Engagement rate
Like rate
Comment rate
Content Features
Category
Tag count
Tag presence
Visibility Classification

A binary visibility variable is created using the 90th percentile of view counts.

Top 10% of videos
│
▼
High Visibility

Remaining 90%
│
▼
Lower Visibility
Methodology

The empirical workflow follows:

YouTube Data API
│
▼
Data Collection
│
▼
Data Cleaning
│
▼
Feature Engineering
│
▼
Exploratory Data Analysis
│
▼
Statistical Analysis
│
▼
Machine Learning
│
▼
Algorithmic Economy Interpretation
Chapter Five — Empirical Findings

The empirical analysis is structured around four research questions:

RQ1
Visibility Across Categories
│
▼
RQ2
Content Characteristics
│
▼
RQ3
Video Duration
│
▼
RQ4
Predicting Highly Visible Content
Completed analysis

RQ1 — Visibility Across YouTube Categories

The first empirical analysis has been completed. It examines differences in visibility across YouTube content categories using descriptive statistics and inferential analysis.

The analysis includes:

Category distribution
Mean views
Median views
View distributions
Outlier analysis
ANOVA
Eta squared
Post-hoc comparisons

The current findings indicate that visibility differs substantially across content categories, while category membership alone explains only a portion of the variation in video views.

Current Research Progress
✅ Research framework developed
✅ Research questions defined
✅ YouTube API data collection pipeline completed
✅ Dataset assembled
✅ Data cleaning completed
✅ Feature engineering completed
✅ RQ1: Category-level visibility analysis completed
✅ RQ2: Content characteristics associated with visibility
✅ RQ3: Video duration and visibility
✅ RQ4: Machine-learning prediction
✅ Final empirical interpretation
✅ Research manuscript completion
Machine Learning

The machine-learning component investigates whether highly visible videos can be predicted from observable characteristics.

Candidate models:

Logistic Regression
Random Forest
XGBoost

Evaluation metrics:

Accuracy
Precision
Recall
F1 Score
ROC-AUC

Model interpretation will focus on identifying which observable characteristics contribute most strongly to the classification of highly visible content.

The machine-learning results will subsequently be interpreted through the Algorithmic Economy framework rather than being treated simply as a prediction exercise.

Expected Contributions
Empirical Contribution

Provides a computational analysis of YouTube visibility using a structured dataset collected through the YouTube Data API.

Methodological Contribution

Demonstrates how computational social science methods can be used to investigate patterns of digital visibility through API-collected platform data.

Conceptual Contribution

Develops the Algorithmic Economy as an integrative framework for understanding the relationship between:

Algorithms
↓
Visibility
↓
Attention
↓
Engagement
↓
Value

The framework does not claim to reveal YouTube's proprietary ranking algorithm. Instead, it provides a theoretical lens for interpreting observable patterns of visibility within an algorithmically mediated platform environment.

Important Limitation

The study measures observable visibility primarily through video view counts.

YouTube's internal recommendation and ranking systems are proprietary and cannot be directly observed through the YouTube Data API. Consequently, statistical associations between video characteristics and views should not be interpreted as proof that YouTube's algorithm directly rewards a particular characteristic.

The study identifies patterns associated with visibility, rather than recovering the causal decision rules of YouTube's recommendation system.

Other limitations include:

API-based sampling does not represent the complete YouTube ecosystem.
Discovery pathways in the dataset are research sampling mechanisms rather than exhaustive representations of YouTube's internal recommendation system.
View counts are influenced by multiple factors that cannot all be observed in the dataset.
Cross-sectional observational data cannot establish causal relationships between content characteristics and visibility.
Highly visible content may be influenced by external events, celebrity status, paid promotion, audience size, or factors unavailable through the API.
Future Research

Potential extensions include:

Expanding the dataset beyond 100,000 videos
Incorporating natural-language processing of titles and descriptions
Incorporating thumbnail or visual-content analysis
Comparing different countries or regions
Conducting longitudinal analysis of visibility
Extending the framework to other platforms such as TikTok, Instagram, and X
Developing comparative models of algorithmically mediated visibility across platforms
Repository Structure
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
Author

Innocent Josiah Patrick

Computational Social Science • Machine Learning • Digital Sociology • Platform Studies
