import streamlit as st

st.set_page_config(
    page_title="CareMap",
    page_icon="🧭",
    layout="centered"
)

# ---------------- CAREMAP THEME ----------------

st.markdown("""
<style>

    /* Main page */
    .stApp {
        background-color: #F8FAFC;
        color: #0F2A44;
        font-family: Arial, sans-serif;
    }

    /* Main content width and spacing */
    .block-container {
        max-width: 1100px;
        padding-top: 3rem;
        padding-bottom: 4rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    /* Main headings */
    h1 {
        color: #0F2A44 !important;
        font-size: 2.7rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
    }

    h2 {
        color: #0F2A44 !important;
        font-weight: 700 !important;
    }

    h3 {
        color: #0F2A44 !important;
        font-weight: 700 !important;
    }

    /* Normal text */
    p, label {
        color: #0F2A44;
        font-family: Arial, sans-serif;
    }

    /* Divider */
    hr {
        border: none;
        border-top: 2px solid #00A8E8;
        margin: 1.5rem 0;
    }

    /* Primary buttons */
    .stButton > button {
        background-color: #4A90E2;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.65rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background-color: #00A8E8;
        color: white;
    }

    /* Select boxes */
    div[data-baseweb="select"] > div {
        background-color: white;
        border: 1px solid #E2E7ED;
        border-radius: 10px;
    }

    /* Success message */
    div[data-testid="stAlert"] {
        border-radius: 12px;
    }

</style>
""", unsafe_allow_html=True)

# Create a screen tracker
if "page" not in st.session_state:
    st.session_state.page = "home"


# ---------------- HOME PAGE ----------------

if st.session_state.page == "home":

    st.title("🧭 CareMap")
    st.subheader("Understand support. Find compatibility. Reduce barriers.")

    st.write(
        "CareMap helps families understand their support capacity "
        "and discover child-care compatibility based on specific support needs."
    )

    st.divider()

    st.markdown("### How CareMap works")

    st.write("1. Answer questions about your family's support capacity.")
    st.write("2. Build your Family Support Capacity Profile.")
    st.write("3. Compare your profile with child support requirements.")
    st.write("4. Understand compatibility and potential support gaps.")

    st.divider()

    if st.button("Start Family Assessment", type="primary"):
        st.session_state.page = "assessment"
        st.rerun()


# ---------------- ASSESSMENT PAGE ----------------

elif st.session_state.page == "assessment":

    st.title("👨‍👩‍👧 Family Support Assessment")

    st.write(
        "Tell us about the support your family can provide. "
        "There are no right or wrong answers."
    )

    st.divider()

    healthcare = st.selectbox(
        "🏥 How easily can your family access healthcare?",
        [
            "Very easily",
            "Somewhat easily",
            "With difficulty"
        ]
    )

    time_available = st.selectbox(
        "⏰ How much time can your family dedicate to additional care?",
        [
            "High availability",
            "Moderate availability",
            "Limited availability"
        ]
    )

    therapy = st.selectbox(
        "🧑‍⚕️ How accessible are therapy or rehabilitation services?",
        [
            "Easily accessible",
            "Available with travel",
            "Difficult to access"
        ]
    )

    accessibility = st.selectbox(
        "🏠 How accessible is your home environment?",
        [
            "Highly accessible",
            "Partially accessible",
            "Not currently accessible"
        ]
    )

    communication = st.selectbox(
        "🗣️ What communication support can your family provide?",
        [
            "Strong communication support",
            "Can learn with guidance",
            "Limited experience"
        ]
    )

    experience = st.selectbox(
        "💙 Does your family have relevant caregiving experience?",
        [
            "Yes",
            "Some experience",
            "No"
        ]
    )

    st.divider()

    if st.button("Create My Support Profile", type="primary"):

        st.session_state.family_profile = {
            "Healthcare Access": healthcare,
            "Time Availability": time_available,
            "Therapy Access": therapy,
            "Home Accessibility": accessibility,
            "Communication Support": communication,
            "Caregiving Experience": experience
        }

        st.session_state.page = "profile"
        st.rerun()


# ---------------- PROFILE PAGE ----------------

elif st.session_state.page == "profile":

    st.title("📋 Your Family Support Profile")

    st.write(
        "CareMap has structured your answers into a Support Capacity Profile."
    )

    st.divider()

    profile = st.session_state.family_profile

    for category, answer in profile.items():
        st.markdown(f"**{category}**")
        st.write(answer)

    st.divider()

    st.success("Family Support Capacity Profile created successfully!")

    if st.button("Continue to Child Matching", type="primary"):
        st.session_state.page = "matching"
        st.rerun()

# ---------------- MATCHING PAGE ----------------

elif st.session_state.page == "matching":

    st.title("🧩 Child Matching")

    st.write(
        "CareMap compares your Family Support Capacity Profile "
        "with the support requirements of available children."
    )

    st.divider()

    st.markdown("### Available Child Profiles")

    child_1 = st.container()

    with child_1:
        st.subheader("Child A — Age 6")
        st.write("Primary support needs: Speech & communication support")
        st.write("Therapy requirement: Regular speech therapy")
        st.write("Healthcare access: Moderate")
        
        if st.button("View Compatibility", key="child_a"):
            st.session_state.selected_child = "Child A"
            st.session_state.page = "result"
            st.rerun()

    st.divider()

    child_2 = st.container()

    with child_2:
        st.subheader("Child B — Age 8")
        st.write("Primary support needs: Mobility & physical support")
        st.write("Therapy requirement: Physiotherapy")
        st.write("Healthcare access: High")

        if st.button("View Compatibility", key="child_b"):
            st.session_state.selected_child = "Child B"
            st.session_state.page = "result"
            st.rerun()

# ---------------- RESULT PAGE ----------------

elif st.session_state.page == "result":

    st.title("📊 Compatibility Result")

    selected_child = st.session_state.selected_child

    st.subheader(selected_child)

    st.divider()

    st.metric("Support Compatibility", "82%")

    st.success("Good support alignment identified.")

    st.markdown("### Why this match?")

    st.write("✓ Healthcare access is compatible")
    st.write("✓ Family has moderate-to-high time availability")
    st.write("✓ Therapy access is available")
    st.write("✓ Family can provide communication support")

    st.markdown("### Potential Support Gap")

    st.warning(
        "Additional specialized therapy access may be required."
    )

    st.divider()

    if st.button("View Barrier Insights", type="primary"):
        st.session_state.page = "barriers"
        st.rerun()

# ---------------- BARRIER INSIGHTS PAGE ----------------

elif st.session_state.page == "barriers":

    st.title("🔎 Barrier Insights")

    st.write(
        "CareMap aggregates recurring support gaps to identify "
        "potential placement barriers."
    )

    st.divider()

    st.subheader("Observed Support Gaps")

    st.write("🗣️ Communication support — 3 families")
    st.write("🧑‍⚕️ Specialized therapy access — 5 families")
    st.write("🏥 Healthcare proximity — 2 families")

    st.divider()

    st.info(
        "Insight: Specialized therapy access appears to be "
        "a recurring support gap among participating families."
    )