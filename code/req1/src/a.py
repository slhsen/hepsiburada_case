import pandas as pd
from datetime import datetime
from src.sql import a_query
from src.utils import get_conn


def transform_datas(datas):
    grouped_datas = datas.groupby("categoryid")
    category_arr = datas['categoryid'].unique()

    category_prods = []
    for i in category_arr:
        category_prods.append(grouped_datas.get_group(i)['productid'].to_list())

    converted_datas = pd.DataFrame(category_prods, index=list(map(lambda x: f"category-{x}", category_arr)))

    return converted_datas


def main():
    conn = get_conn()
    datas = pd.read_sql_query(a_query, conn)

    transformed_datas = transform_datas(datas)

    now = datetime.now().strftime("%Y-%d-%m, %H")

    transformed_datas.to_csv(f"./a_{now}.csv")