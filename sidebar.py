import streamlit as st

def sidebarData():
    st.sidebar.title("Data Display Options")
    cond = []
    if st.sidebar.checkbox("Head"):
        cond.append("head")
    if st.sidebar.checkbox("Tail"):
        cond.append("tail")
    if st.sidebar.checkbox("Describe"):
        cond.append("describe")
    if st.sidebar.checkbox("Info"):
        cond.append("info")
    if st.sidebar.checkbox("Shape"):
        cond.append("shape")
    if st.sidebar.checkbox("Columns"):
        cond.append("columns")
    if st.sidebar.checkbox("Dtypes"):
        cond.append("dtypes")
    if st.sidebar.checkbox("Sample"):
        cond.append("sample")
    if st.sidebar.checkbox("Value Counts"):
        cond.append("value_counts")
    if st.sidebar.checkbox("Is Null"):
        cond.append("isnull")
    if st.sidebar.checkbox("nunique"):
        cond.append("nunique")
    if st.sidebar.checkbox("unique"):
        cond.append("unique")
    else:
        st.markdown(
        """
        <style>
            .navbar {
                padding: 10px;
                background-color: #fffff;
                border-bottom: 1px solid #e6e6e6;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .nav-links {
                display: flex;
                list-style-type: none;
                margin: 0;
                padding: 0;
            }
            .nav-link {
                margin-right: 20px;
            }
            .nav-link:last-child {
                margin-right: 0;
            }
        </style>
        """
        , unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="navbar">
            <div>
                <h3>Amazon India Sales data</h3>
                <ul>
                <li>Select Operation to be performed from sidebar
                </ul>
            </div>
        </div>
        """
        , unsafe_allow_html=True
    )

    return cond

def sidebarClean():
    st.sidebar.title("Data Cleaning Display Options")
    cond = []
    if st.sidebar.checkbox("Drop columns"):
        cond.append("drop")
    if st.sidebar.checkbox("Delete Duplicate"):
        cond.append("DD")
    if st.sidebar.checkbox("Fill NAN"):
        cond.append("Nan")
    else:
        st.markdown(
        """
        <style>
            .navbar {
                padding: 10px;
                background-color: #fffff;
                border-bottom: 1px solid #e6e6e6;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .nav-links {
                display: flex;
                list-style-type: none;
                margin: 0;
                padding: 0;
            }
            .nav-link {
                margin-right: 20px;
            }
            .nav-link:last-child {
                margin-right: 0;
            }
        </style>
        """
        , unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="navbar">
            <div>
                <h3>Amazon India Sales data</h3>
                <ul>
                <li>Select Operation to be performed from sidebar
                </ul>
            </div>
        </div>
        """
        , unsafe_allow_html=True
    )

    return cond

def sidebarGraph():
    st.sidebar.title("Graph Display Options")
    cond = []
    if st.sidebar.checkbox("Heat"):
        cond.append("heat")
    if st.sidebar.checkbox("Net Revenue"):
        cond.append("NetRevenue")
    if st.sidebar.checkbox("Average Monthly Order"):
        cond.append("AvgMonth")
    if st.sidebar.checkbox("Top Product"):
        cond.append("TopPro")
    if st.sidebar.checkbox("percent product revenue"):
        cond.append("perRevenue")
    if st.sidebar.checkbox("Sales by product size"):
        cond.append("size")
    if st.sidebar.checkbox("sales by quartile"):
        cond.append("sales")
    else:
        st.markdown(
        """
        <style>
            .navbar {
                padding: 10px;
                background-color: #fffff;
                border-bottom: 1px solid #e6e6e6;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .nav-links {
                display: flex;
                list-style-type: none;
                margin: 0;
                padding: 0;
            }
            .nav-link {
                margin-right: 20px;
            }
            .nav-link:last-child {
                margin-right: 0;
            }
        </style>
        """
        , unsafe_allow_html=True
    )


    st.markdown(
        """
        <div class="navbar">
            <div>
                <h3>Amazon India Sales data</h3>
                <ul>
                <li>Select Operation to be performed from sidebar
                </ul>
            </div>
        </div>
        """
        , unsafe_allow_html=True
    )

    return cond