
import streamlit as st
def main():
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
                <li>for data operation from sidebar select DataOperation
                <li>for Graph operation from sidebar select GraphOperation
                </ul>
            </div>
        </div>
        """
        , unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

