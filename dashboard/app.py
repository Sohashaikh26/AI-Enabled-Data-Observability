import streamlit as st
import pandas as pd
from datetime import datetime


# =========================================
# PAGE CONFIGURATION
# =========================================

st.set_page_config(
    page_title="AI Data Observability",
    page_icon="🔭",
    layout="wide"
)


# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.stApp {
    background: #0e1117;
}


/* Remove extra top space */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}


/* Main text */
h1, h2, h3, h4 {
    color: white;
}


/* Gradient Header */

.hero {
    background: linear-gradient(
        135deg,
        #5b4bff,
        #2563eb,
        #06b6d4
    );

    padding: 35px;
    border-radius: 20px;
    margin-bottom: 25px;
}


.hero h1 {
    color: white;
    margin-bottom: 5px;
    font-size: 42px;
}


.hero p {
    color: #e5e7eb;
    font-size: 18px;
}


/* Metric Cards */

.metric-card {

    background: #181c25;

    border: 1px solid #2b3140;

    padding: 20px;

    border-radius: 16px;

    transition: 0.3s;

}


.metric-card:hover {

    border: 1px solid #6366f1;

    transform: translateY(-3px);

}


.metric-title {

    color: #9ca3af;

    font-size: 14px;

}


.metric-value {

    color: white;

    font-size: 30px;

    font-weight: bold;

    margin-top: 8px;

}


/* Section cards */

.section-card {

    background: #181c25;

    padding: 25px;

    border-radius: 18px;

    border: 1px solid #2b3140;

    margin-bottom: 20px;

}


/* Status cards */

.status-green {

    background: #12372a;

    padding: 15px;

    border-radius: 12px;

    border-left: 5px solid #22c55e;

    color: white;

}


.status-yellow {

    background: #3b2f12;

    padding: 15px;

    border-radius: 12px;

    border-left: 5px solid #f59e0b;

    color: white;

}


.status-red {

    background: #3b1618;

    padding: 15px;

    border-radius: 12px;

    border-left: 5px solid #ef4444;

    color: white;

}


/* Divider */

hr {

    border-color: #2b3140;

}


/* Footer */

.footer {

    text-align: center;

    color: #6b7280;

    padding: 20px;

}

</style>
""", unsafe_allow_html=True)


# =========================================
# LOAD DATA
# =========================================

data = pd.read_csv("../data/sales_data.csv")


# =========================================
# LOAD OBSERVABILITY RESULTS
# =========================================

try:

    results = pd.read_csv(
        "../data/observability_results.csv"
    )

    health_score = results["health_score"].iloc[0]

except:

    health_score = "N/A"


# =========================================
# BASIC CALCULATIONS
# =========================================

total_records = len(data)

missing_values = data.isnull().sum().sum()

duplicate_records = data.duplicated().sum()


# =========================================
# HEADER
# =========================================

st.markdown("""

<div class="hero">

<h1>🔭 AI Data Observability</h1>

<p>
Intelligent monitoring for data quality, freshness,
schema changes and AI-powered anomaly detection.
</p>

</div>

