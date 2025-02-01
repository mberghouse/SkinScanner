# src/index.py
import streamlit as st

# Set a default page, if not already set
if "page" not in st.session_state:
    st.session_state.page = "landing"

if st.session_state.page == "landing":
    import app
    app.main()
elif st.session_state.page == "analysis":
    import main
    main.main()