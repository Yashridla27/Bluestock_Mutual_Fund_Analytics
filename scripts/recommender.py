
import pandas as pd

scorecard = pd.read_csv("../Data/Processed/fund_scorecard.csv")

scorecard["risk_grade"] = pd.qcut(
    scorecard["score"],
    q=3,
    labels=["Low", "Moderate", "High"]
)

risk_appetite = input("Enter Risk Appetite (Low/Moderate/High): ")

recommendations = (
    scorecard[scorecard["risk_grade"] == risk_appetite]
    .sort_values("sharpe_ratio", ascending=False)
    [["amfi_code","scheme_name","risk_grade","sharpe_ratio","score"]]
    .head(3)
)

print("\nTop 3 Recommended Funds:\n")
print(recommendations.to_string(index=False))
