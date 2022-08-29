import pandas as pd

fifty_five_up_df = pd.read_csv("below_poverty_over_55.csv")
total_pop = (
        pd.read_csv("full_pop_zip.csv")
            .rename(columns={
                "zip code tabulation area": "ZIP",
                "S0101_C01_001E": "population",
                }
            )
            .drop(["NAME","Unnamed: 0"], axis=1)
            .set_index("ZIP")
)

by_zips = (
        fifty_five_up_df.sort_values("below poverty over 55", ascending=False)
            .set_index("ZIP")
            .drop("Unnamed: 0", axis=1)
            .join(total_pop)
)

by_zips.to_csv("BelowPovertyOver55.csv")