""", unsafe_allow_html=True)


# =========================================
# DASHBOARD OVERVIEW
# =========================================

st.markdown("## 📊 System Overview")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(f"""

    <div class="metric-card">

    <div class="metric-title">
    📁 TOTAL RECORDS
    </div>

    <div class="metric-value">
    {total_records}
    </div>

    </div>

    """, unsafe_allow_html=True)


with col2:

    st.markdown(f"""

    <div class="metric-card">

    <div class="metric-title">
    ⚠️ MISSING VALUES
    </div>

    <div class="metric-value">
    {missing_values}
    </div>

    </div>

    """, unsafe_allow_html=True)


with col3:

    st.markdown(f"""

    <div class="metric-card">

    <div class="metric-title">
    🔁 DUPLICATES
    </div>

    <div class="metric-value">
    {duplicate_records}
    </div>

    </div>

    """, unsafe_allow_html=True)


with col4:

    st.markdown(f"""

    <div class="metric-card">

    <div class="metric-title">
    💚 DATA HEALTH
    </div>

    <div class="metric-value">
    {health_score}%
    </div>

    </div>

    """, unsafe_allow_html=True)


st.write("")


# =========================================
# CREATE TABS
# =========================================

tab1, tab2, tab3, tab4 = st.tabs([

    "🔍 Data Quality",

    "⏱️ Freshness",

    "🤖 AI Anomalies",

    "📋 Data Explorer"

])


# =========================================
# TAB 1 - DATA QUALITY
# =========================================

with tab1:

    st.markdown("## 🔍 Data Quality Monitoring")

    st.markdown("""

    <div class="section-card">

    <h3>Data Quality Analysis</h3>

    <p>
    Monitor missing values and identify
    potential data quality issues.
    </p>

    </div>

    """, unsafe_allow_html=True)


    missing_data = data.isnull().sum()


    quality_df = pd.DataFrame({

        "Column": missing_data.index,

        "Missing Values": missing_data.values

    })


    col1, col2 = st.columns([2, 1])


    with col1:

        st.dataframe(

            quality_df,

            use_container_width=True,

            hide_index=True

        )


    with col2:

        if missing_values == 0:

            st.markdown("""

            <div class="status-green">

            🟢 <b>DATA QUALITY: GOOD</b>

            <br><br>

            No missing values detected.

            </div>

            """, unsafe_allow_html=True)

        else:

            st.markdown("""

            <div class="status-yellow">

            🟡 <b>DATA QUALITY WARNING</b>

            <br><br>

            Missing values detected.

            </div>

            """, unsafe_allow_html=True)


# =========================================
# TAB 2 - DATA FRESHNESS
# =========================================

with tab2:

    st.markdown("## ⏱️ Data Freshness Monitoring")


    data["date"] = pd.to_datetime(data["date"])


    latest_date = data["date"].max()


    current_date = datetime.now()


    data_age = (
        current_date - latest_date
    ).days


    col1, col2 = st.columns(2)


    with col1:

        st.markdown(f"""

        <div class="metric-card">

        <div class="metric-title">

        📅 LATEST AVAILABLE DATA

        </div>

        <div class="metric-value">

        {latest_date.date()}

        </div>

        </div>

        """, unsafe_allow_html=True)


    with col2:

        st.markdown(f"""

        <div class="metric-card">

        <div class="metric-title">

        ⏳ DATA AGE

        </div>

        <div class="metric-value">

        {data_age} Days

        </div>

        </div>

        """, unsafe_allow_html=True)


    st.write("")


    if data_age <= 2:

        st.markdown("""

        <div class="status-green">

        🟢 <b>DATA IS FRESH</b>

        <br><br>

        The latest data is recent and
        suitable for analysis.

        </div>

        """, unsafe_allow_html=True)


    else:

        st.markdown("""

        <div class="status-yellow">

        🟡 <b>DATA IS STALE</b>

        <br><br>

        The dataset may require updating.

        </div>

        """, unsafe_allow_html=True)


# =========================================
# TAB 3 - AI ANOMALIES
# =========================================

with tab3:

    st.markdown("## 🤖 AI Anomaly Detection")

    st.markdown("""

    <div class="section-card">

    <h3>Isolation Forest Model</h3>

    <p>

    Artificial Intelligence is used to identify
    unusual patterns in quantity, price and
    sales amount.

    </p>

    </div>

    """, unsafe_allow_html=True)


    try:

        anomaly_data = pd.read_csv(

            "../data/anomaly_detection_results.csv"

        )


        anomalies = anomaly_data[

            anomaly_data["anomaly_status"]
            == "ANOMALY"

        ]


        col1, col2 = st.columns([1, 2])


        with col1:

            st.markdown(f"""

            <div class="metric-card">

            <div class="metric-title">

            🚨 ANOMALIES DETECTED

            </div>

            <div class="metric-value">

            {len(anomalies)}

            </div>

            </div>

            """, unsafe_allow_html=True)


            st.write("")


            if len(anomalies) > 0:

                st.markdown("""

                <div class="status-red">

                🚨 <b>ANOMALIES DETECTED</b>

                <br><br>

                Unusual data patterns
                require attention.

                </div>

                """, unsafe_allow_html=True)


            else:

                st.markdown("""

                <div class="status-green">

                🟢 <b>NO ANOMALIES</b>

                <br><br>

                Data patterns appear normal.

                </div>

                """, unsafe_allow_html=True)


        with col2:

            if len(anomalies) > 0:

                st.markdown("### 🚨 Detected Records")

                st.dataframe(

                    anomalies,

                    use_container_width=True,

                    hide_index=True

                )


    except:

        st.markdown("""

        <div class="status-yellow">

        ⚠️ <b>ANOMALY RESULTS NOT AVAILABLE</b>

        <br><br>

        Please run anomaly_detection.py first.

        </div>

        """, unsafe_allow_html=True)


# =========================================
# TAB 4 - DATA EXPLORER
# =========================================

with tab4:

    st.markdown("## 📋 Data Explorer")


    st.markdown("### Dataset Preview")


    st.dataframe(

        data,

        use_container_width=True,

        hide_index=True

    )


    st.write("")


    st.markdown("### 📈 Sales Amount Distribution")


    chart_data = data.set_index(

        "transaction_id"

    )["sales_amount"]


    st.bar_chart(chart_data)


# =========================================
# FOOTER
# =========================================

st.markdown("---")


st.markdown("""

<div class="footer">

🔭 AI-Enabled Data Observability System

<br>

Data Quality &nbsp; • &nbsp;
Freshness &nbsp; • &nbsp;
Schema Monitoring &nbsp; • &nbsp;
AI Anomaly Detection

</div>

""", unsafe_allow_html=True)