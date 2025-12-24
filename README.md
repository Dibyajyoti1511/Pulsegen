# App Review Trend Analysis using Agentic AI

## Overview
This project builds an agentic AI system to analyze Google Play Store reviews
and generate a rolling 30-day trend report of product issues, requests, and feedback.

## Why Agentic AI?
Traditional topic modeling (LDA, TopicBERT) fragments semantically similar issues.
This system avoids that using multiple cooperating agents.

## Agents
1. Review Ingestion Agent – daily batch ingestion
2. Topic Mining Agent – high recall extraction
3. Canonical Topic Agent – semantic deduplication
4. Trend Agent – rolling T-30 to T aggregation

## Output
A CSV table where:
- Rows = Canonical topics
- Columns = Dates (T-30 → T)
- Cells = Topic frequency per day

## Assumptions
- Offline batch processing
- English reviews
- Rule-based topic extraction for recall

## Limitations
- Topic rules can be expanded
- Clustering threshold may need tuning at larger scale
