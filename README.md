# 🔭 AI-Enabled Data Observability

An AI-powered data observability system designed to monitor the reliability, quality, freshness, and consistency of data before it is used for analytics and decision-making.

## 📌 Project Overview

Modern applications depend on large volumes of data. Even small issues such as missing values, duplicate records, outdated data, schema changes, or unusual data patterns can affect the accuracy of analytics.

This project provides a centralized data observability system that automatically monitors important data health indicators and presents them through an interactive Streamlit dashboard.

## 🎯 Objectives

- Monitor data quality and identify missing values.
- Detect duplicate records.
- Monitor data freshness.
- Detect schema and data type changes.
- Identify unusual data patterns using Artificial Intelligence.
- Calculate an overall Data Health Score.
- Provide an interactive dashboard for monitoring data health.

## ⚙️ System Workflow

```text
Data Source
    ↓
Data Ingestion
    ↓
PostgreSQL / Dataset
    ↓
Data Quality Monitoring
    ↓
Freshness Monitoring
    ↓
Schema Monitoring
    ↓
AI Anomaly Detection
    ↓
Observability Engine
    ↓
Data Health Score
    ↓
Streamlit Dashboard
