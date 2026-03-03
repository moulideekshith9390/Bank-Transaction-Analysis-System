from data_generator import generate_transactions
from data_loader import load_data
from eda import basic_summary, category_spending, monthly_spending, recurring_merchants
from mining import spending_clusters, detect_anomalies
from visualization import plot_category_spending, plot_monthly_spending, plot_clusters

def main():
    # Generate data if needed
    generate_transactions()

    df = load_data()

    # EDA
    basic_summary(df)

    cat_spend = category_spending(df)
    print(cat_spend)

    monthly = monthly_spending(df)
    print(monthly)

    print(recurring_merchants(df))

    # Visualization
    plot_category_spending(cat_spend)
    plot_monthly_spending(monthly)

    # Data Mining
    df = spending_clusters(df)
    plot_clusters(df)

    anomalies = detect_anomalies(df)
    print("\n===== DETECTED ANOMALIES =====")
    print(anomalies)

if __name__ == "__main__":
    main()