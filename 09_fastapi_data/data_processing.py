import json
from fastapi.responses import JSONResponse


class DataExplorer:
    def __init__(self, df, limit=100):
        self._df_full = df
        self._df = df.head(limit)

    @property
    def df(self):
        return self._df

    def summary(self):
        self._df = (
            self._df_full.describe()
            .drop(["count"])
            .drop(["Day", "Year"], axis=1)
            .T.reset_index()
        )
        return self

    def kpis(self, country):
        if not country:
            df = self._df_full
        else:
            df = self._df_full.query("Country.str.casefold() == @country")
        return {
            "total_revenue": str(df["Revenue"].sum()),
            "total_profit": str(df["Profit"].sum()),
            "total_cost": str(df["Cost"].sum()),
            "number_of_purchases": str(len(df)),
        }

    def json_response(self):
        json_data = self.df.to_json(orient="records")
        return JSONResponse(json.loads(json_data))
