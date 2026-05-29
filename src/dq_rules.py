def check_duplicates(df, key_columns):
    """
    Checks duplicate records based on one or more key columns.
    """
    return int(df.duplicated(subset=key_columns).sum())


def check_missing_values(df, column_name):
    """
    Checks missing/null values for a specific column.
    """
    return int(df[column_name].isna().sum())


def check_relationship(child_df, parent_df, child_key, parent_key):
    """
    Checks whether child key values exist in the parent table.
    """
    return int((~child_df[child_key].isin(parent_df[parent_key])).sum())


def check_invalid_date_order(df, start_date_column, end_date_column):
    """
    Checks records where start date is greater than end date.
    """
    return int((df[start_date_column] > df[end_date_column]).sum())


def check_missing_amounts(df, amount_column="amount"):
    """
    Checks missing values in financial amount column.
    """
    return int(df[amount_column].isna().sum())