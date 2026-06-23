# Algorithmic Economy

## A Data Analysis of YouTube's Attention Economy in the Age of Monetized Content

---

## Background

Social media platforms have transformed attention into a valuable economic resource. Creators, businesses, institutions, and public figures increasingly depend on visibility, engagement, and audience reach to generate income, influence, and cultural relevance.

This project introduces the concept of the **Algorithmic Economy**, defined as a digital ecosystem in which platform algorithms allocate visibility, and that visibility can be converted into economic, social, and cultural value.

While traditional economies allocate resources such as labor, land, and capital, modern digital platforms allocate a different resource: **attention**.

On YouTube, visibility is not distributed uniformly. Instead, content is surfaced through multiple discovery systems that determine what users see and what creators are rewarded for producing.

This project investigates how these algorithmic pathways shape content visibility and whether algorithmic success can be explained and predicted using data science and machine learning techniques.

---

## Research Problem

In traditional economies, access to productive resources often determines economic outcomes.

In social media ecosystems, visibility functions as a form of capital.

However, visibility is not distributed equally. Instead, it is mediated through algorithmic systems that influence what content users encounter and what content creators are incentivized to produce.

The central question of this project is:

> How does YouTube allocate visibility across different content types, and what characteristics are associated with engagement and virality within the platform's attention economy?

---

## Research Objectives

This project seeks to:

1. Identify content categories that generate the highest engagement.
2. Examine how YouTube's discovery pathways influence content visibility.
3. Investigate which content characteristics are associated with higher engagement.
4. Explore the relationship between content structure and algorithmic success.
5. Build machine learning models capable of predicting virality.
6. Interpret findings through the lens of the Algorithmic Economy framework.

---

## Research Questions

### ❓ RQ1: What content categories generate the highest engagement?

#### Metrics

- Views
- Likes
- Comments
- Engagement Rate

#### Expected Output

- Ranked category performance
- Engagement distribution visualizations
- Category-level comparison charts

---

### ❓ RQ2: How do YouTube discovery pathways differ?

#### Discovery Sources

- Trending
- Search
- Recent Uploads
- Channel Sampling

#### Questions

- Which content categories dominate each discovery pathway?
- Which pathways generate the highest visibility?
- Are some categories amplified disproportionately?

#### Expected Output

- Source vs Category analysis
- Distribution visualizations
- Cross-tabulation analysis

---

### ❓ RQ3: Which content characteristics are associated with engagement?

#### Variables

- Category
- Duration
- Tags
- Posting time
- Discovery source
- Publishing patterns

#### Expected Output

- Correlation analysis
- Feature relationship visualizations
- Statistical summaries

---

### ❓ RQ4: Does video duration influence engagement?

#### Questions

- Do shorter videos outperform longer videos?
- Is there an optimal duration range for engagement?
- Does duration influence virality?

#### Expected Output

- Duration distributions
- Duration vs Engagement analysis
- Duration vs Virality analysis

---

### ❓ RQ5: Can virality be predicted?

#### Definition

For this project, a viral video is operationally defined as a video whose view count falls within the **top 10% of all videos in the dataset**.

#### Expected Output

- Binary classification model
- Model evaluation metrics
- Feature importance analysis
- Virality prediction pipeline

---

### ❓ RQ6: What does YouTube appear to reward?

#### Questions

- Which features contribute most to engagement?
- Which features contribute most to virality?
- What patterns emerge among highly visible videos?

#### Expected Output

- Feature importance rankings
- Model interpretation
- Algorithmic Economy analysis

---

## Dataset

The dataset was collected using the **YouTube Data API v3** through a custom-built data collection pipeline.

The collection process samples videos through multiple discovery mechanisms:

- Trending videos
- Search-based discovery
- Recent uploads
- Channel-based sampling

Each collected record contains metadata including:

- Video ID
- Title
- Description
- Channel information
- Category
- Tags
- Publication timestamp
- Duration
- View count
- Like count
- Comment count

The dataset represents a structured sample of YouTube's visibility ecosystem rather than a complete population of all uploaded videos.

---

## Data Processing

The raw dataset undergoes several preprocessing and feature engineering steps.

### Data Cleaning

- Duplicate removal using `video_id`
- Missing value handling
- Data type standardization

### Feature Engineering

#### Temporal Features

- Hour of publication
- Day of week

#### Duration Features

YouTube durations are provided in ISO 8601 format (e.g., `PT4M50S`).

These are transformed into:

- Duration in seconds
- Duration in minutes
- Short-form indicator

#### Engagement Features

- Like Rate
- Comment Rate
- Total Engagement
- Engagement Rate

#### Log Transformations

To address highly skewed distributions:

- Log Views
- Log Likes
- Log Comments
- Log Engagement

#### Tag Features

- Tag Count
- Tag Presence Indicator

#### Category Features

YouTube category IDs are mapped to human-readable category names while retaining numeric identifiers for machine learning.

#### Virality Label

A binary virality label is generated using the 90th percentile of views:

- Viral = Top 10% of videos by view count
- Non-Viral = Remaining 90%

---

## Methodology

### Phase 1 — Data Collection

- YouTube Data API v3
- Multi-source collection pipeline

### Phase 2 — Data Cleaning

- Validation
- Deduplication
- Feature creation

### Phase 3 — Exploratory Data Analysis

- Category analysis
- Discovery pathway analysis
- Engagement analysis

### Phase 4 — Machine Learning

- Virality prediction
- Feature importance analysis
- Model evaluation

---

## Conceptual Framework: The Algorithmic Economy

This project treats YouTube as an economic system in which visibility functions as a scarce resource.

Within this framework:

- Algorithms act as allocation mechanisms.
- Engagement functions as market feedback.
- Visibility functions as capital.
- Virality functions as extreme concentration of attention.

The objective is not merely to identify high-performing content, but to understand the underlying allocation patterns that shape success within the platform.

---

## Findings

_To be completed._

---

## Limitations

- API-based sampling does not capture the full YouTube population.
- YouTube recommendation systems remain proprietary and cannot be directly observed.
- Engagement metrics are proxies for attention and do not necessarily measure quality.
- Trending content represents only one component of YouTube's broader visibility ecosystem.

---

## Future Work

- Expand dataset size beyond 50,000 videos.
- Improve channel-based sampling coverage.
- Incorporate Natural Language Processing (NLP) features from titles, descriptions, and tags.
- Compare findings across multiple countries and regions.
- Extend analysis to additional platforms such as Reddit or X.
- Explore deep learning approaches for virality prediction.

---
