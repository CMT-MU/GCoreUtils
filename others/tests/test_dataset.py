"""
test for dataset
"""
from gcoreutils.dataset import DataSet

data = {
    "site": (["name", "idx", "position", "color"], ["text", "number", "math", "color"]),
    "bond": (["name", "idx", "center", "vector"],),
}

ds = DataSet(data)
for i in range(3):
    ds.append("site", ["Te", i, "[1,2,3]", "yellow"])
    ds.append("site", ["Te", i - 1, "[2,1,3]", "white"])
    ds.append("bond", ["Te-Te", i, "[1/2,0,1/2]", "[0,0,1]"])
    ds.append("bond", ["Te-Te", i - 1, "[1/2,0,1/2]", "[0,0,1]"])
# ds.load_csv("sample", "sample_news.csv")
# ds.load_csv("data", "data.csv")

print("-------------")
print(ds.role["site"], ds.role["bond"])
ds.set_role("bond", ["text", "number", "math", "math"])
print(ds.role["site"], ds.role["bond"])
print("-------------")
print(ds.indexed("site", ["name", "idx"]))
print("-------------")
print(ds.indexed("bond", ["name", "idx"], sort=False))
print("-------------")
print(ds.extract("site", "idx == 1", index=True))
print("-------------")
print(ds.extract("site", "name == 'Te'"))
print("-------------")
data1 = ds.to_data()
ds1 = DataSet(data1)
ds1.remove("site", "idx == 1", inplace=True)
for name, df in ds1.items():
    print(name, "\n", df)

ds1.save_csv("outdata", "site")
