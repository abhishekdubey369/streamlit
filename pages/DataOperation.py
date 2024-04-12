from data import dataDisplay
from sidebar import sidebarData
import streamlit as st
import pandas as pd

def main():
    data = pd.read_csv(f"EDA\sales\Amazon Sale Report.csv\Amazon Sale Report.csv",low_memory=False)
    cond = sidebarData()
    dataDisplay(data, cond)

if __name__ == "__main__":
    main()
