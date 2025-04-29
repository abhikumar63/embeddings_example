import pandas as pd
from var import *

output = query(texts)

embeddings = pd.DataFrame(output)

embeddings.to_csv("embeddings.csv", index=False)