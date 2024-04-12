from data import DataOp as CleanOp
from sidebar import sidebarClean
import streamlit as st
import pandas as pd

def main():
    data = pd.read_csv(f"EDA\sales\Amazon Sale Report.csv\Amazon Sale Report.csv")
    cond = sidebarClean()
    CleanOp(data, cond)

if __name__ == "__main__":
    main()
