
def transform(df):
    df = df.drop_duplicates()
    df['quantity'] = df['quantity'].fillna(1)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total_amount'] = df['quantity'] * df['price']
    return df
