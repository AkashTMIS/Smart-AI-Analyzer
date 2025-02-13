# import streamlit as st
# import json

# # Job Roles Data (Simulating job_roles.py)
# JOB_ROLES = {
#     "Software Development and Engineering": {
#         "Frontend Developer": {
#             "required_skills": ["HTML", "CSS", "JavaScript", "React", "Angular", "Vue.js", "UI/UX", "Responsive Design"],
#             "description": "Create user interfaces and implement visual elements",
#             "sections": ["Technical Skills", "Projects", "Work Experience", "Education"],
#             "recommended_skills": {
#                 "technical": ["HTML5", "CSS3", "JavaScript", "React/Angular/Vue", "TypeScript", "Git"],
#                 "soft": ["Communication", "Problem-solving", "Attention to detail", "Creativity"]
#             }
#         }
#     }
# }

# # Initialize session state
# if "job_roles" not in st.session_state:
#     st.session_state.job_roles = JOB_ROLES

# # Job Role Selection
# categories = list(st.session_state.job_roles.keys())
# selected_category = st.selectbox("Job Category", categories)

# roles = list(st.session_state.job_roles[selected_category].keys())
# selected_role = st.selectbox("Specific Role", roles)

# role_info = st.session_state.job_roles[selected_category][selected_role]


# # Update Button
# if st.button("Update Role Info"):
#     # User Inputs for Updating Role Info
#     new_description = st.text_area("Update Job Description", role_info["description"])
#     new_required_skills = st.text_area("Update Required Skills (comma-separated)", ", ".join(role_info["required_skills"]))
#     new_technical_skills = st.text_area("Update Recommended Technical Skills (comma-separated)", ", ".join(role_info["recommended_skills"]["technical"]))
#     new_soft_skills = st.text_area("Update Recommended Soft Skills (comma-separated)", ", ".join(role_info["recommended_skills"]["soft"]))

#     role_info["description"] = new_description
#     role_info["required_skills"] = [skill.strip() for skill in new_required_skills.split(",")]
#     role_info["recommended_skills"]["technical"] = [skill.strip() for skill in new_technical_skills.split(",")]
#     role_info["recommended_skills"]["soft"] = [skill.strip() for skill in new_soft_skills.split(",")]
#     st.success("Job role information updated!")





# Editing Mode
if st.button("Update Role Info"):
    with st.form("update_form"):
        new_description = st.text_area("Update Job Description", role_info["description"])
        new_required_skills = st.text_area("Update Required Skills (comma-separated)", ", ".join(role_info["required_skills"]))
        new_technical_skills = st.text_area("Update Recommended Technical Skills (comma-separated)", ", ".join(role_info["recommended_skills"]["technical"]))
        new_soft_skills = st.text_area("Update Recommended Soft Skills (comma-separated)", ", ".join(role_info["recommended_skills"]["soft"]))

        save_button, cancel_button = st.columns(2)

        with save_button:
            if st.form_submit_button("Save"):
                # Update job roles dictionary
                role_info["description"] = new_description
                role_info["required_skills"] = [skill.strip() for skill in new_required_skills.split(",")]
                role_info["recommended_skills"]["technical"] = [skill.strip() for skill in new_technical_skills.split(",")]
                role_info["recommended_skills"]["soft"] = [skill.strip() for skill in new_soft_skills.split(",")]

                # Save updates to JSON file
                save_job_roles(job_roles)

        with cancel_button:
            if st.form_submit_button("Cancel"):
                st.warning("Changes discarded.")
                st.rerun()  # Refresh to discard changes