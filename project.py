import pandas as pd
import matplotlib.pyplot as plt



def load_and_prepare_data():
    orders = pd.read_csv("orders.csv").drop_duplicates()
    customers = pd.read_csv("customers.csv").drop_duplicates()
    products = pd.read_csv("products.csv").drop_duplicates()


    orders["order_date"] = pd.to_datetime(orders["order_date"])
    customers["registration_date"] = pd.to_datetime(customers["registration_date"])


    for col in ["first_name", "last_name", "city"]:
        customers[col] = customers[col].str.strip()

    for col in ["product_name", "brand"]:
        products[col] = products[col].str.strip()

    orders["payment_type"] = orders["payment_type"].str.strip()


    orders["order_month"] = orders["order_date"].dt.to_period("M")
    orders["revenue"] = (
        orders["quantity"] * orders["unit_price"] * (1 - orders["discount"])
    )

    return orders, customers, products



def get_monthly_revenue(orders):
    return (
        orders.groupby("order_month")["revenue"]
        .sum()
        .reset_index()
    )


def get_customer_stats(orders, customers):
    customer_stats = (
        orders.merge(customers, on="customer_id", how="left")
              .groupby(["customer_id", "first_name", "last_name", "city"])
              .agg(
                  order_count=("order_id", "count"),
                  total_revenue=("revenue", "sum"),
                  avg_order_value=("revenue", "mean")
              )
              .reset_index()
    )

    customer_stats["full_name"] = (
        customer_stats["first_name"] + " " + customer_stats["last_name"]
    )

    return customer_stats


def segment_customer(revenue):
    if revenue >= 5000:
        return "High Value"
    elif revenue >= 2000:
        return "Medium Value"
    else:
        return "Low Value"



def create_dashboard(monthly_revenue, customer_stats):
    plt.figure(figsize=(12, 8))


    plt.subplot(2, 2, 1)
    plt.plot(
        monthly_revenue["order_month"].astype(str),
        monthly_revenue["revenue"]
    )
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)


    top_customers = (
        customer_stats
        .sort_values("total_revenue", ascending=False)
        .head(10)
    )

    plt.subplot(2, 2, 2)
    plt.bar(top_customers["full_name"], top_customers["total_revenue"])
    plt.title("Top 10 Customers by Total Revenue")
    plt.xlabel("Customer")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)


    plt.subplot(2, 2, 3)
    plt.scatter(
        customer_stats["order_count"],
        customer_stats["total_revenue"]
    )
    plt.title("Orders vs Total Revenue")
    plt.xlabel("Number of Orders")
    plt.ylabel("Total Revenue")


    customer_stats["segment"] = (
        customer_stats["total_revenue"].apply(segment_customer)
    )
    segment_counts = customer_stats["segment"].value_counts()

    plt.subplot(2, 2, 4)
    plt.bar(segment_counts.index, segment_counts.values)
    plt.title("Customer Segmentation")
    plt.xlabel("Segment")
    plt.ylabel("Number of Customers")

    plt.tight_layout()
    plt.show()



def main():
    orders, customers, products = load_and_prepare_data()

    monthly_revenue = get_monthly_revenue(orders)
    customer_stats = get_customer_stats(orders, customers)

    create_dashboard(monthly_revenue, customer_stats)


if __name__ == "__main__":
    main()
