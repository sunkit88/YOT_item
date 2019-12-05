import pandas as pd

item_raw = pd.read_csv(".\item.csv")
item_cat_raw = pd.read_csv(".\item_cat.csv")
item_full_raw = pd.read_csv(".\item_full.csv", dtype={'scode':str})

item = item_raw[(item_raw["pcat"] == "PUR")]
item = item[["desc", "unit", "Item Category Code", "pcat"]]

item_cat = item_cat_raw[(item_cat_raw["pcat"] == "PUR")]
item_cat = item_cat[["desc", "pcat", "item_cat"]]

item_full = item_full_raw

item_full_join = pd.merge(item_full, item_cat, on='desc', how='left')
item_full_join = pd.merge(item_full_join, item, on='desc', how='left')

item_full_melt = pd.melt(item_full_join, id_vars =['desc'], value_vars =['scode', 'bcode', 'bcode2'])
item_full_join.to_csv(".\item_full_join.csv", index=0, encoding="utf_8_sig")
item_full_melt.to_csv(".\item_full_melt.csv", index=0, encoding="utf_8_sig")

